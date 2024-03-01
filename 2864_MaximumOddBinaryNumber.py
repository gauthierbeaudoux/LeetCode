from collections import Counter

s = "010"

def maximumOddBinaryNumber(s: str) -> str:
    freq_s = Counter(s)
    return (freq_s['1']-1)*'1' + freq_s['0']*'0' + '1'


print(maximumOddBinaryNumber(s))