class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count=0
        for val in hours:
            if val>=target:
                count += 1
        return count
        