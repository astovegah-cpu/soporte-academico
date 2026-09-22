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


def asignar_prioridad(tipo_consulta):
    if tipo_consulta == "matricula":
        return "Alta"

    if tipo_consulta == "pagos":
        return "Alta"

    if tipo_consulta == "plataforma":
        return "Alta"

    return "Baja"


def validar_texto(texto):
    if texto == "":
        return False

    return True


def mostrar_menu():
    print("\n--- SOPORTE ACADÉMICO ---")
    print("1. Registrar solicitud")
    print("2. Salir")


def mostrar_resumen(codigo, nombre, tipo_consulta, descripcion, prioridad):
    print("\n--- RESUMEN DE LA SOLICITUD ---")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Tipo de consulta:", tipo_consulta)
    print("Descripción:", descripcion)
    print("Prioridad:", prioridad)


def registrar_solicitud():
    print("\n--- REGISTRO DE SOLICITUD ---")

    codigo = input("Ingrese código del estudiante: ")

    while not validar_codigo(codigo):
        print("Código inválido. Debe tener al menos 8 caracteres.")
        codigo = input("Ingrese código del estudiante: ")

    nombre = input("Ingrese nombre del estudiante: ")

    while not validar_texto(nombre):
        print("El nombre no puede estar vacío.")
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

    while not validar_texto(descripcion):
        print("La descripción no puede estar vacía.")
        descripcion = input("Ingrese una descripción breve: ")

    prioridad = asignar_prioridad(tipo_consulta)

    mostrar_resumen(
        codigo,
        nombre,
        tipo_consulta,
        descripcion,
        prioridad
    )


mostrar_menu()
registrar_solicitud()