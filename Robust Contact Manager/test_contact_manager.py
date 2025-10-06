# test_contact_manager.py

import unittest
# Import all necessary components from the refactored module
from contact_manager import (
    add_contact, 
    find_contact, 
    delete_contact, 
    DuplicateContactError
)

class TestContactManager(unittest.TestCase):
    """Unit tests for the contact manager functions."""

    def setUp(self):
        """
        Set up a fresh, empty dictionary for contacts before each test.
        This ensures tests are isolated and don't affect each other.
        """
        self.test_contacts = {}

    # --- Test Cases for add_contact ---

    def test_add_new_contact(self):
        """Test that a new contact is correctly added."""
        name = "Randy"
        phone = "123-4567"
        
        # Action
        add_contact(self.test_contacts, name, phone)
        
        # Assertion
        self.assertIn(name, self.test_contacts)
        self.assertEqual(self.test_contacts[name], phone)

    def test_add_duplicate_contact_raises_error(self):
        """Test that adding an existing contact raises 
        DuplicateContactError."""
        name = "Bobby"
        phone = "987-6543"
        
        # Setup: Add the contact first
        add_contact(self.test_contacts, name, phone)
        
        # Assertion: Use assertRaises to check for the custom exception
        with self.assertRaises(DuplicateContactError) as cm:
            add_contact(self.test_contacts, name, "000-0000") 
        
        # Optional: Check the error message content
        self.assertIn("already exists", str(cm.exception))


    # --- Test Cases for find_contact ---

    def test_find_existing_contact(self):
        """Test that finding an existing contact returns the correct phone 
        number."""
        name = "Lucy"
        phone = "555-5555"
        self.test_contacts[name] = phone
        
        # Action & Assertion
        result = find_contact(self.test_contacts, name)
        self.assertEqual(result, phone)

    def test_find_non_existent_contact(self):
        """Test that finding a non-existent contact returns None gracefully."""
        # Action & Assertion
        result = find_contact(self.test_contacts, "NonExistent")
        # The refactored function returns None on KeyError instead of crashing
        self.assertIsNone(result)

    # --- Test Cases for delete_contact ---

    def test_delete_existing_contact(self):
        """Test that an existing contact is successfully removed."""
        name = "David"
        self.test_contacts[name] = "111-1111"
        
        # Action
        success = delete_contact(self.test_contacts, name)
        
        # Assertions
        self.assertTrue(success)
        self.assertNotIn(name, self.test_contacts)

    def test_delete_non_existent_contact(self):
        """Test that deleting a non-existent contact handles the KeyError 
        gracefully (returns False)."""
        name = "Emily"
        
        # Action
        success = delete_contact(self.test_contacts, name)
        
        # Assertions: Should return False and not crash
        self.assertFalse(success)
        self.assertEqual(len(self.test_contacts), 0) 

if __name__ == '__main__':
    unittest.main()