import os as os

def main():
  while True:
    jeff()

def jeff():
  l = input("Do you want to login? Y/n ")
  if l == "Y" or l == "y" or l == "Y." or l == "y." or l == "yes" or l == "Yes" or l == "Yes." or l == "yes." or l=="YES" or l=="YES.":
    print("You wrote yes.")
  elif l=="n" or l=="N" or l=="n." or l=="N." or l=="no" or l=="No" or l=="No." or l=="no." or l=="NO" or l=="NO.":
    print("You wrote no.")
  elif l=="yeet":
    print("Yeah bro Yeet!!!!")
  else:
    print("Not a yes or no value.")

if 1 == 1: main()
