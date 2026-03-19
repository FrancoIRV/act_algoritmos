def bubble(lst):
    lst_picks = []
    loops = len(lst) -1
    while  loops > 1 :
        for i in range (loops):
            if lst[i] > lst[i+1]:
                numMenor = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = numMenor
                lst_picks.append(lst.copy())
        loops = loops -1
    return lst_picks

prueba = [3,2,1, 5, 6]
print(bubble(prueba))