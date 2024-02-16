# Clasificación de Correos Electrónicos con Análisis de Texto en Python
![Imagen del proyecto](https://github.com/alejandro-lobos/python-machine-learning-spam-detection/blob/6ea30109a81da02b611195d5dd685a5cf7586a1e/imagen-spam.png)

<!-- ## Ejemplo en vivo
- [URL-de-github-pages-de-este-proyecto](URL-de-github-pages-de-este-proyecto)
- [URL-de-la-api](URL-de-la-api) -->

## Descripción 📑

Este proyecto se centra en la clasificación de correos electrónicos utilizando técnicas de análisis de texto en Python. Se implementa un sistema que procesa el contenido de los correos electrónicos, eliminando etiquetas HTML, URLs y aplicando técnicas de procesamiento de texto como tokenización, eliminación de stopwords, puntuación y stemming. Posteriormente, se utiliza un modelo de Regresión Logística junto con un vectorizador CountVectorizer para entrenar y evaluar la clasificación de los correos electrónicos en categorías.

Durante la realización de este proyecto, he aprendido a trabajar con el análisis de texto en Python utilizando bibliotecas como nltk y scikit-learn. También he ganado experiencia en la manipulación de correos electrónicos, el procesamiento de datos no estructurados y la construcción de un modelo de clasificación para tareas de procesamiento de lenguaje natural (NLP). Este proyecto ha mejorado mis habilidades en la implementación de flujos de trabajo de preprocesamiento de texto y modelado de datos, y ha proporcionado conocimientos prácticos sobre cómo aplicar estas técnicas en problemas del mundo real, como la clasificación de correos electrónicos.

## Tecnologías 🛠
<!-- Iconos sacados de: https://github.com/hendrasob/badges/blob/master/README.md y https://github.com/alexandresanlim/Badges4-README.md-Profile -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Vista previa del proyecto
Si quieres hechas un vistazo al proyecto, te recomiendo:

![Captura del proyecto](https://github.com/alejandro-lobos/python-machine-learning-spam-detection/blob/6ea30109a81da02b611195d5dd685a5cf7586a1e/imagen-resultado-correos-procesados-y-entrenamiento.png)
![Captura del proyecto](https://github.com/alejandro-lobos/python-machine-learning-spam-detection/blob/6ea30109a81da02b611195d5dd685a5cf7586a1e/imagen-etiqueta-real-y-accuracy.png)

## Autor ✒️
Alejandro Lobos Arenas

* [LinkedIn](https://www.linkedin.com/in/alejandro-lobos-arenas/)
* [GitHub](https://github.com/alejandro-lobos)
* [Porfolio web](https://alejandrolobos.com/)

## Instalación 

1. Instalar python 3.11.5
2. Descargar el archivo
3. Descargar la base de datos de correos https://drive.google.com/file/d/12tOk621gfGYwQh6KkwbU108kwemFbLQt/view?usp=drive_link
4. Instalar desde terminal pip install scikit-learn pip install nltk
5. Desde la terminal python main.py
6. Se puede personalizar la cantidad de correos a utilizar, ya que el conjunto de datos contiene alrededor de 70,000 correos, lo que podría llevar mucho tiempo. Esta configuración se realiza en la sección del código que se presenta a continuación:
   - "X, y = crear_dataset('full/index', 500)" En esta línea, se especifica que se utilizarán 500 correos electrónicos para el análisis. Linea 101
   - "X_train, y_train = X[:250], y[:250]" Representan los 250 correos que se utilizarán para entrenar el algoritmo. Linea 103
   - "X_test, y_test = X[250:], y[250:]" Corresponden a los correos que el algoritmo clasificará de manera automática. Linea 104


