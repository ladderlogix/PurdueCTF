from Crypto.Hash import SHA256
from Crypto.Random.random import randint
from collections import Counter


def green(c):   return '\033[42m' + c + '\033[0m'


def gray(c):    return '\033[40m' + c + '\033[0m'


def yellow(c):  return '\033[43m' + c + '\033[0m'

def hash(s):
   h = SHA256.new()
   h.update(s)
   return h.hexdigest()

def compare(s, s0):
   n = len(s0)
   assert len(s) == n #Make sure its the same length
   # get greens
   ans = [None]*n
   rest0 = Counter()
   for i in range(n):
      if s[i] == s0[i]: ans[i] = green(s[i])
      else: rest0.update(s0[i])
   # color rest
   for i in range(n):
      if ans[i] != None: continue
      cnt = rest0.get(s[i])
      if cnt == None or cnt == 0: ans[i] = gray(s[i])
      else:
         rest0[s[i]] -= 1
         ans[i] = yellow(s[i])
   return "".join(ans)

#x = compare("3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b", "b0fef621727ff82a7d334d9f1f047dc662ed0e27e05aa8fd1aefd19b0fff312c")


#print(x)
print(hash("intos".strip().encode().lower()))
#d7569caa21238d1ed3e018e782551055e49502cc5cee6154cee578e70d4da9f5