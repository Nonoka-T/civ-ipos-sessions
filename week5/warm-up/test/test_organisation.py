import unittest
from src.organisation import Organisation
from src.contact import Contact

# Step 1
class TestOrganisation(unittest.TestCase):
    def test_add_organisation(self):
        # Create an organization
        org = Organisation("NMTafe")
        self.assertEqual(org.name, "NMTafe")

    # Step 3
    def test_add_contact(self):
        # Create an organisation
        org = Organisation("NMTafe")

        # Create a contact
        contact = Contact("Nonoka T", "john@exmple.com")
        # Add contact to organisation
        org.add_contact(contact)
        # Check if contact is added to the organisation
        self.assertIn(contact, org.get_contacts)

if __name__ == '__main__':
    unittest.main()