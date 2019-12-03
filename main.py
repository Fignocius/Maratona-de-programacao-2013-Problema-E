def buscar(n, r, inteiros):
    if r == len(inteiros):
        if n == r:
            return "*"
        ret = []
        for i in range(1, n + 1):
            if i not in inteiros:
                ret.append(i)
        string = ' '.join(map(str, ret)) + ' '
        return string
    else:
        return False

#n, r = input("Entradas ").split(' ')
#inteiros = list(map(int, input("Restantes ").split()))
#print(buscar(int(n), int(r), inteiros))