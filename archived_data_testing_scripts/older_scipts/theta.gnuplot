reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'theta (rad)'
set xrange[0:4]
# set yrange[0:1000]


theory = "~/Desktop/research/data_testing/theory/theory_theta.dat"
theta_light = "~/Desktop/research/data_testing/binned_data/theta_light_"
theta_dark = "~/Desktop/research/data_testing/binned_data/theta_dark_"
theta_both = "~/Desktop/research/data_testing/binned_data/theta_both_"

set output "~/Desktop/research/data_testing/plots/theta/theta_light_0gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After 0Gy'
plot theta_light."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After 0Gy'
plot theta_dark."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/theta/theta_both_0gy.jpeg"
set title 'Histogram of Total Theta Distribution After 0Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/theta/theta_light_0p25gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After .25Gy'
plot theta_light."p25gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_0p25gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After .25Gy'
plot theta_dark."p25gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/theta/theta_both_0p25gy.jpeg"
set title 'Histogram of Total Theta Distribution After .25Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/theta/theta_light_0p50gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After .5Gy'
plot theta_light."p5gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_0p50gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After .5Gy'
plot theta_dark."p5gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 



set output "~/Desktop/research/data_testing/plots/theta/theta_both_0p50gy.jpeg"
set title 'Histogram of Total Theta Distribution After .50Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/theta/theta_light_0p75gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After .75Gy'
plot theta_light."p75gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_0p75gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After .75Gy'
plot theta_dark."p75gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/theta/theta_both_0p75gy.jpeg"
set title 'Histogram of Total Theta Distribution After .75Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

set output "~/Desktop/research/data_testing/plots/theta/theta_light_1gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After 1Gy'
plot theta_light."1gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_1gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After 1Gy'
plot theta_dark."1gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/theta/theta_both_1gy.jpeg"
set title 'Histogram of Total Theta Distribution After 1Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/theta/theta_light_2gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After 2Gy'
plot theta_light."2gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/theta/theta_dark_2gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After 2Gy'
plot theta_dark."2gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/theta/theta_both_2gy.jpeg"
set title 'Histogram of Total Theta Distribution After 2Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/theta/theta_light_3gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After 3Gy'
plot theta_light."3gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_3gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After 3Gy'
plot theta_dark."3gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_both_3gy.jpeg"
set title 'Histogram of Total Theta Distribution After 3Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

set output "~/Desktop/research/data_testing/plots/theta/theta_light_4gy.jpeg"
set title 'Histogram of Light Matter Theta Distribution After 4Gy'
plot theta_light."4gy.dat" using 2:1  with boxes title 'actual',  theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_dark_4gy.jpeg"
set title 'Histogram of Dark Matter Theta Distribution After 4Gy'
plot theta_dark."4gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/theta/theta_both_4gy.jpeg"
set title 'Histogram of Total Theta Distribution After 4Gy'
plot theta_both."0gy.dat" using 2:1  with boxes title 'actual', theory   using 1:2 with lines title 'both', theory   using 1:3 with lines title 'light',  theory   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 