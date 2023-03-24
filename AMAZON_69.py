def asteroid_collision(asteroids):
    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(asteroid)
            elif stack[-1] == -asteroid:
                stack.pop()
    return stack

# Example usage
n = int(input())
asteroids = list(map(int, input().split()))
result = asteroid_collision(asteroids)
print(*result)  # Output: 5 10
