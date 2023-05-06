# **EncurtaLink**

EncurtaLink é um projeto de encurtador de links feito em Python. Ele permite que você encurte URLs longas para que elas possam ser facilmente compartilhadas em plataformas de redes sociais, e-mails e mensagens. 

## 🖥️ **Tecnologias utilizadas:**

<p>O EncurtaLink foi construído usando as seguintes tecnologias:</p>

- Python 3

## 💾 **Instalação:** 

Para instalar o EncurtaLink, siga estes passos:

1. Clone o repositório do EncurtaLink em sua máquina local:

```bash
git clone https://github.com/seuusuario/encurta-link.git
```

2. Crie um ambiente virtual:

```bash
python3 -m venv env
```

3. Ative o ambiente virtual:
```bash
source env/bin/activate
```

4. Instale as dependências do projeto:
```python
pip install -r requirements.txt
```

5. Rode as migrações do Django:
```python
python manage.py migrate
```

6. Execute o servidor local:
```python
python manage.py runserver
```

7. Acesse a aplicação em seu navegador em `http://localhost:8000`

## 🤩 **Uso do APP:**

Ao acessar a aplicação em `http://localhost:8000`, você será direcionado à página inicial. Para encurtar uma URL, basta digitar a URL longa no campo de entrada e clicar no botão "Encurtar". A aplicação irá gerar uma URL curta correspondente e exibirá ambas na página. Para acessar a URL longa correspondente a uma URL curta, basta acessar a URL curta gerada na página inicial.

---

## ⭐ **Contribuição:**

Se você quiser contribuir para o EncurtaLink, fique a disposição. Caso veja algum problema, não deixe de reportar.

## 🚶🏻 **Próximos passos:**

1. Criação do site com HTML e SCSS
2. Estudar sobre a possibilidade de criar um link custom para clientes pagos.
3. Deploy do projeto.