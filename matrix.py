def diagonalOrder(matrix, row, col):
    final = []
    for line in range(1, (row + col)):
        start_col = max(0, line - row)
        count = min(line, (col - start_col), row)
        for j in range(0, count):
            final.append(matrix[min(row, line) - j - 1][start_col + j])
    return final
 
 
def sort(row=4, col=4):
    incrementar = 0
    start = 1
    end = col
    lista = []
    for row in range(start, (row + 1)):
        lista.append(list(range(start, (end + 1))))
        incrementar += 1
        start = col * incrementar + 1
        end = end + col
    return diagonalOrder(lista, row, col)
 
 
# la lista a ordenar; las dimensiones
def sort_list(og_list, row, col):
    order = sort(row, col)
    return [og_list[i - 1] for i in order]

def linear_to_counterdiagonal_sort(lista):
    n = len(lista) ** 0.5
    if not n == round(n):
        return 'given list does not conform a square'
    else:
        sorted_list = []
        sorted_list[0: n ** 2] = None
        for i in range(len(lista)):
            two_d_row, two_d_col = i // n, i % n 
        return 
           
testlist = [i for i in range(25)]

print(linear_to_counterdiagonal_sort(testlist))
