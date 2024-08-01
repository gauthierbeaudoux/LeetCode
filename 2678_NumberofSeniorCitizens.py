details = ["7868190130M7522","5303914400F9211","9273338290F4010"]

def countSeniors(details: list[str]) -> int:
    result = 0
    for i in details:
        # print(i[11:13])
        if int(i[11:13]) > 60:
            result += 1
    return result

print(countSeniors(details))