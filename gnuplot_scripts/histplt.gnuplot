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

# reset
# set terminal png 
# # wxt persist
# set output "../quick_plots/hist_4g.png"
# set key off
# set title ''
# set xlabel 'lambda'
# set ylabel 'beta'
# # set zlabel 'Likelihood'
# # set xrange[0:6]
# set yrange[0:.5]
# 
# plot "../histogram_20kEMD_v150.hist"   using 2:4 with boxes