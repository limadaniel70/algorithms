# EXERCÍCIOS SOBRE LISTAS

## 1. Um programa que soma todos os itens de uma lista

```python
total = 0
for numero in reference_list:
    total += numero
print(total)
```

## 2. Um programa que encontra o maior item dentro de uma lista de números

```python
reference = reference_list[0]
for numero in reference_list:
    if numero > reference:
        reference = numero
print(reference)
```

## 3. Um programa que checa se uma lista está vazia

Esse pode ser feito de três formas:

Forma 1:

```python
if len(reference_list) == 0:
    print("Vazia")
else:
    print("Possui itens")
```

Forma 2:

```python
if not reference_list:
    print("Vazia")
else:
    print("Possui itens")
```

Forma 3:
```python
if reference_list == []:
    print("Vazia")
else:
    print("Possui itens")
```

## 4. Um programa que verificia se todos os números de uma lista são pares

```python
par: bool = True
for numero in reference_list:
    if numero % 2 == 0:
        continue
    else:
        par = False
        break
print(f"Par: {par}")
```
