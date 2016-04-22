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

using namespace std;

#define sqr(x) ( x * x )
#define sqrdel(x1, x2) sqr( (x1 -x2 ))
#define fifth(x) (x*x*x*x*x)
#define fivehalf(x) (sqrt( fifth(x)))
#define negone(x) (1.0/x )

/*
 * THIS HAS NOT BEEN UPDATED AND SHOULD NOT BE USED UNLESS IT IS
 */




/*
 * This code calculates the viral ratio for the entire system as a whole
 */

  struct bodies
  {
   double x;
   double y;
   double z;
   double vx, vy, vz;
   double mass;
   int type;
  };

/*This gets the number of positional data from the raw data files*/
int get_size(int type, string extension)
{
  string s;
    if(type==1){s= string("./raw_data/light_matter_"+extension+".dat");}
  else {s= string("./raw_data/dark_matter_"+extension+".dat");}
   int N=0;
  double datax;
 /*getting the length of the data set*/
   ifstream length;
   length.open (s);
   while(length>>datax>>datax>>datax>>datax>>datax>>datax)
    {
//       cout<<datax<<endl;
      N++;
    }
    length.close();
   
   return N;
}


void get_data(int Nd,int Nl,struct bodies * b, string extension,
	       double mass_per_dark_particle, double mass_per_light_particle, int type_dark, int type_light)
{
  
    string s;
    double datax,datay,dataz,datavx,datavy,datavz;
    int i=0;
    int N= Nd + Nl;
    s= string("raw_data/dark_matter_"+extension+".dat");
    ifstream data;
    data.open (s);
    while(data>>datax>>datay>>dataz>>datavx>>datavy>>datavz)
      {
	  b[i].x=datax;
	  b[i].y=datay;
	  b[i].z=dataz;
	  b[i].vx=datavx;
	  b[i].vy=datavy;
	  b[i].vz=datavz;
	  b[i].mass=mass_per_dark_particle;
	  b[i].type=type_dark;
	  i++;
	}
    data.close();

    s= string("raw_data/light_matter_"+extension+".dat");
    ifstream data2;
    data2.open (s);
    while(data2>>datax>>datay>>dataz>>datavx>>datavy>>datavz)
      {
	  b[i].x=datax;
	  b[i].y=datay;
	  b[i].z=dataz;
	  b[i].vx=datavx;
	  b[i].vy=datavy;
	  b[i].vz=datavz;
	  b[i].mass=mass_per_light_particle;
	  b[i].type=type_light;
	  i++;
	}
    data2.close();
  
  }
  
void print_rho(double * rho, int N, struct bodies * b, string s)
{
  
  double x, y, z, r;
  string name="./test_output/"+s+".txt";
  ofstream file;
  file.open(name);
  for(int i=0; i<N; i++)
  {
    x=b[i].x;
    y=b[i].y;
    z=b[i].z;
    r= sqrt( sqr(x) + sqr(y) + sqr(z));
    file<<rho[i]<<"\t"<<r<<endl;
  }
  file.close();
} 
  
  
double mass_enc(double r, double rscale, double mass)
{
  double rcube=r*r*r;
  double mass_enclosed= mass*rcube*pow( (r*r+ rscale*rscale), -1.5);
 
  return mass_enclosed;
  
}
  
  
void calc_rho(double * rho, int N, struct bodies * b, double massl, double massd, double rscale_l, double rscale_d)
{
  double x, y, z, r;
  double coeff, coeff_light, coeff_dark, denom_light, denom_dark;
  double pi=4*atan(1);
  double mass_enc_light, mass_enc_dark;
  coeff=( 3.0/(4.0*pi) );
  
  
  
  
  for(int i=0; i<N; i++)
  {
    x=b[i].x;
    y=b[i].y;
    z=b[i].z;
    r= sqrt( sqr(x) + sqr(y) + sqr(z));
    
    mass_enc_light=mass_enc(r, rscale_l, massl);
    mass_enc_dark=mass_enc(r, rscale_d, massd);
    
    coeff_light=(mass_enc_light/rscale_l);
    coeff_dark=(mass_enc_dark/rscale_d);
    
    denom_light=fivehalf( (1.0 + sqr(r)/sqr(rscale_l) )  );
    denom_dark=fivehalf( ( 1.0 + sqr(r)/sqr(rscale_d)  ) );
    
    rho[i]= coeff*( coeff_light*negone(denom_light) + coeff_dark*negone(denom_dark) );
    
  }
}

void calc_vel_dis(int N, struct bodies * b, string s)
{
 
  double vx, vy, vz, v[N];
  double x, y, z, r;
  
  for(int i=0; i<N; i++)
  {
   
    vx=b[i].vx;
    vy=b[i].vy;
    vz=b[i].vz;
    v[i]= sqrt( sqr(vx) + sqr(vy) + sqr(vz));
  }
  print_rho(v, N, b, s);
  
}


  
  
int main (int argc, char * const argv[])
{
  /*taking in command line data. should be the same parameters used to calculate the simulation*/
   string simtime= argv[1];
   double backtime  = atof(argv[2]);
   double rscale_l  = atof(argv[3]);
   double light_r_ratio = atof(argv[4]);
   double dwarfmass = atof(argv[5]);
   double light_mass_ratio = atof(argv[6]);
   double diff_masses=atof(argv[7]);
   
   string extension= simtime+"gy";
   /*changes the parameters to usable info*/
   double massl= dwarfmass * light_mass_ratio;
   double massd= dwarfmass - (dwarfmass * light_mass_ratio);
   double rscale_d= rscale_l/light_r_ratio;
   
  /*these are markers for the type of data being sent into functions*/
  int d=0;//dark matter
  int l=1;//light matter
  
  int Nd= get_size(0, extension);
  int Nl= get_size(1, extension);
  
  int N=Nd+ Nl;
  bodies b[N];
  double rho[N];
  double mass_per_light_particle;
  double mass_per_dark_particle;
  
  if(diff_masses==1)
  {
    mass_per_light_particle= massl/ (Nl);
    mass_per_dark_particle= massd/ (Nd);
    cout<<mass_per_dark_particle<<"\t"<<mass_per_light_particle<<endl;
  }
  else if(diff_masses==0)
  {
    cout<<"hello"<<endl;
    mass_per_light_particle= (massl+massd)/ (N);
    mass_per_dark_particle= (massl+massd)/ (N);
    cout<<mass_per_dark_particle<<"\t"<<mass_per_light_particle<<endl;
  }
  
//   cout<<Nl<<"  "<< Nd<<endl;

  get_data(Nd, Nl, b, extension, mass_per_dark_particle, mass_per_light_particle, d, l);
  
  string s="rho_test";
  calc_rho(rho, N, b, massl, massd, rscale_l, rscale_d);
  print_rho(rho, N, b,s);
  
  
  string vel_extension="vel_dis";
  calc_vel_dis(N, b, vel_extension);
  
  
  
/*  
  FILE * file;
  file=fopen("./test_output/rho_test.txt", "a");
//   printf("ke \t pot \t ratio \t time\n");
  fprintf(file, "%f \t %f \t %f \t %f \t%f\t %f \n", ke, pot,pot2, ratio,ratio2, atof(argv[1]));
  fclose(file);*/

//   FILE * file2;
//   file2=fopen("masses.txt", "a");
//   for(int i=0;i<N;i++)
//   {  
//     fprintf(file2, "%f \n", b[i].mass);
//   }
//     fclose(file2);
  
  
}