for _ in range(int(input())):
    nums = input().split()
    if int(nums[0]) + int(nums[2]) == 180 and int(nums[1]) + int(nums[3]) == 180:
        print('YES')
    else:
        print('NO')