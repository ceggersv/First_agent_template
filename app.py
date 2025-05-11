from smolagents import CodeAgent
from tools.final_answer import FinalAnswerTool
from tools.web_search import DuckDuckGoSearchTool  # ✅ Aquí importamos la clase correcta
# from tools.visit_webpage import visit_webpage
from tools.visit_webpage import VisitWebpageTool
from Local_api_model import LocalApiModel
from Gradio_UI import GradioUI
# Imagenes
from tools.image_generator import LocalImageGeneratorTool

import yaml

# Cargar prompt templates desde prompts.yaml
with open("prompts.yaml", "r", encoding="utf-8") as f:
    prompt_templates = yaml.safe_load(f)

# Crear modelo local apuntando a tu LLM Studio
model = LocalApiModel({
    "api_url": "http://127.0.0.1:1234/v1/chat/completions",
    "model": "qwen2.5-7b-instruct",
    "temperature": 0.5,
    "max_tokens": 2048
})

# Crear instancia del agente con las herramientas necesarias
agent = CodeAgent(
    model=model,
    tools=[
        FinalAnswerTool(),
        DuckDuckGoSearchTool(),  # ✅ Correctamente registrado como 'web_search'
        VisitWebpageTool(),  # ✅ ¡Esta es la instancia correcta!
        LocalImageGeneratorTool()
    ],
    prompt_templates=prompt_templates,
    max_steps=6,
    verbosity_level=1,
)

# Lanzar la interfaz con Gradio
GradioUI(agent).launch()
