import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square,cube and fifth power")
n = st.number_input("Enter am integer",value = 1,step = 1)

square = n**2
cube = n**3
fifth_power = n**5

st.write(f"The Square is :{square}")
st.write(f"The Cube is :{cube}")
st.write(f"The Fifth Power is :{fifth_power}")
