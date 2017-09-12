# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#

#   0 1 2 3
#   -----------
#   1 0 0 0 - 0
#   0 1 0 0 - 1
#   0 0 1 0 - 2
#   0 0 0 1 - 3
#
# - Print this two dimensional list to the output

# matrix = [[],[],[],[]]
# for i in range(len(matrix)):
#     matrix[i] = [0,0,0,0]
#     matrix[i][i]+=1
#     print(matrix[i])


matrix = []
for row in range(4):
    a = []
    for i in range(4):
        if row == i:
            a.append(1)
        else:
            a.append(0)
    matrix.append(a)
        
    print(a)
# print(matrix)