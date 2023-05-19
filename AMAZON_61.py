def max_distance(n, seats)
    left = [-1] * n  # stores the closest person to the left of the seat
    right = [-1] * n  # stores the closest person to the right of the seat
   
    # find the closest person to the left of each seat
    for i in range(n):
        if seats[i] == 1:
            left[i] = i
        elif i > 0:
            left[i] = left[i-1]
   
    # find the closest person to the right of each seat
    for i in range(n-1, -1, -1):
        if seats[i] == 1:
            right[i] = i
        elif i < n-1:
            right[i] = right[i+1]
   
    # compute the maximum distance to the closest person for each empty seat
    max_dist = 0
    for i in range(n):
        if seats[i] == 0:
            dist_left = i - left[i] if left[i] >= 0 else float('inf')
            dist_right = right[i] - i if right[i] >= 0 else float('inf')
            max_dist = max(max_dist, min(dist_left, dist_right))
   
    return max_dist

# Example usage
n = int(input())
seats = list(map(int, input().split()))
print(max_distance(n, seats))  # Output: 1
