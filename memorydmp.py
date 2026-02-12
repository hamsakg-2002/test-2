import subprocess

CDB = r"C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe"
DUMP = r"C:\Windows\MEMORY.DMP"

cmd = [
    CDB,
    "-z", DUMP,
    "-c", "!analyze -v; q"
]

result = subprocess.run(
    cmd,
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)
