from collections import defaultdict

def getHint(secret: str, guess: str) -> str:
    nb_bulls = 0
    nb_cows = 0
    memo_secret = defaultdict(int)
    memo_guess = defaultdict(int)
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            nb_bulls += 1
        memo_secret[secret[i]] += 1
        memo_guess[guess[i]] += 1
        
        
    for chiffre, val in memo_secret.items():
        nb_cows += min(memo_guess[chiffre], memo_secret[chiffre])
        
    return f"{nb_bulls}A{nb_cows-nb_bulls}B"

secret = "1807"
guess = "7810"
print(getHint(secret, guess))