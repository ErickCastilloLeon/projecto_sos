import sys
sys.path.append(r"C:\Users\Sebastian\Desktop\DIGS") 

from googletrans import Translator
from flask import Flask, render_template, request, jsonify

# Inicializar Flask
app = Flask(__name__, static_folder='static', template_folder='templates')
translator = Translator()

# Ruta principal - Muestra la interfaz HTML
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar las traducciones (llamada desde JavaScript)
@app.route('/traducir', methods=['POST'])
def traducir():
    try:
        texto = request.form['texto']
        # Traducir de español (es) a valenciano (ca)
        traduccion = translator.translate(texto, src='es', dest='ca')
        return jsonify({
            'status': 'success',
            'traduccion': traduccion.text
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Configuración para desarrollo
if __name__ == '__main__':
    app.run(debug=True, port=5000)