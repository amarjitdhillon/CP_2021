class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Solving this by using a 2d list of form [x,y]
        Here index of this list is the ith person
        x is the number of people this person trusts
        y is the number of people who trust this guy
        
        Once we create this list, then we will loop through it to find the judge
        The judge will be then person having [0, n-1] as it trusts no one and n-1 people trusts it
        """
        # special case
        if n == 1 and len(trust) == 0:
            return 1
        
        link = [[0,0] for x in range(n+1)] # create a emppty link array
        
        for x,y in trust:
            link[x][0] = link[x][0] + 1 # as this guy trusts one more person
            link[y][1] = link[y][1] + 1 # as this guy is trusted by one more person
        
        judge = -1
        for x in range(n+1):
            if link[x][0] == 0 and link[x][1] == n-1: #condition for a judge
                judge = x
                break
        return judge