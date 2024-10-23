
# Custom Chatbot with Langchain, Flask RESTful API, Selenium, and Gemini LLM
## Project Overview
This project creates a custom chatbot that interacts with technical course data from **Brainlox**. The data extraction is handled using Selenium for scraping, followed by BeautifulSoup (bs4) for text formatting. Embeddings are generated using Huggingface models and stored in a Qdrant vector database. The chatbot itself is powered by the Gemini model LLM and is exposed through a Flask RESTful API.

## Features
-**Data Extraction** : Web scraping is performed using Selenium. BeautifulSoup (bs4) is used to format the scraped HTML content into clean text.

-**Embeddings Creation**: Text embeddings are generated using Huggingface embeddings.

-**Vector Store**: Embeddings are stored in a Qdrant database for efficient search and retrieval.

-**Conversation Handling**: The chatbot, powered by the Gemini LLM, is integrated into a Flask RESTful API to handle user conversations.
