from datetime import datetime

pessoas = {
    "nome": input('Nome: '),
    "ctps": int(input('Carteira de Trabalho (0 não tem): '))
}

data = []
nascimento = int(input('Ano de nascimento: '))
data.append(nascimento)
data.append(pessoas)

if "ctps" != 0:
    pessoas["contratação"] = int(input('Ano de contratação: '))
    pessoas["salário"] = float(input('Salário: ').replace(",", "."))

ano_atual = datetime.now().year
idade = (ano_atual - nascimento) - 1
aposentadoria = idade + pessoas["contratação"] + 35 - datetime.now().year

print(f'''nome tem o valor {pessoas["nome"]}
idade tem o valor {idade}
ctps tem o valor {pessoas["ctps"]}
contratação tem o valor {pessoas["contratação"]}
salário tem o valor {pessoas["salário"]}
aposentadoria tem o valor {aposentadoria}''')
