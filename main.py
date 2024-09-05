from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        escolha = request.form['escolha']

        if escolha == '+':
            resultado = num1 + num2
        elif escolha == '-':
            resultado = num1 - num2
        elif escolha == '*':
            resultado = num1 * num2
        elif escolha == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero!"
        else:
            resultado = "Operação inválida. Por favor, digite +, -, * ou /."
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
