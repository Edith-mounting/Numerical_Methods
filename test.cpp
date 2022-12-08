#include <iostream>
#include <cmath>
#include <iomanip>
#include <assert.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <fstream>
using namespace std;
#define EPSILON 1e-5

void fixedPointIterationMethod(double x, double (*functionValue) (double), int iterCount = 0){
    double newX = functionValue(x);
    double difference = abs(newX - x);
    cout << "Iter#" << iterCount << " : " << x << " " << newX << endl;

    if(iterCount > 20){
        cout << "---------------------------------\n";
        cout << "MAximum iteration reached.......\n";
        cout << "The root of the function is: " << setprecision(10) << newX << endl;
        cout << "---------------------------------\n";
        return;
    }

    if(difference < EPSILON){
        cout << "---------------------------------\n";
        cout << "Number of Iterations taken: " << iterCount << endl;
        cout << "The root of the function is: " << setprecision(10) << newX << endl;
        cout << "---------------------------------\n";
    }else{
        fixedPointIterationMethod(newX, functionValue, iterCount+1);
    }
}


double anotherFunction(double x){
    return pow((3*x*x-2*x), 1/(double)3.0);
}

double functionValue(double x){
    return (3*x*x-x*x*x)/2;
}

double functionValue2(double x){
    return sqrt((x*x*x + 2*x) / (double) 3.0);
}


void fixedPointIterationMethodWithRelaxationParamter(double x, double (*functionValue) (double), double relaxParameter, int iterCount = 0){
    double value = functionValue(x);
    double newX = relaxParameter * x + (1-relaxParameter) * value;
    double difference = abs(newX - x);
    cout << "Iter#" << iterCount << " : " << x << " " << newX << endl;


    if(iterCount > 20){
        cout << "---------------------------------\n";
        cout << "MAximum iteration reached.......\n";
        cout << "The root of the function is: " << setprecision(10) << newX << endl;
        cout << "---------------------------------\n";
        return;
    }

    if(difference < EPSILON){
        cout << "-------------------------------------------------------" << endl;
        cout << "Number of Iterations taken: " << iterCount << endl;
        cout << "The root of the function is: " << setprecision(10) << newX << endl;
        cout << "-------------------------------------------------------" << endl << endl;
    }else{
        fixedPointIterationMethodWithRelaxationParamter(newX, functionValue, relaxParameter,  iterCount+1);
    }
}

void falsePostionMethod(double low, double high, double (*functionValue) (double)){
    double leftValue = functionValue(low);
    double rightValue = functionValue(high);
    double mid = high - rightValue* (low - high) / (leftValue - rightValue);
    double value = functionValue(mid);

    if(abs(value) < EPSILON){
        cout << "The root of given function is: " << setprecision(10) << mid << endl;
    }else if(value > 0){
        falsePostionMethod(low, mid, functionValue);
    }else{
        falsePostionMethod(mid, high, functionValue);
    }
}

vector<double> GaussEliminationWithPartialPivoting(vector<vector<double> > &M, vector<double> &C){
    int n = M.size();
    assert(n > 0);
    assert(n == (int) M[0].size());
    assert(n == (int) C.size());

    for(int k=0; k<n; k++){
        int maxRow = k;
        for(int i=k+1; i<n; i++){
            if(abs(M[i][k]) > abs(M[maxRow][k]) ){
                maxRow = i;
            }
        }
        swap(M[k], M[maxRow]);
        swap(C[k], C[maxRow]);

        for(int i=k+1; i<n; i++){
            double factor = M[i][k] / M[k][k];
            M[i][k] = (double)0.0;
            for(int j=k+1; j<n; j++){
                M[i][j] = M[i][j] - factor * M[k][j];
            }
            C[i] = C[i] - factor * C[k];
        }

    }

    vector<double> x(n, (double)0.0);
    x[n-1] = C[n-1] / M[n-1][n-1];
    for(int i=n-2; i>=0; i--){
        double sum = C[i];
        for(int j=i+1; j<n; j++){
            sum = sum - M[i][j] * x[j];
        }
        x[i] = sum / M[i][i];
    }

    return x;
}

void printMatrix(vector<vector<double> > &M){
    for(auto i: M){
        for(auto j: i){
            cout << j << ' ';
        }
        cout << endl ;
    }
}
void printVector(vector<double> &C){
    for(auto i: C){
        cout << i << ' ';
    }
    cout << endl ;
}

void solveBVP(double start, double end, int n){
    n++;
    double h = (end - start) / (n-1);
    vector<vector<double> > M(n, vector<double>(n, (double) 0.0));
    vector<double> C(n, (double)0.0);
    M[0][0] = - (double) 1.0;
    M[0][1] = (double) 1.0;

    for(int i=1; i<n-1; i++){
        M[i][i-1] = (double)1.0;
        M[i][i] =  - (double) 2.0;
        M[i][i+1] = (double) 1.0;
        C[i] = (double) - 400000.0 * h * h ;
    }
    cout << h << "\n";
    M[n-1][n-2] = (double) 1.0;
    M[n-1][n-1] = - (1 + h * (double) 100.0);
    C[n-1] = h * (double) -100.0 * (double) 10;
    printMatrix(M);
    // printVector(C);
    vector<double> T = GaussEliminationWithPartialPivoting(M, C);
    for(int i=0; i<n; i++){
        cout << "At x = " << start << " T = " << T[i] << '\n';
        start = start + h;
    }


}

int main(){
    int intervals;
    intervals = 5;
    solveBVP((double) 0.0, 0.01, intervals);

    return 0;
}