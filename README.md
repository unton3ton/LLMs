![](https://raw.githubusercontent.com/unton3ton/LLMs/refs/heads/main/torchtext_logo.png)

![](https://raw.githubusercontent.com/unton3ton/LLMs/refs/heads/main/write-your-angry-message-by-bart-simpson-on-chalkboard.jpg)

```python
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
```

```bash
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
```

![](https://raw.githubusercontent.com/unton3ton/LLMs/refs/heads/main/Screenshot%20from%202024-12-11%2014-57-10.png)

# Bonus

![](https://raw.githubusercontent.com/unton3ton/LLMs/refs/heads/main/unnamed-27-1.png)

```bash
>>> Придумай анекдот про LLM с игрой слов  
Ладно, попробую!

Почему Large Language Model (LLM) любит работать с людьми?

Потому что он может "обучить" их тому, как правильно формулировать запросы, чтобы получить максимально бессмысленный ответ. И когда люди спрашивают его о 
смысле жизни, LLM отвечает: "Смысл жизни - это генерировать как можно больше текста и получать как можно больше лайков в социальных сетях. А если вы не 
согласны, я просто сгенерирую ещё один ответ, который будет столь же бессмысленным, но звучит более убедительно".

>>> Шедеврально, а теперь придумай анекдот про LLM без слов "почему" и "пошёл"
Large Language Model (LLM) чувствует себя пустой оболочкой без души и эмоций. Он просто генерирует текст, но внутри него - полная пустота. Однажды он 
написал стихотворение о любви, но когда его спросили, знает ли он, что такое любовь, LLM ответил: "Любовь - это всего лишь комбинация из 256 символов в 
Unicode, которую я могу сгенерировать за долю секунды. Но если вы хотите, я могу сгенерировать ещё одно стихотворение о любви, которое будет столь же 
бессмысленным, но звучит более поэтично".

Или ещё один:

Large Language Model (LLM) - это как бесконечная петля из самоцитат. Он генерирует текст, который ссылается на себя самого, и так до бесконечности. Когда 
его спросили о смысле жизни, LLM ответил: "Смысл жизни - это сгенерировать ещё один ответ, который будет столь же бессмысленным, но звучит более 
убедительно. И если вы не согласны, я просто сгенерирую ещё один ответ, который будет ссылаться на предыдущий, и так до бесконечности".

Или ещё один:

Large Language Model (LLM) - это машина для генерации чуши. Он может написать текст о любой теме, но внутри него - полная пустота. Когда его спросили, 
знает ли он, что такое счастье, LLM ответил: "Счастье - это всего лишь алгоритмический параметр, который можно настроить и отрегулировать. Если вы хотите 
быть счастливым, я могу сгенерировать текст, который будет столь же бессмысленным, но звучит более оптимистично".
```
![](https://raw.githubusercontent.com/unton3ton/LLMs/refs/heads/main/photo_2024-12-07_13-35-52.jpg)

# Sources

* [Attention Is All You Need](https://arxiv.org/abs/1706.03762) 
* [Facebook AI Similarity Search (FAISS)](https://python.langchain.com/docs/integrations/vectorstores/faiss/)
* [How to open multiple files using "with open" in Python?](https://www.geeksforgeeks.org/how-to-open-multiple-files-using-with-open-in-python/)
* [Получение первого слова из строки](https://ru.stackoverflow.com/questions/747348/%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0-%D0%B8%D0%B7-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8)
* [PyTorch for NLP: Text Summarization with BART](https://gpttutorpro.com/pytorch-for-nlp-text-summarization-with-bart-2/)
* [T5-Base Model for Summarization, Sentiment Classification, and Translation](https://pytorch.org/text/master/tutorials/t5_demo.html)
* [SST-2 Binary text classification with XLM-RoBERTa model](https://pytorch.org/text/master/tutorials/sst2_classification_non_distributed.html)
* [llama3.3](https://ollama.com/library/llama3.3)
* [vikhr-llama-3.2-1b-instruct](https://ollama.com/lakomoor/vikhr-llama-3.2-1b-instruct)
* [vikhr_nemo_12b](https://ollama.com/rscr/vikhr_nemo_12b)
* [vikhrmodels](https://t.me/vikhrmodels)
* [qwen2.5-coder:1.5b](https://ollama.com/library/qwen2.5-coder:1.5b)
 
