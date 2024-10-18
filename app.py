import streamlit as st
import math

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Evaluate the expression
        result = str(eval(expression))
    except Exception as e:
        result = "Error"
    return result

# Initialize the expression variable
expression = ""

# Title of the app
st.title("Scientific Calculator")

# Display area
calc_display = st.text_input("Expression", expression, disabled=True)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sqrt', 'log', 'sin', 'cos'],
    ['tan', '(', ')', 'C']
]

# Store the current expression
if "calc_exp" not in st.session_state:
    st.session_state.calc_exp = ""

# Function to update the calculator expression
def update_expression(value):
    if value == "=":
        st.session_state.calc_exp = evaluate_expression(st.session_state.calc_exp)
    elif value == "C":
        st.session_state.calc_exp = ""
    elif value == "sqrt":
        try:
            st.session_state.calc_exp = str(math.sqrt(float(st.session_state.calc_exp)))
        except:
            st.session_state.calc_exp = "Error"
    elif value == "log":
        try:
            st.session_state.calc_exp = str(math.log10(float(st.session_state.calc_exp)))
        except:
            st.session_state.calc_exp = "Error"
    elif value == "sin":
        try:
            st.session_state.calc_exp = str(math.sin(math.radians(float(st.session_state.calc_exp))))
        except:
            st.session_state.calc_exp = "Error"
    elif value == "cos":
        try:
            st.session_state.calc_exp = str(math.cos(math.radians(float(st.session_state.calc_exp))))
        except:
            st.session_state.calc_exp = "Error"
    elif value == "tan":
        try:
            st.session_state.calc_exp = str(math.tan(math.radians(float(st.session_state.calc_exp))))
        except:
            st.session_state.calc_exp = "Error"
    else:
        st.session_state.calc_exp += str(value)

# Creating the button layout
for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        if cols[i].button(button):
            update_expression(button)

# Display the updated expression
st.text_input("Updated Expression", st.session_state.calc_exp, disabled=True)
