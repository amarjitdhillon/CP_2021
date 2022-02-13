class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:     
        # Sort the meeting times by the start time first
        intervals.sort()
          
        # We iterate from the second meeting time till the last meeting time. The logic is that the start time for the current meeting should be more than the end time of the previous meeting 
        for x in range(1,len(intervals)): 
            startTimeCurrentMeeting = intervals[x][0] 
            endTimePrevMeeting      = intervals[x-1][1]
            # if start Time of Current Meeting is less then the end Time of Prev Meeting, it means the person won't be able to attend that meeting
            if startTimeCurrentMeeting < endTimePrevMeeting:
                return False
        # if all meetings can be attended, return True
        return True
            