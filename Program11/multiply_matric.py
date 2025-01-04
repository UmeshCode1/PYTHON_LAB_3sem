# Write a python program to multiply.


def multiply_matrix(X, Y):
  result = [[0,0,0],
            [0,0,0],
            [0,0,0]]
  for i in range(len(X)):
    for j in range(len(Y[0])):
      for k in range(len(Y)):
        result[i][j] += X[i][k] * Y[k][j]
  return result

X = [[1,2,3],
      [4,5,6],
      [7,8,9]]
Y = [[1,2,3],
      [4,5,6],
      [7,8,9]]

result = multiply_matrix(X, Y)
for r in result:
  print(r)
  