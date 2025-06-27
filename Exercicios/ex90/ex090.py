escola = {}
alunos = []

escola["nome"] = input('Digite seu nome: ')
escola["nota_1"] = float(input('Primeira nota: '))
escola["nota_2"] = float(input('Segunda nota: '))

media = (escola['nota_1'] + escola['nota_2']) / 2

alunos.append(escola.copy())

if media >= 5.0:
    print(f'''Nome: {escola["nome"]}
    Média de {escola["nome"]}: {media}
    Situação é igual, APROVADO''')
else:
    print(f'''Nome: {escola["nome"]}
    Média de {escola["nome"]}: {media}
    Situação é igual, REPROVADO''')