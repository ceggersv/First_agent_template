import requests

# Clase mínima para cumplir con la interfaz esperada por smolagents
class ChatMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content

class LocalApiModel:
    def __init__(self, data):
        self.api_url = data.get("api_url", "http://127.0.0.1:1234/v1/chat/completions")
        self.model = data.get("model", "qwen2.5-7b-instruct")
        self.temperature = data.get("temperature", 0.7)
        self.max_tokens = data.get("max_tokens", 1024)

    def run(self, messages, stop_sequences=None):
        # ✅ Filtra los mensajes con roles válidos
        allowed_roles = {"user", "assistant", "system", "tool"}
        filtered_messages = [msg for msg in messages if msg["role"] in allowed_roles]

        headers = {"Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": filtered_messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        if stop_sequences:
            payload["stop"] = stop_sequences

        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content']

        # Debug
        print("✅ Llamada al modelo local exitosa.")
        print("📨 Prompt recibido:", filtered_messages)
        print("📤 Respuesta generada:", reply)

        # ✅ Devuelve en el formato esperado por smolagents
        return ChatMessage(role="assistant", content=reply)

    def __call__(self, messages, **kwargs):
        return self.run(messages, **kwargs)


