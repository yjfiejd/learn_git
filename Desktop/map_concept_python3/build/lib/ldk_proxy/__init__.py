import platform, threading, os

class ProxyRunner(threading.Thread):
    def __init__(self, executable):
        #super(ProxyRunner).__init__()
        threading.Thread.__init__(self)
        self.executable = executable

    def run(self):
        os.system(self.executable)

ldkHost = os.getenv('LDK_HOST', '10.0.0.236')
if ldkHost:
    print('LDK_HOST: ' + ldkHost)
else:
    raise SystemError('LDK_HOST environment is not defined.')

system = platform.system()
currentDir = os.path.dirname(__file__)

if system == 'Linux':
    ProxyRunner(os.path.join(currentDir, "proxy.linux-x64")).start()
elif system == 'Darwin':
    ProxyRunner(os.path.join(currentDir, "proxy.osx-x64")).start()
elif system == 'Windows':
	ProxyRunner(os.path.join(currentDir, "proxy.win-x64.exe")).start()
else:
    print("OS is not supported")
    raise Exception("OS is not supported")
