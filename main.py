import streamlit as st
from utils import generate_script

st.title("🎬 视频脚本生成器")
with st.sidebar:
    API_KEY = st.text_input("🔑 API_KEY:")
    st.markdown("[获取API_KEY](https://chat.openai.com/)")

video_subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("⏲ 请输入视频的大致时长(单位：分钟)", step=0.1)
video_creativity = st.slider("🧠 请输入视频脚本的创造力（数字越低越严谨，越高越多样）", min_value=0.1, value=0.2,
                             max_value=1.0,
                             step=0.2)
button = st.button("生成脚本")
if button and not API_KEY:
    st.info("请输入API_KEY")
    st.stop()
if button and (not video_subject or video_length == 0):
    if not video_subject:
        st.info("请输入视频主题")
    else:
        st.info("请输入视频长度")
    st.stop()
if button:
    with st.spinner(text='🏃 正在生成...'):
        response = generate_script(API_KEY, video_length, video_creativity, video_subject)
    st.success("⭐ 已生成")
    st.subheader("🍊 标题：")
    st.write(response[1])
    st.subheader("🥐 视频脚本：")
    st.write(response[2])
    with st.expander("🍞 wiki信息"):
        st.write(response[0])
