class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result, plogs = [], []
        
        for i, log in enumerate(logs):
            lg = log.split(" ")  # split the string over the space and convert to list
            
            if lg[1].isalpha(): # if this is a word or not: this can be checked if 2nd element is string or not?
                # tuple with 4 keys (k1,k2,k3,k4)
                # k1 for which type of logs, k2 for contents of logs, k3 for log identifier and k4 for original index in logs list
                plogs.append((0,lg[1:], lg[0],i))   
            else:
                plogs.append((1,None, None,i))  # here k2 and k3 are not required as we do not need to sort if it's a digit
                
        plogs = sorted(plogs)
        
        for plog in plogs:
            index = plog[3]              # get the index of this string in the original logs array
            result.append(logs[index])   # add the string to result list based on the index we got
        return result