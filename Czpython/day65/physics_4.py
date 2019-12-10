import numpy as np

U = [214,214,214,214,214,164,164,164,164,164,271,271,271,271,271,265,265,265,265,265]
T = [12.6,12.51,13.46,13.70,13.94,22.27,23.36,22.95,23.95,23.94,24.59,23.16,23.19,23.31,23.10,17.31,18.31,16.45,17.76,17.11]


e = np.double(1.602176565)
Q = []
sum1 = int(0)
sum2 = int(0)
s1 = []
s2 = []

'''
s = [9.75, 9.68, 9.64, 9.39, 9.50, 23.22, 22.82, 23.48, 23.70, 22.85, 13.55, 13.44, 14.36, 14.02, 14.34, 10.74, 10.96,
     10.77, 11.06, 11.08]
'''


for u,t in zip(U,T):
    u = np.int(u)
    t = np.double(t)
    q = pow(10, 19) * 1.0218 * pow(10, -14) / pow((t * (1 + 0.0219 * pow(t, 0.5))), 1.5) / u
    Q.append(q)


for i in Q:
    s1.append(round(i/e))

for i, j in zip(Q, s1):  # zip()可以同时迭代两个list
    s2.append(i / j)
    sum1 += i / j

for i, j, k in zip(Q, s1, s2):
    print("%.2f"%i, j, "%.2f" % k)

for k in s2:
    sum2 += np.fabs(k - e)

print("%.2f" % (sum1 / 20))
print("%.2f" % (sum2 / 20))
print("%.2f" % (np.fabs((sum1 / 20 - e) / e) * 100), "%")