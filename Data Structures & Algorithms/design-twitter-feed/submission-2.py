from collections import deque
import heapq
class Twitter:

    def __init__(self):
        self.TID_ALL = 0

        self.user_post = {}
        self.user_following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        user_posts = self.user_post.get(userId, deque())
        if len(user_posts)==10:
            user_posts.popleft()
        user_posts.append([self.TID_ALL, tweetId])
        self.user_post[userId] = user_posts
        self.TID_ALL += 1
        # print('Post', self.user_post)

    def getNewsFeed(self, userId: int) -> List[int]:
        followings = self.user_following.get(userId, set())
        followings.add(userId)

        heap = []
        for user in followings:
            user_posts = self.user_post.get(user, deque())
            post_num = len(user_posts)
            if post_num > 0:
                latest = user_posts[post_num-1]
                            # TID_ALL,  tweetId  , userID, index of tweet id
                heap.append([-latest[0], latest[1], user, post_num-1])
        heapq.heapify(heap)
        
        res = []
        while heap and len(res)<10:
            print('heap', heap)
            _, tweetId, userId, idx = heapq.heappop(heap)

            res.append(tweetId)
            if idx>0:
                user_posts = self.user_post[userId]
                next_record = user_posts[idx-1]
                heapq.heappush(heap, [-next_record[0], next_record[1], userId, idx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        followings = self.user_following.get(followerId, set())
        followings.add(followeeId)
        self.user_following[followerId] = followings
        # print('follow', self.user_following)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followings = self.user_following.get(followerId, set())
        # print('before unfollow', self.user_following, followerId, followeeId)
        if followeeId in followings:
            followings.remove(followeeId)
            self.user_following[followerId] = followings
        # print('unfollow', self.user_following)
        
        
