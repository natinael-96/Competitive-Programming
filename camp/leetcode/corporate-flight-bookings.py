class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        ans = [0]*(n+1)
        for frst, last, seat in bookings:
            ans[frst-1] += seat
            ans[last] -= seat
        
        for i in range(1,n):
            ans[i] += ans[i-1]
        return ans[:-1]
