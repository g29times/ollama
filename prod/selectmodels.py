# 支持多模态模型切换的web程序

import streamlit as st
import ollama
from PIL import Image  
from io import BytesIO

# 设置可用的模型列表
available_models = [
    'yi',
    'llava',
]

model_choice = st.sidebar.selectbox('选择模型:', available_models)

user_input = st.text_area('提出一个问题:', '', height=150) 

st.markdown("""
    <style>
    .dashed-box {
        border: 2px dashed #FFA500;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

uploaded_file = st.file_uploader("上传图片", type=['jpg','png','jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    
    # 将RGBA图像转换为RGB
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    st.image(img, caption='上传的图片', use_column_width=True)

if st.button('提交'):
    messages = [{'role': 'user', 'content': user_input}]

    if uploaded_file:
        
        with BytesIO() as buffer:
            img.save(buffer, 'jpeg')
            img_bytes = buffer.getvalue()

        messages[0]['images'] = [img_bytes]

    response = ollama.chat(
        model=model_choice,
        messages=messages,
        stream=True
    )

    final_response = ''
    for chunk in response:
        if 'content' in chunk.get('message', {}):
            final_response += chunk['message']['content']

    st.markdown(f'<div class="dashed-box">{final_response}</div>', unsafe_allow_html=True)