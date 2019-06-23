#nroEstados=int(input('Entre com o nro de estados: '))

#estado=[input('Entre com o estado: ') for i in range(0,nroEstados)]

#nroSimbolosAlfabeto=int(input('Entre com o nro de simbolos do alfabeto: '))

#simbolo=[input('Entre com o simbolo do alfabeto: ') for i in range(0,nroSimbolosAlfabeto)]

#estadoFinal=input('Especifique o estado final: ')

#transicao=[0 for i in range(len(estado))]

#for i in range(len(estado)):
#    transicao[i]=[0 for j in range(len(simbolo))]
#    for j in range(len(simbolo)):
#        transicao[i][j]=input('A partir de '+estado[i]+' utilizando '+simbolo[j]+' vai para: ')

# Abre arquivo para leitura e pega linhas do autômato ----------------------------------

arquivo_entrada = open('Entrada_Xadrez.txt', 'r');
arq = arquivo_entrada.readlines();

# Pega os estados do automato ----------------------------------------------------------

estados = arq[0].split('{')[1];
estados = estados.split('}')[0];

# Conta a quantidade de estados --------------------------------------------------------

nroEstados = int(estados.count(',') + 1)


# Cria array com cada estado -----------------------------------------------------------

estado=[0 for i in range(nroEstados)]

for i in range(0, nroEstados):
    estado[i] = estados.split(',')[i].strip(' ')


# Pega os simbolos do alfabeto ---------------------------------------------------------

simbolosAutomato = arq[0].split('{')[2]
simbolosAutomato = simbolosAutomato.split('}')[0]

# Conta a quantidade de simbolos -------------------------------------------------------

nroSimbolosAlfabeto = int(simbolosAutomato.count(',') + 1)

# Cria array com cada simbolo ----------------------------------------------------------
simbolo = [0 for i in range(nroSimbolosAlfabeto)]

for i in range(0, nroSimbolosAlfabeto):
    simbolo[i] = simbolosAutomato.split(',')[i].strip(' ')


# Pega o simbolo inicial ---------------------------------------------------------------
simboloInicial = arq[0].split('{')[2]
simboloInicial = simboloInicial.split('}')[1]
simboloInicial = simboloInicial.split(',')[1].strip(' ')

# Pega os estados finais ---------------------------------------------------------------

simbolosFinais = arq[0].split('{')[3]
simbolosFinais = simbolosFinais.split('}')[0]

nroSimbolosFinais = int(simbolosFinais.count(',') + 1)

simbFinais = [0 for i in range(nroSimbolosFinais)]

for i in range(0, nroSimbolosFinais):
    simbFinais[i] = simbolosFinais.split(',')[i].strip(' ')



# ============= PEGA AS TRANSIÇÕES DO AUTÔMATO ==========================================

transicao=[0 for i in range(len(estado))]

i = 0
j = 0
ok = 0

while True:
    j = 0
    k = 1
    
    if (i == nroEstados): break
    
    transicao[i]=[0 for j in range(len(simbolo))]
    estadoAtual = estado[i]

    while True:
        if (j == nroSimbolosAlfabeto):break
        
        simboloAtual = simbolo[j]
        k=1
    
        while True:
            if (k == len(arq)):
             #   print('aqui')
                break
            estadoProd = arq[k].strip(' \n').split('(')[1].split(',')[0].strip(' ')
                
            simboloProd = arq[k].strip(' \n').split(')')[0].split(',')[1].strip(' ')
            #print(estadoAtual, simboloProd, simboloAtual)

            if estadoProd == estadoAtual and simboloProd == simboloAtual:
                transicao[i][j] = arq[k].strip(' \n').split('=')[1].strip(' ')
                #print(estadoProd)
                #print(simboloProd)
                #print(transicao[i][j])
                #k = 1
                break
            else:
                k = k + 1

        j = j + 1
        
    i = i + 1
    

#print(transicao[39][13])


def mudaEstado(estadoCorrente,palavraEntrada):
    lista.append(transicao[estado.index(estadoCorrente)][simbolo.index(palavraEntrada)])
    return transicao[estado.index(estadoCorrente)][simbolo.index(palavraEntrada)]

while True:
    lista=[]
    estadoAtual=estado[0]
    palavraEntrada=input('Palavra a ser verificada: ')
    
    for i in palavraEntrada:
        estadoAtual=mudaEstado(estadoAtual,i)

    ok = 0

    for i in range(0, nroSimbolosFinais):
        if lista[-1] == simbFinais[i]:
            print('Palavra aceita pela linguagem( '+estado[0]+'-->'+'-->'.join(lista)+')')
            ok = 1

    if ok == 0:
        print('Palavra não aceita pela linguagem...')
