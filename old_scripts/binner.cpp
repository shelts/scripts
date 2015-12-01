
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


/*This gets the number of positional data from the raw data files*/
int get_size(double * args, string file)
{
   int N=0;
  double datax;
 /*getting the length of the data set*/
   ifstream length;
   length.open (file);
   while(length>>datax>>datax>>datax>>datax>>datax>>datax)
    {
//       cout<<datax<<endl;
      N++;
    }
    length.close();
   
   return N;
}

/*this actually gets the data and stores it*/
void get_data(int N, double * x,double * y, double * z, double * vx,double * vy, double * vz, int type, string file)
{
  double datax,datay,dataz,datavx,datavy,datavz;
  int l=0;
  
  ifstream data;
  data.open (file);
  /*reading in data*/
  while(data>>datax>>datay>>dataz>>datavx>>datavy>>datavz)
  {
    x[l] =datax;
    y[l] =datay;
    z[l] =dataz;
    vx[l]=datavx;
    vy[l]=datavy;
    vz[l]=datavz;
    
    l=l+1;
  }
  data.close();
}

/*this is a binning routine, makes a histogram*/
void binner(int binN,double binwidth, double * x,int N, int type, string file)
{
  // binN=number of bins
  //binwidthsize of bins
  double bins[binN];
  double range=0;
  double upper=binN*binwidth;
 
/*binning*/

/*initializing bins*/
  for(int i=0; i!=binN;i++)
    {bins[i]=0;}
  ofstream bin;
  bin.open (file);

  for(int j=0; j<N;j++)/*tests one of the numbers at a time*/
  {
      range=0;/*resets the range so that the bins can be tested again against the number*/
      for(int i=0;i<binN;i++)/*for each bin, the number is tested*/
      {
      /*these two if statements justs for end points. if the range of the bin
      includes the upper interval, 1, then the second one runs. if not the first
      one runs. the only difference is the first is only less than range+binwidth
      and the second is less than or equal to range+binwidth. */
	  if((range+binwidth)< upper)
	  {
	      /*this if statement tests to see if the random number is in that
	      bin range.*/
	      if (x[j]>=range && x[j]< (range+binwidth))
	      {	
		bins[i]=bins[i]+1;
		break;
	      }
	      range=range+binwidth;/*this statement changes the range of testing
	      so that a new new bin can be checked against the number*/
	  }
	  else if((range+binwidth)==upper)/*includes the upper interval*/
	  {
	      if (x[j]>=range && x[j]<= (range+binwidth))
	      {
		bins[i]=bins[i]+1;
	        break;
	      }
	      range=range+binwidth;
	  }

      }
  }

  double binrange=0;
  double normed;
  for(int i=0; i!=binN;i++)
  {
      binrange=binrange+binwidth;
      normed=(bins[i])/double(N);
      bin<<normed<<"\t"<<binrange<<endl;
// 	bin<<bins[i]<<"\t"<<binrange<<endl;
  }

  bin.close();
}



int main (int argc, char * const argv[])
{
 /*taking in command line data. should be the same parameters used to calculate the simulation*/
   string file= argv[1];
   
   double parameter1  = atof(argv[2]);
   double parameter1  = atof(argv[3]);
   double parameter1 = atof(argv[4]);
   double parameter1 = atof(argv[5]);
   double parameter1 = atof(argv[6]);
    
  
  /*paramters for binning routine*/
  int number_of_bins=100;
  double bin_width=1;
  
  /*these are markers for the type of data being sent into functions*/
  int d=0;//dark matter
  int l=1;//light matter
  int vd=2;//vel
  int vl=3;//vel
  int Nd= get_size(extension);//getting the size of the dark matter data
  int Nl= get_size(argv, extension);//getting the size of the light matter data
  
  double rd[Nd], rl[Nl];//, r[Nd+Nl];  
  
  cout<<Nl<<"  "<< Nd<<endl;
  double dx[Nd], dy[Nd],dz[Nd],dvx[Nd], dvy[Nd],dvz[Nd];//vectors to store dark positions
  double lx[Nl], ly[Nl],lz[Nl],lvx[Nl], lvy[Nl],lvz[Nl];//vectors to store light positions
  double dv[Nd];//this is a vector to store the velocity distribution
  double lv[Nl];//this is a vector to store the velocity distribution
  
    /*getting the positional and velocity data*/
  get_data(Nd, dx, dy, dz, dvx, dvy, dvz, d, extension);  
  get_data(Nl, lx, ly, lz, lvx, lvy, lvz, l, extension);
  
  
  
  
}