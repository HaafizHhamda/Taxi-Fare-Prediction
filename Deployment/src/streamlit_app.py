import streamlit as st
import EDA, predict

with st.sidebar:
    st.title('Page Navigation')
    # input 
    page =st.radio('Page', ('EDA','Model Demo'))
    st.write('# About')
    st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat.
''')

if page=='EDA':
    EDA.run()
else :
    predict.run()