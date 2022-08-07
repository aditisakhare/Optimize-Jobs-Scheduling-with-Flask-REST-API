from typing import List

class SpaceshipRental:
    def spaceship_scheduling(self, names: List[str], startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Calculates the optimal profit for renting spaceship
        Input: 
            names: names of jobs 
            startTime: start time of jobs
            endTime: end time of jobs
            profit: profit for renting spaceships
        Output:
            Total Profit
            Optimal Path
        Time Complexity: o(n log n)
        """
        n = len(profit)
        jobs = [(startTime[i],endTime[i],profit[i],names[i]) for i in range(n)]
        jobs.sort(key = lambda x: x[1])
        
        def binarySearch(x,low,high):
            
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= x : low = mid + 1
                else: high = mid - 1
            
            return high

        path = [[]] * n
        total_profit = [0]*n
        for index in range(n):
            
            i = binarySearch(jobs[index][0] , 0 , index - 1)
            to_add = total_profit[i] if i != -1 else 0
            total_profit[index] = max(total_profit[index-1],jobs[index][2] + to_add)

            if total_profit[index-1] > (jobs[index][2] + to_add):
                path[index] = path[index-1]
            else:
                path[index] = path[i] + [jobs[index][3]]


        return total_profit[-1], path[-1]