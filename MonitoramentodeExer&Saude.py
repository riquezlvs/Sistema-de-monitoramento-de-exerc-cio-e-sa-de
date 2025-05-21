import random 

# VARIÁVEIS INICIAIS

# Listas que armazenam os dados dos exercícios
n_ex = ["Corrida", "Bicicleta", "Natação", "Caminhada", "Pular corda", "Corrida"]  # Nome do exercício
tmp  = [30, 45, 60, 40, 20, 25]  # Tempo gasto em minutos
cal  = [300, 400, 500, 200, 250, 350]  # Calorias queimadas
dia  = ["segunda", "terça", "quarta", "quinta", "sexta", "quinta"]  # Dia da semana do exercício

# FUNÇÕES DO MENU

# Exibe o menu principal
def exibir_menu():
    print(" " + "_" * 38)
    print("|                                     |")
    print("| 1.Cadastro de exercícios            |")
    print("| 2.Relatório Diário                  |")
    print("| 3.Cálculo de IMC                    |")
    print("| 4.Meta Semanal                      |")
    print("| 5.Frases Motivacionais              |")
    print("| 6.Média de Calorias por Exercício   |")
    print("| 7.Código de Barras no Terminal      |")
    print("|" + "_" * 37 + "|")

# Menu principal com chamadas de funções
def menu():
    while True:
        exibir_menu()
        menuOption = input("\nEscolha uma opção (ou 'sair' para encerrar): ")

        if menuOption == '1':
            cad_exercicios()
        elif menuOption == '2':
            rel_diario()
        elif menuOption == '3':
            calculo_imc()
        elif menuOption == '4':
            meta_semanal()
        elif menuOption == '5':
            frase_motivacional()
        elif menuOption == '6':
            med_cal_exer()
        elif menuOption == '7':
            grafico_barras()
        elif menuOption.lower() == 'sair':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")

# FUNÇÕES DAS OPÇÕES

# 1. Cadastro de novos exercícios
def cad_exercicios():
    while True:
        n_ex.append(input("\nNome do exercício: "))
        tmp.append(int(input("Tempo gasto (minutos): ")))
        cal.append(int(input("Calorias queimadas: ")))
        dia.append(input("Dia da semana: ").lower())
        opn = input("Pressione Enter para continuar cadastrando ou '1' para voltar ao menu principal... ")
        if opn == "1":
            break  

# 2. Relatório de exercícios por dia da semana
def rel_diario():
    print(dia)
    sem = input("Digite o dia da semana para o relatório: ").lower()
    total_tempo = 0
    total_calorias = 0
    encontrados = 0

    for i in range(len(dia)):
        if dia[i] == sem:
            encontrados += 1
            print(f"\nExercício: {n_ex[i]}")
            print(f"Tempo gasto: {tmp[i]} min")
            print(f"Calorias queimadas: {cal[i]} kcal")
            total_tempo += tmp[i]
            total_calorias += cal[i]

    if encontrados > 0:
        print(f"\nResumo do dia {sem}:")
        print(f"Total de tempo gasto: {total_tempo} minutos")
        print(f"Total de calorias queimadas: {total_calorias} kcal")
    else:
        print(f"\nNenhum exercício registrado na {sem}.")

# 3. Cálculo do IMC
def calculo_imc():
    peso = int(input("Digite seu peso: "))
    alt = float(input("Digites sua altura: "))
    imc = peso / (alt ** 2)
    if imc < 18.5:
        print("Baixo peso")
    elif imc >= 18.5 and imc < 24.9:
        print("Peso normal")
    elif imc >= 25 and imc < 29.9:
        print("Excesso de peso")
    else:
        print("Obesidade")

# 4. Meta semanal de calorias
def meta_semanal():
    meta = int(input("Qual sua meta de calorías semamal? "))

    soma_cal = 0
    for i in range(len(cal)):
        soma_cal += cal[i]
    
    if soma_cal >= meta:
        print("Parabéns! Sua meta foi atingida.")
    else:
        print("Que pena, sua meta não foi alcançada :/. Tente novamente!")

# 5. Frase motivacional aleatória
def frase_motivacional():
    frases = [
        "Não pare até se orgulhar.",
        "A dor que você sente hoje é a força que sentirá amanhã.",
        "Seu corpo pode suportar quase tudo. É sua mente que você precisa convencer.",
        "Treine enquanto eles dormem. Lute enquanto eles descansam.",
        "A disciplina é o combustível da conquista.",
        "Não é sobre ser o melhor, é sobre ser melhor do que ontem.",
        "Cada treino é um passo mais perto do seu objetivo.",
        "Você não precisa ir rápido. Você só precisa ir.",
        "Levante. Treine. Supere.",
        "O sucesso começa com a decisão de tentar."
    ]

    frase = random.choice(frases)
    print("\nFrase motivacional do dia:\n" + frase)

# 6. Cálculo da média de calorias para um exercício específico
def med_cal_exer():
    print("\nExercícios disponíveis:", n_ex)
    exer = input("Qual exercício gostaria de saber a média de calorías gastas? ")
    tot_cal = 0
    contador = 0

    for i in range(len(n_ex)):
        if n_ex[i] == exer:
            tot_cal += cal[i]
            contador += 1

    if contador > 0:
        mdiaCal = tot_cal / contador
        print(f"\nA média de calorias do exercício '{exer}' é {mdiaCal:.2f} kcal")
    else:
        print("Exercício não existe")

# 7. Exibe gráfico de barras simples no terminal (calorias por exercício)
def grafico_barras():
    print("\nGráfico de Calorias Queimadas por Exercício:\n")
    
    for i in range(len(n_ex)):
        barras = '█' * (cal[i] // 10) 
        print(f"{n_ex[i]:<15} | {barras} ({cal[i]} kcal)")

# EXECUTA O PROGRAMA

menu()
