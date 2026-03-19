def bubble(lst):
    lst_picks = []
    listaOrdenada = False
    while listaOrdenada == False:
        for i in range (0, len(lst) -1):
            if lst[i] > lst[i+1]:
                numMenor = lst[i+1]
                lst[i+1 ] = lst[i]
                lst[i] = numMenor
                lst_picks.append(lst)
            else:
                listaOrdenada = True
    return lst_picks

prueba = [3,2,1, 5, 6]
print(bubble(prueba))