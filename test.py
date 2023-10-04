# numb = input("Enter number:     ")
#
# numb2 = (numb[0:3])
# numb3 = (numb[3:])
#
# print(numb2, numb3)
# sum = (0)
# for i in numb2:
#     sum = sum + int(i)
# print(sum)
#
# sum2 = (0)
# for j in numb3:
#     sum2 = sum2 + int(j)
# print(sum2)
#
# if sum == sum2:
#     print("Your ticket is lucky")
# else:
#     print("Ticket is not lucky")


print("Enter number m:    ")
m = int(input())

print("Enter number n:    ")
n = int(input())

print("Enter number k:    ")
k = int(input())
# при условии, что k < n*m


if ((k % n == 0) or (k % m == 0)):
    print('yes')
else:
    print('no')
