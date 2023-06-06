'''
Creates the interface (streamlit)
'''
import streamlit as st

def show_questions_get_answers():
    st.markdown("""# Dark Triad Personality Prediction
    Rate the following items on a five point scale with the labels: 1=disagree, 3=neutral, 5=agree""")
    answers = []
    questions = ["It's not wise to tell your secrets.",
                 "I like to use clever manipulation to get my way.",
                 "Whatever it takes, you must get the important people on your side. ",
                 "Avoid direct conflict with others because they may be useful in the future. ",
                 "It’s wise to keep track of information that you can use against people later. ",
                 "You should wait for the right time to get back at people. ",
                 "There are things you should hide from other people because they don’t need to know.",
                 "Make sure your plans benefit you, not others.",
                 "Most people can be manipulated.",
                 "People see me as a natural leader. ",
                 "I hate being the center of attention.",
                 "Many group activities tend to be dull without me.  ",
                 "I know that I am special because everyone keeps telling me so. ",
                 "I like to get acquainted with important people. ",
                 "I feel embarrassed if someone compliments me.",
                 "I have been compared to famous people. ",
                 "I am an average person.",
                 "I insist on getting the respect I deserve.",
                 "I like to get revenge on authorities.",
                 "I avoid dangerous situations.",
                 "Payback needs to be quick and nasty. ",
                 "People often say I’m out of control. ",
                 "It’s true that I can be mean to others. ",
                 "People who mess with me always regret it.",
                 "I have never gotten into trouble with the law.",
                 "I enjoy having sex with people I hardly know ",
                 "I’ll say anything to get what I want.]"]

    for i, q in enumerate(questions):
        option = st.selectbox(f"{i+1})  {q}", ('Select a number', '1', '2', '3', '4', '5'))
        # print('option', option)
        if option != 'Select a number':
            st.write('You selected:', option)
            answers.append(int(option))
            # print('answers', answers)

    # Add custom CSS to align button to the right
    st.markdown(
        """
        <style>
        .st-bk {
            width: 200px;
        }
        """,
        unsafe_allow_html=True
    )

    if st.button('See your results') and answers == []:
        # Perform validation
        st.error('You must choose a number')

    return answers # a list of numbers

show_questions_get_answers()
