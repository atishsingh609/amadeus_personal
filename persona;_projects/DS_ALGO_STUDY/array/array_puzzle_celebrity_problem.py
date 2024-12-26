"""
Facebook,Amazon, Microsoft, Google

There is a party of N people, where there is only one person(celebrity) is known to everyne and that person
does not know anyone in the party. We can only ask questions like "does A know B"?. Find the person(celebrity) in minimum
numbers queries.

Optimal Approach: The idea is to use two pointers, one from start and one from the end. Assume the start person is A,
and the end person is B. If A knows B, then A must not be the celebrity. Else, B must not be the celebrity.
At the end of the loop, only one index will be left as a celebrity.
Go through each person again and check whether this is the celebrity.
The Two Pointer approach can be used where two pointers can be assigned, one at the start and the other at the end, and
the elements can be compared and the search space can be reduced.


Algorithm :

Create two indices i and j, where i = 0 and j = n-1
Run a loop until i is less than j.
Check if i knows j, then i can’t be a celebrity. so increment i, i.e. i++
Else j cannot be a celebrity, so decrement j, i.e. j–
Assign i as the celebrity candidate
Now at last check that whether the candidate is actually a celebrity by re-running a loop from 0 to n-1  and
constantly checking that if the candidate knows a person or if there is a candidate who does not know the candidate,
then we should return -1. else at the end of the loop, we can be sure that the candidate is actually a celebrity.
"""


def find_celebrity(matrix, n):
    x = 0
    y = n-1
    while x < y:
        if matrix[x][y] == 1:
            x += 1
        else:
            y -= 1
    celebrity = x
    for k in range(n):
        if k != celebrity:
            if matrix[celebrity][k] == 1 or matrix[k][celebrity] == 0:
                return -1
    return celebrity


matrix = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]
print(find_celebrity(matrix, 4))