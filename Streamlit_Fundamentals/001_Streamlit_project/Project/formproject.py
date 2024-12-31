import streamlit as st
import mysql.connector
from PIL import Image
import io


# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        user="root",  # replace with your MySQL username
        password="1234!@#$Tushar",  # replace with your MySQL password
        host="localhost",  # replace with your MySQL host if different
        database="demo",  # replace with your database name
    )


# print(connect_to_db)

# # Title of the application
st.title("Special Form in Streamlit")

# Create the form
with st.form("my_form"):
    st.subheader("Fill in your details")

    # Form fields
    name = st.text_input("Your Name", placeholder="Enter your full name")
    age = st.number_input("Your Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Your Email", placeholder="Enter your email address")
    feedback = st.text_area("Your Feedback", placeholder="Share your thoughts...")
    agree = st.checkbox("I agree to the terms and conditions")

    # File uploader
    file = st.file_uploader(
        "Upload your profile picture (optional)", type=["jpg", "png"]
    )

    # Submit button
    submitted = st.form_submit_button("Submit")

# Process form submission
if submitted:
    if not agree:
        st.warning("You need to agree to the terms and conditions to submit the form.")
    else:
        # Show success message
        st.success("Form submitted successfully!")

        # Process the uploaded file
        if file is not None:
            # Convert the uploaded file to binary data
            image = Image.open(file)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format="PNG")
            img_byte_arr = img_byte_arr.getvalue()  # Get binary data
        else:
            img_byte_arr = None  # No image uploaded

        # Connect to the database
        db_connection = connect_to_db()
        cursor = db_connection.cursor()
        print(cursor)

        # Insert form data into the database
        try:
            cursor.execute(
                "INSERT INTO table1 (name, age, email, feedback, agree) "
                "VALUES (%s, %s, %s, %s, %s)",
                (name, age, email, feedback, agree),
            )
            # st.write("Testing1")

            print(db_connection.commit())
            st.write("**Name:**", name)
            st.write("**Age:**", age)
            st.write("**Email:**", email)
            st.write("**Feedback:**", feedback)

            # Show the uploaded image (if any)
            if file is not None:
                st.image(
                    file, caption="Uploaded Profile Picture", use_container_width=True
                )

            # st.write("Testing2")
            st.success("Data has been saved to the database successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
        finally:
            cursor.close()
            db_connection.close()


# CREATE DATABASE my_database;

# USE my_database;

# CREATE TABLE form_data (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     email VARCHAR(255),
#     feedback TEXT,
#     agree BOOLEAN,
#     profile_picture BLOB
# );

# Necessary Libraries for this..
# pip install mysql-connector-python Pillow
