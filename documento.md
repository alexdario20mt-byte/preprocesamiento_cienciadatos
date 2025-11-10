DOCUMENTACIÓN DEL PROYECTO: PREPROCESAMIENTO DE DATOS ONLINE RETAIL
1. Introducción
El presente proyecto tiene como objetivo aplicar de manera práctica el uso de Git y GitHub para la gestión de versiones y la colaboración en proyectos de Ciencia de Datos. Además, se implementa un flujo completo de preprocesamiento de datos utilizando Python y la biblioteca Pandas, aplicando técnicas de limpieza, transformación, normalización y eliminación de valores nulos en el dataset 'Online Retail'. Este proceso permite preparar los datos para un análisis posterior o para alimentar modelos de aprendizaje automático.
2. Objetivo del proyecto y funcionalidades implementadas
El objetivo del proyecto es diseñar y ejecutar un proceso automatizado de preprocesamiento de datos que cumpla con las buenas prácticas de ingeniería de datos. Las funcionalidades implementadas incluyen:
- Carga de datos desde archivos CSV.
- Limpieza y manejo de valores nulos y duplicados.
- Conversión de tipos de datos.
- Eliminación de valores atípicos.
- Normalización de variables numéricas.
- Documentación del flujo de trabajo y uso de control de versiones mediante Git y GitHub.
3. Comandos Git usados: Descripción y propósito
git clone → Clona el repositorio desde GitHub al equipo local.
git config --global user.name → Configura el nombre del usuario de Git.
git config --global user.email → Configura el correo electrónico del usuario de Git.
git checkout -b feature-preprocesamiento → Crea y cambia a una nueva rama de desarrollo.
git add → Añade los archivos modificados al área de preparación.
git commit -m 'mensaje' → Guarda los cambios realizados con un mensaje descriptivo.
git push origin feature-preprocesamiento → Sube la nueva rama y sus commits al repositorio remoto.
git merge feature-preprocesamiento → Fusiona los cambios de la rama secundaria con la rama principal.
git branch -d feature-preprocesamiento → Elimina la rama local después de la fusión.
git push origin --delete feature-preprocesamiento → Elimina la rama remota en GitHub.
4. Automatización con GitHub Actions
Se implementó un flujo de trabajo automatizado mediante GitHub Actions para verificar el código Python en cada cambio (push o pull request) dentro del repositorio. Este flujo asegura que el código se mantenga funcional y estandarizado. El archivo de configuración se encuentra en la ruta '.github/workflows/python-app.yml' y ejecuta los siguientes pasos:
1. Instalar dependencias del entorno de Python.
2. Ejecutar las pruebas unitarias.
3. Validar el código antes de integrarlo a la rama principal.
5. Capturas de pantalla
Capturas de pantalla



6. Enlaces finales
Enlace al archivo DOCUMENTACION.md en GitHub: [Agrega aquí el enlace al archivo subido en tu repositorio]
Enlace al repositorio GitHub: [https://github.com/alexdario20mt-byte/preprocesamiento_cienciadatos]
7. Bibliografía
• Chacon, S., & Straub, B. (2014). Pro Git. Apress.
• McKinney, W. (2018). Python for Data Analysis. O’Reilly Media.
