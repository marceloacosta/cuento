import os

import replicate
import streamlit as st
from dotenv import load_dotenv
from elevenlabs import generate
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
eleven_api_key = os.getenv("ELEVEN_API_KEY")

llm = OpenAI(temperature=0.9, max_tokens = 2048 )

def generate_recipe(tema, edad):
    prompt = PromptTemplate(
        input_variables=["tema", "edad"],
        template=""" 
         Eres un experto en contar historias, crea un cuento corto sobre el siguiente tema: {tema} adecuado para un niño o niña de {edad} años.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({
    'tema': tema,
    'edad': edad
    })


def generate_audio(text, voice):
    audio = generate(text=text, voice=voice, api_key=eleven_api_key)
    return audio


def generate_images(cuento):
    output = replicate.run(
        "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={"prompt": cuento}
    )
    return output

def app():
    st.title("Genera Cuentos")

    with st.form(key='my_form'):
        tema = st.text_input(label="De que quieres que se trate tu historia?", placeholder="De que quieres que se trate tu historia?")
        edad = st.number_input(label="Escribe para que edad es este cuento", min_value=1, max_value=99, value=5)

        options = ["Bella", "Antoni", "Arnold", "Adam", "Domi", "Elli", "Josh", "Rachel", "Sam"]
        voice = st.selectbox("Select a voice", options)

        submit_button = st.form_submit_button("Crear cuento")

    if submit_button:
        cuento = generate_recipe(tema, edad) 
        audio = generate_audio(cuento, voice)

        st.markdown(cuento)

        st.audio(audio, format='audio/mp3')

        images = generate_images(tema)
        st.image(images[0])


if __name__ == '__main__':
    app()