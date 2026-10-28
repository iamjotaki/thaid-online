import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('129.221.170.225', username='ubuntu', key_filename=r'C:\NV\oracle_key.pem')
stdin, stdout, stderr = ssh.exec_command('docker ps --format "table {{.Names}}\t{{.Status}}"')
print(stdout.read().decode())
stdin, stdout, stderr = ssh.exec_command('docker ps -a --filter "status=running" --filter "ancestor=coolify-helper" --format "{{.Names}}"')
print("Coolify helper / builds:", stdout.read().decode())
ssh.close()
