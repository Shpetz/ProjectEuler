#!/usr/local/bin/python2.7
  
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
  solution1()

def solution1():
  ceiling = 1000
  totalSum = 0
  for multiple in range(1, ceiling):
    if ((multiple % 3 == 0 ) | (multiple % 5 == 0 )):
      totalSum += multiple
  
  print str(totalSum)

#does not work, thought any n*3 would be % = 0
def solution2():
  totalSum = 0
  ceiling = 1000
  fiveMultiples = []
  threeMultiples = []
  
  for n in range(1, ceiling):
    threeMultiples.append(n*3)
  
  for n in range(1, ceiling):
    fiveMultiples.append(n*5)
  
  for multiple in list(set(threeMultiples)|set(fiveMultiples))  :
    totalSum += multiple
  
  print str(totalSum)
  
if __name__ == "__main__":
  main()
