minas = [
    "-*-*-",
    "--*--",
    "----*",
    "*----",
]
minas = [list(col) for col in minas]


# Hace un check de '*' y bordes
def set_number(rowI, colI):
    cant = 0
    # LEFT CHECK
    if colI != 0:
        if (rowI != 0) and (minas[rowI - 1][colI - 1] == "*"):
            cant = cant + 1
        if minas[rowI][colI - 1] == "*":
            cant = cant + 1
        if (rowI != 3) and (minas[rowI + 1][colI - 1]) == "*":
            cant = cant + 1

    # RIGHT CHECK
    if colI != 4:
        if (rowI != 0) and (minas[rowI - 1][colI + 1] == "*"):
            cant = cant + 1
        if minas[rowI][colI + 1] == "*":
            cant = cant + 1
        if (rowI != 3) and (minas[rowI + 1][colI + 1]) == "*":
            cant = cant + 1

    # BOTTOM
    if (rowI != 0) and (minas[rowI - 1][colI] == "*"):
        cant = cant + 1

    # TOP
    if (rowI != 3) and (minas[rowI + 1][colI] == "*"):
        cant = cant + 1

    return cant


for row in range(len(minas)):
    for col in range(len(minas[row])):
        if minas[row][col] != "*":
            minas[row][col] = set_number(row, col)
    "".join(str(mina) for mina in minas[row])

for mina in minas:
    print(mina)