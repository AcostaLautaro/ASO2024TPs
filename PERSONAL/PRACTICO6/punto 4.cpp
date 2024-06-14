#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

//prototipo de funciones

void mostrar (int arr[], int n);
void ordenarInsercion(int arr[], int cant);
void busquedaBinaria(int arr[], int n);


//cuerpo principal
int main(){
int main;
const int n = 10;
int arreglo[n];
srand(time(NULL));

for(int x = 0; x < n; x++){
    arreglo[x] = rand() % 100 + 1;
}

cout << "muestro arreglo desordenado" << endl;

for(int x = 0; x < n; x++){
    cout << arreglo[x] << "\t";
}
cout << endl;

ordenarInsercion(arreglo, n);
mostrar(arreglo,n);

cout << endl;

busquedaBinaria(arreglo, n);



return 0;
}

//definicion de funciones
void ordenarInsercion(int arr[], int cant){

    cout << "Ordenacion por insercion...\n" << endl; // Mensaje para indicar que se va a ordenar el arreglo
    int pos, aux;
    for(int i = 0; i < cant; i++){
        pos = i; // Guardar la posición actual
        aux = arr[i]; // Guardar el valor actual
        // Mover los elementos mayores a la derecha para hacer espacio para el elemento actual
        while((pos > 0) && (arr[pos - 1] > aux)){
            arr[pos] = arr[pos - 1]; // Mover el elemento a la derecha
            pos--; // Mover la posición hacia la izquierda
        }
        arr[pos] = aux; // Insertar el elemento en su posición correcta
    }
}
void mostrar (int arr[], int n){
cout << "muestro arreglo" << endl;
for(int x = 0; x < n; x++){
    cout << arr[x] << "\t";
}

}

void busquedaBinaria(int arr[], int n){
int numero,mitad,primero,ultimo,x;

    primero = 0;

    ultimo = 9;

    x = 0;

    cout<< "ingresa el numero a buscar:" ;

    cin>> numero;


    while (primero <= ultimo && x == 0)

    {

        mitad = (primero + ultimo) / 2;

        cout << mitad << "\t";

        if (numero == arr[mitad])

            x = 1;

        else if (numero < arr[mitad])

            ultimo = mitad -1;

        else if (numero > arr[mitad])

            primero = mitad + 1;

    }
    cout << endl;

    if (x == 1)

        cout<<" El numero se encuentra en el vector";

    else

        cout<< "El numero no se encuentra el vector";

}

