
# 🧠 Descripción General del Proyecto con SmolAgents, Gradio y LLM Local

Este proyecto implementa un **sistema de agentes inteligentes** usando la librería [🤖 SmolAgents](https://github.com/huggingface/smolagents), diseñada por Hugging Face para construir agentes multi-paso capaces de razonar, planificar y usar herramientas (`tools`) para resolver tareas complejas. En este caso, se combina con:

- **Un modelo de lenguaje local** expuesto como API (vía LLM Studio).
- **Una interfaz web** con Gradio para facilitar la interacción del usuario.
- **Herramientas personalizadas** (`web_search`, `visit_webpage`, `final_answer`) que el agente puede invocar como funciones.

---

## 🔄 Flujo General de Ejecución

1. **Inicio del Agente**: `app.py` lanza una interfaz web (`GradioUI`) que permite enviar preguntas o tareas al agente.
2. **Input del Usuario**: El usuario escribe una pregunta/tarea (ej: *"¿Quién fue Albert Einstein?"*).
3. **Razonamiento del Agente**: El agente analiza la tarea, aplica `prompt_templates` y genera un ciclo de:
   - `Thought:` razonamiento textual
   - `Code:` ejecución en Python
   - `Observation:` salida de ejecución
4. **Uso de Herramientas (Tools)**: El agente puede usar herramientas como:
   - `web_search`: búsqueda web vía DuckDuckGo
   - `visit_webpage`: convierte HTML a Markdown desde una URL
   - `final_answer`: marca el fin del razonamiento
5. **Llamada al LLM**: Se llama a `LocalApiModel`, que comunica con tu modelo local vía API REST.
6. **Ejecución del Código**: El modelo genera bloques de código Python que se ejecutan paso a paso.
7. **Finalización**: Cuando el agente usa `final_answer(...)`, termina la tarea y se muestra la respuesta.

---

## 🧩 Componentes Personalizados

| Componente            | Descripción |
|----------------------|-------------|
| `LocalApiModel.py`   | Clase que conecta con tu modelo local (vía HTTP) |
| `prompts.yaml`       | Lógica del razonamiento multi-paso del agente |
| `Gradio_UI.py`       | Interfaz web Gradio para interacción paso a paso |
| `tools/`             | Herramientas que el agente puede invocar como funciones |
| `agent.json`         | Define herramientas y modelo usados al cargar un agente preconfigurado |

---

## ✅ Ventajas de este Enfoque

- Puedes agregar nuevas herramientas fácilmente (`tools/*.py`).
- No dependes de APIs externas: el modelo se ejecuta localmente.
- Todo el razonamiento del agente es transparente y editable.
- Se puede ampliar para tareas más complejas (agentes jerárquicos, con memoria, etc.).

---

## 🧪 Recomendaciones Finales

- Asegúrate de que tus herramientas están decoradas o definidas correctamente (`@tool` o heredan de `Tool`).
- Verifica que `prompts.yaml` contenga todas las plantillas necesarias (especialmente `final_answer`).
- Usa el archivo `app.py` como punto de entrada centralizado para configurar modelo, herramientas y agente.

---

Documentación generada automáticamente para el proyecto de Carlos Eggers 🚀
