# https://python.langchain.com/docs/integrations/vectorstores/faiss/

# source FAUST/bin/activate


# pip install -qU langchain-community faiss-gpu
# pip install -qU langchain-ollama ollama
# ollama run llama3.2



from langchain_ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(model="llama3.2")
embeddings = OllamaEmbeddings(model="lakomoor/vikhr-llama-3.2-1b-instruct:1b")

import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

# index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
index = faiss.IndexFlatL2(len(embeddings.embed_query("всем привет")))

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

import ollama

# file_paths = glob("SDAtextsEn/*.txt") #['file1.txt', 'file2.txt', 'file3.txt']
# file_paths = glob("SDAtextsRu/*.txt") 
file_paths = glob("gogol/*.txt") 

with ExitStack() as stack:
    files = [stack.enter_context(open(file_path, 'r')) for file_path in file_paths]
    contents = [' '.join(re.sub(r'\<[^>]*\>', '', file.read()).split()) for file in files]

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

print(len(documents))


uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, ids=uuids)

vector_store.delete(ids=[uuids[-1]])

# results = vector_store.similarity_search(
#     "SDA satellites will not deorbit",
#     k=2,
#     filter={"source": "Military"},
# )

results = vector_store.similarity_search(
                                        "раскаты грома в ночи",
                                        k=2,
                                        filter={"source": "РИМ"},
)

text_ru = ""

for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
    text_ru += res.page_content


prompt_ru = f"Напиши основную информацию из текста (данные, измерения, результаты, ключевые слова): {text_ru}"

res = ollama.chat(
                  model="lakomoor/vikhr-llama-3.2-1b-instruct:1b", # GPU
                  messages=[
                        {
                            'role': 'user',
                            # 'content': f'{prompt}', 
                            'content': f'{prompt_ru}',
                        }
                    ],

                options={
                    'temperature': 0.1, # значение от 0,0 до 0,9 (или 1) определяет уровень креативности модели или ее неожиданных ответов.
                    'top_p': 0.9, #  от 0,1 до 0,9 определяет, какой набор токенов выбрать, исходя из их совокупной вероятности.
                    'top_k': 90, # от 1 до 100 определяет, из скольких лексем (например, слов в предложении) модель должна выбрать, чтобы выдать ответ.
                    'num_ctx': 131000, # устанавливает максимальное используемое контекстное окно, которое является своего рода областью внимания модели.
                    # 'num_ctx': 8190, # saiga (max) ~ 6100 words
                    'num_predict': 1000, # задает максимальное количество генерируемых токенов в ответах для рассмотрения (100 tokens ~ 75 words).
                },
            )



print(res['message']['content'])


# vector_store.save_local("faiss_index")

# new_vector_store = FAISS.load_local(
#     "faiss_index", embeddings, allow_dangerous_deserialization=True
# )

# docs = new_vector_store.similarity_search_with_score("LangChain", 
# 													  k=3, 
# 													  filter={"source": "news"})
# print(docs)


'''
$ python faiss-the-best-search.py 
НЕВСКИЙПРОСПЕКТ
ПОРТРЕТ
HOC
РИМ
ШИНЕЛЬ
5
* РИМ Клянусь, этаких очей нельзя представить и вообразить, их тоже немощна передать кисть художника. 
Как угли, так они черны, [а. Это уголь б. Черные как угли] а из них льются молнии. [и сверкающие как молния] 
А чело, плечи. [Далее начато: только одно италианское на той [сто] половине] Это солнечное сияние, 
облившее белые стены каменных домов. А волосы, боже, какие волосы! Темная громовая ночь 
[Далее начато: а лоск на них] и всё в лоске. О нет, такой женщины не сыскать в Европе, об 
них только живут предания да бледные бесчувственные портреты их иногда являются в правильных 
созданиях художников. У, как смело, как ловко обхватило платье ее могучие [сильные] прекрасные члены, 
но лучше если бы оно не обхватило ее вовсе. Покровы прочь, и тогда бы увидели все, что это богиня. 
А попробуйте покровы прочь с немки или англичанки или француженки и выйдет чорт знает что: цыпленок. 
Вот, повернулась картинная голова, коса кольцом, сверкнул затылок и тонкая снежная шея. Еще 
[Еще далее] движение и уже видна благородная прямая линия носа, тонкой конец брови и три длинные 
[три черные] иглы ресниц. А что же далее… но нет, не гляди [не гляди, не поворачивайся], 
не подноси своих молний. Читай у [Не дописано.] [{'source': 'РИМ'}]


### Основные Сведения о РИМ Клянусь

1. **Описание персонажа**: Рим Клянусь - это не просто имя или фамилия, но и образец в мире литературы.
2. **Символика**: Углы могут символизироватьStrength (силу) и Weakness (победу), что может быть интерпретировано как описание личности или характера персонажа.
3. **Ключевые слова**:
   - Рим Клянусь
   - Углы
   - Сила
   - Победа

### Исследование Истории и Мифологии

1. **История**: В тексте упоминается "солнечное сияние", что может быть связано с практикой солнечного света в древних культурах.
2. **Мифология**: Углы, как символизирующиеStrength и Weakness, могут иметь исторические корни в различных культурных традициях.

### Анализ Контекста

1. **Контекст**: Текст содержит элементы фантастики и мифологии, что может указывать наpresence в истории или литературе какого-то конкретного персонажа.
2. **Связь с реальностью**: В тексте говорится о "пробуить покровы прочь", что может быть интерпретировано как попытка найти путь к новому началу, но в контексте истории или литературного произведения это необычный и потенциально опасный шаг.

### Выводы

- Рим Клянусь - это персонаж с уникальной историей и мифологией.
- Углы могут быть символом силы и слабости в различных культурах.
- Текст может содержать элементы фантастики или литературного произведения, что требует дополнительных исследований для полноценного анализа.

Если у вас есть конкретные вопросы о тексте или вам нужен анализ на другой уровень, пожалуйста, уточните ваш запрос.
'''