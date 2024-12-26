# # import streamlit as st

# # st.sidebar.image("portfolio-image.png", use_container_width=True, caption="Tushar")
# # st.sidebar.subheader("Navigation")
# # radio_btn = st.sidebar.radio("Go to", ["Dashboard", "Settings", "Profile"])

# # if radio_btn == "Dashboard":
# #     st.title("I am the Dashboard Page")
# #     st.header("I am the Dashboard Header")
# #     st.subheader("I am the Dashboard subheader")
# # elif radio_btn == "Settings":
# #     st.title("I am the Settings Page")
# #     st.header("I am the Settings Header")
# #     st.subheader("I am the Settings subheader")
# # else:
# #     st.title("I am the Profile Page")
# #     st.header("I am the Profile Header")
# #     st.subheader("I am the Profile subheader")


# import streamlit as st

# st.title("Special Form in Streamlit")

# with st.form("my-form"):
#     st.header("Fill in your Details")

#     text1 = st.text_input("Your Name", placeholder="Enter your full name")
#     number1 = st.number_input("Your Age", min_value=0, max_value=100, value=0)
#     text2 = st.text_input("Your Email", placeholder="Enter your Email Address")
#     text3 = st.text_area("Your Feedback", placeholder="Share Your Thoughts")

#     check_val = st.checkbox("I agree to the terms and conditions")

#     file_val = st.file_uploader(
#         "Upload your profile picture (optional)", type=["jpg", "png", "pdf", "jpeg"]
#     )

#     submitted = st.form_submit_button("Submit")

# if submitted:
#     if not check_val:
#         st.error("Please accept the terms and condition")
#     else:
#         st.success("Form Submitted")
#         st.write("Your name:- ", text1)
#         st.write(number1)
#         st.write(text2)
#         st.write(text3)

#         if file_val is not None:
#             st.image(file_val, caption="Uploaded Image")
