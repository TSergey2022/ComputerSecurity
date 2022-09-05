A6T = "abcdefghijklmnopqrstuvwxyz"
C3T_A6T = "uyhkfztanbwsqmrljcvpoxgdei"

def crypt(text):
  rez=""
  for ch in text:
    if ch in A6T:
      rez+=C3T_A6T[A6T.find(ch)]
    else:
      rez+=ch
  return rez
def decrypt(text):
  rez=""
  for ch in text:
    if ch in C3T_A6T:
      rez+=A6T[C3T_A6T.find(ch)]
    else:
      rez+=ch
  return rez

if __name__ == "__main__":
  txt = "abc xyz hello world"
  print(txt)
  crypted = crypt(txt)
  print(crypted)
  print(decrypt(crypted))