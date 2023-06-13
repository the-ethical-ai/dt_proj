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
    image_file = "https://github.com/Habeus-Crimpus/dt_proj/blob/master/7n590c.jpg?raw=true"
    st.image(image_file, caption="Image Caption", use_column_width=True)

    # Add new line
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    image_file = "https://github.com/Habeus-Crimpus/dt_proj/blob/master/7nmpjd.gif?raw=true"
    st.image(image_file, caption="Image Caption", use_column_width=True)
