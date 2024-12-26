# # import streamlit as stm

# #  we need to create the form using the streamlit library..
# import streamlit as st

# # Sidebar for navigation
# # page = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact"])

# # if page == "Home":
# #     st.title("Home Page")
# #     st.write("Welcome to the Home Page!")
# # elif page == "About":
# #     st.title("About Page")
# #     st.write("This is the About Page!")
# # elif page == "Contact":
# #     st.title("Contact Page")
# #     st.write("Get in touch with us here!")

# # import streamlit as st

# # # Add elements to the sidebar
# # st.sidebar.title("Sidebar Title")
# # st.sidebar.header("Options")
# # st.sidebar.text("This is a sidebar")

# # # Main content
# # st.title("Main Content Area")
# # st.write("This is the main area of the app.")

# # import streamlit as st

# # # Sidebar
# # st.sidebar.image("portfolio-image.png", caption="Logo", use_container_width=True)
# # st.sidebar.title("Navigation")
# # selected_page = st.sidebar.radio("Go to", ["Dashboard", "Settings", "Profile"])

# # # Main content
# # if selected_page == "Dashboard":
# #     st.title("Dashboard")
# #     st.write("Welcome to the dashboard.")
# # elif selected_page == "Settings":
# #     st.title("Settings")
# #     st.write("Change your preferences here.")
# # elif selected_page == "Profile":
# #     st.title("Profile")
# #     st.write("View and edit your profile.")


# import streamlit as st

# # Inject custom CSS to move the sidebar
# st.markdown(
#     """
#     <style>
#         /* Move the sidebar to the right */
#         .css-1d391kg {
#             order: 1;
#         }
#         .css-1v3fvcr {
#             order: 2;
#         }
#     </style>
# """,
#     unsafe_allow_html=True,
# )

# # Sidebar
# st.sidebar.title("Right Sidebar")
# st.sidebar.write("This is the right-aligned sidebar.")

# # Main content
# st.title("Main Content Area")
# st.write("This is the main area of the app.")


# # stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
# # stm.title("This is the Home Page Geeks.")
# # stm.text("Geeks Home Page")


# # import streamlit as stm
# # from streamlit_extras import add_vertical_space as avs

# # stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
# # stm.title("This is the Home Page Geeks.")
# # stm.text("Geeks Home Page")

# # # Text before putting space
# # stm.write("The text after which we will put spaces")

# # # Putting 5 vertical spaces
# # avs.add_vertical_space(5)

# # # Text after the 5th space.
# # stm.write("The text after putting spaces")

# # import streamlit as stm
# # from streamlit_extras import add_vertical_space as avs
# # import annotated_text as ant
# # from annotated_text import annotation

# # stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
# # stm.title("This is the Home Page Geeks.")
# # stm.text("Geeks Home Page")

# # # Vertical Space
# # stm.write("The text after which we will put spaces")
# # avs.add_vertical_space(5)
# # stm.write("The text after putting spaces")

# # # Annotated Text
# # ant.annotated_text(
# #     "Hey",
# #     annotation("GeeksforGeeks", color="#07a631"),
# #     ("is", "the", "blue"),
# #     # Text is - 'is','the',
# #     # the color of them is 'blue',
# #     # we don't need to use color
# #     # kwarg here like annotation
# #     # function below to give color.
# #     # We can also provide Hex values of colors as well as names
# #     annotation("BEST", border="3px groove yellow"),
# #     annotation("for", "EVERYTHING", color="#f7f8fa"),
# # )


# # import streamlit as stm
# # from streamlit_extras.buy_me_a_coffee import button

# # stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
# # stm.title("This is the Home Page Geeks.")
# # stm.text("Geeks Home Page")

# # button(username="Geeks", floating=False, width=250)


# # import streamlit as stm
# # from streamlit_card import card


# # stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
# # stm.title("This is the Home Page Geeks.")
# # stm.text("Geeks Home Page")


# # # Card

# # card(
# #     title="Hello Geeks!",
# #     text="Click this card to redirect to GeeksforGeeks",
# #     image="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190710102234/download3.png",
# #     url="https://www.geeksforgeeks.org/",
# # )


# # import streamlit as stm
# # from streamlit_extras.dataframe_explorer import dataframe_explorer
# # import pandas as pd


# # stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
# # stm.title("This is the Home Page Geeks.")
# # stm.text("Geeks Home Page")


# # df = pd.read_csv("iris.csv")

# # filtered_df = dataframe_explorer(df)
# # stm.dataframe(filtered_df, use_container_width=True)


# # import streamlit as stm
# # from streamlit_extras.keyboard_url import keyboard_to_url
# # from streamlit_extras.keyboard_text import key

# # keyboard_to_url(key="G", url="https://www.geeksforgeeks.org/")
# # stm.write(
# #     f"""Now hit {key("G", False)} on your keyboard...!""",
# #     unsafe_allow_html=True,
# # )

# # # keeping it True after G will print G on screen, False will not show
