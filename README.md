# Song-Popularity-Prediction
DS40 Final Project

# 1. Exploratory Data Analysis (EDA) (1 orang), kandidat rima

**pahamin dataset :**
- bisa pake df.info() dan df.describe() untuk melihat tipe data, distribusi nilai, sama data yang mungkin hilang.

**liat missing values:**
- bisa pake df.isnull().sum() bisa terus visualisasikan pake heatmap dari seaborn buat liat kolom mana yang memiliki missing values.

**Analisis distribusi variabel target (si popularity):**
- visualisasiin distribusi variabel target (popularitas) dengan histogram atau bar chart untuk melihat pola dasar dari target. basicly ngecek kondisi si y

**bisa juga analisis korelasi fitur-fitur numerik:**
- bisa pake sns.heatmap() buat liat korelasi antara fitur numerik seperti duration_ms, key, tempo, dan lainnya.

**Visualisasi kategori genre:**
- Buat countplot untuk kategori seperti genre untuk melihat distribusi genre di dataset.

**Analisis outliers:**
- pake boxplot untuk fitur numerik seperti duration_ms, tempo, loudness, untuk mengidentifikasi apakah ada outliers yang perlu ditangani.

**Visualisasi hubungan antara fitur penting dan popularitas:**
- Gunakan scatter plot untuk melihat hubungan antara variabel numerik yang paling relevan (seperti loudness, tempo, atau duration_ms) dengan popularitas lagu.

ps : gaharus semua, ini reference aja karena EDA intinya biar lebih tau soal data kita, karena ini dataset kaggle yang notabenenya udah diatur bagus dan buat latian. Gw rasa datanya bakal dalam kondisi oke.
