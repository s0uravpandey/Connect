text="Cricket is a sport that requires the use of a bat and ball. It is easily one of the most prevalent sports in the world. This game consists of two teams that include 11 players each. The main aim of the game is to score the highest number of runs. It is played on a pitch in a field that is well-maintained for the same purpose. Cricket is particularly famous in England and India. There is a lot of potential in Cricket which allows players to earn well. Cricket does not have one single format but various ones. Similarly, each format has a different set of rules and duration.As Cricket has various formats, it has a different fan base for each of them. Some people like watching test matches because of their intensity and authenticity. While some enjoy Twenty-20, that require minimum engagement and are highly entertaining. Test Match is a format of cricket that is quite traditional."
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
stopwords=list(STOP_WORDS)
nlp = spacy.load('en_core_web_md')
doc=nlp(text)
tokens=[token.text for token in doc]
punctuation=punctuation + '\n'
word_frequencies={}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text]=1
            else:
                word_frequencies[word.text]+=1
max_frequency=max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word]=word_frequencies[word]/max_frequency
sentence_tokens=[sent for sent in doc.sents]
sentence_scores={}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
from heapq import nlargest
select_length=int(len(sentence_tokens)*0.3)
summary=nlargest(select_length,sentence_scores,key=sentence_scores.get)
final_summary = [word.text for word in summary]
summary=' '.join(final_summary)


