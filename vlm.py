import torch
from transformers import AutoProcessor, AutoModel
from PIL import Image

class VLMConversationalBot:
    def __init__(self, model_name="unum-cloud/uform-gen2-qwen-500m"):
        """
        Initialize the bot by loading the model and processor.
        """
        self.model = AutoModel.from_pretrained(model_name, trust_remote_code=True)
        self.processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def preprocess_image(self, image_path):
        """
        Preprocess the image from the given image path.
        """
        image = Image.open(image_path)
        return image

    def generate_response(self, image, prompt):
        """
        Generate a response from the model using the image and prompt.
        """
        inputs = self.processor(images=image, text=prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs, do_sample=False,
            use_cache=True,
            max_new_tokens=256,
            eos_token_id=151645
        )
        response = self.processor.decode(outputs[0], skip_special_tokens=True)
        return response

    def converse(self, image_path, prompt):
        """
        Handle a conversation with the user by processing the image and prompt.
        """
        image = self.preprocess_image(image_path)
        response = self.generate_response(image, prompt)
        return response

