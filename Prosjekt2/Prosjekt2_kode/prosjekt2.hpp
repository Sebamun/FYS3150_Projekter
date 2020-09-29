#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>
#include <armadillo>
#include <time.h>
#include <vector>
#include <string>

using namespace std;
using namespace arma;

int Initialize(int Dim, double Rmin, double Rmax, mat &U);
int check(int Dim, double Rmax, mat &U, string filename, string file_for_plot);
int offdiag(mat A, int &p, int &q, int n, double &max);
//void Jacobi_rotate(int n, mat &A, mat &R, int k, int l);
void Jacobi_rotate(mat &A, mat &R, int k, int l, int n);
//void find_le(int dim, mat R, string filename);
