#!/usr/bin/env python3.8
from hider import User
from hider import Credentials
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
  return Credentials.copy_pass(platform)