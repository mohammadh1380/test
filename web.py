import stdio
n=stdio.readInt()
link_count=[[0]*n for i in range(n)]
out_degrees=[0]*n
while not stdio.isEmpty():
    i=stdio.readInt()
    j=stdio.readInt()
    out_degrees[i]+=1
    link_count[i][j]+=1
print('%d %d' %(n,n))
for i in range(n):
    for j in range(n):
        p=0.9*(link_count[i][j]/out_degrees[i])+0.1/n
        print('%8.5f' %p,end='')
    print()