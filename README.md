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

# 2. Data Pre-processing (2 orang), kandidat Bintang,Nugroho deadline : 19 september

**Missing Values Handling:**
- tentuin cara nanganin missing values pada kolom-kolom yang ditemukan dari EDA (misalnya mode atau mean untuk numerik, atau most frequent untuk kategori).

**categorical Data Encoding:**
- lakuin encoding untuk kategori seperti genre dan key menggunakan OneHotEncoder dari scikit-learn.

**Feature Engineering:**
- tambahkan fitur baru jika diperlukan. misal, bisa buat tempo_range untuk mengkategorikan tempo lagu (slow, medium, fast).

**Scaling:**
- Normalisasi atau standardisasi fitur numerik kayak duration_ms, tempo, loudness menggunakan StandardScaler atau MinMaxScaler.

**Train-Test Split:**
- pakai train_test_split untuk memisahkan data menjadi training dan testing dengan proporsi misal 80:20.

  # 3. Model Training (2 orang), Farhad, Puteri deadline : 21 september

**Model Selection:**

Pilih beberapa model regresi, misal:
- Linear Regression,RandomForestRegressor, GradientBoostingRegressor atau XGBoost
- atau bisa ngacu ke : https://scikit-learn.org/1.3/tutorial/machine_learning_map/index.html (menurut gw tp pake yg atas aja krn akurasi mrk biasa gede :v)

**Train Models:**
- Implementasi model kayak import,buat model, fit,dll

**Hyperparameter Tuning:**
- hyper tuning tiap model beda, jadi pilih aja 2/3 model terbaik untuk lanjut (seperti n_estimators dan max_depth untuk Random Forest atau learning rate untuk Gradient Boosting.)
- bisa pakai GridSearchCV atau RandomizedSearchCV buat menemukan hyperparameter terbaik

**Cross-Validation:**
- Lakukan k-fold cross-validation (misalnya k=5) untuk memvalidasi performa model secara konsisten.

**Save model pakai pickle** (ini perlu ga ya, soalnya setau gw ini kalo mau dishare aja modelnya):
- Simpan model terbaik setelah tuning menggunakan joblib atau pickle.

  # 4. Model Evaluation (1 orang), scud . deadline : 22

**Evaluate on Test Set:**
- Evaluasi model menggunakan data testing.

**Metrik Evaluasi:**
- Gunakan metrik regresi kyk Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), dan R-squared untuk menilai performa model.

**Feature Importance (ini opsional aja kayaknya):**
- Untuk model seperti Random Forest dan Gradient Boosting, analisis fitur penting yang paling berpengaruh terhadap prediksi popularity.

**Compare Models:**
- Bandingkan performa berbagai model berdasarkan metrik seperti MSE, RMSE, dan R-squared.

  ISSUE 1 :
- untuk dataset kalau pakai drive kan harus akses drive masing2, itu gimana
- solusi sementara : buat folder dan nama file yang sama untuk tiap orang di drive nya, pakai g down, atau pakai google brg

ISSUE 2 :
- ada beberapa bagian DEPENDANT sama bagian lain (misal modeling perlu diselesain dahulu data preprocessing). Untuk EDA setau gw ga dependant karena itu insight aja tanpa ada manipulasi isi dari data
- solusi sementara : buat yg dependant buat deadline bayangan (?), atau di merge aja bagian yang beririsan

ISSUE 3 :    
- ada yg ngerti cara deployment ga hehe
- solusi sementara : jujur kalau ada 1 orang yang khusus deploy gw rasa bole aja, nanti di pembagian bisa diatur seakan dia ngerjain code
