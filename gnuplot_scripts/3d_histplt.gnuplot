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

# splot "./histogram_out_even_seed498649_10kEMD_4_1_p5_p2_30_p2.hist"   using 2:3:4 
splot "../histogram_20kEMD_v150.hist"   using 2:3:4

reset
set terminal png 
# wxt persist
set output "../quick_plots/hist_1g_3d.png"
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
# splot "./histogram_50kEMD_v150.hist"   using 2:3:4