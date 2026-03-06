

def checkOnesSegment(s: str) -> bool:
        is_one = False
        i = 0
        while i < len(s):
            if not is_one and s[i] == '1':
                is_one = True
                while i < len(s) and s[i] == "1":
                    i += 1
            elif s[i] == '1' and is_one:
                return False

            i += 1
        
        return True
    
    
s = "1001"
print(checkOnesSegment(s))