


def crear(MAX_HORIZONTAL, MAX_VERTICAL, texto):

    tmñ = len (texto)
    spc_vacio= (MAX_HORIZONTAL-tmñ) // 2
    spc_drcha = " " * spc_vacio
    spc_izqrda = " " * spc_vacio


    HORIZONTAL= " " + "-" * MAX_HORIZONTAL
    espacios = "|" + " " * MAX_HORIZONTAL + "|"
    linea_texto = f"|{spc_izqrda}{texto}{spc_drcha}|"

    if (MAX_HORIZONTAL-tmñ) % 2 ==1:
        linea_texto = f"|{spc_izqrda}{texto}{spc_drcha} |"

    print(f"{HORIZONTAL}")
    for i in range(MAX_VERTICAL):
        if i == MAX_VERTICAL // 2:
            print(linea_texto)
        else:
            print(f"{espacios}")

    print(f"{HORIZONTAL}")

