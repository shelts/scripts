#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <typeinfo>
#include <vector>
#include <string>
using namespace std;

#define sqr(x)  ((x) * (x))


int get_size(string s)
{
    int N = 0;
    double datax;
 /*getting the length of the data set*/
    ifstream length;
    length.open (s);
    while(length>>datax>>datax)
    {
        N++;
    }
    length.close();
   
   return N;
}

void get_data(int N, double * bins, double * counts, string s)
{
    double datax, datay;
    int l = 0;

    ifstream data;
    data.open (s);
    /*reading in data*/
    while(data>>datax>>datay)
    {
        counts[l]  = datax;
        bins[l]    = datay;
        
        l++;
    }
    data.close();
}


double chi_sqr(double * countsa, double * countsb, int N)
{
    double ka, kb;
    double sa = 0.0;
    double sb = 0.0;
    double chisq = 0.0;
    double num, denom;
    double lines = 0.0;
    for(int i = 0; i < N; i++)
    {
        sa += countsa[i];
    }
    for(int i = 0; i < N; i++)
    {
        sb += countsb[i];
    }
    
    ka = sqrt( sb / sa);
    kb = sqrt( sa / sb);
    printf("sa = %f\t sb = %f\n", sa, sb);
    printf("ka = %f\t kb = %f\n", ka, kb);
    
    for(int i = 0; i < N; i++)
    {
        num = sqr(ka * countsa[i] - kb * countsb[i]);
        denom = countsa[i] + countsb[i];
        if(denom == 0.0)
        {
            continue;
        }
        lines += 1.0;
        chisq +=  num / denom ;
    }
    printf("lines = %f\n", lines);
    return chisq;
}



int main (int argc, char * const argv[])
{
    string a = argv[1];
    string b = argv[2];

    int Na, Nb;
    double chisq;
    
    Na = get_size(a);//getting the size of the dark matter data
    Nb = get_size(b);//getting the size of the light matter data
    const char * ca = a.c_str();
    const char * cb = b.c_str();
//     printf("%s \n %s \n ", ca, cb);
    printf("number of bins: %i %i\n", Na, Nb);
    
    double binsa[Na];
    double binsb[Nb];
    
    double countsa[Na];
    double countsb[Nb];
    
    get_data(Na, binsa, countsa, a);
    get_data(Nb, binsb, countsb, b); 
    
    chisq = chi_sqr(countsa, countsb, Na);
    
    printf("chi sqr = %f \n", chisq);

    
}
