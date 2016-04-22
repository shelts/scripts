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


void get_data(int Nd,int Nl,struct bodies * dark, struct bodies * light, string extension,
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
	  dark[i].x=datax;
	  dark[i].y=datay;
	  dark[i].z=dataz;
	  dark[i].vx=datavx;
	  dark[i].vy=datavy;
	  dark[i].vz=datavz;
	  dark[i].mass=mass_per_dark_particle;
	  dark[i].type=type_dark;
	  i++;
	}
    data.close();

    s= string("raw_data/light_matter_"+extension+".dat");
    ifstream data2;
    data2.open (s);
    i=0;
    while(data2>>datax>>datay>>dataz>>datavx>>datavy>>datavz)
      {
	  light[i].x=datax;
	  light[i].y=datay;
	  light[i].z=dataz;
	  light[i].vx=datavx;
	  light[i].vy=datavy;
	  light[i].vz=datavz;
	  light[i].mass=mass_per_light_particle;
	  light[i].type=type_light;
	  i++;
	}
    data2.close();
  
  }
  
double mass_enc(double r, double rscale, double mass)
{
  double rcube=r*r*r;
  double mass_enclosed= mass*rcube*pow( (r*r+ rscale*rscale), -1.5);
 
  return mass_enclosed;
  
}
  
  
  
double kinetic(int N, struct bodies * b)
{
  string s;
//   if(type==1){s= string("energy/kinetic_e_light_"+extension+".dat");}
//   else {s= string("energy/kinetic_e_dark_"+extension+".dat");}
  
  double ke=0.0;
  double vx, vy, vz;
  for(int i=0; i<N; i++)
  {
    vx=b[i].vx;
    vy=b[i].vy;
    vz=b[i].vz;
    ke+= 0.5*b[i].mass*(sqr(vx) + sqr(vy) + sqr(vz));
  }
  return ke;
}


double potential_energy(int N, struct bodies * b, string extension)
{
 string s;
 double pot=0.0;
 double rad_diff=0.0;
 double x1, y1, z1;
 double x2, y2, z2;
 double mass1, mass2;
  for(int i=0; i<N; i++)
  {
    for(int j=0; j<N; j++)
    { 
      if(i==j){continue;}
      else
      {
	x1=b[i].x;
	x2=b[j].x;
	
	y1=b[i].y;
	y2=b[j].y;
	
	z1=b[i].z;
	z2=b[j].z;
	
	mass1=b[i].mass;
	mass2=b[j].mass;
	
	rad_diff= sqrt( sqrdel(x1,x2) + sqrdel(y1, y2) + sqrdel(z1, z2) );
	pot+=-mass1* mass2* 1.0/(rad_diff);
// 	printf("pot= %f \n", pot);
      }
    }
  }
  
  return pot;
}

double potential( struct bodies * b, double mass, double rscale, int N)
{
  
  double pot=0.0;
  double x, y, z, r, part_mass;
  double mass_enclosed;
  for(int i=0; i<N; i++)
  {	
	x=b[i].x;
	y=b[i].y;
	z=b[i].z;
	r= sqrt( sqr(x) + sqr(y) + sqr(z));
	part_mass=b[i].mass;
// 	mass_enclosed=mass;
	mass_enclosed=mass_enc(r, rscale, mass);
    pot+=-1.0*mass*(mass_enclosed/sqrt(sqr(r) + sqr(rscale)) );
  }
  return pot;
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
  
  int Nd= get_size(0, extension);//getting the size of the dark matter data
  int Nl= get_size(1, extension);//getting the size of the light matter data
  
  int N=Nd+ Nl;
  bodies dark[Nd];
  bodies light[Nl];
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
  double ke_dark, ke_light;
  double pot_dark, pot2_dark;
  double pot_light, pot2_light;
  get_data(Nd, Nl, dark, light, extension, mass_per_dark_particle, mass_per_light_particle, d, l);
  
  ke_dark=  kinetic(Nd,dark);
  ke_light= kinetic(Nl,light);
  
  pot_dark=  potential(dark, massd, rscale_d, Nd);
  pot_light= potential(light, massl, rscale_l, Nl);
  
  pot2_dark=  potential_energy(Nd, dark, extension);
  pot2_light= potential_energy(Nl, light, extension);
  
  double ratio_dark=   fabs(2.0*ke_dark/pot_dark);
  double ratio2_dark= fabs(2.0*ke_dark/pot2_dark);
  
  double ratio_light=   fabs(2.0*ke_light/pot_light);
  double ratio2_light= fabs(2.0*ke_light/pot2_light);
  
  
   FILE * file1;
  file1=fopen("./test_output/component_virial_energy_output.txt", "a");
//   printf("ke \t pot \t ratio \t time\n");
  fprintf(file1, "%f \t %f \t %f \t %f \t %f \t %f \n", ke_dark, ke_light, pot_dark, pot_light,pot2_dark,pot2_light  );
  fclose(file1);
  
  
  FILE * file;
  file=fopen("./test_output/component_virial_output.txt", "a");
//   printf("ke \t pot \t ratio \t time\n");
  fprintf(file, "%f \t %f \t %f \t %f \n", ratio_dark, ratio_light, ratio2_dark, ratio2_light);
  fclose(file);

//   FILE * file3;
//   file3=fopen("./test_output/kes.txt", "w");
//   for(int i=0;i<Nl;i++)
//   {  
//     fprintf(file3, "%f \t %f\t %f\n", light[i].vx, light[i].vy, light[i].vz);
//   }
//     fclose(file3);
  
  
}