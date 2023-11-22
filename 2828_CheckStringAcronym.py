words = ["alice","bob","charlie"]
s = "abc"


def isAcronym(words: list[str], s: str) -> bool:
    # sortie = ''
    # for mot in words:
    #     sortie += mot[0]
    # return sortie == s
    return ''.join(mot[0] for mot in words) == s
    


print(isAcronym(words, s))