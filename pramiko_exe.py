import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.88.37", username="etechserver2", password="123", port=22)
print("connected")
sftp = ssh.open_sftp()
remote_folder = "/home/etechserver2/hamsaa"
remote_file = "test.py"
remote_file_path = f"{remote_folder}/{remote_file}"
with sftp.open(remote_file_path, 'r') as f:
    content = f.read().decode()
#print(f"\n--- Content of {remote_file} ---")
print(content)
print("hlo hamsa")
sftp.close()
ssh.close()


