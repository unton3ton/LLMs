# https://gpttutorpro.com/pytorch-for-nlp-text-summarization-with-bart-2/

'''
BART is a neural network model that can generate natural language text from 
structured or unstructured data. BART is based on the Transformer architecture, 
and uses a denoising autoencoder objective to pre-train on a large corpus of text. 
BART can be fine-tuned for various natural language generation tasks, such as text 
summarization, machine translation, text simplification, and data-to-text generation. 
BART achieves state-of-the-art results on several benchmarks, including CNN/Daily Mail, 
XSum, and Gigaword for text summarization, and SQuAD, CoQA, and QuAC for question answering. 
BART also shows strong performance on low-resource and abstractive settings, 
such as the RotoWire and E2E datasets.
'''

# Using pip
# pip install transformers
 
# Using conda
# conda install -c huggingface transformers

import torch
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)} is available.")
else:
    print("No GPU available. Training will run on CPU.")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

# Import the transformers library
from transformers import pipeline
 
# Load BART for text summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn", device='cuda')

# Define the text to summarize
text = """The US Centers for Disease Control and Prevention on Friday released a highly anticipated 
		  update to travel guidance for people who are fully vaccinated against Covid-19, eliminating 
		  some testing and quarantine recommendations. The CDC says that fully vaccinated people can 
		  travel at low risk to themselves. The agency said that as long as coronavirus precautions 
		  are taken, including mask wearing, fully vaccinated people can travel within the United 
		  States without getting tested for Covid-19 before or self-quarantining after. For international 
		  travel, fully vaccinated people don't need a Covid-19 test prior to travel -- unless it is 
		  required by the destination -- and do not need to self-quarantine after returning to the United 
		  States, unless required by state or local authorities. The CDC says they should still have a 
		  negative Covid-19 test before boarding a flight to the US, and a follow up test three to five 
		  days after their return. The CDC also notes the potential for virus variants around the world 
		  and urges caution when traveling internationally. The new guidance does not change the agency's 
		  existing guidance for people who are not fully vaccinated. People who are not fully vaccinated 
		  are still advised to avoid nonessential travel. If they do travel, the CDC says to get tested 
		  one to three days before the trip, and three to five days after. People who are not fully 
		  vaccinated are asked to self-quarantine for seven days after travel if they receive a negative 
		  test, and for 10 days if they do not get a test."""
 
# Generate a summary of the text
summary = summarizer(text)
 
# Print the summary
print("Summary:\n", summary[0]["summary_text"])

'''
Summary:
 The CDC says that fully vaccinated people can travel at low risk to themselves. 
 The new guidance does not change the agency's existing guidance for people who are 
 not fully vaccinated. The CDC also notes the potential for virus variants around 
 the world and urges caution when traveling internationally. If they do travel, 
 the CDC says to get tested one to three days before the trip, and three to five days after.
'''