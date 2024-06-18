import joblib
import streamlit as st

# membaca model
model_path = 'ModelNasta.hdf5'
Obes_Model = joblib.load(model_path)

# judul web
st.title('Prediksi Obesitas Anda')

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Age = st.text_input ('Input Nilai Umur')

with col2:
    gender_option = st.selectbox('Select Gender', ['Wanita', 'Pria'])
    Gender = 0 if gender_option == 'Wanita' else 1

with col1 :
    Height = st.text_input ('Input Tinggi Badan')
    try:
        height = int(Height)
    except ValueError:
        height = 180

with col2 :
    Weight = st.text_input ('Input Berat Badan')
    try:
        weight = int(Weight)
    except ValueError:
        weight = 90


height_in_meters = height / 100  # konversi tinggi badan ke meter
bmi = weight / (height_in_meters ** 2)

with col1:
    st.text_input('BMI', value=f"{bmi:.2f}", disabled=True)

with col2:
    PhysicalActivityLevel = st.selectbox(
        'Pilih Skala Kegiatan Fisik (1-4)',
        [
            '1 - Jarang beraktivitas',
            '2 - Sedikit beraktivitas',
            '3 - Cukup beraktivitas',
            '4 - Sangat aktif beraktivitas'
        ]
    )

    # Ekstraksi nilai numerik dari pilihan
    PhysicalActivityLevelValue = int(PhysicalActivityLevel[0])

# code untuk prediksi
Obes_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    Obes_prediction = Obes_Model.predict([[Age, Gender, Height, Weight, bmi, PhysicalActivityLevelValue]])
    if(Obes_prediction[0] == 'Normal weight'):
        Obes_diagnosis = 'Pasien normal'
    elif(Obes_prediction[0] == 'Obese'):
        Obes_diagnosis = 'Pasien obesitas'
    elif(Obes_prediction[0] == 'Overweight'):
        Obes_diagnosis = 'Pasien kelebihan berat badan'
    elif(Obes_prediction[0] == 'Underweight'):
        Obes_diagnosis = 'Pasien kekurangan berat badan'
    else :
        Obes_diagnosis = 'Pasien alien'
    def x(result):
        return  result
    st.success(Obes_diagnosis)
