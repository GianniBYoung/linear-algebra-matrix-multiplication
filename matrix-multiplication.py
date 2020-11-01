def matrix_multiplication(matrix1,matrix2):
    n=len(matrix1)
    output = [[0 for i in range(n+1)] for j in range(n)]

    for i in range(n):
        for k in range(len(matrix2)):
            for j in range(n+1):
                output[i][j] += matrix1[i][k] * matrix2[k][j]

    print(output)
    return output


input1 = open('input1.txt', 'r')
input2 = open('input2.txt', 'r')

rowCount=0;
firstLine=input1.readline().split(",")
input1Rows=firstLine[0]
input1Cols=firstLine[1]

firstLine=input2.readline().split(",")
input2Rows=firstLine[0]
input2Cols=firstLine[1]

if int(input1Cols) != int(input2Rows):
    print("These matrices can not be multiplied - dimension mismatch\n")
    print(input1Cols) 
    print(input2Rows)
    input1.close()

    input2.close()
    exit()


matrix1 = []
matrix2 = []

for i in range(int(input1Rows)):
    col = []
    for j in range(int(input1Cols)):
        col.append(0)
    matrix1.append(col)


for i in range(int(input2Rows)):
    col = []
    for j in range(int(input2Cols)):
        col.append(0)
    matrix2.append(col)


while rowCount !=int(input1Rows):
    row= input1.readline().strip().split(",")

    for x in range(int(input1Cols)):
        matrix1[rowCount][x] = int(row[x])
    rowCount+=1


rowCount=0

while rowCount !=int(input2Rows):
    row= input2.readline().strip().split(",")
    input2Cols=len(row)

    for x in range(input2Cols):
        matrix2[rowCount][x] = int(row[x])
    rowCount+=1



input1.close()
input2.close()

matrix_multiplication(matrix1,matrix2)
