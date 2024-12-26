import streamlit as st
import mysql.connector
from PIL import Image
import io


# Function to connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        user="your_username",  # replace with your MySQL username
        password="your_password",  # replace with your MySQL password
        host="localhost",  # replace with your MySQL host if different
        database="my_database",  # replace with your database name
    )


# Title of the application
st.title("Special Form in Streamlit")


# Function to display data from the database
def read_data():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM form_data")
    rows = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return rows


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

        # Insert form data into the database
        try:
            cursor.execute(
                "INSERT INTO form_data (name, age, email, feedback, agree, profile_picture) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (name, age, email, feedback, agree, img_byte_arr),
            )
            db_connection.commit()
            st.success("Form submitted and data has been saved to the database.")

            st.write("**Name:**", name)
            st.write("**Age:**", age)
            st.write("**Email:**", email)
            st.write("**Feedback:**", feedback)

            # Show the uploaded image (if any)
            if file is not None:
                st.image(
                    file, caption="Uploaded Profile Picture", use_container_width=True
                )
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
        finally:
            cursor.close()
            db_connection.close()

# Display Data (Reading)
st.subheader("Existing Data")
rows = read_data()
for row in rows:
    st.write(
        f"**ID**: {row[0]}, **Name**: {row[1]}, **Age**: {row[2]}, **Email**: {row[3]}"
    )
    st.write(f"**Feedback**: {row[4]}, **Agreed**: {row[5]}")

    # Show the uploaded image (if any)
    if row[6] is not None:
        st.image(
            io.BytesIO(row[6]), caption="Profile Picture", use_container_width=True
        )

# Update Data
st.subheader("Update Data")
update_id = st.number_input(
    "Enter the ID of the record you want to update", min_value=1
)
if st.button("Fetch Record"):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM form_data WHERE id = %s", (update_id,))
    record = cursor.fetchone()
    if record:
        # Pre-fill the form with existing data
        name = st.text_input("Name", value=record[1])
        age = st.number_input(
            "Age", min_value=0, max_value=120, step=1, value=record[2]
        )
        email = st.text_input("Email", value=record[3])
        feedback = st.text_area("Feedback", value=record[4])
        agree = st.checkbox("I agree to the terms and conditions", value=record[5] == 1)
        file = st.file_uploader(
            "Upload Profile Picture (optional)", type=["jpg", "png"]
        )

        if st.button("Update"):
            if file is not None:
                image = Image.open(file)
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format="PNG")
                img_byte_arr = img_byte_arr.getvalue()
            else:
                img_byte_arr = record[
                    6
                ]  # Keep existing image if no new one is uploaded

            # Update the record in the database
            cursor.execute(
                "UPDATE form_data SET name = %s, age = %s, email = %s, feedback = %s, agree = %s, profile_picture = %s "
                "WHERE id = %s",
                (name, age, email, feedback, agree, img_byte_arr, update_id),
            )
            db_connection.commit()
            st.success("Record updated successfully!")
    else:
        st.error("Record not found.")
    cursor.close()
    db_connection.close()

# Delete Data
st.subheader("Delete Data")
delete_id = st.number_input(
    "Enter the ID of the record you want to delete", min_value=1
)
if st.button("Delete Record"):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM form_data WHERE id = %s", (delete_id,))
    db_connection.commit()
    st.success(f"Record with ID {delete_id} has been deleted successfully.")
    cursor.close()
    db_connection.close()
