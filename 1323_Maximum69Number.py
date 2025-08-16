num = 9996

def maximum69Number (num: int) -> int:
    str_num = str(num)
    for i, nume in enumerate(str_num):
        if nume == '6':
            result = str_num[:i] + '9' + str_num[i+1:]
            return int(result)
    return num
            


print(maximum69Number(num))