# Counting Words - Voxy - Guilherme Gibosky

### Requisitos

Necessário ter Docker instalado
Node versão 18 ou superior


### Executar
Executar o backend: ```docker-compose up --build backend```
Navegar para a pasta angular-material-forms e executar o comando: ```npm start```


## Introdução

Foi gerado uma aplicação em Angular com backend em FastApi em um ambiente dockerizado

O problema a ser resolvido era fazer um contador de palavras que tem uma interface com o usuário.

## Metodologia

### Premissas adotadas

- Tudo que não é um espaço é considerado como palavra
- Está sendo apresentado dosi tipos de estratégias:
    - Regex: Foi usado regex para indetificar as palavras e com o um match all, gerar um array com as palavras e através dele, contar
    - String split: Usando o método comum a praticamente todas as linguagens de programação que "parte" uma *string* a partir de um texto base
- Foi implementada ambas no front-end quanto no back-end
- Não foi feita uma solução própria pois foi avaliado que a eficiência não seria superior so metodos citados e introduziria uma complexidade desnecessária mas estou ciente que seria uma solução customizavel e isso tem suas vantagens (Não existe bala de prata!!!)

## Desafios e Melhorias

### Desafios

- Criar um ambiente angular em docker, na nova versão foi um desafio pois não existe um documentação extensa e muitos dos problemas envolvem npm que é notóriamente problematico e pesado
- A solução da split não é "perfeita", pois em uma string somente com espaços, dá um falso positivo, apontando uma contagem.
- Trabalhar com FastApi que é uma ferramenta que estou estudando e aprendendo, de modo que alguns erros desconhecidos tomaram um certo tempo.

### Melhorias

- Criar um profile de eficiência de tempo de processamento de cada solução
- Pensar uma maneira de fazer com o split tenho um comportamento mais próximo da perfeição
- Conseguir usar regex para desconsiderar coisas como proposições e outros componentes do alfabeto.
- Dockerizar o angular