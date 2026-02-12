import subprocess
import sys
import os

# ==============================
# CONFIGURATION
# ==============================
DPCMD_PATH = r"C:\Program Files (x86)\DediProg\SF Programmer\dpcmd.exe"
BIN_FILE = r"C:\Users\default.DESKTOP-MOGIHTS\Documents\bios.bin"

BACKUP_FILE = "backup.bin"

# ==============================
# HELPER FUNCTION
# ==============================
def run_cmd(cmd, step_name):
    print(f"\n===== {step_name} =====")
    print("Command:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)
    if result.returncode != 0:
        print("ERROR:")
        print(result.stderr)
        sys.exit(1)

# ==============================
# MAIN FLOW
# ==============================
if not os.path.exists(DPCMD_PATH):
    print("ERROR: dpcmd.exe not found")
    sys.exit(1)

if not os.path.exists(BIN_FILE):
    print("ERROR: bios.bin not found")
    sys.exit(1)

# 1. Detect programmer & chip
run_cmd([DPCMD_PATH, "-i"], "Detect programmer & chip")

# 2. Read JEDEC ID
run_cmd([DPCMD_PATH, "-j"], "Read JEDEC ID")

# 3. Backup existing flash
run_cmd([DPCMD_PATH, "-rf", BACKUP_FILE], "Read flash (backup)")

# 4. Erase chip
run_cmd([DPCMD_PATH, "-e"], "Erase flash")

# 5. Blank check (optional but recommended)
run_cmd([DPCMD_PATH, "-b"], "Blank check")

# 6. Write BIOS image
run_cmd([DPCMD_PATH, "-wf", BIN_FILE], "Write BIOS")

# 7. Verify written data
run_cmd([DPCMD_PATH, "-v"], "Verify flash")

# 8. Calculate checksum & CRC
run_cmd([DPCMD_PATH, "-s"], "Checksum & CRC")

print("\n✅ FLASHING COMPLETED SUCCESSFULLY")
