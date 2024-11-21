import streamlit as st
import pandas as pd
import pickle
from joblib import load

# Cargar el modelo y los codificadores previamente entrenados
model = load("random_forest_model_updated.pkl")
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
target_encoder = pickle.load(open("target_encoder.pkl", "rb"))

st.title("Predicción de Retención de Estudiantes")

# Definir las categorías de salida como las mencionaste
category_map = {
    0: "Abandono",
    1: "Aprobado",
    2: "En curso"
}

# Opciones para variables categóricas
marital_status_options = {
    1: "Soltero", 2: "Casado", 3: "Viudo", 4: "Divorciado", 5: "Unión de hecho", 6: "Separado legalmente"
}
application_mode_options = {
    1: "1ª fase - contingente general", 2: "Ordenanza No. 612/93", 5: "1ª fase - contingente especial (Islas Azores)",
    7: "Titulares de otros cursos superiores", 10: "Ordenanza No. 854-B/99", 15: "Estudiante internacional (licenciatura)"
}
course_options = {
    1: "Tecnologías de Producción de Biocombustibles", 3: "Diseño de Animación y Multimedia",
    10: "Servicio Social (turno nocturno)", 15: "Agronomía", 17: "Diseño de Comunicación"
}
qualification_options = {
    1:'Educación secundaria',2:'Educación superior - grado de bachiller', 3: 'Educación superior - licenciatura',
    4:'Educación superior - máster', 5:'Educación superior - doctorado', 6:'Frecuencia de educación superior',
    7: '12º año de escolaridad - no completado', 8:'11º año de escolaridad - no completado',
    9: 'Otro - 11º año de escolaridad', 10:'10º año de escolaridad', 11:'10º año de escolaridad - no completado',
    12: 'Educación básica 3er ciclo (9º/10º/11º año) o equiv.', 13:'Educación básica 2º ciclo (6º/7º/8º año) o equiv.',
    14: 'Curso de especialización tecnológica', 15:'Educación superior - licenciatura (1er ciclo)',
    16: 'Curso técnico superior profesional',17: 'Educación superior - máster (2º ciclo)'
}
nationality_options = {
    1:'Portuguesa', 2:'Alemana', 3:'Española', 4:'Italiana', 5:'Holandesa', 6:'Inglesa', 7:'Lituana', 
    8:'Angoleña', 9:'Caboverdiana',10: 'Guineana', 11:'Mozambiqueña', 12:'Santotomense', 13:'Turca',
    14: 'Brasileña', 15:'Rumana', 16:'Moldava', 17:'Mexicana', 18:'Ucraniana', 19:'Rusa', 20:'Cubana',
    21:'Colombiana'
}
mothers_qualification_options={
    1:'Educación Secundaria - 12º año de escolaridad o Eq.', 2:'Educación Superior - Grado de Bachiller',
    3:'Educación Superior - Licenciatura', 4:'Educación Superior - Máster', 5:'Educación Superior - Doctorado',
    6:'Frecuencia de Educación Superior', 7:'12º año de escolaridad - No Completado', 8:'11º año de escolaridad - No Completado',
    9:'7º año (Antiguo)', 10:'Otro - 11º año de escolaridad', 11:'10º año de escolaridad', 12:'Curso general de comercio', 
    13:'Educación Básica 3er Ciclo (9º/10º/11º año) o Equiv.', 14:'Curso técnico-profesional', 15:'7º año de escolaridad',
    16:'2º ciclo del curso general de secundaria', 17:'9º año de escolaridad - No Completado', 18:'8º año de escolaridad',
    19:'Desconocido', 20:'No sabe leer ni escribir', 21:'Puede leer sin tener 4º año de escolaridad', 22:'Educación básica 1er ciclo (4º/5º año) o equiv.',
    23:'Educación Básica 2º Ciclo (6º/7º/8º año) o Equiv.', 24:'Curso de especialización tecnológica', 25:'Educación superior - licenciatura (1er ciclo)',
    26:'Curso de estudios superiores especializados', 27:'Curso técnico superior profesional', 28:'Educación Superior - Máster (2º ciclo)',
    29:'Educación Superior - Doctorado (3er ciclo)'
}
fathers_qualification_options={
    1:'Educación Secundaria - 12º año de escolaridad o Eq.', 2:'Educación Superior - Grado de Bachiller',
    3:'Educación Superior - Licenciatura', 4:'Educación Superior - Máster', 5:'Educación Superior - Doctorado',
    6:'Frecuencia de Educación Superior', 7:'12º año de escolaridad - No Completado', 8:'11º año de escolaridad - No Completado',
    9:'7º año (Antiguo)', 10:'Otro - 11º año de escolaridad', 11:'10º año de escolaridad', 12:'Curso general de comercio', 
    13:'Educación Básica 3er Ciclo (9º/10º/11º año) o Equiv.', 14:'Curso técnico-profesional', 15:'7º año de escolaridad',
    16:'2º ciclo del curso general de secundaria', 17:'9º año de escolaridad - No Completado', 18:'8º año de escolaridad',
    19:'Desconocido', 20:'No sabe leer ni escribir', 21:'Puede leer sin tener 4º año de escolaridad', 22:'Educación básica 1er ciclo (4º/5º año) o equiv.',
    23:'Educación Básica 2º Ciclo (6º/7º/8º año) o Equiv.', 24:'Curso de especialización tecnológica', 25:'Educación superior - licenciatura (1er ciclo)',
    26:'Curso de estudios superiores especializados', 27:'Curso técnico superior profesional', 28:'Educación Superior - Máster (2º ciclo)',
    29:'Educación Superior - Doctorado (3er ciclo)',30:'Educación Superior - Doctorado (4to ciclo)',31:'Educación Superior - Doctorado (5to ciclo)',
    32:'Educación Superior - Doctorado (6to ciclo)',33:'Educación Superior - Doctorado (7mo ciclo)',34:'Educación Superior - Doctorado (8vo ciclo)'
}
mothers_occupation_options={
    1:'Estudiante', 2:'Representantes del Poder Legislativo y Órganos Ejecutivos, Directores y Gerentes Ejecutivos',
    3:'Especialistas en Actividades Intelectuales y Científicas', 4:'Técnicos y Profesiones de Nivel Intermedio',
    5:'Personal administrativo', 6:'Trabajadores de Servicios Personales, Seguridad y Vendedores',
    7:'Agricultores y Trabajadores Calificados en Agricultura, Pesca y Silvicultura',8:'Trabajadores Calificados de la Industria, Construcción y Artesanos',
    9:'Operadores de Instalaciones y Máquinas y Trabajadores de Ensamblaje',10:'Trabajadores No Calificados',
    11:'Profesiones de las Fuerzas Armadas', 12:'Otra Situación', 13:'(en blanco)', 14:'Profesionales de la salud',
    15:'Profesores', 16:'Especialistas en tecnologías de la información y comunicación (TIC)',
    17:'Técnicos y profesiones de nivel intermedio en ciencia e ingeniería', 18:'Técnicos y profesionales de nivel intermedio de salud',
    19:'Técnicos de nivel intermedio de servicios jurídicos, sociales, deportivos, culturales y similares',
    20:'Trabajadores de oficina, secretarios en general y operadores de procesamiento de datos',
    21:'Operadores de servicios de datos, contabilidad, estadística, financieros y registro',
    22:'Otro personal de apoyo administrativo', 23:'Trabajadores de servicios personales', 24:'Vendedores',
    25:'Trabajadores de cuidados personales y similares', 26:'Trabajadores calificados de la construcción y similares, excepto electricistas',
    27:'Trabajadores calificados en impresión, fabricación de instrumentos de precisión, joyeros, artesanos y similares',
    28:'Trabajadores en procesamiento de alimentos, madera, confección y otras industrias y artesanías', 29:'Trabajadores de limpieza',
    30:'Trabajadores no calificados en agricultura, producción animal, pesca y silvicultura',
    31:'Trabajadores no calificados en industria extractiva, construcción, manufactura y transporte',
    32:'Ayudantes de preparación de comidas'
}
fathers_occupation_options={
    1:'Estudiante', 2:'Representantes del Poder Legislativo y Órganos Ejecutivos, Directores y Gerentes Ejecutivos',
    3:'Especialistas en Actividades Intelectuales y Científicas', 4:'Técnicos y Profesiones de Nivel Intermedio',
    5:'Personal administrativo', 6:'Trabajadores de Servicios Personales, Seguridad y Vendedores',
    7:'Agricultores y Trabajadores Calificados en Agricultura, Pesca y Silvicultura',8:'Trabajadores Calificados de la Industria, Construcción y Artesanos',
    9:'Operadores de Instalaciones y Máquinas y Trabajadores de Ensamblaje',10:'Trabajadores No Calificados',
    11:'Profesiones de las Fuerzas Armadas', 12:'Otra Situación', 13:'(en blanco)', 14:'Profesionales de la salud',
    15:'Profesores', 16:'Especialistas en tecnologías de la información y comunicación (TIC)',
    17:'Técnicos y profesiones de nivel intermedio en ciencia e ingeniería', 18:'Técnicos y profesionales de nivel intermedio de salud',
    19:'Técnicos de nivel intermedio de servicios jurídicos, sociales, deportivos, culturales y similares',
    20:'Trabajadores de oficina, secretarios en general y operadores de procesamiento de datos',
    21:'Operadores de servicios de datos, contabilidad, estadística, financieros y registro',
    22:'Otro personal de apoyo administrativo', 23:'Trabajadores de servicios personales', 24:'Vendedores',
    25:'Trabajadores de cuidados personales y similares', 26:'Trabajadores calificados de la construcción y similares, excepto electricistas',
    27:'Trabajadores calificados en impresión, fabricación de instrumentos de precisión, joyeros, artesanos y similares',
    28:'Trabajadores en procesamiento de alimentos, madera, confección y otras industrias y artesanías', 29:'Trabajadores de limpieza',
    30:'Trabajadores no calificados en agricultura, producción animal, pesca y silvicultura',
    31:'Trabajadores no calificados en industria extractiva, construcción, manufactura y transporte',
    32:'Ayudantes de preparación de comidas', 33:'Chef', 34:'Ingeniero', 35:'Economista', 36:'Porfesor', 37:'Independiente',
    38:'Bartender', 39:'Guardabosques', 40:'Psicólogo', 42:'Escritor', 43:'Alfarero', 44:'DJ', 45:'Hotelero', 46:'Pintor'
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
previous_qualification= st.selectbox("Calificación Previa", options=list(qualification_options.keys()),
                                 format_func=lambda x: qualification_options[x])
nacionality =st.selectbox("Nacionalidad", options=list(nationality_options.keys()),
                                 format_func=lambda x: nationality_options[x])
mothers_qualification =st.selectbox("Calificación de la Madre", options=list(mothers_qualification_options.keys()),
                                 format_func=lambda x: mothers_qualification_options[x])
fathers_qualification =st.selectbox("Calificación del Padre", options=list(fathers_qualification_options.keys()),
                                 format_func=lambda x: fathers_qualification_options[x])
mothers_occupation = st.selectbox("Ocupación de la Madre", options=list(mothers_occupation_options.keys()),
                                 format_func=lambda x: mothers_occupation_options[x])
fathers_occupation = st.selectbox("Ocupación del Padre", options=list(fathers_occupation_options.keys()),
                                 format_func=lambda x: fathers_occupation_options[x])
displaced = st.radio("Desplazado", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
educational_special_needs = st.radio("Necesidades Especiales", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
debtor = st.radio("Deudor", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
tuition_fees_up_to_date = st.radio("Pagos al Día", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
gender = st.radio("Género", options=[1, 0], format_func=lambda x: "Masculino" if x == 1 else "Femenino")
scholarship_holder = st.radio("Becado", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
age_at_enrollment = st.number_input("Edad al Matricularse", min_value=17, max_value=70, step=1)
international = st.radio("Internacional", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
curricular_units_1st_sem_credited = st.number_input("Unidades Curriculares Acreditadas (1er Semestre)", min_value=0, max_value=20, step=1)
curricular_units_1st_sem_enrolled = st.number_input("Unidades Curriculares Matriculadas (1er Semestre)", min_value=0, max_value=26, step=1)
curricular_units_1st_sem_evaluations = st.number_input("Unidades Curriculares Evaluadas (1er Semestre)", min_value=0, max_value=45, step=1)
curricular_units_1st_sem_approved = st.number_input("Unidades Curriculares Aprobadas (1er Semestre)", min_value=0, max_value=26, step=1)
curricular_units_1st_sem_grade = st.number_input("Nota Media (1er Semestre)", min_value=0.0, max_value=18.88, step=0.1)
curricular_units_1st_sem_without_evaluations = st.number_input("Unidades Curriculares Sin Evaluar (1er Semestre)", min_value=0, max_value=12, step=1)
curricular_units_2nd_sem_credited = st.number_input("Unidades Curriculares Acreditadas (2do Semestre)", min_value=0, max_value=19, step=1)
curricular_units_2nd_sem_enrolled = st.number_input("Unidades Curriculares Matriculadas (2do Semestre)", min_value=0, max_value=23, step=1)
curricular_units_2nd_sem_evaluations = st.number_input("Unidades Curriculares Evaluadas (2do Semestre)", min_value=0, max_value=33, step=1)
curricular_units_2nd_sem_approved = st.number_input("Unidades Curriculares Aprobadas (2do Semestre)", min_value=0, max_value=20, step=1)
curricular_units_2nd_sem_grade = st.number_input("Nota Media (2do Semestre)", min_value=0.0, max_value=18.57, step=0.1)
curricular_units_2nd_sem_without_evaluations = st.number_input("Unidades Curriculares Sin Evaluar (2do Semestre)", min_value=0, max_value=12, step=1)
unemployment_rate = st.number_input("Tasa de Desempleo (%)", min_value=7.6, max_value=16.2, step=0.1)
inflation_rate = st.number_input("Tasa de Inflación (%)", min_value=-0.80, max_value=3.7, step=0.1)
gdp = st.number_input("PIB (%)", min_value=-4.06, max_value=3.51, step=0.1)

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
    'Curricular units 1st sem (credited)': [curricular_units_1st_sem_credited],
    'Curricular units 1st sem (enrolled)': [curricular_units_1st_sem_enrolled],
    'Curricular units 1st sem (evaluations)': [curricular_units_1st_sem_evaluations],
    'Curricular units 1st sem (approved)': [curricular_units_1st_sem_approved],
    'Curricular units 1st sem (grade)': [curricular_units_1st_sem_grade],
    'Curricular units 1st sem (without evaluations)': [curricular_units_1st_sem_without_evaluations],
    'Curricular units 2nd sem (credited)': [curricular_units_2nd_sem_credited],
    'Curricular units 2nd sem (enrolled)': [curricular_units_2nd_sem_enrolled],
    'Curricular units 2nd sem (evaluations)': [curricular_units_2nd_sem_evaluations],
    'Curricular units 2nd sem (approved)': [curricular_units_2nd_sem_approved],
    'Curricular units 2nd sem (grade)': [curricular_units_2nd_sem_grade],
    'Curricular units 2nd sem (without evaluations)': [curricular_units_2nd_sem_without_evaluations],
    'Unemployment rate': [unemployment_rate],
    'Inflation rate': [inflation_rate],
    'GDP': [gdp]
})


# Codificar las variables categóricas usando los codificadores
for col, le in label_encoders.items():
    if col in input_data.columns:
        input_data[col] = le.transform(input_data[col])

# Realizar la predicción
if st.button("Predecir"):
    prediction = model.predict(input_data)  # Predicción de la clase (0, 1, 2)
    prediction_prob = model.predict_proba(input_data)  # Probabilidades de cada clase

    # Mostrar la predicción categorizada
    st.write("Categoría Predicha: ", category_map[prediction[0]])

    # Mostrar las probabilidades de las clases
    st.write("Probabilidades de cada categoría:")
    for i, class_name in enumerate(category_map.values()):
        st.write(f"{class_name}: {prediction_prob[0][i]:.2f}")