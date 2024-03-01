class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        frst, scnd = inf, inf
        
        for thrd in nums:
            
            if scnd < thrd: 
                return True
            if thrd <= frst:
                frst = thrd    
            else:  
                scnd = thrd 
                
        return  False