

#include "prosjekt2.hpp"

int Initialize(int Dim, double Rmin, double Rmax, mat& A)
{
    int i, j;
    double Step, DiagConst, NondiagConst;
    A = zeros<mat>(Dim, Dim);
    // Integration step length
    Step = Rmax / Dim;
    DiagConst = 2.0 / (Step * Step);
    NondiagConst = -1.0 / (Step * Step);

    // Setting up tridiagonal matrix and diagonalization using Armadillo
    A(0, 0) = DiagConst;
    A(0, 1) = NondiagConst;
    for (i = 1; i < Dim - 1; i++)
    {
        A(i, i - 1) = NondiagConst;
        A(i, i) = DiagConst;
        A(i, i + 1) = NondiagConst;
    }
    A(Dim - 1, Dim - 2) = NondiagConst;
    A(Dim - 1, Dim - 1) = DiagConst;

    return 0;

}

int check(int Dim, double Rmax, mat& A){
    // diagonalize and obtain eigenvalues
    double Step, DiagConst, NondiagConst;
    Step = Rmax / Dim;
    DiagConst = 2.0 / (Step * Step);
    NondiagConst = -1.0 / (Step * Step);
    vec Eigval(Dim);
    eig_sym(Eigval, A);
    double pi = acos(-1.0);
    cout << "RESULTS:" << endl;
    cout << setiosflags(ios::showpoint | ios::uppercase);
    cout << "Number of Eigenvalues = " << setw(15) << Dim << endl;
    cout << "Exact versus numerical eigenvalues:" << endl;
    for (int i = 0; i < Dim; i++)
    {
        double Exact = DiagConst + 2 * NondiagConst * cos((i + 1) * pi / (Dim + 1));
        cout << setprecision(8) << fabs(fabs(Eigval[i]) - Exact) << endl;
    }
    return 0;
} //  end of main function

// the offdiag function, using Armadillo
int offdiag(mat A, int &p, int &q, int n, double& max){
    max = 0.0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            double aij = fabs(A(i, j));
            if (aij > max)
            {
                max = aij;
                p = i;
                q = j;
            }
        }
    }
    return 0;
}

void Jacobi_rotate(mat& A, mat &R, int k, int l, int n)
{
    double s, c;
    if (A(k, l) != 0.0)
    {
        double t, tau;
        tau = (A(l, l) - A(k, k)) / (2 * A(k, l));
        if (tau >= 0)
        {
            t = 1.0 / (tau + sqrt(1.0 + tau * tau));
        }
        else
        {
            t = -1.0 / (-tau + sqrt(1.0 + tau * tau));
        }
        c = 1 / sqrt(1 + t * t);
        s = c * t;
    }
    else
    {
        c = 1.0;
        s = 0.0;
    }
    double a_kk, a_ll, a_ik, a_il, r_ik, r_il;
    a_kk = A(k, k);
    a_ll = A(l, l);
    A(k, k) = c * c * a_kk - 2.0 * c * s * A(k, l) + s * s * a_ll;
    A(l, l) = s * s * a_kk + 2.0 * c * s * A(k, l) + c * c * a_ll;
    A(k, l) = 0.0; // hard-coding non-diagonal elements by hand
    A(l, k) = 0.0; // same here
    for (int i = 0; i < n; i++)
    {
        if (i != k && i != l)
        {
            a_ik = A(i, k);
            a_il = A(i, l);
            A(i, k) = c * a_ik - s * a_il;
            A(k, i) = A(i, k);
            A(i, l) = c * a_il + s * a_ik;
            A(l, i) = A(i, l);
        }
        // And finally the new eigenvectors
        r_ik = R(i, k);
        r_il = R(i, l);
        R(i, k) = c * r_ik - s * r_il;
        R(i, l) = c * r_il + s * r_ik;
    }
    return;
}