import streamlit as st
from send_email import send_email

with st.form(key='form'):
    email = st.text_input('Your Email Address')
    topic = st.selectbox('What topic do you want to discuss?', ['Job Inquiries', 'Project Proposals', 'Other'])
    raw_message = st.text_area('Text')
    message = f'''\
    Subject : {topic} from {email}
    
    From: {email}
    {raw_message}
    '''
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Your email was sent successfully!')
