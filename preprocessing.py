from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce
from nltk.stem import WordNetLemmatizer
import re



stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()


class Preprocess:
    def lowercasing(self, text):
        return text.lower()
    
    def removing_stopword(self, text):
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        return ''.join(filtered_words)
    
    def stemming(self, text):
        '''
        reducing inflection in words to their root form.
        '''
        words = word_tokenize(text)
        
        return reduce(lambda x,y: x+" " +ps.stem(y), words,"")
    
    def lemmatizing(self, text):
        '''(maybe) better way than stemming in removing inflection'''
        return lemmatizer.lemmatize(text)
    
    def removing_special_character(self,text):
        return re.sub('\W+','', text)
