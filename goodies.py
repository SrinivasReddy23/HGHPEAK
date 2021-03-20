inp1 = input().split()

n=int(inp1[-1])

inp2 = input()

inp3=input().split()

di = {}
val=[]
out=[]

while len(inp3)>0: 
    key = ' '.join(inp3[:len(inp3)-1])
    di[key]=int(inp3[-1])
    val.append(int(inp3[-1]))
    try:
    	inp3=input().split()
    except:
    	break

for i in range(len(val)):
    for j in range(i+1,len(val)):
        if val[i]>val[j]:
            t=val[i]
            val[i]=val[j]
            val[j]=t

st,end=-1,-1
mini=10000000
for i in range(len(val)-n+1):
    ll=val[i:i+n]
    if abs(ll[0]-ll[-1])<mini:
        mini=abs(ll[0]-ll[-1])
        st=i
        end=i+n-1

for i in range(st,end+1):
    out.append(val[i])
    


res="The goodies selected for distribution are: \n"

for i in out:
    for j in di.items():
        if i==j[1]:
            res+=str(j[0])+" "+str(i)+"\n"

res+="And the difference between the chosen goodie with highest price and the lowest price is "+str(abs(out[0]-out[-1]))

print(res)
