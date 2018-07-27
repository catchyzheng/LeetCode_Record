'''
基本一样，唯一区别在于把hash size从1万开到10万，就过了。。

'''
class BloomHash:
    def __init__(self, c, s):
        self.hash_size = c
        self.seed = s
    
    def getHash(self, str):
        res = 0
        for c in str:
            res = (res * self.seed + ord(c))%self.hash_size
        return res

class CountingBloomFilter:
    """
    @param: k: An integer
    """
    capacity = 100000
    hashCollections = []
    count = [0] * capacity
    def __init__(self, k):
        for i in range(k):
            self.hashCollections.append(BloomHash(self.capacity, 2*i+39))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for hash_func in self.hashCollections:
            self.count[hash_func.getHash(word)] += 1
                

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        for hash_func in self.hashCollections:
            self.count[hash_func.getHash(word)] -= 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for hash_func in self.hashCollections:
            if self.count[hash_func.getHash(word)] == 0:
                return False
        return True
