#!/usr/local/bin/python2.7
  
"""
The arithmetic sequence, 1487, 4817, 8147, in which each
of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def main():
  primeList = []
  primePermList = []
  for x in range(1000,10000):
    if checkPrime(x) == True:
      primeList.append(x)    
      #print "prime!" + str(x)
  for prime in primeList:
    #print prime
    checkSequence(permutate(prime))
  
def checkSequence(primeList):  
  culledPrimeList = list(set(primeList))
  #print culledPrimeList
  #convert strings to int
  culledPrimeList = map(int, culledPrimeList)
  
  #filter out the non prime permutations
  for prime in culledPrimeList:
    if not checkPrime(prime):
      culledPrimeList.remove(prime)
  
  diffA = 0
  diffB = 0
  temp = culledPrimeList[0]
  
  for x in range(1, len(culledPrimeList)):
    diffA = abs(culledPrimeList[x] - temp)
    
    #out of bounds check
    if culledPrimeList[x] == culledPrimeList[-1]:
      diffB = 0
    else:
      diffB = abs(culledPrimeList[x] - culledPrimeList[x+1])
    
    if diffA == diffB:
      series = [temp, culledPrimeList[x], culledPrimeList[x+1]]
      print "Series:"
      print sorted(series)

      concatNum = ""

      for number in sorted(series):
        concatNum += str(number)
      
      print "\nConcatenated number:"
      print concatNum
    temp = culledPrimeList[x]
    
def checkPrime(n):
  i = 2
  while i < n:
    if n % i == 0:
      return False
    else:
      i += 1
  return True  
  
def permutate(seq):
  seq = str(seq) #only works with strings
  if not seq:
    return [seq] # is an empty sequence
  else:
    temp = []
  for k in range(len(seq)):
    part = seq[:k] + seq[k+1:]
    #print k, part # test
    for m in permutate(part):
      temp.append(seq[k:k+1] + m)
      #print m, seq[k:k+1], temp # test
  return temp

if __name__ == "__main__":
  main()
