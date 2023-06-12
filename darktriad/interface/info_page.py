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
