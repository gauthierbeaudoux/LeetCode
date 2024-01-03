bank = ["011001","000000","010100","001000"]


def numberOfBeams(bank: list[str]) -> int:
    result = 0
    prec_nb_1 = 0
    for i in bank:
        nber_of_1 = i.count('1')
        if nber_of_1 > 0:
            result += prec_nb_1*nber_of_1
            prec_nb_1 = nber_of_1
    return result

print(numberOfBeams(bank))