import streamlit as st
from pathlib import Path

parent_path = Path(__file__).parent.parent

def info_page():
    # Display an image
    st.markdown("")
    st.markdown(":red[The Dark Triad] refers to the trio of the three personality traits - narcissism, psychopathy and Marchiavellianism.")
    image_file = Path(parent_path, "images", "image_front.jpg").absolute().as_posix()
    st.image(image_file, caption="Dark Triad", use_column_width=True)
    
    # st.header("Page Info Content")
    # wiki
    # short descriptions
    links = "[Machiavellianism](https://en.wikipedia.org/wiki/Machiavellianism_(psychology))&nbsp;&nbsp;[Narcissism](https://en.wikipedia.org/wiki/Narcissism)&nbsp;&nbsp;[Psychopathy](https://en.wikipedia.org/wiki/Psychopathy)"
    st.markdown(f"""
        - Not familiar with the **terms**? Check this out:&nbsp; {links}
        - Our aim is to provide you insights about your personality with just a **few clicks**!""")
    
    st.divider()
    st.markdown("**Disclaimer: Any personality disorder can only be diagnosed by mental health professionals.**")



    # image_file = Path(parent_path, "images", "7nmpjd.gif").absolute().as_posix()
    # st.image(image_file, caption="Image Caption", use_column_width=True)
