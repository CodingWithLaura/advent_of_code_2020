def passwords(input):
 liste_wort = []
 valid = 0
 
 for t in input:
     wort = list(t[3])
     count = 0
     for w in wort:
         if w == t[2]:
             count += 1
     if count >= t[0] and count <= t[1]:
         valid += 1
 return valid
    
def main():
 input = [[1,3,"a","abcde"],[1,3,"b","cdefg"],[2,9,"c","ccccccccc"]]
 test = passwords(input)

 f = open("numbers.txt", "r")
 lines = f.readlines()
 result = []
 bonds =[]
 letters = []
 woerter = []


 for x in lines:
     y = x.strip("\n")
     result.append(y.split(" "))
     
 for r in result:
     blubb = r[0].split("-")
     bonds.append(blubb)

 for b in result:
     lala =b[1].strip(":")
     letters.append(lala)

 for c in result:
     lulu = list(c[2])
     woerter.append(lulu)

 for wort in range(0,len(woerter)):
  woerter[wort].extend(letters[wort])

 counts = []
   
 for wort in woerter:
  last_element = (wort.pop())
  count = 0
  for i in wort:
   if i == last_element:
    count += 1
  counts.append(count)

 for bond in range(0,len(bonds)):
  bonds[bond].append(counts[bond])

 good_pwd = 0

 for bond in bonds:
  last_element = bond.pop()
  if last_element >= int(bond[0]) and last_element <= int(bond[1]):
   good_pwd +=1
 print(good_pwd)
           
if __name__ == "__main__":
    main()
