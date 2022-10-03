A6T = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def decrypt(text, R2L_A6T, C5T_A6T):
  rez=""
  for ch in text:
    if ch in C5T_A6T:
      rez+=R2L_A6T[C5T_A6T.find(ch)]
    else:
      rez+=ch
  return rez

def calc_frec(text):
  counts = {}
  for char in text:
    if not char in A6T:
      continue
    if not char in counts:
      counts[char] = 0
    counts[char] += 1
  full_count = 0
  calced_frecs = {}
  for k,v in counts.items():
    full_count += v
  for k,v in counts.items():
    calced_frecs[k] = v/full_count
  return calced_frecs

if __name__ == "__main__":
  with open('in.txt', 'r', encoding="utf-8") as file:
    text = file.read().split('\n')

  text = [[text[i*4],text[1+i*4],text[2+i*4]] for i in range(1+len(text)//4)]

  for tple in text:
    src_A6T = tple[0].split(' ')
    src_frec = tple[1].split(' ')
    crypted_text = tple[2]
    crypted_frec = calc_frec(crypted_text)
    lst1 = [(float(src_frec[i]),src_A6T[i]) for i in range(len(src_A6T))]
    lst1.sort(reverse=True)
    lst2 = [(v,k) for k,v in crypted_frec.items()]
    lst2.sort(reverse=True)
    REAL = ""
    CRYPTED = ""
    for t in range(len(lst2)):
      l1 = lst1[t]
      l2 = lst2[t]
      REAL += l1[1]
      CRYPTED += l2[1]
      #print(f"{l1[1]}:{l1[0]:.4f} | {l2[1]}:{l2[0]:.4f}")
    print(REAL)
    print(CRYPTED)
    print(f"ЦЕЗАРЬ {A6T.find(CRYPTED[0])-A6T.find(REAL[0])}")
    print(decrypt(crypted_text, REAL, CRYPTED))
    print()
    