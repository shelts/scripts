reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'phi (rad)'
set xrange[-5:5]
# set yrange[0:1000]



theory = "~/Desktop/research/data_testing/theory/theory_phi.dat"
light = "~/Desktop/research/data_testing/binned_data/phi_vel_light_"
dark = "~/Desktop/research/data_testing/binned_data/phi_vel_dark_"
both = "~/Desktop/research/data_testing/binned_data/phi_vel_both_"


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_0gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After 0Gy'
plot light."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After 0Gy'
plot dark."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_0gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After 0Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_0p25gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After .25Gy'
plot light."p25gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_0p25gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After .25Gy'
plot dark."p25gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_0p25gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After .25Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_0p50gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After .5Gy'
plot light."p5gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_0p50gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After .5Gy'
plot dark."p5gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 



set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_0p50gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After .50Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_0p75gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After .75Gy'
plot light."p75gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_0p75gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After .75Gy'
plot dark."p75gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_0p75gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After .75Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_1gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After 1Gy'
plot light."1gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_1gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After 1Gy'
plot dark."1gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_1gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After 1Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_2gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After 2Gy'
plot light."2gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_2gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After 2Gy'
plot dark."2gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_2gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After 2Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_3gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After 3Gy'
plot light."3gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_3gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After 3Gy'
plot dark."3gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_3gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After 3Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_light_4gy.jpeg"
set title 'Histogram of Light Matter Velocity Phi Distribution After 4Gy'
plot light."4gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_dark_4gy.jpeg"
set title 'Histogram of Dark Matter Velocity Phi Distribution After 4Gy'
plot dark."4gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/vel_phi/phi_vel_both_4gy.jpeg"
set title 'Histogram of Total Velocity Phi Distribution After 4Gy'
plot both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 