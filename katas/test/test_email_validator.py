import unittest
from katas.email_validator import is_valid_email  

class TestIsValidEmail(unittest.TestCase):

    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@cnn.com"))
        self.assertTrue(is_valid_email("john.doe@cnn.com"))
        self.assertTrue(is_valid_email("admin+test@cnn.com"))
        self.assertTrue(is_valid_email("user_name@cnn.com"))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("user@@domain"))
        self.assertFalse(is_valid_email(""))  # empty string
        self.assertFalse(is_valid_email("user@domain..com"))  # double dot in domain
        self.assertFalse(is_valid_email(".user@domain.com"))  # starts with dot
        self.assertFalse(is_valid_email("user.@domain.com"))  # ends with dot
        self.assertFalse(is_valid_email("-user@domain.com"))  # starts with dash
        self.assertFalse(is_valid_email("user-@domain.com"))  # ends with dash
        self.assertFalse(is_valid_email("user@domain.c"))     # TLD too short
        self.assertFalse(is_valid_email("user@domain"))       # missing TLD
        self.assertFalse(is_valid_email("user@.com"))         # domain starts with dot
        self.assertFalse(is_valid_email("user@domain..com"))  # consecutive dots

if __name__ == "__main__":
    unittest.main()
