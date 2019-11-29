# pallindrome
def solve(strn):

    l = len(strn)
    mxl = 0
    start = 0
    end = 0
    for i in range(l):
        
        # even len
        st = i-1
        en = i
        
        while st >= 0 and en < l and strn[st] == strn[en]:
            
            if en - st + 1 > mxl:
                mxl = en - st + 1
                start = st
                end = en
            
            st -= 1
            en += 1
            
        
        # odd len
        
        st = i-1
        en = i+1
        
        while st >= 0 and en < l and strn[st] == strn[en]:
            
            if en - st + 1 > mxl:
                mxl = en - st + 1
                start = st
                end = en
            
            st -= 1
            en += 1
        
    
    return strn[start : end + 1]
            
    
n = int(input())
s = input()
ans = solve(s)
print(len(ans))
print(ans)