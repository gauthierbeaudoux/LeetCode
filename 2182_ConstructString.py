s = "cczazcc"
s = "aababab"
s = "xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt"
repeatLimit = 1

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    s_set = set(s)
    test = {alpha: s.count(alpha) for alpha in s_set}
    print(test)
    result = ""
    while test:
        maxi = max(test)
        if repeatLimit >= test[maxi]:
            result += maxi*test[maxi]
            test.pop(maxi)
        else:
            result += repeatLimit*maxi
            test[maxi] -= repeatLimit
            if test[maxi] == 0:
                test.pop(maxi)
            else:
                max_global = max(test)
                donnee = test.pop(max_global)
                if test:
                    maxi = max(test)
                    result += maxi
                    test[maxi] -= 1
                    if test[maxi] == 0:
                        test.pop(maxi)
                    test[max_global] = donnee
                else:
                    return result
    return result

print(repeatLimitedString(s, repeatLimit))