ip = input()
splitted_words =ip.split(' ')
m = 0
for i in range(1,len(splitted_words)):
    if(len(splitted_words[i]) > len(splitted_words[m])):
        m = i
print(splitted_words[m] +' '+ str(len(splitted_words[m])))   
