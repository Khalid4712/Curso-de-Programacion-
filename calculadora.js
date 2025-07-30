const opcion = prompt ("1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Raiz cuadrada\n6. Modulo\n7. Exponenciar\n\nElige una opcion: ");
switch (opcion) {

    case "1":
    
    let num1 = prompt ("Ingresa el primer numero: ")
    let num1_1 = Number (num1);
    let num2 = prompt ("Ingresa el segundo numero: ");
    let num2_1 = Number (num2)
    let suma = num1_1 + num2_1;
    
    console.log(`El resultado es: ${suma}`);
    break;

    case "2":
    
    let num1_2 = prompt ("Ingresa el primer numero: ")
    let num1_3 = Number (num1_2);
    let num2_2 = prompt ("Ingresa el segundo numero: ");
    let num2_3 = Number (num2_2)
    let resta = num1_2 - num2_2;
    
    console.log(`El resultado es: ${resta}`);
    break;

    case "3":
    
    let num1_4 = prompt ("Ingresa el primer numero: ")
    let num1_5 = Number (num1_4);
    let num2_4 = prompt ("Ingresa el segundo numero: ");
    let num2_5 = Number (num2_4)
    let multiplicacion = num1_4 * num2_4;
    
    console.log(`El resultado es: ${multiplicacion}`);
    break;

    case "4":
    
    let num1_6 = prompt ("Ingresa el primer numero: ")
    let num1_7 = Number (num1_6);
    let num2_6 = prompt ("Ingresa el segundo numero: ");
    let num2_7 = Number (num2_6)
    let division = num1_6 / num2_6;
    
    console.log(`El resultado es: ${division}`);
    break;

    case "5":
    
    let num1_8 = prompt ("Ingresa el numero al que quieres sacar la raiz cuadrada: ")
    let num1_9 = Number (num1_8)
    let raiz_cuadrada = num1_9 ** 0.5;

    console.log (`La raiz cuadrada de ${num1_9} es ${raiz_cuadrada}`);
    break;

    case "6":

    let num10 = prompt ("Ingresa el primer numero: ");
    let num11 = Number (num10);
    let num12 = prompt ("Ingresa el segundo numero (el modulo): ");
    let num12_1 = Number (num12);
    let modulo = num11 % num12_1;

    console.log (`El modulo de ${num11} y ${num12_1} es: ${modulo}`);
    break;

    case "7":

    let exponente = prompt ("Ingresa el numero a exponenciar (el numero base): ")
    let exponente1 = Number (exponente)
    let exponente_1 = prompt ("Ahora ingresa el exponente: ")
    let exponente_2 = Number (exponente_1)
    let potencia = exponente ** exponente_2;

    console.log (`La elevacion de ${exponente} a ${exponente_1} es: ${potencia}`)
    break;

    default:
    console.log("Opcion no valida. Por favor, elige una opcion del 1 al 7.");
    break;
}