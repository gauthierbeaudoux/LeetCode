text1 = "abcde"
text2 = "ace"

text1 = "ezupkr"
text2 = "ubmrapg"



def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text1) <= len(text2):
        text_court = text1
        text_long = text2
    else:
        text_court = text2
        text_long = text1

    char_to_delete = []
    for lettre in text_court:
        if lettre not in text_long:
            char_to_delete.append(lettre)
    for lettre in char_to_delete:
        text_court = text_court.replace(lettre, '')

    char_to_delete = []
    for lettre in text_long:
        if lettre not in text_court:
            char_to_delete.append(lettre)
    for lettre in char_to_delete:
        text_long = text_long.replace(lettre, '')


    def dynamic_approach(text_court, text_long):
        if len(text_long) < len(text_court):
            text_court, text_long = text_long, text_court

        if text_court in text_long:
            return min(len(text_court),len(text_long))
        else:
            longueur_max = -1
            for i in range(len(text_long)):
                longueur_max = max(longueur_max, dynamic_approach(text_court, text_long[:i] + text_long[i+1:]))
            return longueur_max


    return dynamic_approach(text_court, text_long)

print(longestCommonSubsequence(text1, text2))