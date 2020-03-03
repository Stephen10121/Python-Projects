import os as OS

def login():
  print("Login")
  print("Still Not Finished")

def signup():
  print("Signup")
  f=open("username.txt", "r")
  name = input("What is your name? ")
  age = input("How old are you? ")
  def userpik():
    username = input("What username do you want? ")
    if f.mode == 'r':
      contents =f.read()
      if username in contents:
        print("Username Taken.")
        userpik()
      else:
        def paspick():
          password = input("What password do you want? ")
          rpassword = input("Repeat password. ")
          if password == rpassword:
            print("Finished")
            print(name , age , username , password , rpassword)
            write2 = open("username.txt" , "a+")
            write2.write(username)
            write2.write("\r\n")
            OS.mkdir(username)
            OS.chdir(username)
            OS.mkdir("Files")
            write = open("userinfo.txt","w+")
            write.write(name)
            write.write("\r\n")
            write.write(age)
            write.write("\r\n")
            write.write(username)
            write.write("\r\n")
            write.write(password)
          else:
            print("Passwords dont match!")
            paspick()
        paspick()
  userpik()


def logorsig():
  l = input("Do you want to Signup?")
  if l == "Y" or l == "y" or l == "Y." or l == "y." or l == "yes" or l == "Yes" or l == "Yes." or l == "yes." or l=="YES" or l=="YES.":
    signup()
  elif l=="n" or l=="N" or l=="n." or l=="N." or l=="no" or l=="No" or l=="No." or l=="no." or l=="NO" or l=="NO.":
    lm = input("Do you want to login?")
    if lm == "Y" or lm == "y" or lm == "Y." or lm == "y." or lm == "yes" or lm == "Yes" or lm == "Yes." or lm == "yes." or lm=="YES" or lm=="YES.":
      login()
    elif lm=="n" or lm=="N" or lm=="n." or lm=="N." or lm=="no" or lm=="No" or lm=="No." or lm=="no." or lm=="NO" or lm=="NO.":
      print("Okay then...")
      logorsig()
    else:
      print("Huh?")
      logorsig()

logorsig()
