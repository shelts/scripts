reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'phi (rad)'
set xrange[-5:5]
# set yrange[0:1000]


theory_phi = "~/Desktop/research/data_testing/theory/theory_phi.dat"
actual_light = "~/Desktop/research/data_testing/binned_data/phi_light_"
actual_dark = "~/Desktop/research/data_testing/binned_data/phi_dark_"
actual_both = "~/Desktop/research/data_testing/binned_data/phi_both_"

set output "~/Desktop/research/data_testing/plots/phi/phi_light_0gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After 0Gy'
plot actual_light."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After 0Gy'
plot actual_dark."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/phi/phi_both_0gy.jpeg"
set title 'Histogram of Total Phi Distribution After 0Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/phi/phi_light_0p25gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After .25Gy'
plot actual_light."p25gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_0p25gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After .25Gy'
plot actual_dark."p25gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/phi/phi_both_0p25gy.jpeg"
set title 'Histogram of Total Phi Distribution After .25Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/phi/phi_light_0p50gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After .5Gy'
plot actual_light."p5gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_0p50gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After .5Gy'
plot actual_dark."p5gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 



set output "~/Desktop/research/data_testing/plots/phi/phi_both_0p50gy.jpeg"
set title 'Histogram of Total Phi Distribution After .50Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/phi/phi_light_0p75gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After .75Gy'
plot actual_light."p75gy.dat" using 2:1  with boxes title 'actual',  theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_0p75gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After .75Gy'
plot actual_dark."p75gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/phi/phi_both_0p75gy.jpeg"
set title 'Histogram of Total Phi Distribution After .75Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

set output "~/Desktop/research/data_testing/plots/phi/phi_light_1gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After 1Gy'
plot actual_light."1gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_1gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After 1Gy'
plot actual_dark."1gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/phi/phi_both_1gy.jpeg"
set title 'Histogram of Total Phi Distribution After 1Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/phi/phi_light_2gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After 2Gy'
plot actual_light."2gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/phi/phi_dark_2gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After 2Gy'
plot actual_dark."2gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

set output "~/Desktop/research/data_testing/plots/phi/phi_both_2gy.jpeg"
set title 'Histogram of Total Phi Distribution After 2Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
set output "~/Desktop/research/data_testing/plots/phi/phi_light_3gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After 3Gy'
plot actual_light."3gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_3gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After 3Gy'
plot actual_dark."3gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_both_3gy.jpeg"
set title 'Histogram of Total Phi Distribution After 3Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

set output "~/Desktop/research/data_testing/plots/phi/phi_light_4gy.jpeg"
set title 'Histogram of Light Matter Phi Distribution After 4Gy'
plot actual_light."4gy.dat" using 2:1  with boxes title 'actual',  theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_dark_4gy.jpeg"
set title 'Histogram of Dark Matter Phi Distribution After 4Gy'
plot actual_dark."4gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 


set output "~/Desktop/research/data_testing/plots/phi/phi_both_4gy.jpeg"
set title 'Histogram of Total Phi Distribution After 4Gy'
plot actual_both."0gy.dat" using 2:1  with boxes title 'actual', theory_phi   using 1:2 with lines title 'both', theory_phi   using 1:3 with lines title 'light',  theory_phi   using 1:4 with lines title 'dark' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 