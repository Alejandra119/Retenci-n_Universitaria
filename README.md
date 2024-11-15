# Retencion_Universitaria
Este proyecto tiene como objetivo analizar los factores que influyen en la retención, deserción y graduación de los estudiantes universitarios. A través de un enfoque de ciencia de datos, se exploran variables académicas, socioeconómicas y personales para construir métricas clave y desarrollar modelos predictivos que ayuden a identificar patrones y tomar decisiones informadas.

## Objetivos del Proyecto
- Análisis de Retención: Evaluar los factores asociados con la permanencia y éxito académico de los estudiantes.
- Construcción de KPIs: Crear indicadores clave de rendimiento (KPIs) como la tasa de retención, tasa de salida y tasa de graduación.
- Modelo Predictivo: Implementar un modelo de clasificación utilizando Random Forest para predecir el estado del estudiante (deserción, graduación, o inscripción continua).
- Visualización de Resultados: Desarrollar visualizaciones para comprender mejor los patrones de retención y su relación con factores específicos.
## Descripción de los KPIs
- Tasa de Retención: Proporción de estudiantes que permanecen o completan su programa.
- Tasa de Salida: Proporción de estudiantes que abandonan el programa.
- Tasa de Graduación: Proporción de estudiantes que completan su programa con éxito.
## Análisis Exploratorio
Realizamos un análisis exploratorio inicial para entender la distribución de las variables, identificar posibles outliers y examinar la correlación entre factores académicos y el estado final de los estudiantes. Algunos de los hallazgos clave incluyen:

- Distribución de Target: La mayoría de los estudiantes se agrupan en las categorías de "Graduate" y "Enrolled", con una menor proporción en "Dropout".
- Importancia de las Características: Las variables relacionadas con el rendimiento académico, como "unidades aprobadas" y "calificaciones" por semestre, mostraron ser fuertes indicadores del estado de Target.
## Modelo Predictivo
Implementamos un modelo de Random Forest para predecir el estado del estudiante (Target). Los resultados muestran:
- Precisión del Modelo: Se alcanzó una precisión promedio de 98% en validación cruzada, con un AUC-ROC de 0.8743.
- Matriz de Confusión: La mayoría de las predicciones fueron correctas, aunque se observó una mayor confusión al clasificar a la clase "Graduate".
- Curva ROC: Las clases "Dropout" y "Enrolled" tuvieron un rendimiento alto, mientras que "Graduate" mostró una curva más baja, sugiriendo espacio para mejoras.
## Visualización en Dashboard
Se desarrollaron visualizaciones en Power BI para los siguientes KPIs:
- Tasa de Retención: Indicador clave del porcentaje de estudiantes que permanecen o completan.
- Tasa de Salida: Proporción de estudiantes que abandonan el programa.
- Tasa de Graduación: Métrica para entender el éxito en la finalización del programa.
## Gráficos Complementarios
Distribución de Target por Género y Estado Civil: Muestra la proporción de Dropout, Graduate y Enrolled en función del género y estado civil, revelando posibles patrones de riesgo o éxito.
Promedio de Unidades Aprobadas y Calificaciones por Estado de Target: Compara el rendimiento académico promedio entre los diferentes grupos de Target, ayudando a identificar si los estudiantes en "Dropout" tienen menor desempeño académico.
## Requerimientos
- Python 3.8+
- Bibliotecas: pandas, numpy, scikit-learn, matplotlib, seaborn, Power BI para visualizaciones
## Instrucciones
- Cargar los datos y realizar la limpieza inicial.
- Ejecutar el análisis exploratorio de datos para obtener una visión general de las variables.
- Crear KPIs en Power BI según las fórmulas proporcionadas en el análisis.
- Entrenar el modelo de Random Forest y evaluar los resultados.
- Visualizar los resultados en un dashboard de Power BI.
## Conclusión
Este análisis proporciona una comprensión integral de los factores que afectan la retención y el éxito académico de los estudiantes. Los KPIs y el modelo predictivo desarrollados permiten anticipar problemas y apoyar la toma de decisiones estratégicas en la universidad.

