from collections import Counter, defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["abets","bead","remain","betas","abed","baste","airline","leading","beast","dealing","beats","airmen","marine","single","bade","aligned"]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # result = []
    # list_result_counter = []
    # strs.sort(key=len)
    # # print(strs)
    # longueur_precedente = 0
    # j = 0
    # for mot in strs:
    #     if len(mot) > longueur_precedente:
    #         longueur_precedente = len(mot)
    #         j = len(result)
    #     occ_mot = Counter(mot)
    #     for i in range(j,len(result)):
    #         if list_result_counter[i] == occ_mot:
    #             result[i].append(mot)
    #             break
    #     else:
    #         result.append([mot])
    #         list_result_counter.append(occ_mot)
    # return result

    # Solution 10x mieux


    result = defaultdict(list)

    for mot in strs:
        mot_sorted = ''.join(sorted(mot))
        result[mot_sorted].append(mot)

    return result.values()


print(groupAnagrams(strs))