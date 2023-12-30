import streamlit as st
import glob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz

# Membaca DataFrame dari file CSV
st.title("Pencarian Document Menggunakan cosine similarity")

uploaded_file = st.file_uploader("Choose a file")
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df = df[['text', 'url']]

    # Menampilkan data dokumen dan URL
    st.write("Data Dokumen Wikipedia")
    st.write(df)

def fuzzyfinder(user_input, collection, cutoff=60):
    suggestions = []
    for item in collection:
        ratio = fuzz.token_set_ratio(user_input, item)
        if ratio >= cutoff:
            suggestions.append((item, ratio))
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
    return suggestions

def filter_documents(df, keywords):
    filtered_df = df
    for keyword in keywords:
        filtered_df = filtered_df[filtered_df['text'].str.lower().str.contains(keyword.lower())]
    return filtered_df


def make_clickable(url):
    return f'<a href="{url}" target="_blank">{url}</a>'

def truncate_text(text, max_length=250):
    if len(text) > max_length:
        return text[:max_length] + "..."  # Truncate text if it exceeds max_length
    return text

# Mendapatkan input dari pengguna
input_text = st.text_input('Masukkan teks di sini')

# Menampilkan hasil pengurutan berdasarkan relevansi
if st.button('Submit') and input_text:
    keywords = input_text.split()
    filtered_df = filter_documents(df, keywords)
    
    # Memeriksa apakah ada dokumen yang relevan
    if not filtered_df.empty:
        vectorizer = TfidfVectorizer()
        # Menghitung nilai kesamaan dengan cosine_similarity
        vectorizer.fit(df['text'])
        input_vector = vectorizer.transform([input_text])
        filtered_vectors = vectorizer.transform(filtered_df['text'])
        similarities = cosine_similarity(input_vector, filtered_vectors)

        # Mengurutkan berdasarkan kesamaan (dari yang terbesar)
        filtered_df['similarity'] = similarities[0]
        filtered_df = filtered_df.sort_values(by='similarity', ascending=False)

        filtered_df['url'] = filtered_df['url'].apply(make_clickable)
        filtered_df['text'] = filtered_df['text'].apply(truncate_text)
        filtered_df = filtered_df[['text', 'url', 'similarity']].to_html(escape=False)
        # Menampilkan hasil
        st.write(filtered_df, unsafe_allow_html=True)
    else:
        st.write("Tidak ada dokumen yang sesuai dengan kata kunci yang dimasukkan.")
