import random
from quote import quotes
from quote_txt import text_quote
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/quotes/pics', methods=['GET'])
def img_quote():
    
    # Image Quote
    q = random.choice(quotes)
    
    return render_template("pic_quotes.html", quote=q)
                           
@app.route('/quotes/text', methods=['GET'])
def txt_quote():
    
    # Text Quote
    quote_this = random.choice(text_quote)
    x = quote_this.split(":")
    
    return render_template("txt_quotes.html", text_quote=x)

app.run(host='0.0.0.0', port=8080)