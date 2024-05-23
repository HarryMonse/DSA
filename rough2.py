# Number Plate

ans = []
res = 0
for i in range(5000,9999):
    for j in str(i):
        while len(str(i)) != 0:
            res += int(str(i))[1]
            i = str(i)[1:]

        while len(str(res)) != 1:
            res += int(str(res))[1]
            res = str(res)[1:]

        ans.append(int(i))
print(ans)




#             res += int(j)
#             if len(res) != 1:
#                 i = res
#         ans.append(int(i))
# print(ans)
