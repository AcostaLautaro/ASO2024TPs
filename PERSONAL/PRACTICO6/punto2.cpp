#include <iostream>
using namespace std;


//funcion arreglos
int sumaArreglo(int arregloSuma[], int tamanio){
    int suma = 0;
    for(int x = 0; x < tamanio; x++){
        suma+= arregloSuma[x];
    }
        return suma;
}


int main(){
    const int n = 10;
    int valor;
    int arregloSuma[n];
    cout << "ingrese 10 valores para el arreglo" << endl;
    for(int x = 0; x < n; x++){
        cin >> valor;
        arregloSuma[x] = valor;
    }
    cout << "La suma del arreglo es de :" << sumaArreglo(arregloSuma, n) << endl;








return 0;
}
