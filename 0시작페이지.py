import streamlit as st
from openai import OpenAI

st.markdown(
    """
    <div style="text-align: center; font-size: 30px; font-weight: bold;">
        <p><b>✨인공지능 영어 선생님 잉글링👩‍🏫</b></p>
        <p><b>Hi, I'm Momo🖐</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()
st.write("1️⃣ 자기 소개하기, 만나고 헤어질 떄의 인사하기")
st.write("2️⃣ 안부 묻고 답하기")
