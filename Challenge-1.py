ip = input()
for i in range(0,len(ip),2):
    print(ip[i]*int(ip[i+1]), end='')
