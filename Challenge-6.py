ip = int(input())
cnt = 0
div = 5
while(ip/div >0):
    cnt += int(ip/div)
    div *=5
print(cnt)
