class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # zip the time, user and website to one list
        tuw = list(zip(timestamp,username,website))

        # we need to sort them by time --> username --> website
        sorted_tuw = sorted(tuw)

        # get a user history hashmap of various pages visited. The hashmap is of type {user: [pages]}
        user_history = defaultdict(list)
        for t, u, w in sorted_tuw:
            user_history[u].append(w)

        # print("user_history= ", user_history)

        # get various combinations possible for various users
        patternCount = defaultdict(int)
        for user,pages in user_history.items():
            comb = set(combinations(pages,3))
            for c in comb:
                patternCount[c] += 1
        
        values = [-x for x in patternCount.values()]
        c = list(zip(values, patternCount.keys()))
        heapq.heapify(c)

        return heapq.heappop(c)[1]
