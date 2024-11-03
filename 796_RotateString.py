s = "abcde"
goal = "cdeab"

def rotateString(s: str, goal: str) -> bool:
    return False if len(s) != len(goal) else s in goal+goal
        
    
        
        

print(rotateString(s, goal))