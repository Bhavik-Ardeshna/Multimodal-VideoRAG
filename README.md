# Multimodal-VideoRAG: Using BridgeTower Embeddings and Large Vision Language Models

**Multimodal-VideoRAG** is  framework designed to facilitate multimodal information retrieval and question answering on videos by leveraging Video Retrieval-Augmented Generation (VideoRAG). It combines the power of Large Vision-Language Models (VLMs) and BridgeTower embeddings to perform video pre-processing, embedding generation, and multimodal vector database queries.

## Features

- **VideoRAG**: Employs retrieval-augmented generation techniques for video understanding, enhancing the quality of multimodal responses.
- **BridgeTower Integration**: Leverages BridgeTower embeddings to fuse image and text information seamlessly.
- **Multimodal Vector Database**: Efficient multimodal data storage and querying, enabling robust retrieval of video-based information.
- **Flexible Video Preprocessing**: Supports a variety of video preprocessing tasks to convert raw video data into meaningful representations for downstream tasks.

## Prerequisites

To set up **Multimodal-VideoRAG**, you will need:

- **Python 3.8+**
- **PyTorch 1.10+**
- **Transformers Library** (by Hugging Face)
- **BridgeTower Model**
- **LanceDB** for vector search
- **Cv2** for video preprocessing

### Installing Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/Bhavik-Ardeshna/Multimodal-VideoRAG.git
   cd Multimodal-VideoRAG
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Install **LanceDB** for efficient similarity search:

   ```bash
   pip install lancedb
   ```

4. Install **HuggingFace** for video preprocessing:

   ```bash
   pip install transformers
   ```

## Get Started

- **BridgeTowerEmbeddings**: Initializes the model to generate combined text-image embeddings.
- **LanceDB**: Establishes the vector store for video data storage and retrieval.
- **MultimodalLanceDB Retriever**: Retrieves relevant video segments based on similarity searches.
- **VLMConversationalBot**: Interacts with images from the video and generates descriptive responses to user prompts.

### Video Retrieval

```python
text = "astronauts mission"
retrieved_video_segments = retriever.invoke(text)
```

### Conversational Bot Response

```python
bot = VLMConversationalBot()
response = bot.converse(frame_path, "Describe what is happening in this image.")
print(f"Bot's Response: {response}")
```

