import streamlit as st
from pathlib import Path

parent_path = Path(__file__).parent.parent

def info_page():
    # st.header("Page Info Content")
    # wiki
    # short descriptions
    links = "[Machiavellianism](https://en.wikipedia.org/wiki/Machiavellianism_(psychology))&nbsp;&nbsp;[Narcissism](https://en.wikipedia.org/wiki/Narcissism) &nbsp; &nbsp;[Psychopathy](https://en.wikipedia.org/wiki/Psychopathy)"
    st.markdown(f"""
        - Uncover intriguing insights about your personality with just a few clicks!
        - Not sure what they are? &nbsp; {links}
    """)

    st.markdown(" ")
    st.markdown(" ")

    # Display an image
    image_file = Path(parent_path, "images", "7n3krt.jpg").absolute().as_posix()
    st.image(image_file, caption="Image Caption", use_column_width=True)

    # Add new line
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    image_file = Path(parent_path, "images", "7nmpjd.gif").absolute().as_posix()
    st.image(image_file, caption="Image Caption", use_column_width=True)
