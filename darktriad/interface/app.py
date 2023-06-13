'''
Creates the interface (streamlit)
'''
import streamlit as st
from darktriad.interface.info_page import info_page
from darktriad.interface.front_page import front_page
from darktriad.interface.test_page import test_page
from darktriad.interface.result_page import result_page

start_button_clicked = False



###############################Working###################################

st.title("Dark Triad App")

def onNextPage():
    st.session_state['selection'] += 1
    
def reset():
    st.session_state['selection'] = 0

if 'selection' not in st.session_state:
    st.session_state['selection'] = 0

if 'counter' not in st.session_state.keys():
    st.session_state.counter = 0

# Sidebar navigation or menu selection
page = st.sidebar.selectbox("Select Page", ("Info", "Front", "Test", "Result"), index=st.session_state['selection'])

# Display the selected page
if page == "Info":
    info_page()
    next_page_info = st.button('Next Page', on_click=onNextPage)
elif page == "Front":
    front_page()
    next_page_front = st.button('Next Page', on_click=onNextPage)
elif page == "Test":
    test_page()
    if st.session_state.counter == 27:
        next_page_test = st.button('Next Page', on_click=onNextPage)
elif page == "Result":
    result_page()
    go_back = st.button('Go Back', on_click=reset)
