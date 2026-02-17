import csv

nome_digitado = input("Digite o nome: ")
cpf_digitado = input("Digite o CPF: ")

aluno={
    "Nome completo":nome_digitado,
    "CPF": cpf_digitado,
    "CEP": "78110-000",
    "Nascimento": "24/11/2005",
    "Responsável": "Pedro Augusto Nela",
    "Telefone": "(65) 99999-9999",
    "Série": "1º Ano do Ensino médio"
}

colunas = ["Nome completo", "CPF", "CEP", "Nascimento", "Responsável", "Telefone", "Série"]

nome_arquivo= "matricula_" + aluno["Nome completo"]+".csv"

with open(nome_arquivo, mode="a",newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerow(aluno)

