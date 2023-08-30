def dictionary(a):
    splitting=string.split()
    new={}
    for i in splitting:
        if i in new:
            new[i]=new[i]+1
        else:
            new[i]=1
    return new
string="the quick brown fox jumps over the lazy dog the quick brown fox"
check=dictionary(string)
print(check)