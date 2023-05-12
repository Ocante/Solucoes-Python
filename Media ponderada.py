# Solicita ao usuário as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média ponderada com peso 2 e 3, respectivamente
media_ponderada = ((2 * nota1) + (3 * nota2)) / 5

# Imprime o resultado para o usuário
print("A média ponderada do aluno é:", media_ponderada)

##Explicação do código:
##
##Na primeira parte do código, o usuário é solicitado a digitar as duas notas
##do aluno e cada uma dessas notas é armazenada em variáveis separadas (nota1
##e nota2).
##Em seguida, a média ponderada do aluno é calculada multiplicando a primeira
##nota por 2, a segunda nota por 3, somando os resultados e dividindo o resultado por 5. O resultado é armazenado na variável media_ponderada.
##Por fim, o resultado é impresso na tela utilizando a função print(), acompanhado
##da mensagem "A média ponderada do aluno é:".
