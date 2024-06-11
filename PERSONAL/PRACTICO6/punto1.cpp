#include <iostream>

using namespace std;

//punto 1
int suma(int a, int b){
    return a + b;
}

int main()
{
    int a, b;
    cout << "ingrese dos numeros para sumarlos" << endl;
    cin >> a >> b;
    cout << "La suma da: " << suma(a, b) << endl;

    return 0;
}
