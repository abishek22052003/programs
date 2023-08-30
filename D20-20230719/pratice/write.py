file=open("/home/abishek/text/karka.txt","w")
print(file.write("I am Abishek \n"))
print(file.write("I am studing at karka software academy \n"))
file.close()
file=open("/home/abishek/text/karka.txt","r")
print(file.read())
file=open("/home/abishek/text/karka.txt","a")
print(file.write("I'm from Nagercoil"))
file=open("/home/abishek/text/karka.txt","r")
for line in file:
    print(line.split())
    # print(line)

