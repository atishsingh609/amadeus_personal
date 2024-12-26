"""
Facebook, Google, Microsoft, Amazon

Given a square matrix, turn it by 90 degrees in clockwise direction without using any extra space.

a = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    14,15,16,17]]

o/p :- [[14,9,5,1]
        [15,10,6,2]
        [16,11,7,3]
        [17,12,8,4]]
Algo:
First rotate the outer layer.
then rotate the inner layer.


Intuition
What if we only consider outermost square (0 to n-1). There we need to shift all elements by n-1 positions.
Element in 0,0 will be shifted to 0,n-1
Element in n-1,0 will be shifted to n-1,n-1
Element in n-1,n-1 will be shifted to n-1,0
Element in n-1,0 will be shifted to 0,0
For non corner elements what if we have an shift variable which we can add or subtract to get them to their desired places. This varibale can be received by getting the number of elements in a side of a square
Suppose we are done shifting outermost elements, we need to go inside, which means we are dreacsing rows and columns by 2 (1 from start and one from end) Hence new square will be (1 to n-2)
"""

def rotate_matrix(a, n):
    print("matrix before rotation", a)
    for i in range(int(n/2)):
        for j in range(i, n-1-i):
            temp = a[j][n-1-i]
            a[j][n-1-i] = a[i][j]
            a[i][j] = a[n-1-j][i]
            a[n-1-j][i] = a[n-1-i][n-1-j]
            a[n - 1 - i][n - 1 - j] = temp

    print("matrix after rotation", a)

a = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [14,15,16,17]]
# a = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(a, 4)
