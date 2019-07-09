# # du
# s = open('txt.txt')
# content = s.read()
# s.close()
# print (content)

# 写
f = open('txt.txt', 'a')
f.writelines(['w是覆盖', 'a是覆盖'])
f.close()
s = open('txt.txt')
content = s.read()
s.close()
print(content)