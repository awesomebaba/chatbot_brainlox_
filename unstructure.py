from langchain.document_loaders import UnstructuredURLLoader

urls = ["https://brainlox.com/courses/category/technical"]

loader = UnstructuredURLLoader(urls=urls)
documents = loader.load()

print(documents[0].page_content)
