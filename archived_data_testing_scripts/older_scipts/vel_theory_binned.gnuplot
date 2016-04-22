reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'vel (km/s)'
set xrange[0:10]
set yrange[0:1500]
set style fill transparent solid 0.2
# noborder


light = "~/Desktop/research/data_testing/binned_data/light_matter_theory_vel_bins.dat"
dark = "~/Desktop/research/data_testing/binned_data/dark_matter_theory_vel_bins.dat"

light_nemo = "~/Desktop/research/data_testing/binned_data/light_matter_theory_nemo_vel_bins.dat"
dark_nemo = "~/Desktop/research/data_testing/binned_data/dark_matter_theory_nemo_vel_bins.dat"

actual_light = "~/Desktop/research/data_testing/binned_data/light_matter_vel_bins_"
actual_dark = "~/Desktop/research/data_testing/binned_data/dark_matter_vel_bins_"

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_0gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 0Gy'
plot actual_light."0gy.dat" using 2:1  with boxes title 'actual',  light   using 2:1 with lines  title 'light dist'  lw 2  
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2 
# ,  dark   using 2:1 with lines title 'dark dist' lw 2, dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2
#  ' 


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_0gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 0Gy'
plot actual_dark."0gy.dat" using 2:1  with boxes title 'actual',  dark   using 2:1 with lines title 'dark dist' lw 2 
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2 
# ,  light   using 2:1 with lines title 'light dist'  lw 2,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2
#  ' 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_0p25gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After .25Gy'
plot actual_light."p25gy.dat" using 2:1  with boxes title 'actual',  light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_0p25gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After .25Gy'
plot actual_dark."p25gy.dat" using 2:1  with boxes title 'actual', dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_0p50gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After .5Gy'
plot actual_light."p5gy.dat" using 2:1  with boxes title 'actual',  light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_0p50gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After .5Gy'
plot actual_dark."p5gy.dat" using 2:1  with boxes title 'actual',    dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_0p75gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After .75Gy'
plot actual_light."p75gy.dat" using 2:1  with boxes title 'actual',   light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2,

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_0p75gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After .75Gy'
plot actual_dark."p75gy.dat" using 2:1  with boxes title 'actual',   dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_1gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 1Gy'
plot actual_light."1gy.dat" using 2:1  with boxes title 'actual',  light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2, 

set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_1gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 1Gy'
plot actual_dark."1gy.dat" using 2:1  with boxes title 'actual',   dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_2gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 2Gy'
plot actual_light."2gy.dat" using 2:1  with boxes title 'actual',  light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2,  


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_2gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 2Gy'
plot actual_dark."2gy.dat" using 2:1  with boxes title 'actual',   dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_3gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 3Gy'
plot actual_light."3gy.dat" using 2:1  with boxes title 'actual',  light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_3gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 3Gy'
plot actual_dark."3gy.dat" using 2:1  with boxes title 'actual',   dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_light_theory_4gy.jpeg"
set title 'Histogram of Light Matter Velocity Distribution After 4Gy'
plot actual_light."4gy.dat" using 2:1  with boxes title 'actual',   light   using 2:1 with lines title 'light dist'  lw 2
# ,  light_nemo   using 2:1 with boxes title 'light nemo'  lw 2


set output "~/Desktop/research/data_testing/plots/vel_dist/binned_vs_tbins/vel_distribution_dark_theory_4gy.jpeg"
set title 'Histogram of Dark Matter Velocity Distribution After 4Gy'
plot actual_dark."4gy.dat" using 2:1  with boxes title 'actual', dark   using 2:1 with lines title 'dark dist' lw 2
# , dark_nemo   using 2:1 with boxes title 'dark nemo' lw 2  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
