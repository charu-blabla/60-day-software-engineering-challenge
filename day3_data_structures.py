arr =[23,46,87,92,12,58]
max=arr[0]
min =arr[0]
sum=0
freq={}
rev=[]
for num in arr:
    sum+= num
    if num>max:
        max=num
    if num<min:
        min=num
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

for num in range (len(arr),-1,,-1):
    rev.append(arr(num))

print(f"sum: {sum}\nmax: {max}\nmin: {min}\n")
for f in arr:
    print(f"{f}:{freq[f]}")

print(f"orignal list: {arr}\nreversed list: {rev}")

