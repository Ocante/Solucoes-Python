altura = float(input("Digite a altura da pessoa: "))
sexo = input("Digite o sexo da pessoa (M/F): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem com altura", altura, "é", peso_ideal, "kg.")
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com altura", altura, "é", peso_ideal, "kg.")
else:
    print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")


##O programa solicita que o usuário digite a altura e o sexo da pessoa.
##Em seguida, o programa verifica se o sexo digitado é masculino ou feminino
##e realiza o cálculo do peso ideal com base na altura e na fórmula correspondente.
##O resultado é impresso na tela com uma mensagem personalizada. Se o sexo digitado
##não for válido, o programa exibe uma mensagem de erro.
