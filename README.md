# Taxi Fare Prediction


## Problem Background
 Dalam beberapa tahun terakhir, layanan taksi menghadapi berbagai tantangan yang menimbulkan keresahan di kalangan masyarakat. Salah satu masalah utama yang sering dikeluhkan adalah **ketidaktransparanan tarif**. Banyak pengguna merasa harga perjalanan taksi tidak konsisten dan tidak mencerminkan kondisi aktual, seperti jarak, waktu, atau tingkat kemacetan. Hal ini menimbulkan persepsi bahwa sistem penetapan tarif kurang adil dan cenderung merugikan pelanggan.

Secara keseluruhan, keresahan masyarakat terhadap layanan taksi berakar pada **ketidakadilan tarif** dalam operasional. Oleh karena itu, diperlukan inovasi yang mampu menghadirkan sistem tarif dinamis, transparan, dan adil, sehingga kepercayaan masyarakat terhadap layanan taksi dapat kembali meningkat.
## Problem
Predict tarif secara akurat dan faktor apa yang mempengaruh tarif. menggunkan beberapa model untuk meningkatkan transparansi dan keadilan harga 
sehingga meningkatkan kepercayaan pelanggan terhadap tarif perjalanan taxi dan mendorong pelanggan menggunakan Taxi sebagai angkutan terpercaya
## Project Wisdom

- **Pelanggan**:
   - Model ini membantu pelanggan memprediksi tarif perjalanan taksi dengan akurat, transparan, dan adil.
   - Pelanggan dapat memperkirakan biaya perjalanan dengan faktor-faktor tertentu sebelum memesan, sehingga meminimalkan ketidakpastian dan meningkatkan kepercayaan terhadap layanan.
- **Pelaku Bisnis**:
   - Membangun Slogan Taxi 
   `harga dihitung berdasarkan jarak dan waktu tempuh Anda tanpa biaya tersembunyi.`sehingga meningkatkan kepercayaan pelanggan terhadap tarif perjalanan taxi dan mendorong pelanggan menggunakan Taxi sebagai angkutan terpercaya

## Data

Dataset: https://www.kaggle.com/datasets/denkuznetz/taxi-price-prediction 
**Dataset Information**:
- **Trip_Distance**: Total jarak perjalanan dalam kilometer.  
- **Trip_Duration**: Lama waktu perjalanan dalam menit.  
- **Time_of_Day**: Waktu keberangkatan perjalanan (Pagi, Siang, Sore, Malam).  
- **Day_of_Week**: Hari ketika perjalanan dilakukan (Senin–Minggu).  
- **Traffic_Conditions**: Tingkat kepadatan lalu lintas saat perjalanan (Low, Moderate, High, Heavy).  
- **Weather**: Kondisi cuaca selama perjalanan (Clear, Rainy, Cloudy, Foggy).  
- **Passenger_Count**: Jumlah penumpang dalam satu perjalanan.  
- **Trip_Price**: Total tarif atau harga yang dibayarkan untuk perjalanan. 


Predict tarif secara akurat dan faktor apa yang mempengaruh tarif. menggunkan meodel Decision Tree, KKN, SVM, Random Forest, and XGBoost untuk meningkatkan transparansi dan keadilan harga

## Method

- **Data Loading**: Memuat dataset, memeriksa struktur data, tipe kolom, dan missing values.

- **Exploratory Data Analysis (EDA)**: Mengidentifikasi pola, distribusi data, outlier, dan hubungan antar fitur.

- **Feature Engineering**: Cleaning, encoding, scaling, feature selection, dan pembuatan fitur baru.

- **Model Definition**: Menentukan algoritma, pipeline preprocessing, dan parameter awal.

- **Model Training**: Melatih model menggunakan cross-validation untuk memastikan generalisasi.

- **Model Evaluation**: Mengukur performa model (MAE,RMSE dan R2).

- **Model Comparison**: Membandingkan hasil dari beberapa model untuk memilih performa terbaik.

- **Hyperparameter Tuning**: Mengoptimalkan parameter menggunakan GridSearch atau RandomSearch.

- **Model Saving**: Menyimpan model final untuk deployment.

- **Conclusion**: Merangkum insight utama, performa model, dan rekomendasi perbaikan.

## Stacks

- Python:
  - Pandas
  - Numpy
  - Scipy
  - Matplotlib
  - Seaborn
  - Pickle
  - Json
  - Scikit-lern
  - XGboost
- Stremlit
- GitHub

## Reference

- Laporan analisis model data berupa notebook dan visualisasi
- `best_random_forest_regressor.pkl` berupa hasil model
- URL Deployment interaktif

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)