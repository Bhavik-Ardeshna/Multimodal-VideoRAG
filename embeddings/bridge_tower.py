from PIL import Image
import torch
from tqdm import tqdm
from typing import List
from langchain_core.embeddings import Embeddings
from langchain_core.pydantic_v1 import (
    BaseModel,
)
from transformers import BridgeTowerProcessor, BridgeTowerForContrastiveLearning

class BridgeTowerEmbeddings(BaseModel, Embeddings):
    """ BridgeTower embedding model """
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents using BridgeTower.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        embeddings = []
        for text in texts:
            embedding = get_bridgetower_combined_embeddings(text=text, image_path="").tolist()[0]
            embeddings.append(embedding)
        return embeddings

    def embed_query(self, text: str) -> List[float]:
        """Embed a query using BridgeTower.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        return self.embed_documents([text])[0]

    def embed_image_text_pairs(self, texts: List[str], images: List[str], batch_size=2) -> List[List[float]]:
        """Embed a list of image-text pairs using BridgeTower.

        Args:
            texts: The list of texts to embed.
            images: The list of path-to-images to embed
            batch_size: the batch size to process, default to 2
        Returns:
            List of embeddings, one for each image-text pairs.
        """

        # the length of texts must be equal to the length of images
        assert len(texts)==len(images), "the len of captions should be equal to the len of images"  
        
        embeddings = []
        for path_to_img, text in tqdm(zip(images, texts), total=len(texts)):
            embedding = get_bridgetower_combined_embeddings(text=text, image_path=path_to_img)
            embeddings.append(embedding)
        return embeddings


def get_bridgetower_combined_embeddings(image_path, text):
    # Load pre-trained model and processor
    processor = BridgeTowerProcessor.from_pretrained("BridgeTower/bridgetower-large-itm-mlm-itc")
    model = BridgeTowerForContrastiveLearning.from_pretrained("BridgeTower/bridgetower-large-itm-mlm-itc")

    
    if image_path != "":
        # Load and process the image
        image = Image.open(image_path)
        # Process the inputs (image and text)
        
        encoding = processor(image, text, return_tensors="pt")
    
        
        # Get the embeddings from the model
        with torch.no_grad():
            outputs = model(**encoding)
        
        return outputs
    
    else:
        image = Image.open("/Users/bhavikardeshna/PlayGround/LLM/VidRag/data/videos/video1/extracted_frame/frame_0.jpg")
        encoding = processor(image, text, return_tensors="pt")
    
        
        # Get the embeddings from the model
        with torch.no_grad():
            outputs = model(**encoding)
        
        return outputs.text_embeds

