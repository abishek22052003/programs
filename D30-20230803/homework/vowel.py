sentence= "Hai I'm Niranjan and Im from Nagercoil"
list=[]
word=""
vow_len=0
vowels=["a","e","i","o","u"]
for i in sentence:
    if i!="":
        word+=i
    else:
        list+=[word]
vow_words=""
for j in list:
    count=0
    for k in j:
        if k.lower() in vowels:
            count=count+1
    if count>vow_len:
        vow_len=count
        vow_words=j
print("maximum vowel word",vow_words) 
