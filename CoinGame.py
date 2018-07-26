from numpy.random import randint
from matplotlib import pyplot

m = int(input('Enter number of coins per student:'))
n = int(input('Enter number of students:'))
iters = int(input('Enter number of iterations:'))
students = [m] * n

for i in range(iters):
    toss = randint(0, 2)
    s1, s2 = randint(0, n, 2)
    if toss and students[s2]:
        students[s1] += 1
        students[s2] -= 1
    elif (not toss) and students[s1]:
        students[s1] -= 1
        students[s2] += 1
students.sort()

with pyplot.xkcd():
    pyplot.scatter(range(n), students[::-1], marker='.', color='r')
    pyplot.xlabel('Student Rank')
    pyplot.ylabel('Coins owned after ' + str(iters) + ' iterations')
    pyplot.show()
