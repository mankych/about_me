import os
from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()

GIGACHAT_CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS")

async def ask_ai(prompt: str) -> str:
    with GigaChat(
        credentials=GIGACHAT_CREDENTIALS,
        verify_ssl_certs=False,
        model="GigaChat-2",
        scope="GIGACHAT_API_PERS"  # <-- Добавили scope
    ) as giga:
        response = giga.chat(prompt)
        return response.choices[0].message.content