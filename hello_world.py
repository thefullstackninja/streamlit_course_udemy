import streamlit as st

st.title("Hello world App")
st.write("Please provide your details in the sidebar on the left")

# add a sidebar
st.sidebar.subheader("Details about yourself")

first_name = st.sidebar.text_input(label="First Name")

print(first_name)

print(type(first_name))

last_name = st.sidebar.text_input(label="Last Name")

age = st.sidebar.number_input(label="Age", min_value=1, step=1)

gender = st.sidebar.radio(label="Gender", options=['Male', 'Female', 'NA'])

submit_button = st.sidebar.button(label="Submit")

print(submit_button)

print(type(submit_button))

if submit_button:
    st.write("first name is  "+first_name)
    st.write('Last Name is '+last_name)
    st.write("Age is "+ str(age))
    st.write('Gender is '+gender)
