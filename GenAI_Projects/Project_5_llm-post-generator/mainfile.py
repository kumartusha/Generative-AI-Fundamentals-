import streamlit as st
from few_shot_learning import FewShotPosts
from generate_post import generate_post

length_options = ["Shorts", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():
    st.title("Social Media Post Generator")
    col1, col2, col3 = st.columns(3)  # Return the tuple
    fs = FewShotPosts()
    with col1:
        selcted_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selcted_length = st.selectbox("Length", options=length_options)

    with col3:
        selcted_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selcted_length, selcted_language, selcted_tag)
        st.write(post)


if __name__ == "__main__":
    main()
