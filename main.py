from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
   html_style = '''
     <body style="background-color: #546581;">
    
        <h1 style="color: #ce999b;">Hello, %s! ''' % name
   '''</h1>
    
    </body>
    '''
   
   return html_style

if __name__ == '__main__':
   app.run()