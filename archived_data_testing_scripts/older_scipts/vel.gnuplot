reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'vel (km/s)'
set xrange[0:10]
set yrange[0:1200]
set style fill transparent solid 0.5 
# noborder



theory = "~/Desktop/research/data_testing/theory/theory_vel.dat"
light = "~/Desktop/research/data_testing/binned_data/light_matter_vel_bins_"
dark = "~/Desktop/research/data_testing/binned_data/dark_matter_vel_bins_"

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_0gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 0Gy'
plot light."0gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark'
# , theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 0Gy'
plot dark."0gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark'
# , theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_0p25gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After .25Gy'
plot light."p25gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_0p25gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After .25Gy'
plot dark."p25gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_0p50gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After .5Gy'
plot light."p5gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_0p50gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After .5Gy'
plot dark."p5gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_0p75gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After .75Gy'
plot light."p75gy.dat" using 2:1  with boxes title 'actual',   theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_0p75gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After .75Gy'
plot dark."p75gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_1gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 1Gy'
plot light."1gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_1gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 1Gy'
plot dark."1gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_2gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 2Gy'
plot light."2gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_2gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 2Gy'
plot dark."2gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_3gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 3Gy'
plot light."3gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_3gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 3Gy'
plot dark."3gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_light_4gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 4Gy'
plot light."4gy.dat" using 2:1  with boxes title 'actual',   theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_theory/vel_distribution_dark_4gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 4Gy'
plot dark."4gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
