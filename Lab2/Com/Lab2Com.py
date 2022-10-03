A6T = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
words = ['добр', 'дмитрий']

def decrypt(text, shift):
  rez=""
  for ch in text:
    if ch in A6T:
      rez+=A6T[(A6T.find(ch)-shift)%len(A6T)]
    else:
      rez+=ch
  return rez

if __name__ == "__main__":
  with open('in.txt', 'r', encoding="utf-8") as file:
    text = file.read().split('\n')

  for crypted_text in text:
    print(crypted_text)
    for i in range(len(A6T)):
      src_text = decrypt(crypted_text, i)
      for word in words:
        if word in src_text:
          print(f"{i}=>{src_text}")
          break
    print()