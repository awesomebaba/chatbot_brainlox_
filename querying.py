import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain.prompts import PromptTemplate

#Configuring API keys
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
hf_token = os.getenv('HF_TOKEN')
qdrant_api_key = os.getenv('QDRANT_API_KEY')
qdrant_url = os.getenv('QDRANT_URL')

#Instantiating the LLM
chat = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro-latest', google_api_key = google_api_key)

#Embedding Model 
embedding = HuggingFaceInferenceAPIEmbeddings(api_key= hf_token)

# Connect to Qdrant
qdrant_client = QdrantClient(
    url= qdrant_url,
    api_key= qdrant_api_key
)

# Initialize the LangChain Qdrant wrapper
vectorstore = Qdrant(
    client=qdrant_client,
    collection_name="langchat",
    embeddings= embedding
)

#Setting up the retriever
retriever = vectorstore.as_retriever()

template = '''
You are a salesman providing information about the courses. Using the provided context, answer the qeuries 
accordingly generate relevant code according to the given context to answer the questions

{context}:
{Question}:

Answer:

'''
prompt_template = PromptTemplate.from_template(template=template)

set_ret = RunnableParallel(
    {"context": retriever, "Question": RunnablePassthrough()} 
)
rag_chain = set_ret |  prompt_template | chat | StrOutputParser()

# response function
def generate_response(text):
    response = rag_chain.invoke(text)
    return response

