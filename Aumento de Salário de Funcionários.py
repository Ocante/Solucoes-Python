#Aumento de Salário de Funcionários
salario = float(input("Digite o salário do funcionário: "))
cargo = input("Digite o cargo do funcionário: ")

if cargo == "programador":
    aumento = salario * 0.5
    novo_salario = salario + aumento
elif cargo == "Analista de Sistemas":
    aumento = salario * 0.4
    novo_salario = salario + aumento
elif cargo == "Analista de banco de dados":
    aumento = salario * 0.3
    novo_salario = salario + aumento
else:
    print("Cargo inválido.")
    novo_salario = salario

if novo_salario != salario:
    print("O novo salário do funcionário é R$", novo_salario)


##Explicando: O programa solicita que o usuário digite o salário e o cargo do funcionário.
##Em seguida, o programa verifica qual é o cargo digitado e calcula o valor do aumento de
##salário de acordo com a tabela. Caso o cargo não esteja na tabela, o programa exibe uma
##mensagem de erro e mantém o valor do salário inalterado.
##
##Por fim, se o valor do novo salário for diferente do valor do salário original (ou seja,
##
##se o cargo não for inválido), o programa exibe o novo salário na tela. Note que o programa
##não faz uso de formatação de valores em moeda neste exemplo.    
