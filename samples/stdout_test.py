import subprocess
result = subprocess.run(['bash', 't.sh'], stdout=subprocess.PIPE)
# res=result.stdout.decode('utf-8')
res = result.stdout
print(result.returncode)