
from flask import Flask,render_template,request
from PyPDF2 import PdfFileWriter, PdfFileReader
app = Flask(__name__)
a='sai'
@app.route('/', methods =["GET", "POST"])

def hello_world():
   if request.method == "POST":
      # getting input with name = fname in HTML form
      bm = request.form.get("file1")
      bm1 = request.form.get("file2")
      output = PdfFileWriter() # open output
      input1 = PdfFileReader(open('sample1.pdf', 'rb'))
      output.addPage(input1.getPage(0))
      input2 = PdfFileReader(open('sample2.pdf', 'rb'))
      output.addPage(input2.getPage(0))

      parent = output.addBookmark('Introduction', 0) # add parent bookmark
      output.addBookmark('Hello, World', 0, parent) # add child bookmark
      output.write(open('Intoduction','wb'))
   return render_template("index.html")
#app.debug = True
#app.run()
#app.run(debug = True)
if __name__ == '__main__':
   app.run(debug=True)