# sentence="Hai I'm Niranjan and im from Nagercoil"
# word=sentence.split()
# long_word=max(word,key=len)
# print(long_word)

sentence="Hai I'm Niranjan and im from Nagercoil"
splitting=sentence.split()
new=""
num=0
for i in splitting:
    strlen=len(i)
    if strlen>num:
        new=i
print(new)
    

