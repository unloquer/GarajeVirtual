def readtxtline(name):
	with open(name, 'r') as file:
		return str(file.readline())
def writetxt(name,content):
	content = str(content)
	with open(name, 'w') as file:
		file.write(content)
		file.close()
def getAuthFile(name):
	auth = []
	with open(name, 'r') as file:
		for i in file.readlines():
			auth.append(i.replace("\n",""))
		return auth