#include <iostream>

using namespace std;

//prototipo de funciones
void mostrar(int arr[], int cant);
void insercion(int arreglo[], int posiciones);
void insercionIntercambio(int arr[], int posiciones);
void ordenarSeleccionDirecta(int arr[], int posiciones);
void ordenarBurbujeo(int arr[], int cant);



//funcion principal
int main(){
    int const posicionesMAIN = 5;
    int arregloMAIN[]={5,3,2,1,4};
    cout << "Arreglo desordenado:" << endl;
    for(int x = 0; x < posicionesMAIN; x++){
        cout << arregloMAIN[x] << "\t";
    }
    cout << endl;

    insercion(arregloMAIN, posicionesMAIN);
    //insercionIntercambio(arregloMAIN, posicionesMAIN);
    //ordenarSeleccionDirecta(arregloMAIN,  posicionesMAIN);
    //ordenarBurbujeo(arregloMAIN, posicionesMAIN);
    mostrar(arregloMAIN, posicionesMAIN);

return 0;
}
//definicion de funciones

void insercion(int arreglo[], int posiciones){
    int pos;
    int aux;

    //ALGORITMO DE ORDENAMIENTO POR INSERCION
    for (int i=0; i< posiciones; i++) // es para recorrer el arreglo
    {
        pos=i;
        aux= arreglo[i];  // almacena el valor al que ingresa en el arreglo

        while ((pos>0) && (arreglo[pos-1]< aux)) // segunda vuelta cuando el for esta en i=1 pos=1 pos=i, 5 > 3
        {
            arreglo[pos] = arreglo [pos - 1]; // es lo mismo que estar en pos = 1 del arrglo asigna el valor 5 y en la pos =0
            pos--;
        }
        //yo estaba en pos = 1 voy a pos =0 ;
        arreglo[pos] = aux;
    }

    //IMPRIMO EN ORDEN DESCENDENTE ORDENADO !
    cout <<"Arreglo Ordenado de manera Ascendente: " << endl;
    for(int j=0; j < posiciones; j++)
    {
       cout << arreglo[j] <<"\t";
    }
    cout << endl;
}

void insercionIntercambio(int arr[], int posiciones){
cout << "Ordenando por insercion con intercambios...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    int pos, temp;
    for (int i = 0; i < posiciones; i++){ // Recorrer todos los elementos del arreglo
        pos = i; // Guardar la posición actual
        // Mover los elementos mayores a la derecha mediante intercambios para hacer espacio para el elemento actual
        while((pos > 0) && (arr[pos - 1] > arr[pos])){
            temp = arr[pos]; // Guardar el valor del elemento actual
            arr[pos] = arr[pos - 1]; // Mover el elemento a la derecha
            arr[pos - 1] = temp; // Colocar el elemento guardado en la posición correcta
            pos--; // Mover la posición hacia la izquierda
        }
    }
}

void mostrar(int arr[], int cant){
cout << "Mostrando...\n"; // Mensaje para indicar que se va a mostrar el arreglo
    for(int i = 0; i < cant; i++){
        cout << arr[i] << "\t"; // Mostrar cada elemento del arreglo
    }
    cout << endl; // Salto de línea al final de la impresión
}

void ordenarSeleccionDirecta(int arr[], int cant){
cout << "Ordenando por seleccion directa...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    for (int i = 0; i < cant - 1; i++){ // Bucle externo: recorre todos los elementos del arreglo excepto el último
        int mayor = i; // Inicializar la posición del mayor elemento con la posición actual
        for(int j = i + 1; j < cant; j++){ // Bucle interno: recorre los elementos restantes del arreglo
            if(arr[j] > arr[mayor]){ // Encontrar la posición del mayor elemento en el resto del arreglo
                mayor = j;
            }
        }
        // Intercambiar el elemento actual con el mayor elemento encontrado
        if(mayor != i){//En la teoría dice >1 y también está bien, solo queremos saber si mayor no es igual a i
            int temp; // Variable temporal para realizar el intercambio
            temp = arr[i]; // Guardar el valor del elemento actual
            arr[i] = arr[mayor]; // Colocar el mayor elemento en la posición actual
            arr[mayor] = temp; // Colocar el elemento actual en la posición del mayor elemento
        }
    }
}

void ordenarBurbujeo(int arr[], int cant){
cout << "Ordenando por burbujeo...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    bool intercambio = true; // Variable para controlar si se realizó algún intercambio en la pasada actual
    int i = 0; // Inicialización del contador de pasadas
    while((i < cant - 1) && intercambio){ // Bucle principal: continúa mientras haya intercambios y no se haya llegado al final del arreglo
        intercambio = false; // Se asume que no habrá intercambios en esta pasada
        for(int j = cant - 1; j > i; j--){ // Bucle interno: recorre el arreglo desde el final hasta la posición `i`
            if(arr[j] > arr[j - 1]){ // Comparación de elementos adyacentes
                int temp = arr[j]; // Variable temporal para realizar el intercambio
                arr[j] = arr[j - 1]; // Intercambio del elemento actual con el anterior
                arr[j - 1] = temp; // Finaliza el intercambio
                intercambio = true; // Se realizó un intercambio
            }
        }
        if(intercambio){ // Si se realizó algún intercambio
            i++; // Incrementa el contador de pasadas
        }
    }
}


