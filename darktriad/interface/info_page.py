import streamlit as st

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
    image_file = "../images/7n3krt.jpg"
    st.image(image_file, caption="Image Caption", use_column_width=True)

    # Add new line
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    image_file = "../images/7nmpjd.gif"
    st.image(image_file, caption="Image Caption", use_column_width=True)
