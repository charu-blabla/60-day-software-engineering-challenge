fileobj = open("my_file.txt","w+")

n = int(input("Enter Range: "))

for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        result ='FizzBuzz'
    elif i%5 == 0 : 
        result = 'Buzz'
    elif i%3 == 0  :
        result = 'Fizz'
    else:
        result = str(i)
    fileobj.write(result+'\n')
   
fileobj.seek(0)
print(fileobj.read())

fileobj.close()
