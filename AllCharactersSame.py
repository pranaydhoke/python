def allCharacterSame(s):
    n=len(s)
    for i in range(1,n):
        if s[i] !=  s[0]:
            return False
    return True

if __name__=="__main__":

    s="kkkkkkkkkk"
    if allCharacterSame(s): 
        print("all are same")
    else:
        print("not same")
