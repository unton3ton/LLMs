# https://python.langchain.com/docs/integrations/vectorstores/faiss/

# source FAUST/bin/activate


# pip install -qU langchain-community faiss-gpu
# pip install -qU langchain-ollama
# ollama run llama3.2



from langchain_ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(model="llama3.2")
embeddings = OllamaEmbeddings(model="lakomoor/vikhr-llama-3.2-1b-instruct:1b")

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

from glob import glob
from contextlib import ExitStack
import re

# file_paths = glob("SDAtextsEn/*.txt") #['file1.txt', 'file2.txt', 'file3.txt']
file_paths = glob("SDAtextsRu/*.txt") 

with ExitStack() as stack:
    files = [stack.enter_context(open(file_path, 'r')) for file_path in file_paths]
    contents = [file.read() for file in files]

# print(len(contents))

pattern = re.compile(r'\w+')
for content in contents:
    source = pattern.search(content).group()
    print(source)

documents = []

for content in contents:
    document = Document(
                        page_content=f"{content}",
                        metadata={"source": f"{pattern.search(content).group()}"},
                        )
    documents.append(document)

# print(len(documents))


uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, ids=uuids)

vector_store.delete(ids=[uuids[-1]])

# results = vector_store.similarity_search(
#     "SDA satellites will not deorbit",
#     k=2,
#     filter={"source": "Military"},
# )

results = vector_store.similarity_search(
                                        "контракты с компаниями",
                                        k=2,
                                        filter={"source": "Военные"},
)

for res in results:
    print(f"* {res.page_content} [{res.metadata}]")






# vector_store.save_local("faiss_index")

# new_vector_store = FAISS.load_local(
#     "faiss_index", embeddings, allow_dangerous_deserialization=True
# )

# docs = new_vector_store.similarity_search_with_score("LangChain", 
# 													  k=3, 
# 													  filter={"source": "news"})
# print(docs)