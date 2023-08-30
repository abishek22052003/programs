s = "abcabcbb"
new=""
for i in s:
    if i not in new:
        new=new+i
print("the answer is",new,"with the length",len(new))