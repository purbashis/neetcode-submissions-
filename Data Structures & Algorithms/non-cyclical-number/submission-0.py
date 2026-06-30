class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:      # Check FIRST
                return False
            seen.add(n)        # Then add
            
            n = sum(int(d)**2 for d in str(n))
        
        return True

    

        