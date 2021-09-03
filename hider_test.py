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


if __name__ == '__main__':
    unittest.main()