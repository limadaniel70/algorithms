# LISTAS EM PYTHON

## SUMÁRIO

1. [Introdução](#introdução)
2. [Acessando itens](#acessando-os-itens-de-uma-lista)
3. [Manipulando listas](#manipulando-listas)
	1. [Atualizando itens](#atualizando-valor)
	2. [Inserindo itens](#inserindo-itens)
	3. [Removendo itens](#removendo-itens)

## INTRODUÇÃO

As listas são uma coleção de items. Enquanto uma variável pode ter um único valor uma lista pode suportar vários. Ex.:

```python
# Uma string só pode suportar um nome
nome: str = "Daniel"
# Uma lista suporta vários
nomes: list[str] = ["Daniel", "Samuel", "Antonino"]
```

Além de strings, as listas também podem armazenar outros tipos de dados:

```python
# Inteiros
numeros_da_mega_sena: list[int] = [1, 12, 33, 41, 53, 56]
# Racionais
imcs: list[float] = [16.5, 28.89, 35.67]
# Boleanos
tabela_verdade: list[bool] = [True, False, True, False]
```

## ACESSANDO OS ITENS DE UMA LISTA

Para acessar os itens de uma lista precisamos dizer qual a sua posição.

```python
>>> nomes: list[str] = ["Daniel", "Samuel", "Antonino"]
>>> print(nomes[0])
Daniel
>>> print(nomes[1])
Samuel
>>> print(nomes[2])
Antonino
```

> [!NOTE]
> Perceba que a posição do primeiro item não é 1, mas sim 0.

> [!TIP]
> Outro ponto importante é que se o número do índice for negativo ele começara pelo final da lista:
>
>```python
>>>> nomes: list[str] = ["Daniel", "Samuel", "Antonino"]
>>>> print(nomes[-1])
>Antonino
>>>> print(nomes[-2])
>Samuel
>>>> print(nomes[-3])
>Daniel
> ```

Além disso, também é possível acessar um intervalo de itens de uma lista. Exemplo:

```python
>>> frutas: list[str] = ["banana", "morango", "uva", "goiaba", "caju", "abacaxi"]
>>> frutas[2:4]
['uva', 'goiaba']
>>> frutas[1:5]
['morango', 'uva', 'goiaba', 'caju']
```

O exemplo anterior escreve na tela os itens que começam no índice 1 (segunda posição) ao índice 5 (sexta posição).

> [!TIP]
> Também é possível fazer isso usando índices negativos:
>
> ```python
>>>> frutas: list[str] = ["banana", "morango", "uva", "goiaba", "caju", "abacaxi"]
>>>> frutas[-4:-1]
>['uva', 'goiaba', 'caju']
>```
>
> Perceba que ela começa pelo índice 4 (quinta posição) e para antes do índice 1 (segunda posição).

Além disso, é possível verificar se uma lista possuí determinado item:

```python
frutas: list[str] = ["banana", "morango", "uva", "goiaba", "caju", "abacaxi"]

if "banana" in frutas:
	print("Tem banana!")
else:
	print("Não tem banana!")

---

>>> if "banana" in frutas:
...     print("Tem banana!")
... else:
...     print("Não tem banana!")
... 
Tem banana!
```

## MANIPULANDO LISTAS

### Atualizando valor:

```python
>>> nomes: list[str] = ["Daniel", "Samuel", "Antonino"]
>>> print(nomes[0])
Daniel
>>> # Basta colocar qual a posição do item que deve ser alterada
>>> # e difinir outro valor para ele
>>> nomes[0] = "Diego"
>>> print(nomes[0])
Diego
>>> print(nomes)
["Diego", "Samuel", "Antonino"]
```

### Inserindo Itens

Estes são alguns métodos para inserir novos itens em uma lista:

```python
>>> nomes: list[str] = ["Daniel", "Samuel", "Antonino"]
>>> # Adiciona ao final da lista
>>> nomes.append("Diego")
>>> print(nomes)
["Daniel", "Samuel", "Antonino", "Diego"]
>>> # Insere em uma posição especifica
>>> nomes.insert(1, "Clara")
>>> print(nomes)
["Daniel", "Clara", "Samuel", "Antonino", "Diego"]
>>> outros_nome: list[str] = ["Marcel", "Aldair", "Leonardo"]
>>> # Adiciona os itens de outra lista no final
>>> nomes.extend(outros_nomes)
>>> nomes
["Daniel", "Clara", "Samuel", "Antonino", "Diego", "Marcel", "Aldair", "Leonardo"]
```

### Removendo Itens

Estes são alguns métodos para remover itens em uma lista:

```python
>>> frutas: list[str] = ["morango", "goiaba", "uva", "abacaxi", "caju"]
>>> # Remove um item de acordo com seu valor
>>> frutas.remove("morango")
>>> frutas
["goiaba", "uva", "abacaxi", "caju"]
>>> # Remove o ultimo item
>>> frutas.pop()
>>> frutas
["goiaba", "uva", "abacaxi"]
>>> # Remove todo os itens da lista
>>> frutas.clear()
>>> frutas
[]
```

> [!TIP]
> É possível passar um índice para o método ``.pop()``:
> ```python
> >>> frutas: list[str] = ["morango", "goiaba", "uva", "abacaxi", "caju"]
> >>> frutas.pop(1)
> >>> frutas
> ["morango", "uva", "abacaxi", "caju"]
> ```

> [!WARNING]
> Nos métodos em que é possível passar um índice ou um item, caso este índice ou item não exista um erro será gerado. Exemplo: 
>
> ```python
>>>> frutas: list[str] = ["morango", "goiaba", "uva", "abacaxi", "caju"]
>>>> frutas.pop(8)
>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>  IndexError: pop index out of range
>```  

### Outros métodos

```python
>>> frutas: list[str] = ["laranja", "kiwi", "banana", "pera", "kiwi", "abacaxi", "kiwi"]
>>> # Conta quantas vezes um elemento apareceu
>>> frutas.count("kiwi")
3
>>> frutas.count("tangerina")
0
>>> frutas.count("abacaxi")
1
>>> # Encontra qual o índice de um item
>>> frutas.index("kiwi")
1
>>> # Encontra o índice de um item a partir de
>>> # determinada posição
>>> frutas.index("kiwi", 2)
4
>>> # Inverte a ordem dos itens
>>> frutas.reverse()
>>> frutas
['kiwi', 'abacaxi', 'kiwi', 'pera', 'banana', 'kiwi', 'laranja']
>>> # Organiza a lista
>>> frutas.sort()
>>> frutas
['abacaxi', 'banana', 'kiwi', 'kiwi', 'kiwi', 'laranja', 'pera']
```
