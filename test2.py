word1 = "2c6ac23e4ffdf95f08f369eca6488b585bca0def0ddfe69f525e40d4aa2509d3"

from Crypto.Hash import SHA256

def hash(s):
   h = SHA256.new()
   h.update(s)
   return h.hexdigest()

x = hash("crane".strip().encode().lower())

if (word1[2] == x[2]) and (word1[4] == x[4]):
    print("H")