digit=int(12345)
add = 0

def degit_adder(d):
    if d == 0:
        return 0


    return (d % 10) + degit_adder(d // 10)


print(degit_adder(digit))

#using for loop
# add=0
# for i in range(digit):
#
#
#     add= add +digit%10
#     # print(add)
#     digit=digit//10
#     # if digit==0:
#     #     break
#
# print(add)