from flask import Flask, render_template, request

app = Flask(__name__)

def hanoi(n, origem, destino, intermediario, movimentos):
    if n == 1:
        movimentos.append((origem, destino))
    else:
        hanoi(n - 1, origem, intermediario, destino, movimentos)
        movimentos.append((origem, destino))
        hanoi(n - 1, intermediario, destino, origem, movimentos)
    return movimentos

@app.route('/')
def index():
    return render_template('index.html', movimentos=[], num_discos=0)

@app.route('/solve', methods=['POST'])
def solve():
    num_discos = int(request.form['num_discos'])
    movimentos = []
    movimentos = hanoi(num_discos, 0, 2, 1, movimentos)
    return render_template('index.html', movimentos=movimentos, num_discos=num_discos)

if __name__ == "__main__":
    app.run(debug=True)
