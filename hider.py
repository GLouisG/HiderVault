import string
import random
import pyperclip 

class User:
  hider_accs = []
  '''
  class that acts as a blueprint for HiderVault accounts
  '''
  def __init__(self, hider_name, hider_password):
    self.hider_name = hider_name
    self.hider_password = hider_password
  def save_user(self):
    '''
    Saves Hider Accounts
    '''
    User.hider_accs.append(self)
class Credentials:
   '''
   class that acts as a blueprint for credentials
   '''
   credentials_list = []
   def __init__(self, user_name, user_password, user_site, owner):
      self.user_name = user_name
      self.user_password = user_password
      self.user_site = user_site
      self.owner = owner
   def save_credential(self):
     '''
        To save credentials
     '''
     Credentials.credentials_list.append (self)
   def delete_credential(self):
     '''
     To delete credentials
     '''
     Credentials.credentials_list.remove(self)  
  #  @classmethod
  #  def display_credentials(cls):
  #    return cls.credentials_list

   @classmethod
   def display_credentials(cls, c_owner):
        '''
        To display credentials
        '''
        searlist = []
        for credential in cls.credentials_list:
            if credential.owner == c_owner:
                searlist.append(credential)
        return searlist   

   @classmethod
   def search_by_site(cls, search):
     '''
        To locate credentials by site
     '''
     for credential in cls.credentials_list:
       if credential.user_site == search:
         return credential 
   
   def password_gen(length):
    
    # generate passwords for credentials
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str      
   @classmethod
   def credential_exists(cls, site):
     '''
        To confirm existence of credentials
     '''
     for credential in cls.credentials_list:
       if credential.user_site == site:
         return True 
     return False   

   @classmethod
   def copy_password(cls, platform):
    '''
        To copy credentials password
     ''' 
    found_credential = Credentials.search_by_site(platform)
    pyperclip.copy(found_credential.user_password) 
  