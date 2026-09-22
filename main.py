def registrar_solicitud():
    print("\n--- REGISTRO DE SOLICITUD ---")

    codigo = input("Ingrese código del estudiante: ")
    nombre = input("Ingrese nombre del estudiante: ")
    tipo_consulta = input("Ingrese tipo de consulta: ")
    descripcion = input("Ingrese una descripción breve: ")

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }

    return solicitud


solicitud = registrar_solicitud()

print("\n--- SOLICITUD REGISTRADA ---")
print("Código:", solicitud["codigo"])
print("Nombre:", solicitud["nombre"])
print("Tipo de consulta:", solicitud["tipo_consulta"])
print("Descripción:", solicitud["descripcion"])
