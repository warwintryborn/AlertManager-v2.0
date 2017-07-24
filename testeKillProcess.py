##import subprocess
##subprocess.call("taskkill /IM AlertManager.exe")  

import os
os.system("taskkill /f /im  AlertManager.exe")
