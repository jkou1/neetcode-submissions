import heapq
class Twitter:

    def __init__(self):
        self.users = []
        self.followDict = {}
        self.allPosts = [] #dictionary of all poster IDs and the corresponding tweet ID as the value
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.allPosts, (-self.time, userId, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time += 1
        resList = []
        poppedPosts = []

        while self.allPosts:
            curPost = heapq.heappop(self.allPosts)
            heapq.heappush(poppedPosts, curPost)
            if (curPost[1] == userId or curPost[1] in self.followDict.get(userId, set())) and len(resList) < 10:
                resList.append(curPost[2])
        
        if poppedPosts:
            while poppedPosts:
                curPost = heapq.heappop(poppedPosts)
                heapq.heappush(self.allPosts, curPost)
        
        return resList

            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followeeId not in self.followDict.get(followerId, set()):
            self.followDict.setdefault(followerId, set()).add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followeeId in self.followDict.get(followerId, set()):
            self.followDict[followerId].remove(followeeId)
        
