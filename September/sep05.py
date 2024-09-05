class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        # Calculate the total sum we need from n + m rolls
        m = len(rolls)
        total_sum = mean * (n + m)
        
        # Calculate the sum of observed rolls
        rolls_sum = sum(rolls)
        
        # Calculate the sum that the missing rolls must sum to
        missing_sum = total_sum - rolls_sum
        
        # Check if it's possible to distribute the missing sum into n rolls, where each roll is between 1 and 6
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Create a base array with all 1's
        missing = [1] * n
        
        # Distribute the remaining sum across the n rolls
        remaining_sum = missing_sum - n  # We already assigned '1' to each roll
        
        for i in range(n):
            # The maximum we can assign to the current roll is 5 (as it's already 1 and the max is 6)
            add = min(remaining_sum, 5)
            missing[i] += add
            remaining_sum -= add
            
            # If we've distributed all the remaining sum, break early
            if remaining_sum == 0:
                break
        
        return missing