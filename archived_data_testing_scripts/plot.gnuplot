# #radii from simulation
# reset
# set terminal jpeg
# set key off
# set output "plots/radii_distribution_dark_1gy.jpeg"
# set title 'radii'
# set ylabel 'counts'
# set xlabel 'radius'
# set xrange[0:60]
# set yrange[0:.4]
# plot "binned_data/dark_matter_bins.dat" using 2:1  with boxes



reset
set terminal jpeg
set key off
set output "plots/radii_distribution_light_0gy.jpeg"
set title 'Histogram of Light Matter Distribution After 0Gy'
set ylabel 'counts'
set xlabel 'radius (Mpc)'
set xrange[0:30]
set yrange[0:.7]
plot "binned_data/light_matter_bins.dat" using 2:1  with boxes


# # radii from simulation
reset
set terminal jpeg
set key off
set output "plots/radii_distribution_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 0Gy'
set ylabel 'counts'
set xlabel 'radius (Mpc)'
set xrange[0:30]
set yrange[0:.7]
plot "binned_data/dark_matter_bins.dat" using 2:1  with boxes

# 
# 
# reset
# set terminal jpeg
# set key off
# set output "plots/radii_distribution_light_in.jpeg"
# set title 'radii'
# set ylabel 'counts'
# set xlabel 'radius'
# set xrange[0:60]
# set yrange[0:.4]
# plot "binned_data/light_matter_bins.dat" using 2:1  with boxes

# "actual/light_matter_actual.dat" using 1:2 with lines, "actual/dark_matter_actual.dat" using 1:2 with lines

#############################################################################################################################################################
# # radii expected
# reset
# set terminal jpeg
# set key off
# set output "plots/radii_distribution_expected_light.jpeg"
# set title 'radii'
# set ylabel 'counts'
# set xlabel 'radius'
# set xrange[0:2]
# # set yrange[0:.15]
# plot "actual/light_matter_expected_binned.dat" using 1:2  with lines
# # "actual/light_matter_actual.dat" using 1:2 with lines, "actual/dark_matter_actual.dat" using 1:2 with lines
# 
# reset
# set terminal jpeg
# set key off
# set output "plots/radii_distribution_expected_dark.jpeg"
# set title 'radii'
# set ylabel 'counts'
# set xlabel 'radius'
# set xrange[0:120]
# # set yrange[0:.15]
# plot "actual/dark_matter_expected_binned.dat" using 1:2  with lines
# # "actual/light_matter_actual.dat" using 1:2 with lines, "actual/dark_matter_actual.dat" using 1:2 with lines


#############################################################################################################################################################
#velocity

# from simulation
# reset
# set terminal jpeg
# set key off
# set output "plots/velocity_distribution_dark_binned.jpeg"
# set title 'velocity'
# set ylabel 'counts'
# set xlabel 'velocity'
# # set xrange[0:2]
# # set yrange[0:.06]
# plot "binned_data/dark_matter_vel_bins.dat" using 2:1  with boxes
# 
# reset
# set terminal jpeg
# set key off
# set output "plots/velocity_distribution_light_binned.jpeg"
# set title 'velocity'
# set ylabel 'counts'
# set xlabel 'velocity'
# n=2
# total_box_width_relative=0.75
# set boxwidth total_box_width_relative/n relative
# #  set boxwidth -.001
# # set xrange[0:2]
# # set yrange[0:.06]
# plot "binned_data/light_matter_vel_bins.dat" using 2:1 with boxes
# 
# # #raw velocities 
# reset
# set terminal jpeg
# set key off
# set output "plots/velocity_distribution_dark.jpeg"
# set title 'velocity'
# set ylabel 'counts'
# set xlabel 'velocity'
# set xrange[0:3.5]
# set yrange[0:6]
# plot "actual/dark_matter_velocity_dist.dat" using 1:2  with points
# 
# reset
# set terminal jpeg
# set key off
# set output "plots/velocity_distribution_light.jpeg"
# set title 'velocity'
# set ylabel 'counts'
# set xlabel 'velocity'
#  set boxwidth -2
# set xrange[0:3.5]
# set yrange[0:4]
# plot "actual/light_matter_velocity_dist.dat" using 1:2  with points

#############################################################################################################################################################
#velocity expected
# reset
# set terminal jpeg
# set key off
# set output "plots/velocity_distribution_dark_expected.jpeg"
# set title 'velocity'
# set ylabel 'counts'
# set xlabel 'velocity'
#  set boxwidth .01
# # set xrange[-.1:2]
# plot "actual/dark_matter_velocity_dist_expected.dat" using 1:2  with lines
# 
# reset
# set terminal jpeg
# set key off
# set output "plots/velocity_distribution_light_expected.jpeg"
# set title 'velocity'
# set ylabel 'counts'
# set xlabel 'velocity'
# # set xrange[-.1:2]
# plot "actual/light_matter_velocity_dist_expected.dat" using 1:2  with lines
# 
# 
# # reset
# # set terminal jpeg
# # set key off
# # set output "dist.jpeg"
# # set title 'distribution function'
# # set ylabel 'f'
# # set xlabel 'velocity'
# # # set xrange[-.1:2]
# # plot "~/Desktop/research/nbody_test/bin/dist.dat" using 1:2  with lines
