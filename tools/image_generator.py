from smolagents.tools import Tool
from typing import Any
import os
from PIL import Image, ImageDraw

class LocalImageGeneratorTool(Tool):
    name = "image_generator"
    description = "Generates a simple placeholder image with the given prompt as text."
    inputs = {'prompt': {'type': 'string', 'description': 'The image prompt to generate'}}
    output_type = "string"

    def __init__(self, output_dir="generated_images"):
        super().__init__()
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def forward(self, prompt: str) -> str:
        image = Image.new("RGB", (512, 512), color=(73, 109, 137))
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), prompt, fill=(255, 255, 0))
        filename = f"img_{abs(hash(prompt)) % 10**8}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        return filepath

