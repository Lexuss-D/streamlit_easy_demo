import streamlit as st
from transformers import pipeline
from transformers import T5ForConditionalGeneration, T5Tokenizer
import json


# 设置页面标题
st.title("生成モデルのデモ（GPT2-XL）")

# 中英翻訳モデルの定義

@st.cache_resource
def load_translation_pipeline():
    return pipeline("translation", model="openai-community/gpt2-xl")

translator = load_translation_pipeline()
#　画面を2列に
col1, col2 = st.columns(2)

# 入力スペースは左のコラムに
with col1:
    text = st.text_area("Enter here", "")

#　出力スペースは右側に
if text:
    with st.spinner("Translating..."):
        translation = translator(text)
        translated_text = translation[0]['translation_text']
        st.success("Translation completed!")
    
    with col2:
        # 显示翻译后的文本
        st.subheader("Generated text:")
        st.write(translated_text)
