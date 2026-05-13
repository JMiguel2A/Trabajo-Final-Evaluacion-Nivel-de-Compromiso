# Juan Miguel Agudelo
# 13/05/2026
# Fundamentos de Programacion trabajo final

sesiones_iniciadas = [
    ["C001", 132, 12],
    ["C002", 5, 2],
    ["C003", 120, 5],
    ["C004", 300, 42],
    ["C005", 80, 4]
]

# Este bloque de codigo es la matriz de las sesiones iniciadas por los usuarios
# Cada fila representa un usuario y cada columna una  caracteristica
# La primera posicion es el ID
# La segunda es el tiempo de uso en segundos
# La tercera es el numero de clicks realizados

def clasificar_el_compromiso(tiempo_uso, numero_clicks):

    if tiempo_uso > 180 and numero_clicks > 8:
        return "Compromiso_Alto"

    elif tiempo_uso < 60 or numero_clicks < 3:
        return "Compromiso_Bajo"

    else:
        return "Compromiso_Medio"
    
# Este bloque de codigo clasifica el nivel de compromiso del usuario
# La calificacion depende del tiempo de uso y el numero de clicks realizados por el usuario

for sesion in sesiones_iniciadas:

    id_usuario = sesion[0]
    tiempo_uso = sesion[1]
    numero_clicks = sesion[2]

    clasificacion = clasificar_el_compromiso(tiempo_uso, numero_clicks)

    print(f"ID del usuario: {id_usuario}")
    print(f"Clasificacion del compromiso: {clasificacion}")
    print("-----------------------------")
    
#Este bloque de codigo revisa cada sesion iniciada
#Obtiene el ID del usuario, el tiempo de uso y el numero de clicks
#Ya con esto y la regla  de clasifiacion que hay dice su ID y su nivdel de compromiso
