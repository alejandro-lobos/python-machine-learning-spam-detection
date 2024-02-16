from html.parser import HTMLParser
import email
import re
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.tokenize import word_tokenize 
from nltk import PorterStemmer
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score
# nltk.download('punkt')
# nltk.download('stopwords')

class HTMLStripper(HTMLParser):
    
    def __init__(self):
        # Inicializamos la clase padre
        super().__init__()
        # Atributos que almacena los datos
        self.data = []
    
    def handle_data(self, data):
       self.data.append(data)


class EmailParser:

    def parse(self,correo):
        # Obtenemos el cuerpo del correo electronico
        pcorreo =" ".join(self.get_body(correo))
        # eliminamos los tags html
        pcorreo = self.strip_tags(pcorreo)
        # Eliminamos url
        pcorreo = self.remove_urls(pcorreo)
        # Transformamos el texto en tokens
        pcorreo = word_tokenize(pcorreo)
        # Eliminamos stopwords
        # Eliminamos puntuacion
        # Hacemos stemming
        pcorreo = self.clean_text(pcorreo)
        return " ".join(pcorreo)
        
    def get_body(self,correo):
        #Definicion una funcion interna que procese el cuerpo
        pcorreo = email.message_from_string(correo)
        return self._parse_body(pcorreo.get_payload())
    
    def _parse_body(self,payload):
        body = []
        if type(payload) is str:
            return [payload]
        elif type(payload) is list:
            for p in payload:
                body += self._parse_body(p.get_payload())
        return body
    
    def strip_tags(self,correo):
        html_stripper = HTMLStripper()
        html_stripper.feed(correo)
        return ''.join(html_stripper.data)

    def remove_urls(self, correo):
        return re.sub(r"http/S+","",correo)
    
    def clean_text(self,correo):
        pcorreo = []
        st = PorterStemmer()
        punct = list(punctuation) + ["\n", "\t"]
        for word in correo:
            if word not in stopwords.words("english") and word not in punct:
                pcorreo.append(st.stem(word))
        return pcorreo



def leer_correos(indice, num):
    with open(indice,'r') as f:
        labels =f.read().splitlines()
    # leemos los correos de disco
    x=[]
    y=[]
    for l in labels[:num]:
        label, email_path = l.split(' ../')
        y.append(label)
        with open(email_path, errors='ignore') as f:
            x.append(f.read())
    return x,y


def crear_dataset(indice, num):
    email_parser = EmailParser()
    X,y = leer_correos(indice, num)
    X_proc =[]
    for i, email in zip(range(len(X)),X):
        print("\rParsing email:{0}".format(i+1),end='')
        X_proc.append(email_parser.parse(email))
    return X_proc, y


X, y =  crear_dataset('full/index',500)

X_train, y_train = X[:250], y[:250]
X_test, y_test = X[250:], y[250:]

vectorizer = CountVectorizer()
vectorizer.fit(X_train)
X_train = vectorizer.transform(X_train)
X_train.toarray()

clf = LogisticRegression()
clf.fit(X_train, y_train)

X_test = vectorizer.transform(X_test)


y_pred = clf.predict(X_test)

print("\nPrediccion:\n", y_pred)
print("\Etiquetas reales:\n", y_test)


print("Accuracy: {:.3f}".format(accuracy_score(y_test,y_pred)))