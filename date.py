import serial
from datetime import datetime

# Serial port configuration
PORT = "COM6"
BAUD_RATE = 115200
LOG_FILE = "PUTTY2.log"

try:
    ser = serial.Serial(
        port=PORT,
        baudrate=BAUD_RATE,
        timeout=1
    )
    print(f"Connected to {PORT} at {BAUD_RATE} baud")

    with open(LOG_FILE, "a", encoding="utf-8") as logfile:
        while True:
            line = ser.readline()
            if line:
                decoded_line = line.decode(errors="ignore").strip()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"[{timestamp}] {decoded_line}"

                print(log_entry)
                logfile.write(log_entry + "\n")
                logfile.flush()

except serial.SerialException as e:
    print("Serial port error:", e)

except KeyboardInterrupt:
    print("\nLogging stopped by user")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed")

