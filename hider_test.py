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
    def test_delete_cred(self):
            self.new_credential.save_credential()
            test_credential = Credentials("Chap", "JollyOld", "Facebook", "Twit")  
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credentials_list),1)
    # def test_display_creds(self):
    #     self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)    

            '''
        test to check if we can find a contact by phone number and display information
        '''
    def test_display_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credentials("Chap", "JollyOld", "Facebook", "Twit")  
        test_credential.save_credential()

        found_credentials = Credentials.display_credentials("Twit")

        self.assertEqual(found_credentials, Credentials.credentials_list)
    def test_password_gen(self):
        self.new_credential.save_credential()
        test_credential = Credentials("Chap", "JollyOld", "Facebook", "Twit")  
        test_credential.save_credential()

        new_pass = Credentials.password_gen(5)

        self.assertEqual(len(new_pass), 5)    
    def test_credential_exists(self):
       self.new_credential.save_credential()
       test_credential = Credentials("Chap", "JollyOld", "Facebook", "Twit")  
       test_credential.save_credential()

       credential_exists = Credentials.credential_exists("Facebook")

       self.assertTrue(credential_exists)   

if __name__ == '__main__':
    unittest.main()