import threading
import os

def execute():
    threading.Timer(5.0, execute).start()
    bashCmd = '''
                cd ..
                cd /home/ec2-user/arquisoft
                git remote update
                var="$(git status -uno)"
                if [[ $var =~ "branch is behind" ]]; then
                    sudo systemctl restart manejador-comercios.service
                else 
                    echo Up-To-Date
                fi'''
    os.system(bashCmd)
execute()
