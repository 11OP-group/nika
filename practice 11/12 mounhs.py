solutions = []

for n in range(1,13):
    for k in range(1,13):
        for m in range(1,13):
            if 28*n + 30*k + 31*m == 365: solutions.append((n,k,m))

for i in solutions:
    print(f"n = {i[0]}, k = {i[1]}, m = {i[2]}")