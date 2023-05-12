# Coversão de temperatura

# Solicita ao usuário a temperatura em Fahrenheit
temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# Realiza a conversão para Celsius
temp_celsius = (temp_fahrenheit - 32) / 1.8

# Imprime o resultado para o usuário
print("A temperatura em Celsius é:", temp_celsius)

##Explicação do código:
##
##A primeira linha do código solicita ao usuário a temperatura em
##Fahrenheit e armazena esse valor na variável temp_fahrenheit.
##Em seguida, a temperatura em Fahrenheit é convertida para
##Celsius utilizando a fórmula temp_celsius = (temp_fahrenheit - 32) / 1.8,
##e o resultado é armazenado na variável temp_celsius.
##Por fim, o resultado é impresso na tela utilizando a função print(),
##acompanhado da mensagem "A temperatura em Celsius é:".
