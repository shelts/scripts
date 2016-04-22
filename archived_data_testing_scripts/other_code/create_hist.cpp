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


void write_hist(int N, double * bins, double * counts, string s, double massp)
{
 
    int line = 0;
    int i = 0;
    const char * c = s.c_str();
    FILE * hist;
    hist = fopen(c, "w");
    while(1)
    {
        if(line == 0)
        {
            fprintf(hist, "n = 20000 \nmassPerParticle = %f \ntotalSimulated = 20000 \nlambdaBins = %i \nbetaBins = 1\n", massp, N);
        }
        
        if(line > 0)
        {
            fprintf(hist, "1 %12.10f %12.10f %12.10f %12.10f \n\n", bins[i], -100.0, counts[i], 0.0);
        }
        
        line++;
        i++;
        
        if(line >= N){break;}
    }
    
}


int main (int argc, char * const argv[])
{
    string simtime                 = argv[1];
    double mass_per_particle_light = atof(argv[2]); 
    double mass_per_particle_dark  = atof(argv[3]); 
    string extension = simtime + "gy";
    string l, d, b;
    int Nl, Nd, Nb;
    
    b = string("binned_data/both_matter_bins_" + extension + ".h");
    Nb = get_size(b);
    
    d = string("binned_data/dark_matter_bins_" + extension + ".dat");
    Nd = get_size(d);//getting the size of the dark matter data
    
    l = string("binned_data/light_matter_bins_" + extension + ".dat");
    Nl = get_size(l);//getting the size of the light matter data
    
    printf("%i %i\n", Nd, Nl);
    
    double binsl[Nl];
    double binsd[Nd];
    double binsb[Nb];
    
    double countsl[Nl];
    double countsd[Nd];
    double countsb[Nb];
    
    get_data(Nl, binsl, countsl, l);
    get_data(Nd, binsd, countsd, d); 
    get_data(Nb, binsb, countsb, b); 
     
    d = string("hist_data/dark_matter_bins_" + extension + ".hist");
    write_hist(Nd, binsd, countsd, d, mass_per_particle_dark);
    
    l = string("hist_data/light_matter_bins_" + extension + ".hist");
    write_hist(Nl, binsl, countsl, l, mass_per_particle_light);

}
