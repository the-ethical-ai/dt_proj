import streamlit as st

def info_page():
    #st.header("Page Info Content")
    # Add content specific to Page 1
    # wiki
    # short descriptions
    links = "[Machiavellianism](https://en.wikipedia.org/wiki/Machiavellianism_(psychology))&nbsp;&nbsp;[Narcissism](https://en.wikipedia.org/wiki/Narcissism) &nbsp; &nbsp;[Psychopathy](https://en.wikipedia.org/wiki/Psychopathy)"
    st.markdown(f"""
        - Uncover intriguing insights about your personality with just a few clicks!
        - Not sure what they are? &nbsp; {links}
    """)

    # Display an image from a file
    image_file = "/Users/imgeildan/code/imgeildan/dt_proj/darktriad/images/7n3krt.jpg"
    st.image(image_file, caption="Image Caption", use_column_width=True)

    # Add new line
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    image_file = "/Users/imgeildan/code/imgeildan/dt_proj/darktriad/images/7nmpjd.gif"
    st.image(image_file, caption="Image Caption", use_column_width=True)
