from collections import Counter, defaultdict

def findSubstring(s: str, words: list[str]) -> list[int]:
    occ_total = Counter("".join(words))
    freq_words = defaultdict(int)
    for word in words:
        freq_words[word] += 1

    long_mot = len(words[0])
    nb_mots = len(words)
    long_tot = long_mot*nb_mots
    
    memo = Counter(s[:long_tot])
    result = []
    
    i = 0
    while i + long_tot <= len(s):
        if memo == occ_total:
            count_word = defaultdict(int)
            for j in range(nb_mots):
                mot = s[i+j*long_mot:i+long_mot+j*long_mot]
                if mot in words:
                    count_word[mot] += 1
                else:
                    break
            if count_word == freq_words:
                result.append(i)
            
        if i + long_tot == len(s):
            break
        memo[s[i]] -= 1
        if memo[s[i]] == 0:
            del memo[s[i]]
        memo[s[i+long_tot]] += 1
        
        i += 1
    
    return result
    


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(findSubstring(s, words))