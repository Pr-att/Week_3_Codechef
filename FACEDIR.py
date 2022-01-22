for _ in range(int(input())):
    nums = int(input())
    if nums % 4 == 2:
        print('South')
    elif nums % 4 == 1:
        print('East')
    elif nums % 4 == 3:
        print('West')
    else:
        print('North')
