import subprocess
import re
import sys
from pathlib import Path

# ---------------- CONFIG ----------------
CDB_PATH = "C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x64\\cdb.exe"
DUMP_FILE = r"C:\Windows\Minidump\020226-13062-01.dmp"
SYMBOL_PATH =r"C:\Windows\Minidump"
    #"srv*C:\\symbols*https://msdl.microsoft.com/download/symbols"


# ----------------------------------------

def run_windbg(dump_file):
    """
    Run WinDbg (cdb) and return analysis output
    """
    cmd = [
        CDB_PATH,
        "-z", dump_file,
        "-y", SYMBOL_PATH,
        "-c", "!analyze -v; q"
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.stdout
    except Exception as e:
        print("Error running WinDbg:", e)
        sys.exit(1)


def parse_analysis(output):
    """
    Extract key crash details from WinDbg output
    """
    data = {}

    # Bugcheck
    bugcheck = re.search(r"Bugcheck\.Code\.LegacyAPI\s+Value:\s+(0x[0-9a-fA-F]+)", output)
    data["Bugcheck"] = bugcheck.group(1) if bugcheck else "Unknown"

    # Failure Bucket
    bucket = re.search(r"FAILURE_BUCKET_ID:\s+(.+)", output)
    data["Failure_Bucket"] = bucket.group(1).strip() if bucket else "Unknown"

    # Module name
    module = re.search(r"MODULE_NAME:\s+(.+)", output)
    data["Module"] = module.group(1).strip() if module else "Unknown"

    # Detect page table corruption
    data["PageTableCorruption"] = "PAGE_TABLE_RESERVED_BITS_SET" in output

    # Extract stack drivers
    drivers = re.findall(r"\n\S+\s+\S+\s+:\s+.*?:\s+([a-zA-Z0-9_]+)\+0x[0-9a-fA-F]+", output)

    # Remove Windows core modules
    windows_modules = {"nt", "hal", "win32k"}
    culprit = None
    for d in drivers:
        if d.lower() not in windows_modules:
            culprit = d
            break

    data["Faulting_Driver"] = culprit if culprit else "Unknown"

    return data


def print_report(data):
    """
    Print final crash verdict
    """
    print("\n========== CRASH ANALYSIS REPORT ==========\n")
    print(f"Bugcheck Code        : {data['Bugcheck']}")
    print(f"Failure Bucket       : {data['Failure_Bucket']}")
    print(f"Reported Module      : {data['Module']}")
    print(f"Faulting Driver      : {data['Faulting_Driver']}")
    print(f"Page Table Corruption: {data['PageTableCorruption']}")

    print("\n---------- FINAL VERDICT ----------")
    if data["Faulting_Driver"] != "Unknown":
        print(f"✔ Root Cause: Third-party driver '{data['Faulting_Driver']}.sys'")
        print("✔ Crash Type: Kernel memory corruption")
        print("✔ Hardware Failure: Unlikely")
    else:
        print("⚠ Unable to identify exact driver")
        print("⚠ Possible RAM or firmware issue")

    print("\n===================================\n")


def main():
    dump_path = Path(DUMP_FILE)
    if not dump_path.exists():
        print("Dump file not found:", dump_path)
        sys.exit(1)

    print("Running WinDbg analysis...")
    output = run_windbg(str(dump_path))

    print("Parsing analysis...")
    data = parse_analysis(output)

    print_report(data)


if __name__ == "__main__":
    main()
