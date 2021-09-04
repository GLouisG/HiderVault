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
   credentials_list = []
   def __init__(self, user_name, user_password, user_site, owner):
      self.user_name = user_name
      self.user_password = user_password
      self.user_site = user_site
      self.owner = owner
   def save_credential(self):
     Credentials.credentials_list.append (self)
     