reset
set terminal jpeg
set key off
set output ".~/Desktop/research/data_testing/plots/energy/virial.jpeg"
set title 'Virial Ratio over time'
set ylabel 'Virial Ratio'
set xlabel 'Simulation Time (Gyr)'
# set xrange[0:4]
# set yrange[0:3]
plot "~/Desktop/research/data_testing/test_output/virial_output.txt" using 6:4  with points


# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/rho.jpeg"
# set title 'Rho vs r'
# set ylabel 'Rho'
# set xlabel 'r (Mpc)'
# set xrange[0:16]
# set yrange[0:.3]
# plot "~/Desktop/research/data_testing/test_output/rho_test.txt" using 2:1 with dots

# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_0gy.jpeg"
# set title 'Vel dis 0gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_0gy.txt" using 2:1 with dots
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_p25gy.jpeg"
# set title 'Vel dis .25gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_p25gy.txt" using 2:1 with dots
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_p5gy.jpeg"
# set title 'Vel dis .5gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_p5gy.txt" using 2:1 with dots
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_p75gy.jpeg"
# set title 'Vel dis .75gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_p75gy.txt" using 2:1 with dots
# 
# 
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_1gy.jpeg"
# set title 'Vel dis 1gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_1gy.txt" using 2:1 with dots
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_2gy.jpeg"
# set title 'Vel dis 2gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_2gy.txt" using 2:1 with dots
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_3gy.jpeg"
# set title 'Vel dis 3gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_3gy.txt" using 2:1 with dots
# 
# reset
# set terminal jpeg
# set key off
# set output ".~/Desktop/research/data_testing/plots/vel_dist/vel_dis_4gy.jpeg"
# set title 'Vel dis 4gy'
# set ylabel 'V'
# set xlabel 'r (Mpc)'
# set xrange[0:25]
# set yrange[0:8]
# plot "~/Desktop/research/data_testing/test_output/vel_dis_4gy.txt" using 2:1 with dots