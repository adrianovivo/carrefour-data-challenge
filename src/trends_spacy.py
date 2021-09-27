#Módulo para cálculo de similaridade entre grupos de 5 trends topics utilizando o SPACY

from src.services import get_trends_from_mongo, save_similar_mongo

import spacy

trends = get_trends_from_mongo()

top1_5_trends = []
top6_10_trends = []
top11_15_trends = []
top16_20_trends = []

for trend in trends[1:5]: #começa do zero para ignorar primeiro trend
    top1_5_trends.append(trend["name"])

for trend in trends[6:10]:
    top6_10_trends.append(trend["name"])

for trend in trends[11:15]:
    top11_15_trends.append(trend["name"])

for trend in trends[16:20]:
    top16_20_trends.append(trend["name"])

text1 = ' '.join(top1_5_trends)
text2 = ' '.join(top6_10_trends)
text3 = ' '.join(top11_15_trends)
text4 = ' '.join(top16_20_trends)

nlp = spacy.load('pt_core_news_sm')

doc1 = nlp(text1)
doc2 = nlp(text2)
doc3 = nlp(text2)
doc4 = nlp(text2)

ana1 = doc1, "<->", doc2, doc1.similarity(doc2)

map1 = [{"analise": "1º a 5º x 6º a 10º", "similar": doc1.similarity(doc2)},
        {"analise": "1º a 5º x 11º a 15º", "similar": doc1.similarity(doc3)},
        {"analise": "1º a 5º x 16º a 20º", "similar": doc1.similarity(doc4)},
        {"analise": "6º a 10º x 11º a 16º", "similar": doc2.similarity(doc3)},
        {"analise": "6º a 10º x 16º a 20º", "similar": doc2.similarity(doc4)},
        {"analise": "11º a 16º x 16º a 20º", "similar": doc3.similarity(doc4)}]

save_similar_mongo(map1)
#print(map1)


