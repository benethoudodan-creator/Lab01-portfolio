import streamlit as st

st.title("Portfolio Quiz")

st.write("""
Welcome to my portfolio quiz. This will really test your attention span and if actually read through the porfolio throughly.
Good Luck!👍
""")
#Multiple Choice
st.header("1.What instrument does Benet mainly play as a Band leader?")
st.image("Images/Drum-Play.jpeg", caption="Drums")
st.image("Images/Piano-Play.jpeg",caption="Piano")
st.image("Images/Bass-Play.jpeg", caption="Bass")
main_instrument = st.selectbox(
    "Choose one:",
    ["Drums", "Piano", "Bass"]

)


st.header("2.What language is Benet the most fluent in speaking?")

most_fluent_language = st.radio(
    "Choose one:",
    ["English", "French", "Ewe", "Chinese"]

)

st.header("3.What is Benet majoring in while at Georgia Tech?")

Major = st.radio(
    "Choose one:",
    ["Computer Science", "Computer Information Systems", "Psychology", "Computer Engineering"]

)    

#Multi-Select
st.header("4.What courses are part of Benet's relevant coursework for this semester?")

relevant_coursework = st.multiselect(
    "Select Multiple Answers:",
    ["Math 1113", "CHEM 1310", "APPH 1040", "APPH 1050"]

 )


#Number-Input
st.header("5.What is Benet's anticipated graduation date from Georgia Tech?")


graduation_date = st.number_input(
    "Type in a number:",
   
    

)
