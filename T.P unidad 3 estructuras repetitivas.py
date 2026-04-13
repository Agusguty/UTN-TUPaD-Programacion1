#Ejercicio 1: Caja de un Kiosco
nombre_cliente = input("Ingrese el nombre del cliente: ")
while not nombre_cliente.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacio.")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
cantidad_producto = input("Ingrese la cantidad de productos: ")
while not cantidad_producto.isdigit() or int(cantidad_producto) <= 0:
    print("Error: Ingrese un numero entero mayor a 0.")
    cantidad_producto = input("Ingrese la cantidad de productos: ")
cantidad = int(cantidad_producto)
total_con_descuento = 0
total_sin_descuento = 0
for i in range(1, cantidad + 1):
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: El precio debe ser un numero entero.")
        precio_str=input(f"Producto {i} - Precio: ")
    precio = int(precio_str)
    total_sin_descuento += precio
    tiene_descuento = input("Descuento (S/N): ").lower()
    while tiene_descuento not in ["s","n"] or tiene_descuento == "":
        print("Error: Ingrese ‘S’ para si o ‘N’ para no.")
        tiene_descuento = input ("Descuento (S/N): ").lower()
    if tiene_descuento == "s":
        precio_final = precio*0.90
    else:
        precio_final = precio
    total_con_descuento += precio_final
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad
print("-" * 30)
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por descuento: ${promedio:.2f}")

#Ejercicio 2
usuario = "Alumno"
clave = "python123"
intentos_maximos = 3
intentos_realizados = 0
ingreso_exitoso = False
while intentos_realizados < intentos_maximos:
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")
    if usuario_ingresado == usuario and clave_ingresada == clave:
        print("¡Acceso consedido!")
        ingreso_exitoso = True
        break
    else:
        intentos_realizados += 1
        print(f"Error. Intentos resatantes: {intentos_maximos - intentos_realizados}")
if not ingreso_exitoso:
    print("Cuenta bloqueada.")
else:
    opcion =""
    while opcion != "4":
        print("\n---MENU DEL CAMPUS---")
        print("1. Ver estado de insccripcion")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")
        opcion = input("Elija una opcion: ")
        if not opcion.isdigit() or not ("1"<=opcion <= "4"):
            print("Error: Ingrese un numero entre 1 y 4. ")
            continue
        if opcion == "1":
            print("Estado: Inscripto")
        elif opcion == "2":
            nueva_clave = input("Nueva clave (minimo 6 caracteres): ")
            if len(nueva_clave) < 6:
                print("Eror: Clave demaciado corta.")
            else:
                confirmacion = input("Confirme su nueva clave: ")
                if nueva_clave == confirmacion:
                    clave = nueva_clave
                    print("Clave cambiada con exito.")
                else:
                    print("Error: Las claves no coinciden")
        elif opcion == "3":
            print("Frase del dia: El exito y los logros se consiguen trabajando todos los dias un poco.")
        elif opcion == "4":
            print("Saliendo del sistema...")


#Ejercicio 3
l1 = ""
l2 = ""
l3 = ""
l4 = ""
m1 = ""
m2 = ""
m3 = ""
operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Error. Ingrese nombre (solo letras): ")
opcion = ""
while opcion != "5":
    print(f"\n--- Agenda de {operador}---")
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del dia\n4. Ver resumen\n5. Cerrar")
    opcion = input("Opcion: ")
    if opcion == "1":
        #RESERVAR
        dia = input("Dia (1=Lunes, 2=Martes: )")
        if dia == "1" or dia == "2":
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                paciente = input("Error (solo letras): ")
            if dia == "1":
                if paciente == l1 or paciente == l2 or paciente == l3 or paciente == l4:
                    print("Error: El paciente ya tiene un turno este dia.")
                elif l1 == "": l1 = paciente 
                elif l2 == "": l2 = paciente
                elif l3 == "": l3 = paciente
                elif l4 == "": l4 = paciente
                else: print("Lunes sin cupos.")
            else:
                if paciente == m1 or paciente == m2 or paciente == m3:
                    print("Error: Paciente repetido. ")
                elif m1 == "": m1 = paciente
                elif m2 == "": m2 = paciente
                elif m3 == "": m3 = paciente
                else: print("Martes sin cupos.")
    elif opcion == "2":
        #CANCELAR
        dia = input("Dia (1=Lunes, 2=Martes): ")
        baja =input("Nombre del paciente a cancelar: ")
        if dia == "1":
            if l1 == baja: l1 = ""
            elif l2 == baja: l2 = ""
            elif l3 == baja: l3 = ""
            elif l4 == baja: l4 = ""
            else: print("No se encontro al paciente.")
        elif dia == "2":
            if m1 == baja: m1 = ""
            elif m2 == baja: m2 = ""
            elif m3 == baja: m3 = ""
            else: print("No se encontro.")
    elif opcion == "3":
        #VER AGENDA 
        dia = input("Dia a ver (1 o 2): ")
        if dia == "1":
            print(f"1. {l1 if l1 !='' else '(libre)'}")
            print(f"2. {l2 if l2 !='' else '(libre)'}")
            print(f"3. {l3 if l3 !='' else '(libre)'}")
            print(f"4. {l4 if l4 !='' else '(libre)'}")
        elif dia == "2":
            print(f"1. {m1 if m1 != '' else '(libre)'}")
            print(f"2. {m2 if m2 != '' else '(libre)'}")
            print(f"3. {m3 if m3 != '' else '(libre)'}")
    elif opcion == "4":
        #RESUMEN
        ocupados_l = (1 if l1 !="" else 0) + (1 if l2 !="" else 0) + (1 if l3 !="" else 0) +(1 if l4 !="" else 0)
        ocupadso_m = (1 if m1 !="" else 0) + (1 if m2 !="" else 0) + (1 if m2 !="" else 0)
        print(f"Lunes: {ocupados_l} ocupados, {4-ocupados_l} libres.")
        print(f"Martes: {ocupadso_m} ocupados, {3-ocupadso_m} libres.")
        if ocupados_l > ocupadso_m: print("Dia con mas turnos: Lunes")
        elif ocupadso_m > ocupados_l: print("Dia con mas turnos: Martes")
        else: print("Empate en cantidad de turnos.")


#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0  

nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Error. Use solo letras: ")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == True and tiempo <= 3:
        print("¡SISTEMA BLOQUEADO POR ALARMA!")
        break
    print(f"\n--- ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} ---")
    print(f"Alarma: {'ON' if alarma else 'OFF'} | Progreso Código: {codigo_parcial}")
    print("1. Forzar cerradura\n2. Hackear panel\n3. Descansar")
    opcion = input("Acción: ")
    if not opcion.isdigit(): continue
    if opcion == "1":
        #Accion: FORZAR
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1
        if forzar_seguidos >= 3:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
        else:
            if energia < 40:
                print("Riesgo de alarma...")
                riesgo = input("Elija número 1-3: ")
                if riesgo == "3": alarma = True
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Abriste una cerradura!")
    elif opcion == "2":
        #Accion: HACKEAR
        energia -= 10
        tiempo -= 3
        forzar_seguidos = 0 
        for i in range(1, 5):
            letra = input(f"Paso {i} - Ingrese letra para el código: ")
            codigo_parcial += letra
            print(f"Progreso: {codigo_parcial}")
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("¡Panel hackeado! Cerradura abierta.")
        elif opcion == "3":
            #Accion: DESCANSAR
            forzar_seguidos = 0
        tiempo -= 1
        recuperacion = 15
        if alarma: recuperacion -= 10
        energia += recuperacion
        if energia > 100: energia = 100
        print(f"Descansaste. Energía actual: {energia}")
        if cerraduras_abiertas == 3:
            print("--- ¡VICTORIA! La bóveda se ha abierto ---")
else:
    print("--- DERROTA: Te has quedado sin recursos o el sistema se bloqueó ---")


#Ejercicio 5
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")
hp_gladiador = 100
hp_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
juego_activo = True

print("=== INICIO DEL COMBATE ===")
while hp_gladiador > 0 and hp_enemigo > 0:
    print(f"\n{nombre} (HP: {hp_gladiador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = input("Elige acción: ")
    
    while not opcion.isdigit() or not ("1" <= opcion <= "3"):
        print("Error: Ingrese un número válido.")
        opcion = input("Elige acción: ")
    if opcion == "1":
        # Ataque Pesado con "Golpe Crítico" 
        if hp_enemigo < 20:
            danio_final = danio_pesado * 1.5 
            print("¡Golpe Crítico!")
        else:
            danio_final = danio_pesado
        
        hp_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")
    elif opcion == "2":
        # Ráfaga Veloz 
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            hp_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
    elif opcion == "3":
        # Curar (Manejo de Pociones)
        if pociones > 0:
            hp_gladiador += 30
            pociones -= 1
            print(f">> Usaste una poción. HP actual: {hp_gladiador}")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
    # --- Turno del Enemigo (Si sigue vivo) ---
    if hp_enemigo > 0:
        hp_gladiador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos!")
if hp_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")


