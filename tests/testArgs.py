
def size():
    return 2, 3

def disp(x = None):
    if x is not None:
        print(x, end='')
    else:
        print('')

def func1(name, *argv):
    disp(name)
    for arg in argv:
        disp(arg)
    disp()

def func2(name, *argv):
    disp(f'{name}: ')
    n = len(argv)
    for i in range(0, n):
        arg = argv[i]
        if type(arg) is str:
            disp(f"'{arg}'")
        else:
            disp(arg)
        if i < n-1:
            disp(',')
    print('\n')


func1('name','a',1,'b',3, size())
func2('name','a',1,'b',3, size())