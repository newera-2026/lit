def isPalindrome(self, s: str) -> bool:
    if len(s) == 0:
        return True
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    l,r = 0,len(s)-1
    while r > l:
        if s[l] == s[r]:
            l+=1 
            r-=1
            continue
        else :
            return False
    return True