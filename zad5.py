a = 45

try:
	f = [2, 3, 4]
	b = f[3]
	
except IndexError:
	print("indexer")

try:
	print(x)
except NameError:
	print("namer")

try:
	a = a + "s"
except TypeError:
	print("typeer")