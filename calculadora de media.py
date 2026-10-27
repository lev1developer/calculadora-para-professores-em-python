# calculador de media de alunos dos 4 bimestres   

def media(notas):
    return sum(notas) / len(notas) #retorna a media das notas do aluno

aluno = input("Digite o nome do aluno: ").capitalize() #solicitando o nome do aluno

bimestre1 = float(input(f"Digite a nota do {aluno} no 1º bimestre: ")) #solicitando a nota do aluno no 1º bimestre
bimestre2 = float(input(f"Digite a nota do {aluno} no 2º bimestre: ")) #solicitando a nota do aluno no 2º bimestre
bimestre3 = float(input(f"Digite a nota do {aluno} no 3º bimestre: ")) #solicitando a nota do aluno no 3º bimestre
bimestre4 = float(input(f"Digite a nota do {aluno} no 4º bimestre: ")) #solicitando a nota do aluno no 4º bimestre

notas = [bimestre1, bimestre2, bimestre3, bimestre4]

print(f"Média de {aluno}: {media(notas)}")

