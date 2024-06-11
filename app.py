import streamlit as st
from transformers import pipeline
from transformers import T5ForConditionalGeneration, T5Tokenizer
import json


# タイトルの追加
st.title("生成モデルのデモ（GPT2-XL）")

# モデルの定義
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
    with st.spinner("Generating..."):
        translation = translator(text)
        translated_text = translation[0]['translation_text']
        st.success("Generation completed!")
    
    with col2:
        # 出力を右側のコラムに表示
        st.subheader("Generated text:")
        st.write(translated_text)
