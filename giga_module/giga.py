from gigachat import GigaChat
from utils.settings import Settings
Settings.load_data_from_file()
# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
giga = GigaChat(credentials=Settings.get_gigachat_token(), verify_ssl_certs=False)


def get_answer(text: str) -> str:
    
    response = giga.chat(text)
    return response.choices[0].message.content