import subprocess
import sys

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
script_path = 'tapi_encry_decry.sh'


if len(sys.argv) != 4:
    print('Usage: python script.py input_param1 input_param2 input_param3')
    sys.exit(1)

input_param1 = sys.argv[1]
input_param2 = sys.argv[2]
input_param3 = sys.argv[3]

try:
    output = execute_bash_script(script_path, input_param1, input_param2, input_param3)
    print(output)
except Exception as e:
    print(f'Error: {str(e)}')
