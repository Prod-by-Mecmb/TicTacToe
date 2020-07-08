b = ['_' for i in range(9)]

print('---------')
print(f'''| {" ".join(b[:3]).replace("_", " ")} |
| {" ".join(b[3:6]).replace("_", " ")} |
| {" ".join(b[6:9]).replace("_", " ")} |''')
print('---------')

matrix = [(x, y) for y in (3, 2, 1) for x in (1, 2, 3)]
test = dict(zip(matrix, b))
nomer_xoda = 1

def pole_stage():
    global test
    print('---------')
    print(f'''| {' '.join(list(test.values())[:3]).replace("_", " ")} |
| {' '.join(list(test.values())[3:6]).replace("_", " ")} |
| {' '.join(list(test.values())[6:9]).replace("_", " ")} |''')
    print('---------')

xwins = 0
owins = 0
res = ''

while res not in ['X wins', 'O wins', 'Draw']:

    pomogite = [x for x in input('Enter the coordinates: ').split()]
    if any([x.isalpha() for x in pomogite]):
        print('You should enter numbers!')
    elif any(int(x) > 3 for x in pomogite):
        print('Coordinates should be from 1 to 3!')
    else:
        pomogite = tuple([int(x) for x in pomogite])
        if test.get(pomogite) == '_' and nomer_xoda % 2 != 0:
            test[pomogite] = 'X'
            nomer_xoda += 1
            pole_stage()
            if test[(1,3)] == test[(2,2)] == test[(3,1)] == 'X' or test[(3,3)] == test[(2,2)] == test[(1,1)] == 'X':
                res = 'X wins'
                print(res)
            else:
                for i in range(1, 4):
                    if test[(i,1)] == test[(i,2)] == test[(i,3)] == 'X' or test[(1,i)] == test[(2,i)] == test[(3,i)] == 'X':
                        res = 'X wins'
                        print(res)
        elif test.get(pomogite) == '_' and nomer_xoda % 2 == 0:
            test[pomogite] = 'O'
            nomer_xoda += 1
            pole_stage()
            if test[(1,3)] == test[(2,2)] == test[(3, 1)] == 'O' or test[(3,3)] == test[(2,2)] == test[(1,1)] == 'O':
                res = 'O wins'
                print(res)
            else:
                for i in range(1, 4):
                    if test[(i,1)] == test[(i,2)] == test[(i,3)] == 'O' or test[(1,i)] == test[(2,i)] == test[(3,i)] == 'O':
                        res = 'X wins'
                        print(res)
        elif all([value != "_" for value in test.values()]):
            res = 'Draw'
            print(res)
        else:
            print('This cell is occupied! Choose another one!')
