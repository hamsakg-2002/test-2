import subprocess
import os

# ====== Configuration ======
# Path to DediprogCmd.exe
dediprog_path = r"C:\Program Files (x86)\Dediprog\DediprogCmd.exe"

# File names
backup_file = "backup.bin"
write_file = "newdata.bin"

# Optional: specify address range (None for full chip)
address_range = None  # Example: "0x00:0xFF"

# ====== Helper function ======
def run_dediprog_command(args):
    """Run a DediprogCmd command and print output."""
    cmd = [dediprog_path] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        print("Output:", e.stdout)
        print("Errors:", e.stderr)

# ====== 1. Read chip ======
print("=== Reading chip ===")
read_args = ["-r", backup_file]
if address_range:
    read_args.insert(1, address_range)
run_dediprog_command(read_args)

# ====== 2. Erase chip ======
print("=== Erasing chip ===")
erase_args = ["-e"]
if address_range:
    erase_args.append(address_range)
run_dediprog_command(erase_args)

# ====== 3. Write chip ======
print("=== Writing chip ===")
write_args = ["-w", write_file]
if address_range:
    write_args.insert(1, address_range)
run_dediprog_command(write_args)

# ====== 4. Verify chip ======
print("=== Verifying chip ===")
verify_args = ["-v", write_file]
if address_range:
    verify_args.insert(1, address_range)
run_dediprog_command(verify_args)

print("=== Dediprog workflow completed ===")
