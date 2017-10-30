class Solution:
    stack=[]
    queue=[]
    def pushCharacter(self,char):
        self.stack.append(char)
    def enqueueCharacter(self,char):
        self.queue.insert(0,char)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop()