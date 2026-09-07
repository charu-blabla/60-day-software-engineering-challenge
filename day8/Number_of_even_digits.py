arr = list(map(int, input("Enter the array elements: ").split))
count=0
for i in arr:
	c=0
	while i>0:
		c+=1
		i//=10
	if c%2==0:
		count+=1
print(count)
