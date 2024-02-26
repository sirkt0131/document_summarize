from pypdf import PdfReader
from io import BytesIO
from urllib import request
import requests
# from bs4 import BeautifulSoup
from newspaper import Article, ArticleException

class Loader:
    def load_pdf(file_path):
        reader = PdfReader(file_path)
        texts = ""
        for page in reader.pages:
            texts += page.extract_text()
        return texts

    def load_pdf_url(document_url):
        bit_data = request.urlopen(document_url).read()
        data = BytesIO(bit_data)
        return Loader.load_pdf(data)
    
    def load_url(url):
        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # text = ' '.join([p.text for p in soup.find_all('p')])
        article = Article(url)
        article.download()
        article.parse()
        text = article.text.replace('\n','')
        return text
