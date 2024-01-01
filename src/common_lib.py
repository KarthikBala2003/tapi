import subprocess

class CommonLib:
    
    # Eexcuting shell scripts
    # usage command: 'bash \path_to\filename.sh arg1, arg2, arg3, ...'
    def execute_bash_script(script_path, *args):
        command = ['bash', script_path] + list(args)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            return stdout.decode().strip()
        else:
            error_message = stderr.decode().strip()
            raise Exception(f'Bash script execution failed: {error_message}')
    