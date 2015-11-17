reset
set terminal wxt persist
set ylabel 'v'
set zlabel 'v^2*dist'
# set key off
set title 'v^2*f vs r'
# set ylabel 'v'
# set zlabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:3]
# set yrange[0:1.8]

# splot "~/Desktop/research/quick_plots/dist.txt"   using 1:2:5 with points pointtype 7 pointsize .1 title 'func' 



# reset
# set terminal png 
# # wxt persist
# set output "~/Desktop/research/quick_plots/dist_vs_r.png"
# # set key off
# set title 'v^2*f vs r'
# set xlabel 'r'
# set ylabel 'v^2*dist'
# set xrange[0:5]
# # set yrange[0:50]
# 
# plot "~/Desktop/research/quick_plots/dist2.txt"   using 1:2 with lines title 'both', '' using 1:3 with lines title 'theoretical'
# # ,  ''  u 1:4 with lines title 'dark', ''  u 1:3 with lines title 'light'

reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_v.png"
# set key off
set title 'v^2*f vs v'
set xlabel 'v'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:3.5]
# set yrange[0:2]

plot "~/Desktop/research/quick_plots/dist.txt"   using 1:2 with lines title 'calc', '' using 1:3 with lines title 'theoretical'
# , '' u 1:4 with lines title 'frac'


# reset
# set terminal png 
# # wxt persist
# set output "~/Desktop/research/quick_plots/v_vs_r.png"
# set key off
# set title 'v vs r'
# set xlabel 'r'
# set ylabel 'v'
# # set zlabel 'Likelihood'
# # set xrange[0:30]
# # set yrange[0:5]
# 
# plot "~/Desktop/research/quick_plots/dist.txt"   using 1:2 with dots
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 