from pypdf import PdfReader
from io import BytesIO
from urllib import request
import requests
from bs4 import BeautifulSoup

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
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # ここでは例として、すべての段落のテキストを結合しています。
        # 必要に応じて、特定の要素を取得するようにカスタマイズしてください。
        text = ' '.join([p.text for p in soup.find_all('p')])
        return text
