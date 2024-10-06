# METODOS DE STRINGS EM PYTHON

Esses métodos ajudam na modificação de textos de forma simplificada.

## Como utilizar

Para utilizar estas funções bastaseguir este exemplo:

```python
# Todos esses métodos seguem este padrão:
# string.[método]()
# Exemplos:
# Usando uma variável
name = "Daniel"
name.lower()
# Usando um texto
"Daniel".lower()
# Ambos retornam o mesmo valor: 'daniel'
```

> [!NOTE]
> Todas essas métodos retornam um novo valor, não alterando a string original.
> Exemplo, se quisessemos colocar o texto de uma string para letras minúsculas seria necessário fazer isto:
>
>```python
>name = "DANIEL"
>name = name.casefold()
># name agora é igual a 'daniel' 
>```

## capitalize

Transforma a primeira letra em maiuscula:

```python
>>> text = "ola mundo"
>>> text.capitalize()
'Ola mundo'
```

## casefold, lower, upper

Coloca o texto em letras minúsculas (casefold e lower) ou maiusculas (upper):

```python
>>> # casefold
>>> text = "OLA MUNDO"
>>> text.casefold()
'ola mundo'
>>> # lower
>>> text = "OLA MUNDO"
>>> text.lower()
'ola mundo'
>>> # upper
>>> text = "ola mundo"
>>> text.upper()
'OLA MUNDO'
```

> [!TIP]
> Diferença entre casefold e lower:
> o método `casefold()` é projetado para lidar com comparações de strings de maneira mais robusta, especialmente para idiomas com diferenças linguísticas. Ele é recomendado para casos onde você precisa de comparações de strings sem se preocupar com distinções de maiúsculas/minúsculas. Já o método `lower()` simplesmente converte caracteres para suas equivalentes minúsculas, mas pode não lidar corretamente com todos os caracteres de idiomas que têm regras especiais para conversão.
> Exemplo: no idioma alemão, existe o caractere especial ß, que em minúsculas representa "ss". O método casefold() converte ß para "ss", enquanto lower() não faz essa conversão.
>
>```python
>>>> text = "Straße"  # "Straße" significa "rua" em alemão
>>>> text.lower()
>'straße'
>>>> text.casefold()
>'strasse'
>```

## count

Conta vezes um valor (pode ser uma palavra ou letra) apareceu em uma string:

```python
>>> # Sintaxe: string.count(valor, começo, fim)
>>> text = "Eletromagnetismo, na física, é uma interação que ocorre entre partículas com carga elétrica por meio de campos eletromagnéticos. A força eletromagnética é uma das quatro forças fundamentais da natureza. É a força dominante nas interações de átomos e moléculas."
>>> text.count("força")
3
>>> # Contando as ocorrências a partir da posição 200
>>> text.count('força', 200)
1
```

## endswith, startswith

Esses métodos verificam se uma string termina ou começa com determinado valor, respectivamente:

```python
>>> # endswith
>>> text = "Olá mundo"
>>> text.endswith("mundo")
True
>>> # startswith
>>> text = "Olá mundo"
>>> text.startswith("Olá")
True
>>> text.startswith("Oi")
False
```

## expandtabs

Define o valor das tabulaçoes (`\t`) dentro de uma string:

> [!NOTE]
> Nesse sentido, tabulaçoes significam a quantidade de espaços.

```python
>>> text = "Nome\tIdade\tCidade"
>>> text.expandtabs(4)
'Nome    Idade   Cidade'
>>> text.expandtabs(2)
'Nome  Idade Cidade'
>>> text.expandtabs(1)
'Nome Idade Cidade'
>>> text.expandtabs(0)
'NomeIdadeCidade'
```

## find

Busca um valor especificado dentro de uma string e retorna a posição da sua primeira ocorrência:

```python
>>> # Sintaxe: string.find(valor, começo, fim)
>>> txt = "Hello, welcome to my world."
>>> txt.find("e")
1
>>> txt.find("e", 10)
13
>>> txt.find("e", 5, 10)
8
```

## format

Formata uma string inserindo valores em `placeholders` (marcadores de posição):

```python
>>> # Sintaxe: string.format(valor1, valor2, ..., valorn)
>>> # Passando o nome da posição:
>>> "Meu nome é {nome}, eu tenho {idade} anos".format(nome = "Daniel", idade = 20)
'Meu nome é Daniel, eu tenho 20 anos'
>>> # Passando o índice da posição:
>>> "Meu nome é {0}, eu tenho {1} anos".format("Daniel", 20)
'Meu nome é Daniel, eu tenho 20 anos'
>>> # Não passando valores:
>>> "Meu nome é {}, eu tenho {} anos".format("Daniel", 20)
'Meu nome é Daniel, eu tenho 20 anos'
```

## isalnum, isalpha e isdigit

Cada um desses métodos verifica se todos os caracteres da string são alfanuméricos (letras e números), se todos os caracteres da string são letras e se todos os caracteres da string são dígitos, respectivamente:

```python
Copiar código
>>> # Verificando se todos são alfanumericos:
>>> text = "Python123"
>>> text.isalnum()
True
>>> # Verificando se todos são letras:
>>> text = "Python"
>>> text.isalpha()
True
>>> # Verificando se todos são numeros:
>>> text = "12345"
>>> text.isdigit()
True
```

## join

Junta os itens de um `iteravel` (um iterável pode ser uma lista, um dicionário, uma tupla e etc.) usando um separador específicado:

```python
>>> # Sintaxe: string.join(iterável)
>>> # Usando lista como iterável:
>>> nomes = ['Daniel', 'Samuel', 'Henrique', 'Hugo']
>>> ' '.join(nomes)
'Daniel Samuel Henrique Hugo'
>>> ', '.join(nomes)
'Daniel, Samuel, Henrique, Hugo'
>>> '|'.join(nomes)
'Daniel|Samuel|Henrique|Hugo'
>>> '#'.join(nomes)
'Daniel#Samuel#Henrique#Hugo'
>>> # Usando dicionário como iterável:
>>> pessoas = {'daniel':20, 'diogo':30, 'jailson':18}
>>> ' '.join(pessoas)
'daniel diogo jailson'
>>> ', '.join(pessoas)
'daniel, diogo, jailson'
>>> '|'.join(pessoas)
'daniel|diogo|jailson'
```

## replace

Substitui um valor especificado por outro em uma string:

```python
>>> # Sintaxe: string.replace(valor_original, novo_valor, num)
>>> # Sendo o num a quantidade de ocorrências, o padrão são todas as ocorrências
>>> text = "Olá mundo"
>>> text.replace("mundo", "Python")
'Olá Python'
>>> # Usando o num:
>>> "one one was a race horse, two two was one too.".replace("one", "three", 2)
'three three was a race horse, two two was one too.'
>>> # Sem o num:
>>> "one one was a race horse, two two was one too.".replace("one", "three")
'three three was a race horse, two two was three too.'
```

## split e rsplit

Divide a string em uma lista a partir de um separador específicado:

```python
>>> # Sintaxe: string.split(separador, num_max_de_items) 
>>> text = "Olá, meu nome é Rodrigo, tenho 30 anos e curso redes de computadores"
>>> text.split()
['Olá,', 'meu', 'nome', 'é', 'Rodrigo,', 'tenho', '30', 'anos', 'e', 'curso', 'redes', 'de', 'computadores']
>>> # Passando o separador
>>> text.split(', ')
['Olá', 'meu nome é Rodrigo', 'tenho 30 anos e curso redes de computadores']
>>> # Passando o número max de itens
>>> text.split(' ', 3)
['Olá,', 'meu', 'nome', 'é Rodrigo, tenho 30 anos e curso redes de computadores']
```

> [!NOTE]
> Perceba que a lista possuirá uma quantidade uma unidade maior que a variável `num_max_de_items`
>
> ```python
> >>> len(text.split(' ', 3))
> 4
> ```

Usando um dos exepmlos anteriores:

```python
>>> nomes = 'Daniel#Samuel#Henrique#Hugo'.split('#')
['Daniel', 'Samuel', 'Henrique', 'Hugo']
>>> nomes = ', '.join(nomes)
'Daniel, Samuel, Henrique, Hugo'
```

> [!TIP]
> Além do método split existe o método rsplit, a diferença entre eles é que o método split lê da esquerda para a direita, já o método rsplit lê da direita para a esquerda.

## stripe, rstripe e lstripe

## zfill
