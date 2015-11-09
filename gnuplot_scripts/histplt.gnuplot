reset
set terminal png 
# wxt persist
set output "~/Desktop/research/hist.png"
set key off
set title ''
set xlabel 'lambda'
set ylabel 'beta'
# set zlabel 'Likelihood'
# set xrange[0:6]
# set yrange[0:.5]
plot "~/Desktop/research/histogram_20kEMD_v150_0.hist"   using 2:3:4 with image


reset
set terminal png 
# wxt persist
set output "../quick_plots/hist_inital_3d.png"
set key off
# set output "./mass_massratio_precise.jpeg"
set title ''
set xlabel 'lambda'
set ylabel 'beta'
# set zlabel 'Likelihood'
# set xrange[0:6]
# set yrange[-30:30]
set pm3d map 
splot "../histogram_20kEMD_v150.hist"   using 2:3:4
