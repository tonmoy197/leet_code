x=123
y= str(x)
li=[]
for i in y:
    li.append(int(i))

start = 0;
end = len(li) - 1;
while (start < end):
      temp = li[start]
      li[start] = li[end]
      li[end] = temp
      start+=1
      end-=1

print(magic(li))


