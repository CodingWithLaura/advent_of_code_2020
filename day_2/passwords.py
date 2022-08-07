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
 #print(test)

 f = open("numbers_small.txt", "r")
 lines = f.readlines()
 result = []
 bonds =[]
 letters = []
 woerter = []
 tast = []

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
 print(bonds)
 print(letters)
 print(woerter)

 for wort in range(0,len(woerter)):
  woerter[wort].extend(letters[wort])
 print(woerter)

 
   
 for wort in woerter:
  last_element = (wort.pop())
  count = 0
  print(last_element)
  print(wort)
  for i in wort:
   if i == last_element:
    count += 1
  print(count)
  for bond in bonds:
   for y in bond:
    print(y)
     
  

  
         
         
if __name__ == "__main__":
    main()
