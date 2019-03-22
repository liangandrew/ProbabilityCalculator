import math

def choose(n,k):
    n = int(n)
    k = int(k)
    top = math.factorial(n)
    bottom = math.factorial(k) * math.factorial(n - k)
    print(top/bottom)

def perm(n,k):
    n = int(n)
    k = int(k)
    top = math.factorial(n)
    bottom = math.factorial(n-k)
    print(top/bottom)

flag = True
print("Permutation and Combination Calculator")

while flag:
    prob = input("")

    if "c" in prob:
        ex = prob.split("c",1)
        n = ex[0]
        k = ex[-1]
        choose(n,k)

    if "p" in prob:
        ex = prob.split("p",1)
        n = ex[0]
        k = ex[-1]
        perm(n,k)

    if "q" in prob:
        flag = False
