class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # zip the time, user and website to one list
        tuw = list(zip(timestamp,username,website))

        # we need to sort them by time --> username --> website
        sorted_tuw = sorted(tuw)

        # We will polulate a user history hashmap of various pages visited. The hashmap is of type {user: [pages]}
        user_history = defaultdict(list)
        for t, u, w in sorted_tuw:
            user_history[u].append(w)

        # get various combinations possible for various users
        patternCount = defaultdict(int)
        for user,pages in user_history.items():
            
            # get various combinations possible for various users in the pair of 3 and add them to set so that they are unique
            userCombinations = set(combinations(pages,3))
            
            # for every pair of userCombination, we will update the count. This count will make sense for second user onwards having the same pattern
            for userCombination in userCombinations:
                patternCount[userCombination] += 1
        
        # We need to sort both the keys(pattern lexographically) from from min to max and values(score) form max to min 
        # If we inverse the values of keys from val to -val, then we can sort both of them in ascending order, using minhea
        # here invertedValues represent the values with -ve sign added to it
        invertedValues = [-x for x in patternCount.values()]
        
        # Zip both the keys and values so that we can sort them. We are placing invertedValues first as we first need to sort by score and then need to sort lexographically in natural order
        c = list(zip(invertedValues, patternCount.keys()))
        
        # Heapify will sort them in the ascending order as this is min heapify operation and will take nlog(n) time
        heapq.heapify(c)

        # Top of the heap will represent the sorted value by -ve score, we can return the second element from this popped element 
        return heapq.heappop(c)[1]
