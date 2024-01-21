nums = [1,2,3,1]
nums = [2,7,9,3,1]

def rob(nums: list[int]) -> int:
    global mem_liste_passee
    mem_liste_passee = {}

    def calcul_rob(nums):
        bin_val = hash(tuple(nums))
        if len(nums) == 0:
            return 0
        elif bin_val in mem_liste_passee.keys():
            return mem_liste_passee[bin_val]
        else:
            max_cout = -1
            for j in range(len(nums)):
                nums_copy = nums[:]
                if j == 0:
                    del nums_copy[0:2]
                elif j == len(nums_copy)-1:
                    del nums_copy[j-1:j+1]
                else:
                    del nums_copy[j-1:j+2]
                cout = nums[j] + calcul_rob(nums_copy)
                if max_cout == -1 or cout > max_cout:
                    max_cout = cout
        mem_liste_passee[bin_val] = max_cout
        return max_cout
    
    return calcul_rob(nums)

print(rob(nums))