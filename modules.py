import paramiko
hostname = "192.168.88.37"
username = "etechserver2"
password = "123"

remote_file_path = "/home/etechserver2/hamsaa/test.py"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

sftp = ssh.open_sftp()

# READ FILE (correct way)
with sftp.open(remote_file_path, 'r') as f:
    content = f.read().decode()
    print("File content: conneted")
    print(content)

sftp.close()
ssh.close()



