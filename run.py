#!/usr/bin/env python3.8
from hider import User
from hider import Credentials
import pyperclip
def create_user(hname, hpassword):
  '''
  function to create a new vault user
  '''
  new_user = User(hname, hpassword)
  return new_user

def user_saver(user):
  user.save_user()


def create_cred(uname, upass, usite, uowner):

  new_credential = Credentials(uname, upass, usite, uowner)     
  return new_credential
def save_cred(credential):
  credential.save_credential()  
def del_cred(credential):
  credential.delete_credential()
def display_creds(c_owner):
  return Credentials.display_credentials(c_owner)
def site_search(search):
  return Credentials.search_by_site(search)
def pass_gen(length):
  return Credentials.password_gen(length)  
def cred_exists(site):
  return Credentials.credential_exists(site)
def copy_pass(platform):
  return Credentials.copy_password(platform)


def main():
  print("Hello welcome to HiderVault")
  while  True:
    print("Use the following codes ca-Create Account lg-Log In ex-Exit")

    short_code = input().lower()
  
    if short_code == 'ca':
      print("New User")
      print("-"*10)
      print("What will your vault user name be?...")
      hname = input()
      print("What will your vault password be?...")
      hpassword = input()
      user_saver(create_user(hname, hpassword))
      continue
    elif short_code == 'lg':
      print ("Please enter your username---")
      print ("If you wish to return press enter twice only")
      input_hname = input()
      print ("If you wish to return just press enter once only")
      print("What is your vault password?...")
      input_hpassword = input() 
      for user in User.hider_accs:
        while user.hider_name == input_hname and user.hider_password == input_hpassword:
          print("Please use the following codes ac-add credential dc-display credentials del-delete credentials ex-exit cp-copy password")
          tiny_code = input().lower()
          if tiny_code=="ac":
            print("type _leave_ to leave")
            print("Do you want to use a generated password(y/n)")
            
            reply = input().lower()
            if reply == "y":
              print("New Account")
              print("-"*10)
              print("Enter Username...")
              uname = input()
              print("What password length in numbers do you want...")
              length = int(input())
              if isinstance(length, int):
                upass = pass_gen(length)
                print(f"your password is {upass}")
              else:
                print("please enter a number")  
              
              print("Enter Platform/website...")
              usite = input().lower()
              uowner = input_hname
              save_cred(create_cred(uname,upass,usite,uowner)) # create and save new contact.
              print ('\n')
              print(f"New Account {uname} for {usite} created")
              print("--**"*34)
              print ('\n')
            elif reply == "n" :
              print("New Account")
              print("-"*10)
              print("Enter Username...")
              uname = input()
              print("Enter Password...")
              upass = input()
              print("Enter Platform/website...")
              usite = input().lower
              uowner = input_hname
              save_cred(create_cred(uname,upass,usite,uowner)) # create and save new contact.
              print ('\n')
              print(f"New Account {uname} for {usite} created")
              print("--**"*34)
              print ('\n')
            elif reply == "_leave_":
              break
            

          elif tiny_code=="dc":
            if display_creds(hname):
                                   print("Here is a list of all your credentials")
                                   print('\n')
 
                                   for cred in display_creds(hname):
                                           print(f"Username:{cred.user_name} Password:{cred.user_password} Platform:{cred.user_site}")
                                   print("--**"*34)
                                   print('\n')
            else:
                                   print('\n')
                                   print("You dont seem to have any contacts saved yet")
                                   print("--**"*34)
                                   print('\n')
          elif tiny_code=="del":
            print("Which platform's account do you want to delete")
            plat_todel= input()
            del_cred(site_search(plat_todel))
            print("All Done")
            print("--**"*34)
            
          elif tiny_code=="cp": 
            print("Which site/platform password do you want to copy")
            cp_site = input()
            copy_pass(cp_site) 
            print("The password has been copied to your clipboard") 
            print("--**"*34)
          elif tiny_code=="ex": 
            break  
         
        # if len(User.hider_accs) == 0:
        #      print("DOESN'T EXIST")  
        if user.hider_name != input_hname or user.hider_password != input_hpassword:  
           print("YOUR USERNAME OR PASSWORD IS INCORRECT")
           print("--**"*34)
        else :
          print("Sorry I didn't get that kindly use the codes")
          print("--**"*34)
    elif short_code == 'ex':
      break
         

if __name__ == '__main__':

    main()