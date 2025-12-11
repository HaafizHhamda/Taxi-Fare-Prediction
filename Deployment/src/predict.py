import streamlit as st
import pandas as pd
import pickle
import numpy as np

# # Load all files

with open('best_random_forest_regressor.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle

# # ====== Load model (Pipeline) ======
# # @st.cache_resource
# # def load_model():
# #     with open('model_file/best_random_forest_regressor.pkl', 'rb') as f:
# #         return pickle.load(f)

# # model = load_model()

# ====== UI & Inference ======
def run():
    st.title("Taxi Trip Price")

    with st.form(key='taxi_form'):
        st.subheader("Masukan Nilai yang Akan di Check")

        # --- Numerik
        col1, col2 = st.columns(2)
        with col1:
            trip_distance = st.number_input(
                'Trip_Distance_km', min_value=0.0
            )
            base_fare = st.number_input(
                'Base_Fare', min_value=0.0
            )
            per_km_rate = st.number_input(
                'Per_Km_Rate', min_value=0.0
            )
            per_minute_rate = st.number_input(
                'Per_Minute_Rate', min_value=0.0
            )
        with col2:
            passenger_count = st.number_input(
                'Passenger_Count', min_value=1.0
            )
            trip_duration = st.number_input(
                'Trip_Duration_Minutes', min_value=0.0
            )

        st.markdown("---")

        # --- Kategori
        time_of_day = st.selectbox(
            'Time_of_Day',
            options=['Morning', 'Afternoon', 'Evening', 'Night', 'Unknown']
        )
        day_of_week = st.selectbox(
            'Day_of_Week',
            options=['Weekday', 'Weekend', 'Unknown']
        )
        traffic = st.selectbox(
            'Traffic_Conditions',
            options=['Low', 'Medium', 'High', 'Unknown']
        )
        weather = st.selectbox(
            'Weather',
            options=['Clear', 'Rain', 'Unknown']
        )

        submit = st.form_submit_button('Predict')

    if submit:
        # susun data sesuai kolom training
        data_inf = pd.DataFrame([{
            'Trip_Distance_km': float(trip_distance),
            'Time_of_Day': time_of_day,
            'Day_of_Week': day_of_week,
            'Passenger_Count': float(passenger_count),
            'Traffic_Conditions': traffic,
            'Weather': weather,
            'Base_Fare': float(base_fare),
            'Per_Km_Rate': float(per_km_rate),
            'Per_Minute_Rate': float(per_minute_rate),
            'Trip_Duration_Minutes': float(trip_duration),
        }])

        st.caption("Preview data inference")
        st.dataframe(data_inf, use_container_width=True)

        # prediksi (asumsi: model adalah Pipeline yg sudah termasuk preprocessing)
        y_pred = model.predict(data_inf)

        st.success(f"Predicted Trip_Price: **${y_pred[0]:.2f}**")

        # Optional: informasi tambahan
        st.caption("Catatan: Semoga dengan adanya Machine learing ini membantu anda dalam keluhan harga tidak dinamis dan adil.")

if __name__ == '__main__':
    run()
