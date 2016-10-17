
path = r'E:\Project\Python\today\ex_file.txt'
f = open(path,'w')
f.write('Hello')
f.write('World!')
print type(f)
f.close()


f = open(path)
print f.read()
