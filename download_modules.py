import pip
import time

modules = []

print("Coder -> Mostafa M. Mead")

__information__ = """
Python Script To Download Modules
You Can Use This Script Without Any Module
"""

def install(package):
    pip.main(['install', package])

def get_modules(script):
	with open(script) as f:
		lines = f.read().split("\n")
	for line in lines:
		if "import" in line:
			try:
				line = line.split(" ")[1]
			except:
				pass
			else:
				modules.append(line)

def main():
	get_modules(input("Enter Script: "))
	for module in modules:
		try:
			install(module)
		except:
			print("[-] Module Is Already Installed Or Not Found")
	print("[+] Installation Done")
	print("Script Will Close In 20 Sec")
	time.sleep(20)

if __name__ == '__main__':
	main()
