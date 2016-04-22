reset
set terminal jpeg
set key on
set ylabel 'vel (km/s)'
set xlabel 'radius (Kpc)'
set xrange[0:15]
set yrange[0:6]

theory = "~/Desktop/research/data_testing/theory/theory_vel.dat"
light = "~/Desktop/research/data_testing/actual/light_matter_velocity_dist_"
dark = "~/Desktop/research/data_testing/actual/dark_matter_velocity_dist_"

set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_0gy.jpeg"
set title 'Light Velocity as a function of Radius After 0Gy'
plot light."0gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_0gy.jpeg"
set title 'Dark Velocity as a function of Radius After 0Gy'
plot dark."0gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_0p25gy.jpeg"
set title 'Light Velocity as a function of Radius After .25Gy'
plot light."p25gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_0p25gy.jpeg"
set title 'Dark Velocity as a function of Radius After .25Gy'
plot dark."p25gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_0p50gy.jpeg"
set title 'Light Velocity as a function of Radius After .5Gy'
plot light."p5gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_0p50gy.jpeg"
set title 'Dark Velocity as a function of Radius After .5Gy'
plot dark."p5gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_0p75gy.jpeg"
set title 'Light Velocity as a function of Radius After .75Gy'
plot light."p75gy.dat" using 1:2  with dots title 'actual',   theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_0p75gy.jpeg"
set title 'Dark Velocity as a function of Radius After .75Gy'
plot dark."p75gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_1gy.jpeg"
set title 'Light Velocity as a function of Radius After 1Gy'
plot light."1gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_1gy.jpeg"
set title 'Dark Velocity as a function of Radius After 1Gy'
plot dark."1gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_2gy.jpeg"
set title 'Light Velocity as a function of Radius After 2Gy'
plot light."2gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_2gy.jpeg"
set title 'Dark Velocity as a function of Radius After 2Gy'
plot dark."2gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_3gy.jpeg"
set title 'Light Velocity as a function of Radius After 3Gy'
plot light."3gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_3gy.jpeg"
set title 'Dark Velocity as a function of Radius After 3Gy'
plot dark."3gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_light_4gy.jpeg"
set title 'Light Velocity as a function of Radius After 4Gy'
plot light."4gy.dat" using 1:2  with dots title 'actual',   theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 


set output "~/Desktop/research/data_testing/plots/vel_dist/vel_vs_r/vel_vs_r_dark_4gy.jpeg"
set title 'Dark Velocity as a function of Radius After 4Gy'
plot dark."4gy.dat" using 1:2  with dots title 'actual',  theory   using 1:2 with lines title 'light',  theory   using 1:3 with lines title 'dark', theory   using 1:4 with lines title 'both'' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
