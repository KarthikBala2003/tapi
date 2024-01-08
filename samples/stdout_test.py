import subprocess, sys
# result = subprocess.run(['bash', 't.sh'], stdout=subprocess.PIPE)
# # res=result.stdout.decode('utf-8')
# res = result.stdout
# print(result.returncode)

# Example usage
script_path = 't.sh'
input_param1 = "Hello"
input_param2 = "World"

def execute_bash_script(script_path, *args):
    command = ['bash', script_path] + list(args)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print (stdout.decode('utf-8'))
    
    if process.returncode == 0:
        return stdout.decode().strip()
    else:
        error_message = stderr.decode().strip()
        raise Exception(f'Bash script execution failed: {error_message}')

execute_bash_script(script_path, input_param1,input_param2)