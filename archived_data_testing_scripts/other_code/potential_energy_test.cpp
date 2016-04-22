#include <iostream>
#include <fstream>
#include <cmath>
#include <tgmath.h>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <typeinfo>
#include <vector>
#include <string>
#include <ctime>
using namespace std;

#define inv(x)  ((double) 1.0 / (x))
#define seventh(x) ((x) * (x) * (x) * (x) * (x) * (x) * (x))
#define sixth(x) ((x) * (x) * (x) * (x) * (x) * (x))
#define fourth(x) ((x) * (x) * (x) * (x))
#define fifth(x) ((x) * (x) * (x) * (x) * (x))
#define cube(x) ((x) * (x) * (x))
#define sqr(x)  ((x) * (x))
#define sqrdif(x, y) (sqr( (x) - (y) ))

#define seventhhalfs(x) ( sqrt(seventh(x) ) )
#define fivehalves(x)   ( sqrt(fifth(x) ) )
#define threehalves(x)  ( sqrt(cube(x)  ) )


#define minusfivehalves(x) (inv(fivehalves(x)))
#define minusthreehalves(x) (inv(threehalves(x)) )
#define minushalf(x) ( inv(sqrt(x)) )

double randDouble(double low, double high)
{
    double temp;
/* calculate the random number & return it */
    temp = ((double) rand() / (static_cast<double>(RAND_MAX) + 1.0))* (high - low) + low;
    return temp;
}

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// theory functions

double density(double r, double * args)
{
    
    double rscale_l = args[0];
    double rscale_d = args[1];
    double mass_l   = args[2];
    double mass_d   = args[3];
    
    double pi = 4.0 * atan(1.0);
    double rscale_l_cube = cube(rscale_l); 
    double rscale_d_cube = cube(rscale_d); 

    //   double density_result= (3.0/(4.0*pi))*(mass/rscalecube *pow(1+ sqr/sqrrcube, -2.5));
    double density_light_comp = (mass_l/rscale_l_cube) * minusfivehalves( (1.0 + sqr(r)/sqr(rscale_l) ) );
    double density_dark_comp  = (mass_d/rscale_d_cube) * minusfivehalves( (1.0 + sqr(r)/sqr(rscale_d) ) );
    double coeff = 3.0 / (4.0 * pi);

    double density_result = coeff * ( density_light_comp + density_dark_comp);
    return density_result;
}

double mass_enc(double r, double * args)
{
    double rscale_l = args[0];
    double rscale_d = args[1];
    double mass_l   = args[2];
    double mass_d   = args[3];

    double rcube = cube(r);
    double mass_enclosed_l = mass_l * rcube * pow( (sqr(r) + sqr(rscale_l) ), -1.5);
    double mass_enclosed_d = mass_d * rcube * pow( (sqr(r) + sqr(rscale_d) ), -1.5);
    
    double mass_enclosed = mass_enclosed_l + mass_enclosed_d;
    return mass_enclosed;

}

double potential( double r, double * args)
{
    double rscale_l = args[0];
    double rscale_d = args[1];
    double mass_l   = args[2];
    double mass_d   = args[3];
    double pot_light_comp = mass_l/sqrt( sqr(r) + sqr(rscale_l) );
    double pot_dark_comp  = mass_d/sqrt( sqr(r) + sqr(rscale_d) );
    double potential_result = -1.0 * (pot_light_comp + pot_dark_comp);

    return (potential_result);
}


double potential_total_int(double r, double * comp_args, double * args)
{
    /*total potential energy, calculated by integrating this function*/
    double pi  = 4.0 * atan(1.0);
    double pot = potential(r, args);
    double den = density(r, comp_args);
    double func = sqr(r) * pot * den;
    
//     printf("func = %f pot = %f den = %f \n", func, pot, den);
    return func;
}


double potential_total_calc(double r, double * args)
{
    /*from a analytical calc. Does not work for combined compoenents*/
    double rscale_l = args[0];
    double rscale_d = args[1];
    double mass_l   = args[2];
    double mass_d   = args[3];
    
    double pi= 4.0 * atan(1.0);
    
    double func_light_comp = 3.0 * sqr(mass_l) * inv(2.0 * sixth(rscale_l)) * fourth(r) * inv( sqr( 1.0 + sqr(r)/sqr(rscale_l)) );
    double func_dark_comp  = 3.0 * sqr(mass_d) * inv(2.0 * sixth(rscale_d)) * fourth(r) * inv( sqr( 1.0 + sqr(r)/sqr(rscale_d)) );
    
    double func = (func_light_comp + func_dark_comp);
    
//     printf("func = %f pot = %f den = %f \n", func, pot, den);
    return func;
    
}

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// service functions


static double gauss_quad(double (*rootFunc)(double, double *, double *), double * comp_args, double * args, double lower, double upper )
{
    double Ng,hg,lowerg, upperg;
    double intv;
    double coef1,coef2;//parameters for gaussian quad
    double c1, c2, c3;
    double x1, x2, x3;
    double x1n, x2n, x3n;
    
    //this should be from infinity. But the dis func should be negligble here.
    double a = lower; 
    double b = upper;

    intv = 0;//initial value of integral
    Ng = 1000.0;//integral resolution
    hg = (b-a)/(Ng);

    
    lowerg = lower;
    upperg = lowerg + hg; 

    coef2 = (lowerg+upperg)/2.0;//initializes the first coeff to change the function limits
    coef1 = (upperg-lowerg)/2.0;//initializes the second coeff to change the function limits
    c1 = 5.0/9.0;
    c2 = 8.0/9.0;
    c3 = 5.0/9.0;
    x1 = -sqrt(3.0/5.0);
    x2 = 0.0;
    x3 = sqrt(3.0/5.0);
    x1n = (coef1 * x1 + coef2);
    x2n = (coef1 * x2 + coef2);
    x3n = (coef1 * x3 + coef2);
    int counter=0;
    while (1)
    {
                //gauss quad
        intv = intv +  c1 * (*rootFunc)(x1n, comp_args, args) * coef1 +
                       c2 * (*rootFunc)(x2n, comp_args, args) * coef1 + 
                       c3 * (*rootFunc)(x3n, comp_args, args) * coef1;

        lowerg = upperg;
        upperg = upperg + hg;
        coef2  = (lowerg + upperg)/2.0;//initializes the first coeff to change the function limits
        coef1  = (upperg - lowerg)/2.0;

        x1n = ((coef1) * x1 + coef2);
        x2n = ((coef1) * x2 + coef2);
        x3n = ((coef1) * x3 + coef2);

        if(upper > lower)
        {
            if(lowerg >= upper)//loop termination clause
            {
                break;
            }
        }
        else if(lower > upper)
        {
            if(lowerg <= upper)//loop termination clause
            {
                break;
            }
        }
        
        
        counter++;
    }
    return intv;
}


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// theory checking functions

void potential_theory(double bin_width, double * args)
{
    
    double rscale_l = args[0];
    double rscale_d = args[1];
    double mass_l   = args[2];
    double mass_d   = args[3];
    double masspl   = args[4]; 
    double masspd   = args[5];
    
    double light[4] = {rscale_l, rscale_d, mass_l, 0.0};
    double dark[4]  = {rscale_l, rscale_d, 0.0, mass_d};
    double pot_all, pot_l, pot_d;
    double pi = 4.0 * atan(1.0);
    double w = 0.0;
    double pot_pp_l;
    double pot_pp_d;
    //done via integral:
    FILE * pot;
    pot= fopen("./theory/theory_pot_int.dat", "w");
    while(1)
    {
        pot_pp_l = (  potential(w, light) );
        pot_pp_d = (  potential(w, dark)  );
        pot_l    = 4.0 * pi * bin_width * inv(pot_pp_l * masspl ) * potential_total_int(w, light, args); //gauss_quad(potential_total_int, light, 0.0, w);
        pot_d    = 4.0 * pi * bin_width * inv(pot_pp_d * masspd ) * potential_total_int(w, dark, args); //gauss_quad(potential_total_int, dark, 0.0, w);
        pot_all  = 4.0 * pi * bin_width * potential_total_int(w, args, args); //gauss_quad(potential_total_int, args, 0.0, w);
//         printf( "%f\t%f\t%f\t%f\n", pot_pp_l, pot_pp_d , pot_l, pot_all);
        w += 0.01;
        fprintf(pot, "%f\t%f\t%f\t%f\n", pot_pp_l, pot_pp_d , pot_l, pot_d);
            
        if( fabs(w) > 5 * (rscale_l + rscale_d)){break;}
    }
    fclose(pot);
    
    //done via analytical calc
    FILE * pot2;
    pot2= fopen("./theory/theory_pot_calc.dat", "w");
    w = 0.0;
    while(1)
    {
        
        pot_pp_l = potential(w, light);
        pot_pp_d = potential(w, dark);
        
        pot_l = potential_total_calc(w, light) ;
        pot_d = potential_total_calc(w, dark)  ;
        pot_all = pot_l + pot_d;//not corrects
        w += 0.01;
        fprintf(pot2, "%f \t %f \t %f\t%f\n", pot_pp_l, pot_pp_d, pot_l, pot_d);
            
        if( w > 5 * (rscale_l + rscale_d)){break;}
    }
    fclose(pot2);
    
    
    /*  CALCULATION OF TOTAL POTENTIAL ENERGY   */
    
    //single density against both potentials
    double r_inf = 50.0 * (rscale_l + rscale_d);
    pot_l = 4.0 * pi  * gauss_quad(potential_total_int, light, args, 0.0, r_inf);
    pot_d = 4.0 * pi  * gauss_quad(potential_total_int, dark, args, 0.0, r_inf);
    double sum = pot_l + pot_d;
//     printf("\npot_l = %f \t pot_d = %f \t sum = %f\n", pot_l, pot_d, sum);
    
    
    //single density against single potentials
    pot_l = 4.0 * pi  * gauss_quad(potential_total_int, light, light, 0.0, r_inf);
    pot_d = 4.0 * pi  * gauss_quad(potential_total_int, dark, dark, 0.0, r_inf);
    sum = pot_l + pot_d;
//     printf("\npot_l = %f \t pot_d = %f \t sum = %f\n", pot_l, pot_d, sum);
    
}

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// actual data checking function

void potential_distribution(double bin_width, double number_of_bins, string extension, double * args, double * rl, int Nl, double * rd, int Nd)
{
    double rscale_l = args[0];
    double rscale_d = args[1];
    double mass_l   = args[2];
    double mass_d   = args[3];
    double masspl   = args[4]; 
    double masspd   = args[5];
    string s;
    int type = 2;
    double light[4] = {rscale_l, rscale_d, mass_l, 0.0};
    double dark[4]  = {rscale_l, rscale_d, 0.0, mass_d};
    
    double pot_d[Nd];
    double pot_l[Nl];
    double r;
    double pot[Nd + Nl];
    ofstream pod;
    pod.open("./actual/dark_potential_" + extension + ".dat");
    ofstream pol;
    pol.open("./actual/light_potential_" + extension + ".dat");
    int j = 0;
    for(int i = 0; i < Nd; i++)
    {
        r = rd[i];
        pot_d[i] = potential(r, dark);
        pod<<r <<"\t"<<pot_d[i]<<endl;
        pot[j] = pot_d[i];
        j++;
        
    }
    
    for(int i = 0; i < Nl; i++)
    {
        r = rl[i];
        pot_l[i] = potential(r, light);
        pol<<r <<"\t"<<pot_l[i]<<endl;
        pot[j] = pot_l[i];
        j++;
    }
    
    
    pol.close();
    pod.close();
    
    s = string("binned_data/pot_dark_"+extension+".dat");
    binner(number_of_bins, bin_width, pot_d, Nd, s, extension, type);
    s = string("binned_data/pot_light_"+extension+".dat");
    binner(number_of_bins, bin_width, pot_l, Nl, s, extension, type);
    
//     s = string("binned_data/pot_"+extension+".dat");
//     binner(number_of_bins, bin_width, pot, Nd + Nl, type, extension, type);
    
}

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// main function calls
int main (int argc, char * const argv[])
{
    srand(time(NULL));
    string simtime                 = argv[1];
    double rscale_l                = atof(argv[2]);
    double rscale_d                = atof(argv[3]);
    double mass_l                  = atof(argv[4]);
    double mass_d                  = atof(argv[5]);
    double mass_per_particle_light = atof(argv[6]); 
    double mass_per_particle_dark  = atof(argv[7]); 
    string extension = simtime + "gy";
    
//     printf("massl = %f  massd = %f rscale_l = %f rscale_d = %f\n", mass_l, mass_d, rscale_l, rscale_d);
    double args[6]  = {rscale_l, rscale_d, mass_l, mass_d, mass_per_particle_light, mass_per_particle_dark};

    //    printf("rad_light= %f \t rad_dark=%f \n mass_light=%f \t mass_dark=%f\n", rscale_l, rscale_d, mass_l, mass_d);

    /*paramters for binning routine*/
    int number_of_bins = 1000;
    double bin_width = .10;

    /*these are markers for the type of data being sent into functions*/
    
    /*get center of mass*/
    mass = mass_l + mass_d;

    /*getting the radii and vel vectors*/
    
    /*no longer neccessary. Used to calculate the total potential energy, actual and theory*/
    printf(".");
    potential_distribution(bin_width, number_of_bins, extension, args, rl, Nl, rd, Nd);
    printf(".");
    potential_theory(bin_width, args);
    
    printf("done.\n");
}
