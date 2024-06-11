#include <iostream>

using namespace std;


//parametro por valor, usa el valor y lo deja en la funcion, si queres utilizar sus datos, debes guardarlos
int sumar1(int valor){
    valor+=1;
    return valor;
}

//parametro por referencia, literalmente modifica los datos originales
int sumar2(int& valor2){
    valor2+=1;
    return valor2;
}

int main()
{
    int valor2;
    cout << "ingrese un numero" << endl;
    cin >> valor2;
    sumar2(valor2);
    cout << valor2 << endl;

    return 0;
}
