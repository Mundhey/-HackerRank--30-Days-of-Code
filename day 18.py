class Solution:

    def __init__(self):
        self.stack=[]
        self.queue=[]



    def pushCharacter(self,a):
        self.stack.append(a)




    def enqueueCharacter(self,b):
        self.queue.append(b)



    def popCharacter(self):
        return (self.stack.pop(len(self.stack)-1))



    def dequeueCharacter(self):
        self.count=0

        return (self.queue.pop(self.count))










# read the string s
s= raw_input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l / 2):

    print "****"
    print obj.popCharacter()
    print "****"
    print obj.dequeueCharacter()

    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print "The word, " + s + ", is a palindrome."
else:
    print "The word, " + s + ", is not a palindrome."

