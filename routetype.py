#router type
from  flask import Flask
app = Flask(__name__)

@app.route("/cadena/<string:nombre>")
def demo_cadena(nombre):
	return f"Cadena: {nombre} => Tipo de dato: {type(nombre)._name_}"

@app.route("/entero/<int:numero>")
def demo_entero(numero):
	return f"Entero: {numero} => Tipo de dato: {type(numero)._name_}"
	
@app.route("/decimal/<float:decimal>")
def demo_float(decimal):
	return f"Float: {decimal} => Tipo de dato: {type(decimal)._name_}"
	
@app.route("/ruta/<ruta>")
@app.route("/ruta/<path:ruta>")
def demo_ruta(ruta):
	return f"Ruta: {ruta}"

if __name__=='__main__':
    app.run(debug=True)   
