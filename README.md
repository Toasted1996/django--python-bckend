Django Python Backend 🚀

¡Bienvenido al backend de nuestra aplicación, construido con Django y Python! Este repositorio aloja el corazón de la aplicación, una API RESTful robusta, escalable y fácil de mantener.

✨ Características
Django: Utiliza el framework web más popular de Python.

API RESTful: Sigue los principios de REST para una comunicación fluida.

Modular: La estructura del proyecto facilita la adición de nuevas funcionalidades.

Entorno Virtual: Incluye un requirements.txt para gestionar las dependencias de forma limpia.

🛠️ Configuración e Instalación
Sigue estos pasos para poner el proyecto en marcha en tu máquina local.

Clona este repositorio:

Bash

git clone https://github.com/Toasted1996/django--python-bckend.git
cd django--python-bckend
Crea y activa el entorno virtual:

Bash

# 🐧 macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 💻 Windows
python -m venv venv
venv\Scripts\activate
Instala las dependencias necesarias:

Bash

pip install -r requirements.txt
Ejecuta las migraciones de la base de datos:

Bash

python manage.py makemigrations
python manage.py migrate
¡Inicia el servidor!

Bash

python manage.py runserver
🎉 ¡Listo! Ahora puedes acceder a la API en http://127.0.0.1:8000.

📂 Estructura del Proyecto
core/ ⚙️: Archivos de configuración principal de Django.

apps/ 📦: Directorio para todas las aplicaciones de la API.

requirements.txt 📝: Lista de las dependencias.

manage.py 🤖: Script para gestionar el proyecto.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras un error o tienes una mejora, no dudes en crear un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. 📜

