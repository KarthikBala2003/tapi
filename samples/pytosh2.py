import subprocess

def execute_bash_script(script_path, *args):
    command = ['bash', script_path] + list(args)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return stdout.decode().strip()
    else:
        error_message = stderr.decode().strip()
        raise Exception(f'Bash script execution failed: {error_message}')

# Example usage
script_path = 'pytosh2.sh'
input_param1 = 'hello'
input_param2 = 'world'

#input_param3 = 'Encrypt'

# 'Encrypt' 'Decrypt'
input_param3 =  'Decrypt'       


try:
    output = execute_bash_script(script_path, input_param1, input_param2, input_param3)
    print(output)
except Exception as e:
    print(f'Error: {str(e)}')
