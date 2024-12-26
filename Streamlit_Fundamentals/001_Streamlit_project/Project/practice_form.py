import streamlit as st
import mysql.connector
import io


#  Function to build the connection to the sql database.
def databaseConnection():
    return mysql.connector.connect(
        user="root",  # replace with your MySQL username
        password="1234!@#$Tushar",  # replace with your MySQL password
        host="localhost",  # replace with your MySQL host if different
        database="tushardb",  # replace with your database name
    )


#  Form UI..
st.title("Special Form in Streamlit")

with st.form("my_form"):
    st.header("Fill in your details")

    name = st.text_input("Your Name", placeholder="Enter Your name")
    age = st.number_input(
        "Your Age", placeholder="Enter your age", min_value=1, max_value=100
    )
    email = st.text_input("Your email", placeholder="Enter your Email")
    feedback = st.text_area("Your Feedback", placeholder="Hello Guys")

    agree = st.checkbox("I agree to the terms and conditions")

    file = st.file_uploader(
        "Upload your profile picture (optional)", type=["png", "jpg", "pdf"]
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    if not agree:
        st.error("Please accept the terms and conditions")
    else:
        agree = True
        #  we will write the code for push the data into the database..
        st.success("Form Submitted Successfully")

        database_conn = databaseConnection()
        # st.write("Testing1")
        cursor = database_conn.cursor()
        # st.write("Testing2")

        try:
            cursor.execute(
                "INSERT INTO demotable(name, age, email, agree, feedback)"
                "VALUES (%s, %s, %s, %s, %s)",
                (name, age, email, agree, feedback),
            )
            database_conn.commit()

            #  Printing the data.
            st.write("Your name:- ", name)
            st.write("Your age:- ", age)
            st.write("Your email- ", email)
            st.write("Your agree- ", agree)
            st.write("Your Feedback- ", feedback)

            #  Show the uploaded file.
            if file is not None:
                st.image(file, caption="Tushar Image", use_container_width=True)

            st.success("Data Saved Successfully in Database")
        except mysql.connector.Error as e:
            st.error(f"Error:- {e}")
        finally:
            cursor.close()
            database_conn.close()
