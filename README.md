# Generador de Cuentos

Este proyecto es una aplicación de Streamlit que genera cuentos basándose en un tema y edad especificados por el usuario. La aplicación también produce un audio que lee el cuento generado y muestra una imagen que se relaciona con el tema.

## Requisitos

Para usar este proyecto, necesitarás:

- Python 3.7 o superior
- Un API Key de OpenAI
- Un API Key de Elevenlabs

## Instalación

Primero, clona este repositorio en tu máquina local usando:

<pre>
git clone https://github.com/tu_usuario/tu_proyecto.git
</pre>
Instala las dependencias necesarias:

<pre>
pip install -r requirements.txt
</pre>
## Configuración
Crea un archivo .env en la carpeta raíz del proyecto con las siguientes variables:

<pre>
OPENAI_API_KEY=<tu_api_key_de_openai>
ELEVEN_API_KEY=<tu_api_key_de_elevenlabs>
REPLICATE_API_TOKEN=<tu_token_de_replicate>
</pre>
Reemplaza con tus respectivas claves de API.

## Uso
Para correr el proyecto:

<pre>
python main.py
</pre>
Luego, visita http://localhost:8501 en tu navegador para interactuar con la aplicación.

## Contribuir
Si te gustaría contribuir a este proyecto, por favor crea un fork del repositorio, realiza tus cambios, y envía un pull request.