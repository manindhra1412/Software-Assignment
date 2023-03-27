import unittest
import sqlite3
from tkinter import Tk, Label, Entry, Button
from index import submit_form

class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('public_art.db')
        self.c = self.conn.cursor()

    def tearDown(self):
        self.c.execute('DELETE FROM public_art')
        self.conn.commit()
        self.conn.close()

    def test_submit_form(self):
        # Create the main window
        window = Tk()
        window.title("Public Art Registration Form")

        # Create form fields
        city_label = Label(window, text="City:")
        city_label.pack()
        city_entry = Entry(window)
        city_entry.pack()

        artist_label = Label(window, text="Artist Name:")
        artist_label.pack()
        artist_entry = Entry(window)
        artist_entry.pack()

        title_label = Label(window, text="Artwork Title:")
        title_label.pack()
        title_entry = Entry(window)
        title_entry.pack()

        description_label = Label(window, text="Artwork Description:")
        description_label.pack()
        description_entry = Entry(window)
        description_entry.pack()

        image_label = Label(window, text="Artwork Image:")
        image_label.pack()
        image_entry = Entry(window)
        image_entry.pack()

        # Set the form fields with test data
        city_entry.insert(0, 'Mumbai')
        artist_entry.insert(0, 'John Doe')
        title_entry.insert(0, 'Test Artwork')
        description_entry.insert(0, 'This is a test artwork')
        image_entry.insert(0, 'test.jpg')

        # Create submit button and click it
        submit_button = Button(window, text="Submit", command=lambda: submit_form())
        submit_button.pack()
        submit_button.invoke()

        # Check if the data was correctly inserted in the database
        self.c.execute('SELECT * FROM public_art')
        data = self.c.fetchone()
        self.assertIsNotNone(data)
        self.assertEqual(data[1], 'Mumbai')
        self.assertEqual(data[2], 'John Doe')
        self.assertEqual(data[3], 'Test Artwork')
        self.assertEqual(data[4], 'This is a test artwork')
        self.assertEqual(data[5], 'test.jpg')

        # Close the main window
        window.destroy()

if __name__ == '__main__':
    unittest.main()
