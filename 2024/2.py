def check_valid(levels):
        
    valid = True
    increasing = levels[0] < levels[1]

    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])

        # Check if the difference is outside the allowed range
        if diff < 1 or diff > 3:
            valid = False
            break

        # Check the trend (increasing or decreasing)
        if increasing:
            if levels[i] <= levels[i - 1]:  # Should be strictly increasing
                valid = False
                break
        else:
            if levels[i] >= levels[i - 1]:  # Should be strictly decreasing
                valid = False
                break
    return valid

with open('2.in', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    ans = 0

    for line in lines:
        levels = list(map(int, line.split()))  # Convert levels to integers
        if len(levels) < 2:
            continue  # Skip lines with fewer than 2 levels
        
        valid = True
        increasing = levels[0] < levels[1]

        if check_valid(levels):
            ans += 1
            continue 

    print(ans)

    ans = 0

    for line in lines:
        levels = list(map(int, line.split()))  # Convert levels to integers
        if len(levels) < 2:
            continue  # Skip lines with fewer than 2 levels
        
        valid = True
        increasing = levels[0] < levels[1]

        if check_valid(levels):
            ans += 1
            continue
        else:
            for i in range(len(levels)):
                levelCopy = levels.copy()
                levelCopy.pop(i)
                if check_valid(levelCopy):
                    ans += 1
                    break

    print(ans)


