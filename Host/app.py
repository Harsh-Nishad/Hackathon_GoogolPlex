import streamlit as st
import pandas as pd
from PIL import Image

# version of PIL



#title
st.title("Engineering drawing recognition and conversion to SVG format")

ps='<p style="font-family:Courier; color:Red; font-size: 30px; font-weight:10px ">PROBLEM STATEMENT</p>'
st.markdown(ps, unsafe_allow_html=True)

st.markdown('Given a engineering drawing as an input the task is to extract all the significant structures like Lines ,Circles,Text and Keys/Objects.') 

# st.markdown('**:yellow[Given Dataset] :red[colored red]**')
original_title = '<p style="font-family:Courier; color:	rgb(221,160,221); font-size: 20px; font-weight:10px ">Given Dataset</p>'
st.markdown(original_title, unsafe_allow_html=True)

Image=st.image("input_full.png",width=500,use_column_width=True)


obj='<p style="font-family:Courier; color:rgb(221,160,221); font-size: 20px; font-weight:10px ">Object_Detection Output</p>'
# st.markdown('**Object_Detection Output**')
st.markdown(obj, unsafe_allow_html=True)
obj_img=st.image("obj.jpg",width=500,use_column_width=True)


circle='<p style="font-family:Courier; color:rgb(221,160,221); font-size: 20px; font-weight:10px ">Circle_Detection Output</p>'
st.markdown(circle, unsafe_allow_html=True)
cir_img=st.image("cir.jpg",width=500,use_column_width=True)



line='<p style="font-family:Courier; color:rgb(221,160,221); font-size: 20px; font-weight:10px ">Line_Detection Output</p>'
st.markdown(line, unsafe_allow_html=True)

line_img=st.image("line.jpg",width=500,use_column_width=True)

text='<p style="font-family:Courier; color:rgb(221,160,221); font-size: 20px; font-weight:10px ">Text_Detection Output</p>'
st.markdown(text, unsafe_allow_html=True)
tet_img=st.image("text.jpg",width=500,use_column_width=True)





st.markdown('**Common CSV file contaning coordinates of the lines,circles,objects,text**')
#read csv file
df=pd.read_csv('common.csv')
st.write(df)

st.header('After converting coordinated from CSV to SVG format')
Output=st.image("svg output.jpg",width=500,use_column_width=True)


st.markdown('**SVG Output comparison with dataset image**')


out='<p style="font-family:Courier; color:rgb(221,160,0); font-size: 25px; font-weight:10px ">SVG Output</p>'
st.markdown(out, unsafe_allow_html=True)
Output=st.image("svg op imposed.jpg",width=500,use_column_width=True)



st.markdown('**RUNNER UP @HACKATHON Conducted by VIT Chennai**')

# two images in grid
col1, col2 = st.columns(2)
col1.image("pic.jpg",width=500,use_column_width=True)
col2.image("cirf.jpg",width=500,use_column_width=True)

# leave a line space 
st.write("")
st.write("")


columns = st.columns(6)

with columns[1]:
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/harsh-nishad-430b59109/" style="float:center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/1200px-LinkedIn_icon_circle.svg.png" width="22px"></img></a></div>""", unsafe_allow_html=True)
    st.write('  Harsh Nishad')
    
with columns[2]:
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/samuel-shaju-32189b218/" style="float:center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/1200px-LinkedIn_icon_circle.svg.png" width="22px"></img></a></div>""", unsafe_allow_html=True)
    st.write('  Samuel Shaju')

with columns[3]:
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/rishik-kumar/" style="float:center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/1200px-LinkedIn_icon_circle.svg.png" width="22px"></img></a></div>""", unsafe_allow_html=True)
    st.write('  Rishik Kumar')

with columns[4]:
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/pradhyumanarora/" style="float:center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/1200px-LinkedIn_icon_circle.svg.png" width="22px"></img></a></div>""", unsafe_allow_html=True)
    st.write('Pradhyuman Arora')