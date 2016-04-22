reset
set terminal jpeg
set key off
set ylabel 'counts'
set xlabel 'radius (Mpc)'
set xrange[0:50]
set yrange[0:.7]

# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_0gy.jpeg"
set title 'Histogram of Light Matter Distribution After 0Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_0gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_0gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 0Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_0gy.dat" using 2:1  with boxes

##################################################################


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_0p25gy.jpeg"
set title 'Histogram of Light Matter Distribution After .25Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_p25gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_0p25gy.jpeg"
set title 'Histogram of Dark Matter Distribution After .25Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_p25gy.dat" using 2:1  with boxes

##################################################################

# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_0p50gy.jpeg"
set title 'Histogram of Light Matter Distribution After .5Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_p5gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_0p50gy.jpeg"
set title 'Histogram of Dark Matter Distribution After .5Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_p5gy.dat" using 2:1  with boxes

##################################################################
# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_0p75gy.jpeg"
set title 'Histogram of Light Matter Distribution After .75Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_p75gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_0p75gy.jpeg"
set title 'Histogram of Dark Matter Distribution After .75Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_p75gy.dat" using 2:1  with boxes

##################################################################


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_1gy.jpeg"
set title 'Histogram of Light Matter Distribution After 1Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_1gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_1gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 1Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_1gy.dat" using 2:1  with boxes

##################################################################

# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_2gy.jpeg"
set title 'Histogram of Light Matter Distribution After 2Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_2gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_2gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 2Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_2gy.dat" using 2:1  with boxes

##################################################################

# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_3gy.jpeg"
set title 'Histogram of Light Matter Distribution After 3Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_3gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_3gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 3Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_3gy.dat" using 2:1  with boxes

##################################################################


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_light_4gy.jpeg"
set title 'Histogram of Light Matter Distribution After 4Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/light_matter_bins_4gy.dat" using 2:1  with boxes


# reset
# set terminal jpeg
# set key off
set output "plots/radii_distribution_dark_4gy.jpeg"
set title 'Histogram of Dark Matter Distribution After 4Gy'
# set ylabel 'counts'
# set xlabel 'radius (Mpc)'
# set xrange[0:30]
# set yrange[0:.7]
plot "binned_data/dark_matter_bins_4gy.dat" using 2:1  with boxes

##################################################################
