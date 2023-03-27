import unittest
import sqlite3
import index

class TestPublicArtRegistration(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('public_art.db')
        self.c = self.conn.cursor()
        self.c.execute('DELETE FROM public_art')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_submit_form(self):
        # Submit a registration form
        index.city_entry.insert(0, 'Delhi')
        index.artist_entry.insert(0, 'John Doe')
        index.title_entry.insert(0, 'Test Artwork')
        index.description_entry.insert(0, 'This is a test artwork')
        index.image_entry.insert(0, 'test_image.jpg')
        index.submit_form()

        # Check if the form was submitted successfully
        self.c.execute('SELECT * FROM public_art')
        result = self.c.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Delhi')
        self.assertEqual(result[2], 'John Doe')
        self.assertEqual(result[3], 'Test Artwork')
        self.assertEqual(result[4], 'This is a test artwork')
        self.assertEqual(result[5], 'test_image.jpg')

    def test_update_form(self):
        # Insert a record to be updated
        self.c.execute('''INSERT INTO public_art (city, artist_name, artwork_title, artwork_description, artwork_image)
                           VALUES (?, ?, ?, ?, ?)''',
                      ('Mumbai', 'Jane Doe', 'Old Artwork', 'This is an old artwork', 'old_image.jpg'))
        self.conn.commit()

        # Update the record
        index.city_entry.insert(0, 'Mumbai')
        index.artist_entry.insert(0, 'Jane Doe')
        index.title_entry.insert(0, 'New Artwork')
        index.description_entry.insert(0, 'This is a new artwork')
        index.image_entry.insert(0, 'new_image.jpg')
        index.update_form()

        # Check if the record was updated successfully
        self.c.execute('SELECT * FROM public_art WHERE artwork_title = "New Artwork"')
        result = self.c.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Mumbai')
        self.assertEqual(result[2], 'Jane Doe')
        self.assertEqual(result[3], 'New Artwork')
        self.assertEqual(result[4], 'This is a new artwork')
        self.assertEqual(result[5], 'new_image.jpg')

if __name__ == '__main__':
    unittest.main()
