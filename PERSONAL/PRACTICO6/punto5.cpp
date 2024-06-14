#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

//variables globales
const int n = 4;

//prototipo funciones


void sumaMatrices(int arr1[n][n], int arr2[n][n], int n);

int main(){
srand(time(NULL));
int matriz1[n][n];
int matriz2[n][n];
sumaMatrices(matriz1,matriz2, n);




return 0;
}

void sumaMatrices(int arr1[n][n], int arr2[n][n], int n){
//cargo matriz
int matriz3[n][n];
for(int x = 0; x < n; x++){
    for(int y = 0; y < n; y++){
        arr1[x][y] = rand() % 100 + 1;
        arr2[x][y] = rand () % 100 + 1;
    }
 }

 cout << "MATRIZ 1" << endl;
 for(int x = 0; x < n; x++){
    for(int y = 0; y < n; y++){
        cout << arr1[x][y] << "\t";
    }
    cout << endl;
 }

 cout << endl;

 cout << "MATRIZ 2" << endl;
 for(int x = 0; x < n; x++){
    for(int y = 0; y < n; y++){
        cout << arr2[x][y] << "\t";
    }
    cout  << endl;
 }


 for(int x = 0; x < n; x++){
    for(int y = 0; y < n; y++){
       matriz3[x][y] = arr1[x][y] + arr2[x][y];
    }
 }


cout << "Suma de las matrices en su respectiva posicion" << endl;
for(int x = 0; x < n; x++){
    for(int y = 0; y < n; y++){
      cout << matriz3[x][y] << "\t";
    }
    cout << endl;
}
}

