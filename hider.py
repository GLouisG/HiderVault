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
   credentials = []
   def __init__(self, user_name, user_password, user_site,):
      self.hider_name = user_name
      self.hider_password = user_password