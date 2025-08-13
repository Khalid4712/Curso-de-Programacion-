print("NAVE ESPACIAL PERDIDA\n")

nivel1 = input("Estas situado en el hangar de la nave y observas dos pasillos: uno completamente oscuro y otro con un poco de iluminacion.\nQuieres ir por el PASILLO OSCURO o el PASILLO ILUMINADO?\n").lower()

if nivel1 == "pasillo iluminado":
    print("\nVas por el pasillo iluminado y encuentras una puerta con un panel numerico a su derecha(al parecer debes introducir una contraseña).")
    nivel2 = input("Quieres INTENTAR abrir la puerta, VOLVER atras o INSPECCIONAR el pasillo un poco mas?").lower()

    if nivel2 == "intentar":
        print("\nIntentas abrir la puerta, pero necesitas un codigo. La puerta suelta un pitido y permanece cerrada.")
        nivel3 = input("Quieres PROBAR a introducir otro codigo o EXPLORAR el area en busca de pistas?").lower()

        if nivel3 == "probar":
            print("\nEl panel se bloquea debido a la cantidad de intentos fallidos. No puedes seguir por ahi.")
            print("Juego perdido")
        elif nivel3 == "explorar":
            print("\nEncuentras una nota con un numero: 7342. La ingresas en el panel numerico y...¡LO TIENES! La puerta se abre.")
            nivel4 = input("Dentro hay dos caminos: una ESCALERA hacia arriba y un ASCENSOR viejo, en mal estado.\nCual usaras? Se precavido...").lower()

            if nivel4 == "escalera":
                print("\nSubes con cuidado. Llegas a la cabina de mando.")
                nivel5 = input("Quieres ENVIAR una señal de auxilio o EXPLORAR el panel de control?").lower()

                if nivel5 == "enviar":
                    print("Logras enviar una señal de auxilio. Una nave espacial aliada viene a rescatarte. FIN DEL JUEGO")
                elif nivel5 == "explorar":
                    print("Encuentras que el sistema esta dañado. Pierdes demasiado tiempo y te quedas atrapado.")
                    print("Juego perdido")
                else:
                    print("Opcion no valida.")
            elif nivel4 == "ascensor":
                print("El ascensor se detiene entre pisos y quedas atrapado. Juego perdido")
            else:
                print("Opcion no valida.")
        else:
            print("Opcion no valida.")

    elif nivel2 == "volver":
        print("\nRegresas al hangar, pero lamentablemente la compuerta se ha cerrado detras de ti.")
        print("No puedes continuar. Juego perdido")

    elif nivel2 == "explorar":
        print("\nEncuentras una compuerta de mantenimiento.")
        nivel3_1 = input("Quieres ABRIRLA o IGNORARLA?").lower()

        if nivel3_1 == "abrir":
            print("Te arrastras por una tuberia y llegas al sistema electrico de la nave.")
            nivel4_1 = input("Quieres REINICIAR el sistema o BUSCAR salidas alternas? Decidete rapido!").lower()

            if nivel4_1 == "reiniciar":
                print("Reactivas parte de la nave, incluyendo el panel numerico anterior.")
                print("Puedes volver y avanzar. FIN DEL JUEGO")
            elif nivel4_1 == "buscar":
                print("Encuentras una salida alternativa. Escapas al espacio y para tu gran suerte, te rescata otra nave.")
                print("FIN DEL JUEGO")
            else:
                print("Opcion no valida.")
        elif nivel3_1 == "ignorar":
            print("Tonto... perdiste una oportunidad de escape. Te quedas atrapado. Juego perdido")
        else:
            print("Opcion no valida.")

    elif nivel2 == "inspeccionar":
        print("\nInspeccionas mas a fondo y encuentras un pequeño conducto de ventilacion en el techo.")
        nivel3_2 = input("Quieres SUBIR por el conducto o CONTINUAR por el pasillo?").lower()

        if nivel3_2 == "subir":
            print("Te arrastras por el conducto hasta que caes en una sala de control abandonada. La energia esta baja, pero aun funciona un terminal.")
            nivel4_2 = input("Quieres INTENTAR restaurar la energia o EXAMINAR los archivos del terminal?").lower()

            if nivel4_2 == "intentar":
                print("Restauras la energia de la nave, pero un sistema de seguridad se activa y bloquea todas las salidas. Juego perdido.")
            elif nivel4_2 == "examinar":
                print("Los archivos revelan la ubicacion de una baliza de emergencia. La activas y en poco tiempo, una nave de rescate llega a tu posicion. FIN DEL JUEGO.")
            else:
                print("Opcion no valida.")
        elif nivel3_2 == "continuar":
            print("Decides ignorar el conducto y te encuentras con una puerta sellada que no puedes abrir. Te quedas atrapado. Juego perdido.")
        else:
            print("Opcion no valida.")

    else:
        print("Opcion no valida.")

elif nivel1 == "pasillo oscuro":
    print("\nCaminas por el pasillo oscuro. Escuchas ruidos muy extraños... y algo se mueve cerca.")
    nivel2 = input("Quieres ENCENDER tu linterna, CORRER hacia adelante o REGRESAR?").lower()

    if nivel2 == "encender":
        print("\nIluminas el pasillo y ves una figura extraña (como un fantasma) huyendo de ti.")
        nivel3 = input("Quieres SEGUIRLA o ENTRAR por una puerta lateral?").lower()

        if nivel3 == "seguirla":
            print("Resulta que la figura te lleva a una trampa. Juego perdido")
        elif nivel3 == "entrar":
            print("Procedes a ingresar y dentro encuentras un terminal de comunicacion de la nave.")
            nivel4 = input("Quieres ENVIAR MENSAJE o REVISAR ARCHIVOS?").lower()

            if nivel4 == "enviar":
                print("La señal de auxilio es enviada. Te salvan horas despues. FIN DEL JUEGO")
            elif nivel4 == "revisar":
                print("Los archivos que viste te revelan la ubicacion exacta de la capsula de escape.")
                nivel5 = input("Quieres IR a la capsula o QUEDARTE en el terminal?").lower()

                if nivel5 == "ir":
                    print("Encuentras la capsula y escapas justo a tiempo. FIN DEL JUEGO")
                elif nivel5 == "quedarte":
                    print("La energia se agota y quedas atrapado. Juego perdido")
                else:
                    print("Opcion no valida.")
            else:
                print("Opcion no valida.")
        else:
            print("Opcion no valida.")

    elif nivel2 == "correr":
        print("Tropiezas y te das un fuerte golpe en la cabeza. Has perdido el juego")

    elif nivel2 == "regresar":
        print("Te regresas al hangar, pero la compuerta se cierra y quedas totalmente atrapado. Has perdido")

    elif nivel2 == "inspeccionar":
        print("\nInspeccionas el pasillo con cuidado y encuentras una compuerta de mantenimiento oculta en la pared.")
        nivel3_3 = input("Quieres ABRIR la compuerta o CONTINUAR por el pasillo?").lower()

        if nivel3_3 == "abrir":
            print("Logras abrir la compuerta y entras a una sala de control abandonada. Un viejo sistema de navegacion aun funciona.")
            nivel4_3 = input("Quieres USAR el sistema de navegacion para encontrar tu ubicacion o ACTIVAR una baliza de emergencia?").lower()

            if nivel4_3 == "usar":
                print("Usas el sistema para encontrar tu ubicacion, pero un error de calculo te hace saltar a un sistema solar desconocido. Juego perdido.")
            elif nivel4_3 == "activar":
                print("Activas la baliza de emergencia y en poco tiempo una nave de rescate llega a tu posicion. FIN DEL JUEGO.")
            else:
                print("Opcion no valida.")
        elif nivel3_3 == "continuar":
            print("Decides ignorar la compuerta y te encuentras con una criatura que te ataca. Te quedas atrapado. Juego perdido.")
        else:
            print("Opcion no valida.")

    else:
        print("Opcion no valida.")
else:
    print("Opcion no valida.")
