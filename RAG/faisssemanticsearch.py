# pip install faiss-gpu transformers torch pandas
# pip install --upgrade numpy==1.26

# https://deepnote.com/blog/semantic-search-using-faiss-and-mpnet

"""
    The following code has been inspired from 
    https://huggingface.co/sentence-transformers/all-mpnet-base-v2
    as an example to explain the concept of semantic search using ANN
"""

from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
import faiss
import numpy as np
import pandas as pd
import time

class SemanticEmbedding:

    def __init__(self, model_name='sentence-transformers/all-mpnet-base-v2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
    
    #Mean Pooling - Take attention mask into account for correct averaging
    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0] #First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def get_embedding(self, sentences):
        # Tokenize sentences
        encoded_input = self.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        # Perform pooling
        sentence_embeddings = self.mean_pooling(model_output, encoded_input['attention_mask'])

        # Normalize embeddings
        sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
        return sentence_embeddings.detach().numpy()

model = SemanticEmbedding()

# let's test the model by embedding a test phrase: "I love playing football." 
# Note that the output is a 768-dimensional dense vector.
a = model.get_embedding("I love playing football")
# print(a.shape) # (1, 768) -- размер определяется используемой LLM


class FaissIdx:

    def __init__(self, model, dim=768):
        self.index = faiss.IndexFlatIP(dim)
        # Maintaining the document data
        self.doc_map = dict()
        self.model = model
        self.ctr = 0

    def add_doc(self, document_text):
        self.index.add(self.model.get_embedding(document_text))
        self.doc_map[self.ctr] = document_text # store the original document text
        self.ctr += 1

    def search_doc(self, query, k=3):
        D, I = self.index.search(self.model.get_embedding(query), k)
        return [{self.doc_map[idx]: score} for idx, score in zip(I[0], D[0]) if idx in self.doc_map]

# Testing the index
# Note that "laptop computer" has a high similarity while "doctor's office" has a low similarity, 
# which makes sense. Remember that cosine similarity ranges from -1 to 1, with 1 meaning exactly similar.

index = FaissIdx(model)
index.add_doc("laptop computers")
index.add_doc("doctor's office")
# print(index.search_doc("PC computer")) # [{'laptop computers': 0.72760177}, {"doctor's office": 0.2555444}]


# data = pd.read_csv("SICK_train.txt", sep='\t')
# print(data.head())

'''
   pair_ID                                         sentence_A                                         sentence_B  relatedness_score entailment_judgment
0        1  A group of kids is playing in a yard and an ol...  A group of boys in a yard is playing and a man...                4.5             NEUTRAL
1        2  A group of children is playing in the house an...  A group of kids is playing in a yard and an ol...                3.2             NEUTRAL
2        3  The young boys are playing outdoors and the ma...  The kids are playing outdoors near a man with ...                4.7          ENTAILMENT
3        5  The kids are playing outdoors near a man with ...  A group of kids is playing in a yard and an ol...                3.4             NEUTRAL
4        9  The young boys are playing outdoors and the ma...  A group of kids is playing in a yard and an ol...                3.7             NEUTRAL
'''

# print(data.info())
# data.drop_duplicates(subset="sentence_A", inplace=True)
# print('lenght of data: ', len(data))

# start_time = time.time()
# for idx, row in data.iterrows(): 		 
#     index.add_doc(row['sentence_A']) 
# print('Elapsed time: ', time.time() - start_time) # Elapsed time:  47.1509644985199

# print(data.tail(5))
# '''
# Elapsed time:  47.1509644985199
#       pair_ID                                         sentence_A  ... relatedness_score  entailment_judgment
# 4487     9974  A man is typing on a machine used for stenography  ...               1.0              NEUTRAL
# 4490     9981  The violin is being played by a little girl on...  ...               1.0              NEUTRAL
# 4494     9985  A group of people in a large Asian restaurant ...  ...               1.0              NEUTRAL
# 4498     9999        A man in blue has a yellow ball in the mitt  ...               1.2              NEUTRAL
# 4499    10000               Three dogs are resting on a sidewalk  ...               1.0              NEUTRAL
# '''

# start_time = time.time()
# print(index.search_doc("yellow train is going by"))
# print('Elapsed time: ', time.time() - start_time)

# # [5 rows x 5 columns]
# # [{'A yellow dog is stopping on white snow on a sunny day': 0.4479815}, 
# # {'A yellow dog is running on white snow on a sunny day': 0.38209322}, 
# # {'A schoolgirl with a black bag is on a crowded train': 0.38048455}]
# # Elapsed time:  0.015243291854858398

# start_time = time.time()
# print(index.search_doc("sprinting with football"))
# print('Elapsed time: ', time.time() - start_time)

# # [{'A player is running with the ball': 0.59186924}, 
# # {'A group of people playing football is running in the field': 0.58443254}, 
# # {'A group of football players is running in the field': 0.5543271}]
# # Elapsed time:  0.014629364013671875


data = pd.read_csv("sda2enall50texts.txt", sep='\t')
print(data.head())

#                                             Military
# 0  Kratos to develop ground system for U.S. missi...
# 1  The Space Development Agency awarded Kratos a ...
# 2                                       Sandra Erwin
# 3                                  November 13, 2024
# 4  WASHINGTON — The technology company Kratos Def...

print(data.info())
print('lenght of data: ', len(data)) # lenght of data:  874

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 874 entries, 0 to 873
# Data columns (total 1 columns):
#  #   Column    Non-Null Count  Dtype 
# ---  ------    --------------  ----- 
#  0   Military  874 non-null    object
# dtypes: object(1)
# memory usage: 7.0+ KB
# None

start_time = time.time()
for idx, row in data.iterrows(): 		 
    index.add_doc(row['Military']) 
print('Elapsed time: ', time.time() - start_time, '\n\n') # Elapsed time:  18.524787425994873

start_time = time.time()
print(index.search_doc("tHe super cosmic techNology coNpany"))
print('\nElapsed time: ', time.time() - start_time)

# [{'This article first appeared in the June 2024 issue of SpaceNews Magazine.': 0.5412435}, 
# {'“We can move smartly to a more defensible architecture that is not dependent on individual exquisite systems,” 
# Calvelli added. “We’re showing we have the ability to go fast by tapping into the commercial space industry.”': 0.49886668}, 

# {'The Space Force needs to take “available technologies off the shelf and use them,” said Calvellli. “When we create our own technology, 
# we end up down this path of cost-plus contracts because it’s too high of a risk, and we end up down these paths of seven to 10-year 
# development cycles.”': 0.46693242}]

# Elapsed time:  0.01458287239074707

start_time = time.time()
print(index.search_doc("Kratos company"))
print('\nElapsed time: ', time.time() - start_time)

# [{'WASHINGTON — The technology company Kratos Defense & Security Solutions has secured a $116.7 million contract from 
# the U.S. Space Development Agency (SDA) to develop a ground system that supports missile-defense operations with data 
# from low Earth orbit (LEO) satellites. ': 0.61057025}, 
# {'The Space Development Agency awarded Kratos a $116.7 million 
# contract to build ground system for missile defense operations': 0.54347795}, 
# {'San Diego-based Kratos will build the ground infrastructure to facilitate the coordination of real-time data across 
# a constellation of missile-tracking satellites. The ground system will operate from Redstone Arsenal in Alabama, 
# a U.S. Army installation where SDA is standing up one of its main satellite control centers. ': 0.52393585}]

# Elapsed time:  0.014149188995361328