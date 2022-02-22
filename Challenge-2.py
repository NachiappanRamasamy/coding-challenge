ip = input()
cnt = 1
if(len(ip)==1):
    print(ip+str(cnt),end='')    
else:
    for i in range(1,len(ip)):
        if(ip[i]==ip[i-1]):
            cnt +=1
        else:
            print(ip[i-1]+str(cnt),end='')
            cnt=1
        if(i == len(ip)-1):
            if(ip[i]==ip[i-1]):
                print(ip[i-1]+str(cnt),end='')
            else:
                print(ip[i]+str(cnt),end='')
            break
