import streamlit as st

st.title('Proyecto 3')

st.write('60L/min are to be transported through a Schedule 40 commercial steel pipe with ND 1 1/2 inch from P1 to P2 (as shown in the sketch below). If the pressure at P1 is 185psi, what would it be the pressure at P2? The transported fluid is water at 25C with s.w.=9.77kN/m3 and dynamic viscosity of 0.89mPa s. The answer can be given in Pa and psi.')

st.image('Proyecto_3.png', use_column_width=True)

# Initialize constants
gravity = float(9.81)
sw = float(9.77)
caudal = float(60)
pressure = float(1275.5301)

def calculate_button():
    # Calculate the pressure P2
    pressureGoal = ((float(pressure) / float(sw)) + float(z1) + (float(caudal)**2 / (2 * float(gravity))) - float(z2) - (float(caudal)**2) / (2 * float(gravity))) * float(sw)
    gradient = pressureGoal - pressure

    der.subheader('Pressure P2')
    if (units == 'Pa'):
        der.write(str(pressureGoal * 1000) + ' Pa')
    else:
        der.write(str(pressureGoal / 6894.76) + ' psi')

    der.subheader('Pressure gradient')
    if (units == 'Pa'):
        der.write(str(gradient * 1000) + " Pa")
    else:
        der.write(str(gradient / 6894.76) + " psi")


# Use 2 columns
izq, der = st.columns(2)

# Left column
error = False
izq.subheader('Input parameters')
units = izq.radio('Select the units that you want to use:', ('Pa', 'psi'))

z1 = izq.text_input('Input the first height (m)', key='z1', value = 0)
if (float(z1) < 0):
    izq.error('The height must be positive')
    error = True

z2 = izq.text_input('Input the second height (m)', key='z2', value = 0)
if (float(z2) < 0):
    izq.error('The height must be positive')
    error = True

izq.button('Calculate', on_click = calculate_button, help = "Click to calculate the pressure P2", disabled = error)

    

# Right column
der.subheader('Result')