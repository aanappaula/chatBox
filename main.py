import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "MY_KEY_GROK"

client = Groq(api_key=os.environ["GROQ_API_KEY"])

historico = []

while True:
    user = input("Você: ")

    if user.lower() == "x":
        print("\nHistórico:")
        for h in historico:
            print(h)
        break

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user}
            ],
            model="llama-3.1-8b-instant"
        )

        resposta = response.choices[0].message.content

        historico.append(f"Você: {user}")
        historico.append(f"Bot: {resposta}")

        print("Bot:", resposta)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")