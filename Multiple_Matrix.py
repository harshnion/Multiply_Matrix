#Here we take 2 matrix of which we have to do multiplication

X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[9,8],[6,5],[3,2]]

#Here we take an another matrix which will store our output
Result = [[0,0],[0,0],[0,0]]

#Here is the main concept of matrix multiplication 
for i in range (len(X)):
  for j in range (len(Y[0])):
    Result[i][j] += X[i][j] * Y[i][j]
print(Result)
# tan tana!!! you have your answer in output area
