from dotenv import load_dotenv
import os
import google.generativeai as genai
import documentos

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_TOKEN"])

model = documentos.modelo_doc

history = documentos.history_inicial

print("Furia: Fala, furioso(a)! Tudo suave?! Pode mandar a pergunta que quiser sobre o nosso time!!!")

while True:

    user_input = input("Voce: ")

    while (user_input == ""):
        user_input = input("Voce: ")

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f"Furia: {model_response}")

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})