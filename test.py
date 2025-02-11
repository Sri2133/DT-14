import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")


class TextToNum:
    def __init__(self, text):
        self.text = text
        self.cleaned = ""
        self.tkns = []
        self.cl = []
        self.st = []

    def cleaner(self):
        """Removes punctuation and extra spaces from the text."""
        text = re.sub(r',', '', self.text)
        cleaned_text = re.sub(r'[^\w\s]', '', text)  # Removes everything except word characters and spaces
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replaces multiple spaces with a single space
        self.cleaned = cleaned_text.strip()  # Removes leading/trailing whitespace

    def token(self):
        """Tokenizes the cleaned text into words."""
        if not self.cleaned:
            self.cleaner()
        self.tkns = word_tokenize(self.cleaned)

    def removeStop(self):
        """Removes stopwords from tokenized text."""
        if not self.tkns:
            self.token()
        stop = set(stopwords.words('english'))  # Using set for faster lookups
        self.cl = [word for word in self.tkns if word.lower() not in stop]  # Ensure case insensitivity

    def stemme(self):
        """Stems words using Porter Stemmer."""
        if not self.cl:
            self.removeStop()
        ps = PorterStemmer()
        self.st = [ps.stem(word) for word in self.cl]
        return self.st  # Return the stemmed words


# Example Usage:
if __name__ == "__main__":
    text = "Hello! This is an example sentence, demonstrating Text Processing."
    processor = TextToNum(text)

    processor.cleaner()
    processor.token()
    processor.removeStop()
    stemmed_words = processor.stemme()

    print("✅ Original Text:", text)
    print("✅ Cleaned Text:", processor.cleaned)
    print("✅ Tokens:", processor.tkns)
    print("✅ Without Stopwords:", processor.cl)
    print("✅ Stemmed Words:", stemmed_words)
