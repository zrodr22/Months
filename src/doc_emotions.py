import docx
import nltk
import os
import re
import text2emotion as te
import matplotlib.pyplot as plt
import numpy as np
nltk.download('omw-1.4')

def get_paragraph_text(document_path):
    doc = docx.Document(document_path)
    all_paras = doc.paragraphs

    all_paras_text = [para.text for para in all_paras]
    return all_paras_text

def get_text(document_path):
    all_paras_text = get_paragraph_text(document_path)
    return ''.join(all_paras_text)

def get_current_docs(documents_path):
    entries = os.listdir(documents_path)
    valid_entries = []

    for entry in entries:
        if entry[0] is not '~' and entry[-4:] == 'docx':
            valid_entries.append(entry)

    return valid_entries

def get_entries(document_path, month):
    para_text = get_paragraph_text(document_path)
    entries = []

    for para in para_text:
        # print('para', para)
        if(re.search("%s (\d{1}|\d{2}), \d{4}"%month, para)):
            entries.append('')
        elif(re.search("%s"%month, para)):
            continue;
        else:
            try:
                entries[-1] = entries[-1] + para
            except:
                print('something is failing in', month)
                continue
        try: 
            entries[-1] = entries[-1].replace('Entry: ', '')
        except:
            print(month, 'Failed!!!!!')
    
    return entries

total_emotions = {'Happy': 0, 'Angry': 0, 'Surprise': 0, 'Sad': 0, 'Fear': 0}
documents_path = "\\Users\\zrodr\\OneDrive\\Months"
documents = get_current_docs(documents_path)

fear = []
happy = []
sad = []
surprise = []
angry = []

for doc in documents:
    month = doc.split('_')[0]
    year = doc.split('_')[1][0:4]
    document_path = f"{documents_path}\\{month}_{year}.docx"
    entries = get_entries(document_path, month)
    num_entries = len(entries)
    if(num_entries == 0):
        continue

    for entry in entries:
        # print(entry)
        emotions = te.get_emotion(entry)
        total_emotions = {i: total_emotions.get(i, 0) + emotions.get(i, 0)
            for i in set(total_emotions).union(emotions)}
        # print('emotions:', emotions, 'total_emotions', total_emotions)
        # print("----")

    total_emotions_values = np.array(list(total_emotions.values()))
    emotion_titles = np.array(list(total_emotions.keys()))
    sort = np.argsort(emotion_titles)
    emotion_titles = emotion_titles[sort]

    fig = plt.figure(figsize=(10,7))
    plt.pie(total_emotions_values[sort], labels=emotion_titles, autopct='%1.1f%%')
    plt.title(f'{month} {year}')
    plt.savefig(f'.\\plots\\{month}_{year}')
    print(f'{month}_{year}', 'completed!')

# plt.show()