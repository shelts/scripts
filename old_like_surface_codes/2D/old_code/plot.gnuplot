reset
set terminal wxt persist
set key off
set output "plots/ft_vs_bt.jpeg"
set title 'Ft vs bt'
set ylabel 'y'
set xlabel 'x value'
set zlabel 'like'
# set xrange[0:6]
# set yrange[-999:1]
set palette rgbformula -7,2,-7
set cbrange [-1000:0]
plot "<paste parameter_data/ft_vs_bt.txt likelihood_data/ft_vs_bt_data.txt"   using 1:2:3  with image
# points pointtype 7 pointsize .2

# set terminal wxt persist

