import os
from dotenv import load_dotenv
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Configuring API Keys
load_dotenv()
hf_token = os.getenv('HF_TOKEN')
qdrant_api_key = os.getenv('QDRANT_API_KEY')
qdrant_url = os.getenv("QDRANT_URL")

file_path = 'formatted_data.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

docs = [Document(page_content=data)]

# splitting the data
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(docs)

# Embedding Model
embedding = HuggingFaceInferenceAPIEmbeddings(api_key=hf_token)

# Indexing the documents in vectorDB (Qdrant)
qdrant = Qdrant.from_documents(
    texts,  # Use the split texts for vectorizing
    embedding,
    url=qdrant_url,
    prefer_grpc=True,
    api_key=qdrant_api_key,
    collection_name="langchat",
)

print("Indexing done!")
