from flask import Flask
import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
 m = random.choice(['hima','man','amakwkw'])
 return f"{m}"

app.run(host='0.0.0.0', port=81)
