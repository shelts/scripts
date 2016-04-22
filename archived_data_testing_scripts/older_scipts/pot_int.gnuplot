reset
set terminal jpeg
set key on
set ylabel 'counts'
set xlabel 'potential'
set xrange[-20:0]
# set yrange[0:1000]



set output "../gnuplot_scripts/plots/pot/pot_int_light_0gy.jpeg"
set title 'Light Matter Potential Distribution Afte 0Gy'
plot "binned_data/pot_light_0gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark'
# , 'actual/light_potential_0gy.dat' using 1:2 with dots title 'pot'
# , "theory/theory_pot_int.dat"   using 1:2 with lines title 'both'


set output "../gnuplot_scripts/plots/pot/pot_int_dark_0gy.jpeg"
set title 'Dark Matter Potential Distribution Afte 0Gy'
plot "binned_data/pot_dark_0gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark'
# , 'actual/dark_potential_0gy.dat' using 1:2 with dots title 'pot'
# , "theory/theory_pot_int.dat"   using 1:2 with lines title 'both'


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_0p25gy.jpeg"
# set title 'Light Matter Potential Distribution After .25Gy'
# plot "binned_data/pot_light_p25gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_0p25gy.jpeg"
# set title 'Dark Matter Potential Distribution After .25Gy'
# plot "binned_data/pot_dark_p25gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_0p50gy.jpeg"
# set title 'Light Matter Potential Distribution After .5Gy'
# plot "binned_data/pot_light_p5gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_0p50gy.jpeg"
# set title 'Dark Matter Potential Distribution After .5Gy'
# plot "binned_data/pot_dark_p5gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_0p75gy.jpeg"
# set title 'Light Matter Potential Distribution After .75Gy'
# plot "binned_data/pot_light_p75gy.dat" using 2:1  with boxes title 'actual',  "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_0p75gy.jpeg"
# set title 'Dark Matter Potential Distribution After .75Gy'
# plot "binned_data/pot_dark_p75gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_1gy.jpeg"
# set title 'Light Matter Potential Distribution After 1Gy'
# plot "binned_data/pot_light_1gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_1gy.jpeg"
# set title 'Dark Matter Potential Distribution After 1Gy'
# plot "binned_data/pot_dark_1gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_2gy.jpeg"
# set title 'Light Matter Potential Distribution After 2Gy'
# plot "binned_data/pot_light_2gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_2gy.jpeg"
# set title 'Dark Matter Potential Distribution After 2Gy'
# plot "binned_data/pot_dark_2gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_3gy.jpeg"
# set title 'Light Matter Potential Distribution After 3Gy'
# plot "binned_data/pot_light_3gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_3gy.jpeg"
# set title 'Dark Matter Potential Distribution After 3Gy'
# plot "binned_data/pot_dark_3gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_light_4gy.jpeg"
# set title 'Light Matter Potential Distribution After 4Gy'
# plot "binned_data/pot_light_4gy.dat" using 2:1  with boxes title 'actual',  "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# 
# set output "../gnuplot_scripts/plots/pot/pot_int_dark_4gy.jpeg"
# set title 'Dark Matter Potential Distribution After 4Gy'
# plot "binned_data/pot_dark_4gy.dat" using 2:1  with boxes title 'actual', "theory/theory_pot_int.dat"   using 1:3 with lines title 'light',  "theory/theory_pot_int.dat"   using 2:4 with lines title 'dark' 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 