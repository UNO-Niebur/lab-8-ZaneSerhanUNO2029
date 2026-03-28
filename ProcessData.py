#ProcessData.py
#Name: Zane Serhan
#Date: 3/28/2026
#Assignment: Lab8 

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]
    student_id = makeID(first, last, idNum)
    major_year = majorYear(major, year)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
   

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  idLen = len(idNum)
  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + idNum[idLen - 3: ]
  return id.lower()

def majorYear(major, year):
  majorCode = major[:3].upper()

  if year == "Freshman":
    yearCode = "FR"
  elif year == "Sophomore":
    yearCode = "SO"
  elif year == "Junior":
    yearCode = "JR"
  elif year == "Senior":
    yearCode = "SR"
  
  return majorCode + "-" + yearCode


if __name__ == '__main__':
  main()
