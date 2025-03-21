import requests

# Substitua pelo token do seu bot
BOT_TOKEN = "token"
# Substitua pelo ID do chat ou canal onde quer testar (pode ser seu próprio ID)
CHAT_ID = "ID"
# Mensagem que será enviada
TEST_MESSAGE = "Teste de resposta: Meu bot está funcionando?"

def send_message(token, chat_id, message):
    """Envia uma mensagem ao bot e retorna a resposta da API."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()

# Testa o envio da mensagem
response = send_message(BOT_TOKEN, CHAT_ID, TEST_MESSAGE)

if response.get("ok"):
    print("✅ O bot respondeu corretamente!")
    print("Resposta:", response)
else:
    print("❌ Erro ao tentar se comunicar com o bot.")
    print("Detalhes:", response)
