import subprocess

completed = subprocess.run(['cmd','dir'])
print('returncode:', completed.returncode)
