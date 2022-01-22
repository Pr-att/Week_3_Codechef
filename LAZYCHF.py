empty = []
for _ in range(int(input())):
    nums = input().split()
    empty.append(int(nums[0]) * int(nums[1]))
    empty.append(int(nums[0]) + int(nums[2]))
    print(min(empty))
    empty = []

