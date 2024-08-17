class Solution:
    def maxPoints(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        current = [0] * width
        previous = [0] * width
        
        for level in grid:
            peak = 0
            # Forward sweep
            for i in range(width):
                peak = max(peak - 1, previous[i])
                current[i] = peak
            
            peak = 0
            # Backward sweep
            for i in range(width - 1, -1, -1):
                peak = max(peak - 1, previous[i])
                current[i] = max(current[i], peak) + level[i]
            
            previous, current = current, previous
        
        return max(previous)

def main():
    input = sys.stdin.read().strip()

    test_cases = input.splitlines()
    results = []
    for case in test_cases:
        grid = json.loads(case)
        results.append(Solution().maxPoints(grid))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)


#https://leetcode.com/problems/maximum-number-of-points-with-cost/submissions/1357852918/