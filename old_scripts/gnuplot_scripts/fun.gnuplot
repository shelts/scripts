reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/func_vs_r.png"
set key off
set title 'distribution funtion integrand'
set xlabel 'r prime'
set ylabel 'func'
set xrange[0:20]
# set yrange[0:50]

plot "~/Desktop/research/quick_plots/fun.txt"   using 1:2 with lines 


# reset
# set terminal png 
# # wxt persist
# set output "~/Desktop/research/quick_plots/func_vs_v.png"
# set key off
# set title 'distribution funtion integrand'
# set xlabel 'v'
# set ylabel 'func'
# # set xrange[0:20]
# # set yrange[0:50]
# 
# plot "~/Desktop/research/quick_plots/fun2.txt"   using 1:2 with lines 
# 

# reset
# set terminal png 
# # wxt persist
# set output "~/Desktop/research/quick_plots/denom_vs_r.png"
# set key off
# set title 'distribution funtion integrand denom'
# set xlabel 'r'
# set ylabel 'denom'
# # set xrange[0:10]
# # set yrange[0:2]
# 
# plot "~/Desktop/research/quick_plots/denom.txt"   using 1:2 with lines 
# 
# reset
# set terminal png 
# # wxt persist
# set output "~/Desktop/research/quick_plots/num_vs_r.png"
# set key off
# set title 'distribution funtion integrand num'
# set xlabel 'r'
# set ylabel 'num'
# set xrange[0:8]
# # set yrange[0:50]
# 
# plot "~/Desktop/research/quick_plots/num.txt"   using 1:2 with lines 