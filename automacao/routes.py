# rotas do site (links)
from flask import render_template, request
from automacao import app

@app.route('/', methods=['GET', 'POST'])
def index():

    numeros = None
    if request.method == 'POST':
        numeros = request.form.get('numeros')
        print("numeros:", numeros)

        if numeros:
            try:
                numeros = [float(num) for num in numeros.split(',')]
                quantidade = len(numeros)

                soma = sum(numeros)
                media = soma / quantidade

                amplitude = max(numeros) - min(numeros)

                variancia = sum((x - media) ** 2 for x in numeros) / quantidade

                return render_template("index.html", quantidade=quantidade, media=f"{media:.2f}", amplitude=amplitude, variancia=f"{variancia:.2f}")
            except ValueError:
                return render_template("index.html", quantidade=quantidade, error="Por favor, insira números válidos separados por vírgulas.")
    

    return render_template("index.html")
