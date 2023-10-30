# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
#st.balloons()
st.title('무엇이든 대꾸 잘해주는 "말대꾸"')

content = st.text_input('묻고싶은 내용을 입력하세요')
st.text('원하는 답변이 아니면 답해줘 버튼을 다시 눌러주세요^^')
# result = chat_model.predict(content + "국악가사를 써줘")
# print(result)

if st.button("답해줘"):
   with st.spinner('작성중...'):
      result = chat_model.predict(content+'작성해줘')
      st.write(result) 
st.image('https://blog.kakaocdn.net/dn/c7RhxY/btszwdX1c83/Jn5khN1t1JThmPPtZNwWgK/img.gif')
st.link_button("다루 홈페이지로 놀러오세요~", "http://daroousa.com")