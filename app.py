import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square,cube and fifth power")
n = st.number_input("Enter am integer",value = 1,step = 1)

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

st.write(f"The Square is :{square(n)}")
st.write(f"The Cube is :{cube(n)}")
st.write(f"The Fifth Power is :{fifth_power(n)}")
