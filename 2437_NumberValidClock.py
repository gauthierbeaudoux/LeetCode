time = "?5:00"
time = "??:??"


def countTime(time: str) -> int:
    result_list = list(time)
    result_list.pop(2)

    for i in range(len(result_list)):
        if result_list[i] == '?':
            if i == 0:
                result_list[i] = [0, 1, 2]
            elif i == 2:
                result_list[i] = [i for i in range(6)]
            else:
                result_list[i] = [i for i in range(10)]
        else:
            result_list[i] = [int(result_list[i])]
    
    result_hour = 0
    for i in result_list[0]:
        for j in result_list[1]:
            if i*10 + j >= 0 and i*10 + j <= 23:
                result_hour += 1


    result_minutes = len(result_list[2])*len(result_list[3])

    return result_hour*result_minutes
    


print(countTime(time))