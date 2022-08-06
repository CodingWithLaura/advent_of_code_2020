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
 print(test)

if __name__ == "__main__":
    main()
