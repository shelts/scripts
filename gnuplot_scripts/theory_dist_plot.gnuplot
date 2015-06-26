# 
reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_r_theory.png"
set key off
set title 'v^2*f vs r'
set xlabel 'r'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:30]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_1.txt"   using 2:1 with dots


reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_v_theory.png"
set key off
set title 'v^2*f vs v'
set xlabel 'v'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:3.5]
# set yrange[0:0.6]

plot "~/Desktop/research/quick_plots/dist_1.txt"   using 3:1 with dots


reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/v_vs_r_theory.png"
set key off
set title 'v vs r'
set xlabel 'r'
set ylabel 'v'
# set zlabel 'Likelihood'
# set xrange[0:30]
# set yrange[0:5]
plot "~/Desktop/research/quick_plots/dist_1.txt"   using 2:3 with dots


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_r_theory_light.png"
set key off
set title 'v^2*f vs r'
set xlabel 'r'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:30]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_single_masses1.txt"   using 2:1 with dots


reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_v_theory_light.png"
set key off
set title 'v^2*f vs v'
set xlabel 'v'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:3]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_single_masses1.txt"   using 3:1 with dots


reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/v_vs_r_theory_light.png"
set key off
set title 'v vs r'
set xlabel 'r'
set ylabel 'v'
# set zlabel 'Likelihood'
# set xrange[0:3]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_single_masses1.txt"   using 2:3 with dots

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_r_theory_dark.png"
set key off
set title 'v^2*f vs r'
set xlabel 'r'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:30]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_single_masses2.txt"   using 2:1 with dots


reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/dist_vs_v_theory_dark.png"
set key off
set title 'v^2*f vs v'
set xlabel 'v'
set ylabel 'v^2*dist'
# set zlabel 'Likelihood'
# set xrange[0:3]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_single_masses2.txt"   using 3:1 with dots


reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/v_vs_r_theory_dark.png"
set key off
set title 'v vs r'
set xlabel 'r'
set ylabel 'v'
# set zlabel 'Likelihood'
# set xrange[0:3]
# set yrange[0:1.8]

plot "~/Desktop/research/quick_plots/dist_single_masses2.txt"   using 2:3 with dots
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
