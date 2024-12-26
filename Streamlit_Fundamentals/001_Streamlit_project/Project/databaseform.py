import streamlit as st
from sqlalchemy import create_engine
import pymysql

# Database connection details
DB_HOST = "localhost"
DB_PORT = "3306"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "test_db"

# Create a database engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# Streamlit app
st.title("Streamlit Form with SQL Database")

# Streamlit form
with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1, max_value=100)
    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email and age:
            try:
                # Insert data into the database
                with engine.connect() as conn:
                    query = f"""
                    INSERT INTO users (name, email, age)
                    VALUES ('{name}', '{email}', {age})
                    """
                    conn.execute(query)
                    st.success("Data saved successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please fill out all fields.")

# Display data from the database
if st.button("Show Data"):
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT * FROM users")
            rows = result.fetchall()
            if rows:
                st.write("### Users in the Database:")
                for row in rows:
                    st.write(row)
            else:
                st.write("No data found.")
    except Exception as e:
        st.error(f"Error: {e}")


# CREATE DATABASE test_db;

# USE test_db;

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100),
#     age INT
# );
