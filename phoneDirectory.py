# Time Complexity: O(1)
# Space Complexity: O(N) N is the maxNumbers

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.hSet = set()
        self.q = deque()
        for i in range(maxNumbers):
            self.q.append(i)
            self.hSet.add(i)


    def get(self) -> int:
        if not self.q: 
            return -1
        curr = self.q.popleft()
        self.hSet.remove(curr)
        return curr


    def check(self, number: int) -> bool:
        return number in self.hSet

    def release(self, number: int) -> None:
        if number not in self.hSet:
            self.q.append(number)
            self.hSet.add(number)
            


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)