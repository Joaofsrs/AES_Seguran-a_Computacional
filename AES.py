##############################################################################
# Universidade de de Brasilia                                                #
# Instituto de Ciencia Exatas                                                #
# Departamento de Ciencia da Computacao                                      #
#                                                                            #
# Seguranca Computacional - 2021/1                            			     #
# Trabalho 2                                                                 #
# Alunos: Joao Francisco Gomes Targino                                       #
#         Joao Gabriel Ferreira Saraiva                                      #
# Matriculas: 180102991                                                      #
#             180103016                                                      #
# Versao do Compilador:  Python 3.9.7                                        #
#                                                                            #
##############################################################################
import cv2 as cv
import base64
import io
import cv2
import random

'''
    Variaveis globais que serao usadas para fazer operacoes durante o codigo
'''
sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 
]
sbox_Inv = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]
k_ex = [
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 
        0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 
        0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 
        0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 
        0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 
        0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 
        0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 
        0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 
        0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 
        0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 
        0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 
        0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 
        0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 
        0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 
        0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 
        0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d
]
exp = []
'''
    A funcao key_expansion cria a partir da primeira chave cria varias chaves para usar uma diferente a cada rodada
'''
def key_expansion(key, rodadas):
    contcralo = 0
 
    for i in range((rodadas+1)*16):
        '''
            A chave original eh guardada nas primeiras posicoes do vetor
            Se i for divisivel por 16 entao estaremos no primeiro elemento de alguma chave
            e o primeiro elemento tem um calculo diferente a se fazer assim como os elementos 
            pertencentes a mesma coluna dele que serao tratados nos elifs abaixo
        '''
        if i < 16:
            exp.append(key[i])
        elif((i % 16) == 0):
            exp.append(sbox[exp[i-3]] ^ exp[i-16] ^ k_ex[int(i/16)-1])
            contcralo = 1

        elif(contcralo == 1):
            exp.append(sbox[exp[i-3]] ^ exp[i-16])
            contcralo = 2

        elif(contcralo == 2):
            exp.append(sbox[exp[i-3]] ^ exp[i-16])
            contcralo = 3

        elif(contcralo == 3):
            exp.append(sbox[exp[i-7]] ^ exp[i-16])
            contcralo = -1

        else:
            exp.append(exp[i-4] ^ exp[i - 16])

'''
    A funcao around_key funcao pega cada uma das chaves geradas de acordo com a rodada que esta executando
    e combina a palavra de 16 bytes com ela 
'''
def around_key(word,rodada):
    j = rodada*16

    for i in range(16):
        word[i] = word[i] ^ exp[j+i]

'''
    A funcao sub_bytes pega cada posicao da palavra sendo cifrada e substitui pelo caractere correspondente
    na tabela sbox
'''
def sub_bytes(word):

    for i in range(16):
        word[i] = sbox[word[i]]

'''
    A funcao sub_bytes_inv pega cada posicao da palavra sendo decifrada e substitui pelo caractere correspondente
    na tabela sbox_inv
'''
def sub_bytes_inv(word):

    for i in range(16):
	    word[i] = sbox_Inv[word[i]]

'''
    A funcao shift_rows pega a palavra de 16 bytes, deixa a primeira linha igual, shifta cada elemento da segunda linha em uma posicao,
    da terceira em duas posicoes e da quarta em tres posicoes, todos os shifts sao feitos para a direita
'''
def shift_rows(word):
    #linha 1
    aux = word[1]
    word[1] = word[5]   
    word[5] = word[9]
    word[9] = word[13]
    word[13] = aux
    #linha 2
    aux = word[2]
    aux2 = word[6]   
    word[2] = word[10]
    word[6] = word[14]
    word[10] = aux
    word[14] = aux2
    #linha 3
    aux = word[3]
    aux2 = word[7]
    aux3 = word[11] 
    word[3] = word[15]  
    word[7] = aux 
    word[11] = aux2
    word[15] = aux3

'''
    A funcao shift_rows_inv pega a palavra de 16 bytes, deixa a primeira linha igual, shifta cada elemento da segunda linha em uma posicao,
    da terceira em duas posicoes e da quarta em tres posicoes, todos os shifts sao feitos para a esquerda
'''
def shift_rows_inv(word):
    #linha 1
    aux = word[13]
    word[13] = word[9]
    word[9] = word[5]
    word[5] = word[1] 
    word[1] = aux  
    #linha 2    
    aux = word[14]
    aux2 = word[10]   
    word[14] = word[6]
    word[10] = word[2]
    word[6] = aux
    word[2] = aux2
    #linha 3
    aux = word[15]
    aux2 = word[11]
    aux3 = word[7] 
    word[15] = word[3]
    word[11] = aux  
    word[7] = aux2 
    word[3] = aux3

'''
    A funcao Gmul usada para fazer a multiplicacao de polinomios
'''
def Gmul(aux, aux1):
    ret = 0x00
    for i in range(8):
        if ((aux1 & 1) != 0):
            ret = ret ^ aux
        if ((aux & 0x80) != 0):
            aux = aux <<  1
            aux = aux ^ 0x1B
        else:
            aux = aux << 1
        aux1 = aux1 >> 1

    return (ret%256)

'''
    A funcao mix_column eh usada na funcao AES, onde ela eh realizada pela cifra Rijndael, junto com a etapa ShiftRows
    pode se observar que eh realizada uma multiplicacao de polinomios onde temos:

    |aux[0]|    |2 3 1 1|   |word[0]|
    |aux[1]|  = |1 2 3 1| * |word[1]|
    |aux[2]|    |1 1 2 3|   |word[2]|
    |aux[3]|    |3 1 1 2|   |word[3]|

    Temos aux como a coluna final
'''

def mix_column(word):
    aux = []

    for i in range(4):
        aux.append(Gmul(0x02, word[i*4]) ^ Gmul(0x03, word[(i*4)+1]) ^ word[(i*4)+2] ^ word[(i*4)+3])
        aux.append(word[i*4] ^ Gmul(0x02, word[(i*4)+1]) ^ Gmul(0x03, word[(i*4)+2]) ^ word[(i*4)+3])
        aux.append(word[i*4] ^ word[(i*4)+1] ^ Gmul(0x02, word[(i*4)+2]) ^ Gmul(0x03, word[(i*4)+3]))
        aux.append(Gmul(0x03, word[i*4]) ^ word[(i*4)+1] ^ word[(i*4)+2] ^ Gmul(0x02, word[(i*4)+3]))

    return aux

'''
    A funcao mix_column_inv eh usada na funcao AES_inv, onde ela eh realizada pela cifra Rijndael, junto com a etapa ShiftRows
    pode se observar que eh realizada uma multiplicacao de polinomios onde temos:

    |aux[0]|    |14 11 13 09|   |word[0]|
    |aux[1]|  = |09 14 11 13| * |word[1]|
    |aux[2]|    |13 09 14 11|   |word[2]|
    |aux[3]|    |11 13 09 14|   |word[3]|

    Temos aux como a coluna final
'''

def mix_column_inv(word):
    aux = []

    for i in range(4):
        aux.append(Gmul(word[i*4], 14) ^ Gmul(word[(i*4)+3], 9) ^ Gmul(word[(i*4)+2], 13) ^ Gmul(word[(i*4)+1], 11))
        aux.append(Gmul(word[(i*4)+1], 14) ^ Gmul(word[i*4], 9) ^ Gmul(word[(i*4)+3], 13) ^ Gmul(word[(i*4)+2], 11))
        aux.append(Gmul(word[(i*4)+2], 14) ^ Gmul(word[(i*4)+1], 9) ^ Gmul(word[i*4], 13) ^ Gmul(word[(i*4)+3], 11))
        aux.append(Gmul(word[(i*4)+3], 14) ^ Gmul(word[(i*4)+2], 9) ^ Gmul(word[(i*4)+1], 13) ^ Gmul(word[i*4], 11))
    
    return aux

'''
    A funcao AES recebe uma palavra de 16 bytes e o numero de rodadas e faz a cifra dessa palavra 
    primeiro a palavra e mandada para o round_key, e depois entra num for que roda pelo numero de rodadas escolhida
    nesse for a palavra eh mandada para sub_bytes, depois shift_rows, caso o for nao esteja na ultima execucao
    executa mix_column, e por fim around_key, retornando apos o final do for a palavra de 16 bytes cifrada
'''
def AES(word, num):
    around_key(word, 0)

    for i in range(1, num+1):
        sub_bytes(word)
        shift_rows(word)

        if i != num:
            word = mix_column(word)
        around_key(word, i)

    return word

'''
    A funcao AES_inv recebe uma palavra de 16 bytes e o numero de rodadas e faz a decifracao dessa palavra 
    primeiro a palavra e mandada para o round_key, e depois entra num for que roda pelo numero de rodadas escolhida
    nesse for a palavra eh mandada para shift_rows, depois sub_bytes, around_key logo em seguida e por fim
    caso o for nao esteja na primeira execucao executa mix_column, retornando apos o final do for a palavra de 16 bytes decifrada
'''
def AES_inv(word,num):
    around_key(word, num)

    for i in range(num-1, -1, -1):
        shift_rows_inv(word)
        sub_bytes_inv(word)
        around_key(word, i)

        if(i != 0):
            word = mix_column_inv(word)

    return word

'''
    A funcao ECB recebe a imagem e separa ela em blocos para mandar para a funcao AES ou AES_inv
'''
def ECB(word, num, op):
    aux = []
    '''
        Esse for pega todos rgb's e coloca em um vetor
    '''
    for i in range(len(word)):
        for j in range(len(word[i])):
            aux.append(word[i][j][0])
            aux.append(word[i][j][1])
            aux.append(word[i][j][2])     
    '''
        Caso aux nao seja divisivel por 16 ah adicionado 0 ate ele ser
    '''
    while(len(aux) % 16 != 0):
        aux.append(0x00)

    wordfinal = []
    '''
        Nesse for o rgb eh separado em blocos de 16 bytes cada, ou seja cada bloco possui 16 numeros
        pois cada rgb representa um byte.
        Depois de serem separados cada bloco eh mandado para AES ou AES_inv e roda o numero de rodadas pedidas
        e volta sendo concatenado em outro vetor que sera transformado novamente em imagem depois
    '''
    for i in range(int(len(aux)/16)):
        blocos = []

        for j in range(16):
            blocos.append(aux[(i*16)+j])

        if op == 1:
            wordaux = AES(blocos,num)

        else:
            wordaux = AES_inv(blocos,num)

        for k in range(16):
            wordfinal.append(wordaux[k])

    return wordfinal

'''
    A funcao nonce gera um vetor de 16 bytes randomico para ser usado no nonce e na chave caso o usuario queira
'''
def nonce():
    aux = []

    for i in range(16):
        aux.append(random.randrange(0,255))

    return aux

'''
    A funcao CTR recebe uma imagem, o numero de rodadas e uma 'chave' random nonce
    A funcao cifra a palavra(nonce xor contador) de 16 bytes usando a funcao AES, e em seguida usa o resultado da funcao
    para fazer um xor com uma palavra de 16 bytes da imagem, fazendo isso de 16 em 16 bytes com toda a imagem,
    retornando ao final a imagem cifrada/decifrada, essa funcao eh usada para cifrar e decifrar imagens, pois o processo eh o mesmo
'''
def CTR(word, num, noncekey):
    aux = []
    ''' 
        Contador de 128 bits, onde cada posicao do vetor um elemento de um byte
    '''
    cont = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    '''
        Esse for pega todos rgb's e coloca em um vetor
    '''

    for i in range(len(word)):
        for j in range(len(word[i])):
            aux.append(word[i][j][0])
            aux.append(word[i][j][1])
            aux.append(word[i][j][2])    

    '''
        Caso o vetor não seja divisivel por 16, ele completa com 0
    '''

    while(len(aux) % 16 != 0):
        aux.append(0x00)
    
    wordfinal = []
    noncekeyaux = noncekey

    for i in range(int(len(aux)/16)):
        fon = []
        wordaux = []

        '''
            o vetor 'fon' recebe 16 elementos do vetor principal, 
        '''

        for j in range(16):
            fon.append(aux[(i*16)+j])
        '''
            auxvec recebe o resultado da nonce(nonce xor contador) apos ser cifrado pelo AES
        '''
        auxvec = AES(noncekeyaux,num)

        '''
            wordaux recebe o xor entre a palavra de 16 bytes da imagem, e o nonce(nonce xor contador) cifrado e em seguida coloca byte a byte no final da 'imagem'
        '''

        for j in range(16):
            wordaux.append(fon[j] ^ auxvec[j])

        for j in range(16):
            wordfinal.append(wordaux[j])

        '''
            for usado para somar 1 no contador
        '''

        for j in range(15, -1, -1):
            if (cont[j] < 0xFF):
                cont[j] = cont[j] + 1
                break
            else:
                cont[j] = 0

        '''
            for usado para fazer a operacao xor entre o contador e a chave random 'nonce', armazenado na variavel noncekeyaux
        '''

        for j in range(16):
            noncekeyaux[j] = noncekey[j] ^ cont[j]

    '''
        Retorna a imagem cifrada/decifrada
    '''

    return wordfinal

'''
    A funcao learq le o arquivo e coloca os bytes do arquivo em na variavel de chave ou na variavel de noncekey
'''
def learq(num):
    retorno = []
    aux = ''

    if num == 1:
        arq = open("chave.txt")

    else:
        arq = open("nonce.txt")

    txt = arq.read()
    '''
        O byte do arquivo eh lido ate que apareca um espaco, entao esse byte eh transformado de string em um inteiro 
        de 0 a 255 e coloca
    '''
    for i in range(len(txt)):
        if txt[i] == ' ':
            retorno.append(int(float(aux)))
            aux = ''

        else:
            aux += txt[i]

    return retorno

'''
    A funcao print_img pega o vetor que foi cifrado ou decifrado
    tranforma novamente esse vetor no formato da tridimensional da imagem do opencv
    caso o usuario queira mostra essa imagem na tela e depois ela eh salva 
    e o nome depende da escolha ter sido cifracao ou decifracao
'''
def print_img(original, final, op1):
    aux1 = original
    aux2 = 0

    for i in range(len(original)):
        for j in range(len(original[i])):
            for k in range(3):
                aux1[i][j][k] = final[aux2]
                aux2 = aux2 + 1

    op = int(input('Deseja mostrar imagem na tela:\n' '    1-sim\n' '    2-nao\n'))

    if op == 1:
        cv2.imshow('resultado',aux1)
        cv2.waitKey(0)

    if op1 == 1:
        cv2.imwrite('cifrada.png',aux1)

    else:
        cv2.imwrite('imagem_final.png',aux1)

'''
    A funcao salva_hash pega a chave ou o nonce e cria o txt correspondente e salva os 16 bytes que foram usados
    os bytes sao guardados em int separados por espaco 
'''
def salva_hash(chavenonce, op):
    if op == 1:
        arq = open("chave.txt","w+")
    else:
        arq = open("nonce.txt","w+")

    for num in chavenonce:
        arq.write(str(num))
        arq.write(" ")

    arq.close()

'''
    A funcao trata_chave pega a chave lida ou passada e checa se ela tem 16 bytes, caso tenha menos que isso
    ele completa a palavra com o byte 0x00, caso tenha mais que isso a palavra é truncada e somente sao usados
    os bytes de 0 a 15 
'''
def trata_chave(chave):
    if len(chave) < 16: 
        while len(chave) < 16:
            chave += b'\x00'

    elif len(chave) > 16:
        chave = chave[:16]

'''
    A funcao main pega as opcoes e chama as funcoes de acordo com as escolhas do usuario
'''
def main():
    chave = []
    chaveaux = []
    noncekey = []
    word = []

    op1 = int(input('Escolha um modo:\n\n1:ECB\n2:CTR\n'))
    print('\nATENCAO:\nCrie uma imagem com o nome de \'cifra.png\' caso a opcao seja Cifrar e \'cifrada.png\' caso a escolha seja Decifrar e coloque no mesmo diretorio onde esta o programa;')
    print('Se ainda nao existir essa imagem com esse nome o programa nao sera executado corretamente.\nCaso voce decifre, o cifrada.png sera criado automaticamente\n\n')
    op2 = int(input('1:Cifrar\n2:Decifrar\n'))

    if op2 == 1:
        word = cv2.imread('cifra.png')
        print('ATENCAO: EM OP 0, OU SEJA, NO ARQUIVO, SOMENTE SAO ACEITOS NUMEROS INTEIROS SEPARADOS POR ESPACO')
        opk = int(input('Chave a ser usada:\n\n0:arquivo.txt\n1:Chave propria\n2:Chave aleatoria\n'))
    
    else:
        word = cv2.imread('cifrada.png')
        opk = int(input('Chave a ser usada:\n\n0:arquivo.txt\n1:Chave propria\n'))

    if opk == 0:
        chave = learq(1)

    elif opk == 1:
        chaveaux = input('Digite a chave, somente os 16 primeiros bytes da palavra serao considerados.\nCaso tenha menos a chave será completada, caso tenha mais ela será truncada.\n')
        chave = bytes(chaveaux, 'utf-8')

    elif opk == 2:
        chave = nonce()

    if op1 == 2 and op2 == 2:
        noncekey = learq(2)

    elif op1 == 2:
        noncekey = nonce()
        salva_hash(noncekey, 2)

    rodadas = int(input('Digite o numero de rodadas que voce deseja que sejam, feitas:\n'))

    trata_chave(chave)
    salva_hash(chave, 1)
    key_expansion(chave, rodadas)

    if op1 == 1:
        wordfinal = ECB(word,rodadas, op2)
        
    elif op1 == 2:
        wordfinal = CTR(word, rodadas, noncekey)
    
    print_img(word, wordfinal, op2) 
    print('\n\nForam criados na mesma pasta do programa 3 arquivos:\n1:Um Png, que eh o resultado do programa, o nome depende da escolha de cifrar ou decifrar')
    print('2:O arquivo chave.txt, a chave usada para as operacoes\n3:O arquivo nonce.txt, o nonce criado aleatoriamente pelo programa\n')
    print('Caso a opcao escolhida tenha sido ECB o arquivo nonce nao sera criado caso nao exista, e nao sera alterado caso ja existisse')
    print('Caso voce tenha criado uma imagem cifrada e queira decifrar ela na proxima iteracao,\nbasta escolher a opcao 0 de pegar do txt que ele automaticamente usara a chave anterior')
    print('Como nonce eh gerado aleatoriamente sempre, na decifracao ele automticamente pega nonce.txt e usa como nonce, nao existe opcao de digita-lo')


if __name__ == '__main__':
    main()
