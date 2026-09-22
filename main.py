def validar_codigo(codigo):
    if codigo == "":
        return False

    if len(codigo) < 8:
        return False

    return True


def validar_tipo_consulta(tipo_consulta):
    if tipo_consulta == "matricula":
        return True

    if tipo_consulta == "pagos":
        return True

    if tipo_consulta == "constancia":
        return True

    if tipo_consulta == "plataforma":
        return True

    if tipo_consulta == "otro":
        return True

    return False


def registrar_solicitud():
    print("\n--- REGISTRO DE SOLICITUD ---")

    codigo = input("Ingrese código del estudiante: ")

    while not validar_codigo(codigo):
        print("Código inválido. Debe tener al menos 8 caracteres.")
        codigo = input("Ingrese código del estudiante: ")

    nombre = input("Ingrese nombre del estudiante: ")

    tipo_consulta = input(
        "Ingrese tipo de consulta (matricula, pagos, constancia, plataforma u otro): "
    ).lower()

    while not validar_tipo_consulta(tipo_consulta):
        print("Tipo de consulta inválido.")
        tipo_consulta = input(
            "Ingrese tipo de consulta (matricula, pagos, constancia, plataforma u otro): "
        ).lower()

    descripcion = input("Ingrese una descripción breve: ")

    print("\n--- SOLICITUD REGISTRADA ---")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Tipo de consulta:", tipo_consulta)
    print("Descripción:", descripcion)


registrar_solicitud()