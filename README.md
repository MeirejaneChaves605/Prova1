# Prova1   🚀 
A primeira avaliação do cueso de 	Desenvolvimento de Software com Formação BackEnd - Python com Django- Campus Riacho Fundo (1º ciclo)
ministrado pelo o professor Henrique Pereira consistem em:

Faça o exercício 2370 do Beecrowd, insira o código em um repositório local do Git e posteriormente envie para um repositório remoto no GitHub.
Para a avaliação desse exercício, deve ser enviado para o professor:

Print da tela de aceite do beecrowd;
Os prints dos repositórios locais e remoto com o código;
Link do repositório remoto com o código no GitHub;
Os prints de todo o passo a passo para inserir o código no repositório local e no remoto (todos os comandos git utilizados).
Obs: Colocar tudo em uma pasta, compactar e enviar para a avaliação.

O código para a primeira avaliação foi retirado e resolvido pela a plataforma do Beecrowd e o exercício pede o seguinte:

beecrowd | 2370
Times
Por OBI - Olimpíada Brasileira de Informática 2010 BR Brazil

Timelimit: 1
As aulas de educação física, em muitas escolas, acontecem da seguinte maneira: O professor entrega uma bola ao alunos (geralmente de futebol) e estes se dividem em times, onde jogam partidas alternadamente.

A maneira como os times são escolhidos também é semelhante em todas as escolas: decide-se quantos times serão formados, e uma pessoa para montar cada um dos times. Cada pessoa vai escolher, alternadamente, um dos alunos restantes para fazer parte de sua equipe. Como todos querem ter uma boa equipe, a pessoa que vai escolher o próximo membro do time escolhe aquele, dentre os ainda disponíveis, que possui o melhor nível de habilidade. Assim, os times acabam ficando relativamente equilibrados na soma do nível de habilidade dos jogadores.

Dada uma lista de alunos que serão escolhidos e seus respectivos níveis de habilidade para os times e a quantidade de times que serão formados, mostre como ficarão os times ao final do processo de montagem dos mesmos.

Entrada
A primeira linha da entrada contém dois inteiros N (2 ≤ N ≤ 10.000) e T (2 ≤ T ≤ 1000), representando respectivamente a quantidade de alunos e o número de times a serem formados, sendo T ≤ N. As N linhas seguintes descrevem, cada uma, um aluno disponível para escolha de times. Cada uma dessas linhas possui o nome do aluno (composto apenas por letras minúsculas) e um inteiro H (0 ≤ H ≤ 1.000.000) descrevendo seu nível de habilidade).

Não existem dois alunos com o mesmo nível de habilidade, e todos eles possuem nomes diferentes. é possível que alguns times acabem ficando com menos jogadores do que os outros.

Saída
Seu programa deve imprimir a lista de times que será formada ao final do processo de seleção. Para cada time, você deverá mostrar o termo "Time N", onde N é o número do time (1 para o primero, 2 para o segundo, e assim por diante) seguido de K linhas, onde K é a quantidade de jogadores do time, mostrando o nome de cada um dos jogadores do time, em ordem alfabética. Imprima uma linha em branco após cada descrição de time (inclusive do último).

Os times serão escolhidos pelo computador, então não é necessário considerar o aluno que irá fazer a escolha dos times.


#  Com exemplos de Entrada e exemplos de Saída que saão as seguintes:

Exemplos de Entrada	Exemplos de Saída
14 3

felipe 4

alvaro 8

thiago 1

rodrigo 3

robson 2

fabio 9

ricardo 11

rodolfo 0

andre 14

arthur 12

ronaldo 55

rogerio 30

lucas 7

rafael 17

Time 1

andre

fabio

felipe

ronaldo

thiago


Time 2

alvaro

arthur

rodolfo

rodrigo

rogerio


Time 3

lucas

rafael

ricardo

robson


4 3

john 3

richard 0

greg 100

rupert 20

Time 1

greg

richard


Time 2

rupert


Time 3

john 



