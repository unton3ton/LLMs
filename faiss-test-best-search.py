# https://python.langchain.com/docs/integrations/vectorstores/faiss/

# source FAUST/bin/activate


# pip install -qU langchain-community faiss-gpu
# pip install -qU langchain-ollama
# ollama run llama3.2



from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3.2")

import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

from uuid import uuid4

from langchain_core.documents import Document

document_1 = Document(
    page_content="I had chocalate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
)

document_3 = Document(
    page_content="Building an exciting new project with LangChain - come check it out!",
    metadata={"source": "tweet"},
)

document_4 = Document(
    page_content="Robbers broke into the city bank and stole $1 million in cash.",
    metadata={"source": "news"},
)

document_5 = Document(
    page_content="Wow! That was an amazing movie. I can't wait to see it again.",
    metadata={"source": "tweet"},
)

document_6 = Document(
    page_content="Is the new iPhone worth the price? Read this review to find out.",
    metadata={"source": "website"},
)

document_7 = Document(
    page_content="The top 10 soccer players in the world right now.",
    metadata={"source": "website"},
)

document_8 = Document(
    page_content="LangGraph is the best framework for building stateful, agentic applications!",
    metadata={"source": "tweet"},
)

document_9 = Document(
    page_content="The stock market is down 500 points today due to fears of a recession.",
    metadata={"source": "news"},
)

document_10 = Document(
    page_content="I have a bad feeling I am going to get deleted :(",
    metadata={"source": "tweet"},
)

documents = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]
uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, ids=uuids)

vector_store.delete(ids=[uuids[-1]])

results = vector_store.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
    filter={"source": "tweet"},
)

for res in results:
    print(f"* {res.page_content} [{res.metadata}]")


# results = vector_store.similarity_search_with_score(
#     "Will it be hot tomorrow?", k=1, filter={"source": "news"}
# )

# for res, score in results:
#     print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")


# retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1})
# print(retriever.invoke("Stealing from the bank is a crime", filter={"source": "news"}))



# vector_store.save_local("faiss_index")

# new_vector_store = FAISS.load_local(
#     "faiss_index", embeddings, allow_dangerous_deserialization=True
# )

# docs = new_vector_store.similarity_search_with_score("LangChain", 
# 													  k=3, 
# 													  filter={"source": "news"})
# print(docs)