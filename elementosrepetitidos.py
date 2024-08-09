def buscarepeticao(lista):
    nvlista = []
    a = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
                if lista[i] == lista[j]:
                            for y in nvlista:
                                  if y == lista[i]:
                                        a = 1
                            if a == 0:
                                nvlista.append(lista[i])
                            a = 0
    return nvlista
lista = [1,1,1,2,1]
print(buscarepeticao(lista))