N = int(input())

for i in range(1,N+1):
    if i == 1:
        result = "* " * N
    elif i == N:
        spaces = "  " * (N - 1)
        result = spaces + "* " 
    else:
        spaces = "  " * (i - 1)
        hellow = "  " * (N - i - 1)
        result = spaces + "* " + hellow + "* "
    print(result)