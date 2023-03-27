# # import tkinter as tk
# # import sqlite3

# # # Initialize database
# # def init_db():
# #     conn = sqlite3.connect('public_art.db')
# #     c = conn.cursor()

# #     # create table for public art registration
# #     c.execute('''CREATE TABLE IF NOT EXISTS public_art (
# #                     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                     city TEXT NOT NULL,
# #                     artist_name TEXT NOT NULL,
# #                     artwork_title TEXT NOT NULL,
# #                     artwork_description TEXT NOT NULL,
# #                     artwork_image BLOB NOT NULL
# #                 )''')

# #     conn.commit()
# #     conn.close()

# # # Function to submit the registration form
# # def submit_form():
# #     city = city_entry.get()
# #     artist_name = artist_entry.get()
# #     artwork_title = title_entry.get()
# #     artwork_description = description_entry.get()
# #     artwork_image = image_entry.get()

# #     conn = sqlite3.connect('public_art.db')
# #     c = conn.cursor()

# #     c.execute('''INSERT INTO public_art (city, artist_name, artwork_title, artwork_description, artwork_image)
# #                  VALUES (?, ?, ?, ?, ?)''',
# #               (city, artist_name, artwork_title, artwork_description, artwork_image))

# #     conn.commit()
# #     conn.close()

# #     # Clear the form fields after submission
# #     city_entry.delete(0, tk.END)
# #     artist_entry.delete(0, tk.END)
# #     title_entry.delete(0, tk.END)
# #     description_entry.delete(0, tk.END)
# #     image_entry.delete(0, tk.END)

# # # Create the main window
# # window = tk.Tk()
# # window.title("Public Art Registration Form")

# # # Initialize database
# # init_db()

# # # Create form fields
# # city_label = tk.Label(window, text="City:")
# # city_label.pack()
# # city_entry = tk.Entry(window)
# # city_entry.pack()

# # artist_label = tk.Label(window, text="Artist Name:")
# # artist_label.pack()
# # artist_entry = tk.Entry(window)
# # artist_entry.pack()

# # title_label = tk.Label(window, text="Artwork Title:")
# # title_label.pack()
# # title_entry = tk.Entry(window)
# # title_entry.pack()

# # description_label = tk.Label(window, text="Artwork Description:")
# # description_label.pack()
# # description_entry = tk.Entry(window)
# # description_entry.pack()

# # image_label = tk.Label(window, text="Artwork Image:")
# # image_label.pack()
# # image_entry = tk.Entry(window)
# # image_entry.pack()

# # # Create submit button
# # submit_button = tk.Button(window, text="Submit", command=submit_form)
# # submit_button.pack()

# # # Run the main loop
# # window.mainloop()

# import sqlite3

# # connect to the database
# conn = sqlite3.connect('public_art.db')

# # create a cursor object
# c = conn.cursor()

# # execute a query
# c.execute('SELECT * FROM public_art')

# # fetch the results
# rows = c.fetchall()

# # print the results
# for row in rows:
#     print(row)

# # close the cursor and connection
# c.close()
# conn.close()

# import tkinter as tk
# import sqlite3

# # Initialize database
# def init_db():
#     conn = sqlite3.connect('public_art.db')
#     c = conn.cursor()

#     # create table for public art registration
#     c.execute('''CREATE TABLE IF NOT EXISTS public_art (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     city TEXT NOT NULL,
#                     artist_name TEXT NOT NULL,
#                     artwork_title TEXT NOT NULL,
#                     artwork_description TEXT NOT NULL,
#                     artwork_image BLOB NOT NULL
#                 )''')

#     conn.commit()
#     conn.close()

# # Function to submit the registration form
# def submit_form():
#     city = city_entry.get()
#     artist_name = artist_entry.get()
#     artwork_title = title_entry.get()
#     artwork_description = description_entry.get()
#     artwork_image = image_entry.get()

#     conn = sqlite3.connect('public_art.db')
#     c = conn.cursor()

#     c.execute('''INSERT INTO public_art (city, artist_name, artwork_title, artwork_description, artwork_image)
#                  VALUES (?, ?, ?, ?, ?)''',
#               (city, artist_name, artwork_title, artwork_description, artwork_image))

#     conn.commit()
#     conn.close()

#     # Clear the form fields after submission
#     city_entry.delete(0, tk.END)
#     artist_entry.delete(0, tk.END)
#     title_entry.delete(0, tk.END)
#     description_entry.delete(0, tk.END)
#     image_entry.delete(0, tk.END)

#     # Call the test function after the form is submitted
#     test_function()

# # Test function
# def test_function():
#     conn = sqlite3.connect('public_art.db')
#     c = conn.cursor()

#     # Retrieve the data from the database
#     c.execute("SELECT * FROM public_art")
#     rows = c.fetchall()

#     # Print the data to the console
#     for row in rows:
#         print(row)

#     conn.commit()
#     conn.close()

# # Create the main window
# window = tk.Tk()
# window.title("Public Art Registration Form")

# # Initialize database
# init_db()

# # Create form fields
# city_label = tk.Label(window, text="City:")
# city_label.pack()
# city_entry = tk.Entry(window)
# city_entry.pack()

# artist_label = tk.Label(window, text="Artist Name:")
# artist_label.pack()
# artist_entry = tk.Entry(window)
# artist_entry.pack()

# title_label = tk.Label(window, text="Artwork Title:")
# title_label.pack()
# title_entry = tk.Entry(window)
# title_entry.pack()

# description_label = tk.Label(window, text="Artwork Description:")
# description_label.pack()
# description_entry = tk.Entry(window)
# description_entry.pack()

# image_label = tk.Label(window, text="Artwork Image:")
# image_label.pack()
# image_entry = tk.Entry(window)
# image_entry.pack()

# # Create submit button
# submit_button = tk.Button(window, text="Submit", command=submit_form)
# submit_button.pack()

# # Run the main loop
# window.mainloop()







# import tkinter as tk
# import sqlite3

# # Initialize database
# def init_db():
#     conn = sqlite3.connect('public_art.db')
#     c = conn.cursor()

#     # create table for public art registration
#     c.execute('''CREATE TABLE IF NOT EXISTS public_art (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     city TEXT NOT NULL,
#                     artist_name TEXT NOT NULL,
#                     artwork_title TEXT NOT NULL,
#                     artwork_description TEXT NOT NULL,
#                     artwork_image BLOB NOT NULL
#                 )''')

#     conn.commit()
#     conn.close()

# # Function to submit the registration form
# def submit_form():
#     city = city_entry.get()
#     artist_name = artist_entry.get()
#     artwork_title = title_entry.get()
#     artwork_description = description_entry.get()
#     artwork_image = image_entry.get()

#     conn = sqlite3.connect('public_art.db')
#     c = conn.cursor()

#     c.execute('''INSERT INTO public_art (city, artist_name, artwork_title, artwork_description, artwork_image)
#                  VALUES (?, ?, ?, ?, ?)''',
#               (city, artist_name, artwork_title, artwork_description, artwork_image))

#     conn.commit()
#     conn.close()

#     # Clear the form fields after submission
#     city_entry.delete(0, tk.END)
#     artist_entry.delete(0, tk.END)
#     title_entry.delete(0, tk.END)
#     description_entry.delete(0, tk.END)
#     image_entry.delete(0, tk.END)

# # Function to update registration form
# def update_form():
#     id = id_entry.get()
#     city = city_entry.get()
#     artist_name = artist_entry.get()
#     artwork_title = title_entry.get()
#     artwork_description = description_entry.get()
#     artwork_image = image_entry.get()

#     conn = sqlite3.connect('public_art.db')
#     c = conn.cursor()

#     c.execute('''UPDATE public_art SET city=?, artist_name=?, artwork_title=?, artwork_description=?, artwork_image=?
#                  WHERE id=?''',
#               (city, artist_name, artwork_title, artwork_description, artwork_image, id))

#     conn.commit()
#     conn.close()

#     # Clear the form fields after update
#     id_entry.delete(0, tk.END)
#     city_entry.delete(0, tk.END)
#     artist_entry.delete(0, tk.END)
#     title_entry.delete(0, tk.END)
#     description_entry.delete(0, tk.END)
#     image_entry.delete(0, tk.END)

# # Create the main window
# window = tk.Tk()
# window.title("Public Art Registration Form")

# # Initialize database
# init_db()

# # Create form fields
# id_label = tk.Label(window, text="ID (for update only):")
# id_label.pack()
# id_entry = tk.Entry(window)
# id_entry.pack()

# city_label = tk.Label(window, text="City:")
# city_label.pack()
# city_entry = tk.Entry(window)
# city_entry.pack()

# artist_label = tk.Label(window, text="Artist Name:")
# artist_label.pack()
# artist_entry = tk.Entry(window)
# artist_entry.pack()

# title_label = tk.Label(window, text="Artwork Title:")
# title_label.pack()
# title_entry = tk.Entry(window)
# title_entry.pack()

# description_label = tk.Label(window, text="Artwork Description:")
# description_label.pack()
# description_entry = tk.Entry(window)
# description_entry.pack()

# image_label = tk.Label(window, text="Artwork Image:")
# image_label.pack()
# image_entry = tk.Entry(window)
# image_entry.pack()

# # Create submit button
# submit_button = tk.Button(window, text="Submit", command=submit_form)
# submit_button.pack()

# # Create update button
# update_button = tk.Button(window, text="Update", command=update_form)
# update_button.pack()

# # Run the main loop
# window.mainloop()

