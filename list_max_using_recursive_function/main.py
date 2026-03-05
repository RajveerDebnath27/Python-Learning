nums=[12,43,54,65,12,43]

# idx=len(list)

def find_max(list ,idx=0):
    if idx==len(list)-1:
        return 0
    recursive_result = find_max(list,idx+1)
    print(recursive_result)
    return max(recursive_result,list[idx])



print(find_max(nums))
# print(len(nums))

