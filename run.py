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
    