<p align="center">
  <img src="https://www.ime.usp.br/lem/ens-mat/hanoi.gif" width="700" height="400" alt="Torre de Hanói - Imagem Representativa">
</p> <br>

# 📊 Torres de Hanói

Uma aplicação web interativa para demonstrar e resolver o clássico problema matemático das **Torres de Hanói**, desenvolvida para a disciplina de Matemática. Este projeto utiliza **Python** com o framework **Flask** e inclui animações visuais usando HTML5 Canvas.

---

## 📋 Descrição do Projeto

As **Torres de Hanói** são um quebra-cabeça matemático que consiste em mover um conjunto de discos de uma torre para outra, seguindo algumas regras específicas:

1. Apenas um disco pode ser movido por vez.
2. Nenhum disco pode ser colocado sobre outro menor.
3. Todos os discos devem ser movidos para outra torre.

Nesta aplicação, o usuário pode:

- Inserir o número de discos.
- Visualizar a sequência de movimentos necessária.
- Acompanhar uma animação mostrando a solução do problema.

---

## 📁 Estrutura do Projeto

A estrutura de pastas e arquivos do projeto é a seguinte:

```plaintext
TORRES DE HANÓI/
│
├── .venv/                         # Ambiente virtual do Python
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
│
├── static/                        # Arquivos estáticos (CSS e imagens)
│   ├── img/
│   │   └── favicon.png            # Ícone do site
│   └── styles.css                 # Estilos do projeto
│
├── templates/                     # Templates HTML do projeto
│   └── index.html                 # Página principal da aplicação
│
├── app.py                         # Arquivo principal da aplicação Flask
├── requirements.txt               # Lista de dependências do projeto
├── vercel.json                    # Arquivo de configuração para Vercel
└── README.md                      # Documentação do projeto
```

---

## ⚙️ Requisitos do Sistema

### Para **Windows**:

1. **Python 3.9+**: Certifique-se de que o Python está instalado. Caso contrário, [baixe aqui](https://www.python.org/downloads/).
2. **Pip**: Geralmente, vem com o Python. Confirme com:
   ```bash
   pip --version
   ```

3. **Editor de texto**: Recomendado o Visual Studio Code (VS Code)

### Para **Mac**:

1. **Python 3.8+**: Instale usando o [Homebrew](https://brew.sh/) ou faça o download do [site oficial do Python](https://www.python.org/downloads/).
   ```bash
   brew install python
   ```

2. **pip**: Já vem incluído com as versões mais recentes do Python.

3. **Editor de texto**: Recomendado o Visual Studio Code (VS Code)

---

## 📦 Instalação e Configuração

### Para **Windows**:

1. **Clone o repositório**: Abra o terminal (cmd, PowerShell ou terminal do VS Code) e execute:
   ```bash
   git clone https://github.com/solipa365/torres-de-hanoi.git
   cd torres-de-hanoi
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
    ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

### Para **Mac**:

1. **Clone o repositório**: Abra o terminal e execute:
   ```bash
    git clone https://github.com/solipa365/torres-de-hanoi.git
    cd torres-de-hanoi
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
    ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Executar o Projeto

### Para Windows e Mac:

1. **Inicie o servidor Flask**: No terminal, estando dentro do diretório do projeto:
   ```bash
    python app.py
   ```

2. **Acesse no navegador**: Abra o navegador e vá para [http://127.0.0.1:5000](http://127.0.0.1:5000) 

---

## 📚 Documentação

1. Algoritmo das Torres de Hanói

O algoritmo recursivo utilizado para resolver o problema está implementado no arquivo app.py:
   ```bash
    def hanoi(n, origem, destino, intermediario, movimentos):
    if n == 1:
        movimentos.append((origem, destino))
    else:
        hanoi(n - 1, origem, intermediario, destino, movimentos)
        movimentos.append((origem, destino))
        hanoi(n - 1, intermediario, destino, origem, movimentos)
    return movimentos
   ```

Parâmetros:

- n: Número de discos.
- origem: Torre inicial.
- destino: Torre final.
- intermediario: Torre intermediária.
- movimentos: Lista que armazena os movimentos.

2. HTML5 Canvas para Visualização <br>
O arquivo index.html contém o script que utiliza o elemento canvas para criar a animação das Torres de Hanói. Ele desenha as torres e os discos, atualizando dinamicamente os movimentos com base nos cálculos do backend.

3. Arquivo vercel.json <br>
Este arquivo permite o deploy da aplicação na plataforma Vercel, configurando o Flask para funcionar como um servidor backend.

---

## 💡 Funcionalidades

- Resolver o problema das Torres de Hanói com visualização interativa.
- Exibir o número mínimo de movimentos necessários.
- Representar graficamente os movimentos em um canvas HTML.

---

## 🛠️ Tecnologias Utilizadas

- Python 3: Linguagem de programação principal.
- Flask: Framework web para criação do servidor.
- HTML5, CSS3 e JavaScript: Para o front-end interativo.
- Canvas API: Para visualização gráfica dos movimentos.
- Pip: Gerenciador de pacotes para instalação de dependências.

---

## ✨ Autor

Projeto Desenvolvido/Projetado por [António Manuel Domindos Solipa](https://github.com/solipa365).