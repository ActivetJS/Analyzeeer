#pip install --user -U numpy
#pip install --user -U nltk
#python -m pip install -U pip
#python -m pip install -U matplotlib
import string
import nltk
import re
nltk.download('stopwords')
nltk.download('punkt')
f = open('Analiziryemoe.txt', "r", encoding="utf-8")
text = f.read()
print(type(text))
print(len(text))
text[:300]
text = text.lower()
string.punctuation
type(string.punctuation)
spec_chars = string.punctuation + '\n\xa0«»\t—…'
text = re.sub('\n', '', text)
def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])
text = remove_chars_from_text(text, spec_chars)
text = remove_chars_from_text(text, string.digits)
from nltk import word_tokenize
text_tokens = word_tokenize(text)
print(len(text_tokens))
text_tokens[:10]
text = nltk.Text(text_tokens)
print(type(text))
from nltk.probability import FreqDist
fdist = FreqDist(text)
print(fdist)
fdist.most_common(5)
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(['это', 'нею', '„'])
print(len(russian_stopwords))
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
print(len(text_tokens))
text = nltk.Text(text_tokens)
fdist_sw = FreqDist(text)
fdist_sw.most_common(10)
print(fdist_sw.most_common(10))
fdist.plot(30,cumulative=False)
fdist_sw.plot(30,cumulative=False)
str1 = ''.join(str(x) for x in fdist_sw.most_common(len(text)))
fi = open('analiz.txt', 'w', encoding='utf-8')
fi.write(str1)
fi.close()