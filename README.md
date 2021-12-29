# AES_Seguran-a_Computacional
Trabalho de Segurança computacional do semestre 2021/1 da Universidade de Brasilia

Foi necessário instalar o opencv para pegar a imagem.  Versao do compilador: Python 3.9
Se o programa não fechar ao fechar a imagem, basta apertar 0.

Por padrão quando a função de descriptografar é escolhida o programa pega a "imagem cifrada.png", que é criada automaticamente quando uma cifração é feita.

Na escolha de chave pode-se escolher pegar do txt, que deve estar nomeado como "chave.txt", caso a chave seja aleatória, o próprio programa cria esse txt, 
e caso seja rodado qualquer outro teste com esse txt na pasta ele será sobrescrito.

O nosso nonce sempre é gerado aleatoriamente, e salvo no txt "nonce.txt" para a futura decifração.

Obs.: no txt todos os números precisam necessariamente estarem separados por espaço, no txt caracteres não funcionam, e o último número deve ter um espaço 
logo após ser escrito também, pois no nosso código os números são colocados no vetor assim que um espaço é achado na variável que recebeu o txt.
