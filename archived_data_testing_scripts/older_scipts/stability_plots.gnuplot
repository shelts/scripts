reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'radius (Kpc)'
set xrange[0:20]
set yrange[0:1500]



theory_den = "~/Desktop/research/data_testing/theory/theory_den.dat"
light = "~/Desktop/research/data_testing/binned_data/light_matter_bins_"
dark = "~/Desktop/research/data_testing/binned_data/dark_matter_bins_"
both = "~/Desktop/research/data_testing/binned_data/both_matter_bins_



n = light."0gy.dat"
set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_0gy.jpeg"
set title 'Histogram of Light Matter Distribution After 0Gy'
plot n using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 0Gy'
plot dark."0gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_0gy.jpeg"
set title 'Histogram of Combined Matter Distribution After 0Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_0p25gy.jpeg"
set title 'Histogram of Light Matter Distribution After .25Gy'
plot light."p25gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_0p25gy.jpeg"
set title 'Histogram of Dark Matter Distribution After .25Gy'
plot dark."p25gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_0p25gy.jpeg"
set title 'Histogram of Combined Matter Distribution After .25Gy'
plot both."p25gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_0p50gy.jpeg"
set title 'Histogram of Light Matter Distribution After .5Gy'
plot light."p5gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_0p50gy.jpeg"
set title 'Histogram of Dark Matter Distribution After .5Gy'
plot dark."p5gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_0p50gy.jpeg"
set title 'Histogram of Combined Matter Distribution After .5Gy'
plot both."p5gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_0p75gy.jpeg"
set title 'Histogram of Light Matter Distribution After .75Gy'
plot light."p75gy.dat" using 2:1  with boxes title 'actual',  theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_0p75gy.jpeg"
set title 'Histogram of Dark Matter Distribution After .75Gy'
plot dark."p75gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_0p75gy.jpeg"
set title 'Histogram of Combined Matter Distribution After .75Gy'
plot both."p75gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_1gy.jpeg"
set title 'Histogram of Light Matter Distribution After 1Gy'
plot light."1gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_1gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 1Gy'
plot dark."1gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_1gy.jpeg"
set title 'Histogram of Combined Matter Distribution After 1Gy'
plot both."1gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_2gy.jpeg"
set title 'Histogram of Light Matter Distribution After 2Gy'
plot light."2gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_2gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 2Gy'
plot dark."2gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_2gy.jpeg"
set title 'Histogram of Combined Matter Distribution After 2Gy'
plot both."2gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_3gy.jpeg"
set title 'Histogram of Light Matter Distribution After 3Gy'
plot light."3gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_3gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 3Gy'
plot dark."3gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_3gy.jpeg"
set title 'Histogram of Combined Matter Distribution After 3Gy'
plot both."3gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_light_4gy.jpeg"
set title 'Histogram of Light Matter Distribution After 4Gy'
plot light."4gy.dat" using 2:1  with boxes title 'actual',  theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_dark_4gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 4Gy'
plot dark."4gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/rad/radii_distribution_both_4gy.jpeg"
set title 'Histogram of Combined Matter Distribution After 4Gy'
plot both."4gy.dat" using 2:1  with boxes title 'actual', theory_den   using 1:2 with lines title 'both', theory_den   using 1:3 with lines title 'light',  theory_den   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
