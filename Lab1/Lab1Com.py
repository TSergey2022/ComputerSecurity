A6T = "abcdefghijklmnopqrstuvwxyz"
shift = -29

def crypt(text):
  rez=""
  for ch in text:
    if ch in A6T:
      rez+=A6T[(A6T.find(ch)+shift%len(A6T))%len(A6T)]
    else:
      rez+=ch
  return rez
def decrypt(text):
  rez=""
  for ch in text:
    if ch in A6T:
      rez+=A6T[(A6T.find(ch)-shift%len(A6T))%len(A6T)]
    else:
      rez+=ch
  return rez

if __name__ == "__main__":
  txt = "abc xyz hello world"
  print(txt)
  crypted = crypt(txt)
  print(crypted)
  print(decrypt(crypted))