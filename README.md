# README

## Dataset

Dataset yang digunakan adalah wiki_150.csv yang berisi dokumen teks dari Wikipedia. Dataset ini diambil dari dataset good.csv dan dislice karena terlalu berat.

## Permasalahan dan Tujuan Eksperimen

Permasalahan yang ingin diselesaikan adalah bagaimana mencari dokumen yang relevan dengan teks input. Tujuan eksperimen adalah untuk mengetahui seberapa bagus algoritma yang digunakan untuk mencari dokumen yang relevan.

## Model dan Alur Tahapan

Model yang digunakan adalah TFIDVectorizer. Alur tahapan eksperimen adalah sebagai berikut:

- Membuat objek vectorizer dari TfidfVectorizer(), yang digunakan untuk menghitung TF-IDF (Term Frequency-Inverse Document Frequency).
- Melatih vectorizer dengan seluruh teks yang ada dalam dataframe df['text'].
- Mengubah teks input ke dalam bentuk vektor menggunakan vectorizer.transform([input_text]).
- Mengubah teks dalam filtered_df['text'] menjadi vektor.
- Menghitung kesamaan kosinus antara vektor teks input dan vektor dokumen yang telah difilter.
- Menambahkan nilai kesamaan ke dalam filtered_df dan mengurutkannya dari nilai kesamaan tertinggi ke terendah.

## Performa Model / Uji Performa Model

Untuk mengukur performa model, digunakan metric Relevance. Relevance didefinisikan sebagai rasio antara jumlah dokumen yang relevan dengan jumlah total dokumen yang direkomendasikan.

Pada eksperimen ini, didapatkan bahwa Relevance sebesar 0,75. Artinya, 75% dari dokumen yang direkomendasikan adalah dokumen yang relevan dengan teks input.
