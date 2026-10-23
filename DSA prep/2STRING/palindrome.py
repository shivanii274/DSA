class palin:
    def ispalindrome(self , s):
        return s == s[::-1] 
obj = palin()
print(obj.ispalindrome("madam"))
print(obj.ispalindrome("aabbaa"))    
