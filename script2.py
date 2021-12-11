import threading
import os

def execute():
    threading.Timer(5.0, execute).start()
    bashCmd = '''
                cd ..
                cd /Users/andres/Documents/Uniandes/infracomp/infracomp-caso1
                git remote update
                var="$(git status -uno)"
                if [[ $var =~ "branch is behind" ]]; then
                    sudo systemctl restart manejador-ordenes.service
                else 
                    echo Up-To-Date
                fi'''
    os.system(bashCmd)
execute()
