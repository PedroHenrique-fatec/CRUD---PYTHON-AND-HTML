# Importa as funções e métodos necessários do Flask
from flask import Flask, render_template, request, redirect, url_for

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Inicializa a classe Pessoa()
class Pessoa():
    """
    Classe que representa uma pessoa.

    Atributos:
    - nome: Nome da pessoa (string).
    - idade: Idade da pessoa (inteiro).
    - cpf: CPF da pessoa (string).
    """
    def __init__(self, nome, idade, cpf):
        """
        Construtor da classe Pessoa.

        Parâmetros:
        - nome: Nome da pessoa.
        - idade: Idade da pessoa.
        - cpf: CPF da pessoa.
        """
        self.nome = nome  # Atribui o nome passado como parâmetro ao atributo da instância
        self.idade = idade  # Atribui a idade passada como parâmetro ao atributo da instância
        self.cpf = cpf  # Atribui o CPF passado como parâmetro ao atributo da instância

# Declara a variável 'banco_de_dados_pessoas' e inicializa como uma lista vazia
banco_de_dados_pessoas = []

# Define a rota principal da aplicação
@app.route('/')
def home():
    """
    Rota principal que renderiza a página inicial.

    Retorna:
    - Renderiza o template 'index.html', passando a lista de pessoas cadastradas
      para que possam ser exibidas na tabela.
    """
    return render_template('index.html', banco_de_dados_pessoas=banco_de_dados_pessoas)

# Define a rota para receber os dados do formulário
@app.route('/submit', methods=['POST'])
def adicionar_pessoa():
    """
    Rota que processa o formulário de adição de uma nova pessoa.

    Método: POST.

    Recebe os dados do formulário:
    - nome: Nome da pessoa.
    - idade: Idade da pessoa.
    - cpf: CPF da pessoa.

    Após criar uma nova instância da classe Pessoa, adiciona a nova pessoa
    à lista 'banco_de_dados_pessoas' e redireciona para a rota principal.

    Retorna:
    - Redireciona para a função home() na rota principal.
    """
    # Obtém os dados do formulário
    nome = request.form['nome']  # Captura o valor do campo 'nome' do formulário
    idade = request.form['idade']  # Captura o valor do campo 'idade' do formulário
    cpf = request.form['cpf']  # Captura o valor do campo 'cpf' do formulário
    
    # Cria uma nova instância da classe Pessoa
    nova_pessoa = Pessoa(nome, idade, cpf)  # Inicializa uma nova pessoa com os dados recebidos
    
    # Adiciona a nova pessoa à lista
    banco_de_dados_pessoas.append(nova_pessoa)  # Insere a nova pessoa na lista

    # Redireciona para a página inicial
    return redirect(url_for('home'))  # Utiliza url_for para redirecionar para a função home

# Inicia o servidor Flask
if __name__ == '__main__':
    # Inicia a aplicação com o modo de depuração ativado
    app.run(debug=True)  # Permite que mudanças no código sejam aplicadas sem reiniciar o servidor
