import unittest

from src.contact import Contact

class TestContact(unittest.TestCase):
    # Step 2
    def test_contact_creation(self):
        # Create a contact
        name = Contact("Nonoka", "nonoka@example.com")

        # Check if attributes are set correctly
        self.assertIn(name, org.get_contacts)


if __name__ == '__main__':
    unittest.main()