import app as st
import pandas as pd
import pickle

# Cargar el modelo y los codificadores previamente entrenados
model = pickle.load(open("random_forest_model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
target_encoder = pickle.load(open("target_encoder.pkl", "rb"))

st.title("Predicción de Retención de Estudiantes")

# Opciones para variables categóricas
marital_status_options = {
    1: "Soltero", 2: "Casado", 3: "Viudo", 4: "Divorciado", 5: "Unión de hecho", 6: "Separado legalmente"
}
application_mode_options = {
    1: "1ª fase - contingente general", 2: "Ordenanza No. 612/93", 5: "1ª fase - contingente especial (Islas Azores)",
    7: "Titulares de otros cursos superiores", 10: "Ordenanza No. 854-B/99", 15: "Estudiante internacional (licenciatura)"
}
course_options = {
    33: "Tecnologías de Producción de Biocombustibles", 171: "Diseño de Animación y Multimedia",
    8014: "Servicio Social (turno nocturno)", 9003: "Agronomía", 9070: "Diseño de Comunicación"
}

# Inputs para todas las variables
marital_status = st.selectbox("Estado Civil", options=list(marital_status_options.keys()),
                              format_func=lambda x: marital_status_options[x])
application_mode = st.selectbox("Modo de Aplicación", options=list(application_mode_options.keys()),
                                 format_func=lambda x: application_mode_options[x])
application_order = st.number_input("Orden de Solicitud", min_value=0, max_value=9, step=1)
course = st.selectbox("Curso", options=list(course_options.keys()),
                      format_func=lambda x: course_options[x])
daytime_evening_attendance = st.radio("Turno", options=[1, 0], format_func=lambda x: "Diurno" if x == 1 else "Nocturno")
previous_qualification = st.number_input("Calificación Previa", min_value=0, max_value=200, step=1)
nacionality = st.number_input("Nacionalidad (Código)", min_value=1, max_value=200, step=1)
mothers_qualification = st.number_input("Calificación de la Madre (Código)", min_value=1, max_value=50, step=1)
fathers_qualification = st.number_input("Calificación del Padre (Código)", min_value=1, max_value=50, step=1)
mothers_occupation = st.number_input("Ocupación de la Madre (Código)", min_value=0, max_value=200, step=1)
fathers_occupation = st.number_input("Ocupación del Padre (Código)", min_value=0, max_value=200, step=1)
displaced = st.radio("Desplazado", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
educational_special_needs = st.radio("Necesidades Especiales", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
debtor = st.radio("Deudor", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
tuition_fees_up_to_date = st.radio("Pagos al Día", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
gender = st.radio("Género", options=[1, 0], format_func=lambda x: "Masculino" if x == 1 else "Femenino")
scholarship_holder = st.radio("Becado", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
age_at_enrollment = st.number_input("Edad al Matricularse", min_value=17, max_value=70, step=1)
international = st.radio("Internacional", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
curricular_units_1st_sem_enrolled = st.number_input("Unidades Curriculares Matriculadas (1er Semestre)", min_value=0, max_value=20, step=1)
curricular_units_1st_sem_approved = st.number_input("Unidades Curriculares Aprobadas (1er Semestre)", min_value=0, max_value=20, step=1)
curricular_units_1st_sem_grade = st.number_input("Nota Media (1er Semestre)", min_value=0.0, max_value=20.0, step=0.1)
curricular_units_2nd_sem_enrolled = st.number_input("Unidades Curriculares Matriculadas (2do Semestre)", min_value=0, max_value=20, step=1)
curricular_units_2nd_sem_approved = st.number_input("Unidades Curriculares Aprobadas (2do Semestre)", min_value=0, max_value=20, step=1)
curricular_units_2nd_sem_grade = st.number_input("Nota Media (2do Semestre)", min_value=0.0, max_value=20.0, step=0.1)
unemployment_rate = st.number_input("Tasa de Desempleo (%)", min_value=0.0, max_value=100.0, step=0.1)
inflation_rate = st.number_input("Tasa de Inflación (%)", min_value=0.0, max_value=10.0, step=0.1)
gdp = st.number_input("PIB (%)", min_value=-10.0, max_value=10.0, step=0.1)

# Crear el dataframe de entrada
input_data = pd.DataFrame({
    'Marital status': [marital_status],
    'Application mode': [application_mode],
    'Application order': [application_order],
    'Course': [course],
    'Daytime/evening attendance': [daytime_evening_attendance],
    'Previous qualification': [previous_qualification],
    'Nacionality': [nacionality],
    "Mother's qualification": [mothers_qualification],
    "Father's qualification": [fathers_qualification],
    "Mother's occupation": [mothers_occupation],
    "Father's occupation": [fathers_occupation],
    'Displaced': [displaced],
    'Educational special needs': [educational_special_needs],
    'Debtor': [debtor],
    'Tuition fees up to date': [tuition_fees_up_to_date],
    'Gender': [gender],
    'Scholarship holder': [scholarship_holder],
    'Age at enrollment': [age_at_enrollment],
    'International': [international],
    'Curricular units 1st sem (enrolled)': [curricular_units_1st_sem_enrolled],
    'Curricular units 1st sem (approved)': [curricular_units_1st_sem_approved],
    'Curricular units 1st sem (grade)': [curricular_units_1st_sem_grade],
    'Curricular units 2nd sem (enrolled)': [curricular_units_2nd_sem_enrolled],
    'Curricular units 2nd sem (approved)': [curricular_units_2nd_sem_approved],
    'Curricular units 2nd sem (grade)': [curricular_units_2nd_sem_grade],
    'Unemployment rate': [unemployment_rate],
    'Inflation rate': [inflation_rate],
    'GDP': [gdp]
})

# Codificar los datos de entrada
for col, le in label_encoders.items():
    if col in input_data.columns:
        input_data[col] = le.transform(input_data[col])

# Realizar la predicción
if st.button("Predecir"):
    prediction = model.predict(input_data)
    prediction_prob = model.predict_proba(input_data)

    st.write("Predicción:", target_encoder.inverse_transform(prediction)[0])
    st.write("Probabilidades de cada clase:")
    for i, class_name in enumerate(target_encoder.classes_):
        st.write(f"{class_name}: {prediction_prob[0][i]:.2f}")
