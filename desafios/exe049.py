# Projeto: VemPython/exe049
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

pro = int(input('Informe a tabuada que deseja saber: '))

for i in range(0, 11):
    print('{} x {} = {}'.format(pro, i, pro*i))