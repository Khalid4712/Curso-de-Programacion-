#include <iostream>
#include <cmath>

int main() {
         
    int opcion, num1, num2, suma, resta, multiplicacion, division, modulo, cociente;
    float raiz_cuadrada;
    
    std::cout<<"1. Suma\n2. Resta\n3. Multipicacion\n4. Division\n5. Raiz cuadrada\n6. Modulo\n7. Cociente\n8. Seno\n9. Coseno\n10.Tangente\n\nElige una opcion: ";
    std::cin>>opcion;

    switch(opcion){
        case 1:
        std::cout<<"Ingresa el primer numero: ";
        std::cin>>num1;
        
        std::cout<<"Ingresa el segundo numero: ";
        std::cin>>num2;

        suma = num1+num2;

        std::cout<<"El resultado es: "<<suma;
        break;

        case 2:
        std::cout<<"Ingresa el primer numero: ";
        std::cin>>num1;

        std::cout<<"Ingresa el segundo numero: ";
        std::cin>>num2;

        resta = num1-num2;

        std::cout<<"El resultado es: "<<resta;
        break;

        case 3:
        std::cout<<"Ingresa el primer numero: ";
        std::cin>>num1;

        std::cout<<"Ingresa el segundo numero: ";
        std::cin>>num2;

        multiplicacion = num1*num2;

        std::cout<<"El resultado es: "<<multiplicacion;
        break;

        case 4:
        std::cout<<"Ingresa el primer numero: ";
        std::cin>>num1;

        std::cout<<"Ingresa el segundo numero: ";
        std::cin>>num2;

        if (num2!=0){
        division = num1/num2;
        std::cout<<"El resultado es: "<<division;
        }
        else {
            std::cout<<"Division no permitida";
        }
        break;

        case 5:
        std::cout<<"Ingresa el numero: ";
        std::cin>>num1;

        raiz_cuadrada = sqrt(num1);

        std::cout<<"El resultado es: "<<raiz_cuadrada;
        break;

        case 6:
        std::cout<<"Ingresa el primer numero: ";
        std::cin>>num1;

        std::cout<<"Ingresa el segundo numero: ";
        std::cin>>num2;

        modulo = num1%num2;

        std::cout<<"El resultado es: "<<modulo;
        break;

        case 7:
        std::cout<<"Ingresa el dividendo: ";
        std::cin>>num1;

        std::cout<<"Ingresa el divisor: ";
        std::cin>>num2;

        cociente = num1/num2;

        std::cout<<"El resultado es: "<<cociente;
        break;
        
        case 8: 
        std::cout << "Ingresa un numero (en radianes): ";
        std::cin >> num1;
        std::cout << "Seno de " << num1 << " es: " << sin(num1) << std::endl;
        break;

        case 9: 
        std::cout << "Ingresa un numero (en radianes): ";
        std::cin >> num1;
        std::cout << "Coseno de " << num1 << " es: " << cos(num1) << std::endl;
        break;
            
        case 10: 
        std::cout << "Ingresa un numero (en radianes): ";
        std::cin >> num1;
        std::cout << "Tangente de " << num1 << " es: " << tan(num1) << std::endl;
        break;
         
        default:
        std::cout<<"Operador no valido, ingresa uno de los disponibles";
        break;
    }

    return 0;
}