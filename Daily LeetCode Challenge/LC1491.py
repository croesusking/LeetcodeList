class Solution:
    def average(self, salary: List[int]) -> float:
        #1491. Average Salary Excluding the Minimum and Maximum Salary
        salary.sort()
        return (sum(salary[1:-1])/(len(salary)-2))