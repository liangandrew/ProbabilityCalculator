import math

def choose(n,k):
    "Combination n choose k"
    n = int(n)
    k = int(k)
    top = math.factorial(n)
    bottom = math.factorial(k) * math.factorial(n - k)
    print(top/bottom)
    print("\n")

def perm(n,k):
    "Permutation n p k"
    n = int(n)
    k = int(k)
    top = math.factorial(n)
    bottom = math.factorial(n-k)
    print(top/bottom)
    print("\n")

flag = True
print("Permutation and Combination Calculator")
print("Commands:\n (nCk) Combination \n (nPk) Permutation \n (q) quit \n")

while flag:
    prob = input("")

    if "c" in prob:
        ex = prob.split("c",1)
        n = ex[0]
        k = ex[-1]
        if k > n:
            print("k cannot be greater than n")
        else:
            choose(n,k)

    if "p" in prob:
        ex = prob.split("p",1)
        n = ex[0]
        k = ex[-1]
        if k > n:
            print("k cannot be greater than n")
        else:
            perm(n,k)

    if "q" in prob:
        flag = False
