
lista = [1,2,3,4,5,7]
chave = 4
def LocalLista(lista, chave):
    for i in lista:
        if lista[i] == chave:
            return i    
    return -1

def InverteLista(lista):
    tamanho = len(lista)

    for i in range( tamanho // 2 ):
        lista[i], lista[tamanho -1 -i] = lista[tamanho-1-i], lista[i]
    return lista

if __name__ == "__main__":
    posicao = LocalLista(lista, chave)
    print(posicao)
    inverte = InverteLista(lista)
    print(inverte)
