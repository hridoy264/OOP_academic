while True:
    user_input = input()
    
    if user_input.strip() == "STOP":
        break
    
    nums = list(map(int, user_input.split()))
    N = len(nums)
    
    abs_differences = set()
    for i in range(N - 1):
        diff = abs(nums[i] - nums[i + 1])
        abs_differences.add(diff)
        
    expected_differences = set(range(1, N))
    
    if abs_differences == expected_differences:
        print("UB Jumper")
    else:
        print("Not UB Jumper")