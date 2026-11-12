import random
class RandomizedSet:

    def __init__(self):
        self.res = []
        self.mp = {}
    def search(self,val):
        return val in self.mp
        
    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.res.append(val)
        self.mp[val] = len(self.res)-1
        return True 

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        id = self.mp[val]
        self.res[id] = self.res[-1]
        self.mp[self.res[-1]] = id
        self.res.pop()
        del self.mp[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.res)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()