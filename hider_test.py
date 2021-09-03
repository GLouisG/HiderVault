import unittest
from hider import User

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
    
if __name__ == '__main__':
    unittest.main()