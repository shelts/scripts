# Theory:
reset
set terminal png 
# wxt persist
set output "~/Desktop/research/quick_plots/pot.png"
# set key off
set title 'potential vs r'
set xlabel 'r'
set ylabel 'potential'
# set zlabel 'Likelihood'
# set xrange[0:2.5]
# set yrange[0.3:.5]

plot "~/Desktop/research/quick_plots/pot.txt"   using 2:1 with lines title 'light', ''  using 2:3 with lines title 'dark', '' using 2:4 with lines title 'both'
