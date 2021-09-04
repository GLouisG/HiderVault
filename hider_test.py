import unittest
from hider import User
from hider import Credentials
class TestUser(unittest.TestCase):
  def setUp(self):
    self.new_user = User("Guy", "abcdef")
  def tearDown(self):
    User.hider_accs = []

  def test_init(self):
    self.assertEqual(self.new_user.hider_name, "Guy")
    self.assertEqual(self.new_user.hider_password, "abcdef")  

  def test_save_user(self):
    self.new_user.save_user()
    self.assertEqual(len(User.hider_accs),1)
  def test_save_multiple_users(self):
    self.new_user.save_user()
    test_user = User("Chap", "JollyOld")  
    test_user.save_user()
    self.assertEqual(len(User.hider_accs), 2)

class  TestCredentials(unittest.TestCase):
    def setUp(self):
      self.new_credential = Credentials("Guy2", "abc", "twitter", "Twit")
    def tearDown(self):
      Credentials.credentials_list = []

    def test_init(self):
      self.assertEqual(self.new_credential.user_name, "Guy2")
      self.assertEqual(self.new_credential.user_password, "abc") 
      self.assertEqual(self.new_credential.user_site, "twitter")
      self.assertEqual(self.new_credential.owner, "Twit")
    def test_save_user(self):
      self.new_credential.save_credential()
      self.assertEqual(len(Credentials.credentials_list),1)
    def test_save_multiple_creds(self):
      self.new_credential.save_credential()
      test_credential = Credentials("Chap", "JollyOld", "Facebook", "Twit")  
      test_credential.save_credential()
      self.assertEqual(len(Credentials.credentials_list), 2)  

if __name__ == '__main__':
    unittest.main()