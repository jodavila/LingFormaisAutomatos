nroEstados=int(input('Entre com o nro de estados: '))

estado=[input('Entre com o estado: ') for i in range(0,nroEstados)]

nroSimbolosAlfabeto=int(input('Entre com o nro de simbolos do alfabeto: '))

simbolo=[input('Entre com o simbolo do alfabeto: ') for i in range(0,nroSimbolosAlfabeto)]

estadoFinal=input('Especifique o estado final: ')

transicao=[0 for i in range(len(estado))]

for i in range(len(estado)):
    transicao[i]=[0 for j in range(len(simbolo))]
    for j in range(len(simbolo)):
        transicao[i][j]=input('A partir de '+estado[i]+' utilizando '+simbolo[j]+' vai para: ')

def mudaEstado(estadoCorrente,palavraEntrada):
    lista.append(transicao[estado.index(estadoCorrente)][simbolo.index(palavraEntrada)])
    return transicao[estado.index(estadoCorrente)][simbolo.index(palavraEntrada)]

while True:
    lista=[]
    estadoAtual=estado[0]
    palavraEntrada=input('Palavra a ser verificada: ')
    
    for i in palavraEntrada:
        estadoAtual=mudaEstado(estadoAtual,i)

    if lista[-1] == estadoFinal:
        print('Palavra aceita pela linguagem( '+estado[0]+'-->'+'-->'.join(lista)+')')

    else:
        print('Palavra não aceita pela linguagem...')
