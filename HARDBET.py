for _ in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[2] < nums[1] and nums[2] < nums[0]:
        print('Alice')
    elif nums[1] < nums[2] and nums[1] < nums[0]:
        print('Bob')
    else:
        print('Draw')