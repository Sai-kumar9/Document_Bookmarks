
from flask import Flask,render_template,request
app = Flask(__name__)
a='sai'
@app.route('/')
def hello_world():
   return render_template("index.html")
#app.debug = True
#app.run()
#app.run(debug = True)
if __name__ == '__main__':
   app.run()