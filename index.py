from flask import Flask, render_template

app = Flask(__name__)
 
# @app.route('/')
# def home():
#     return "Bienvenid@s!!"

# @app.route('/contacto')
# def contacto():
#         return """<h1>Formulario de Contacto</h1>"""
@app.route('/')
def index():
    return render_template('index.html', the_title="Inicio")
    
@app.route("/contacto")
def contacto():
     return render_template('contacto.html')
 
@app.route("/lenguajes")
def lenguajes():
    mis_lenguajes = ("PHYTON", "PHP", "Javascript", "C++", "NUMPY")
    return render_template("lenguajes.html", lenguajes = mis_lenguajes, el_titulo= "Lenguajes de Programación")  
            
if __name__ == '__main__':
        app.run(debug=True)
    