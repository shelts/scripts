def run_sweep(start1, end1, intv1, para1, start2, end2, intv2, para2):
    counter1 = start1
    counter2 = start2
    name1 = str(counter1)
    name2 = str(counter2)
   
    sweep_name = ""  #sweep name
    
    pipe_name = para1 + "_" + para2  #name of the files
    
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_name)
    data_vals   = folder + "parameter_sweeps" + sweep_name + "/" + pipe_name + "_vals.txt"
    f = open(data_vals, 'w')
    
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    do_correct1 = False
    do_correct2 = False
    
    while counter1 < end1 + intv1:  #this iterates over one parameter on the outside and another on the inside
        counter2 = start2  #restart the inner parameter iteration from beginning
        name2 = str(counter2)
        
        #checks which parameter needs to be updated for the outside loop and updates it
        #also checks to see if the correct answer for the outside lies between current val and next increment, if so it sets do_correct1 to true
        ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct1 = para_init(para1, counter1, intv1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
        
        
        while counter2 < end2 + intv2:  #inner loop.
            output_hist = folder + pipe_name + "_hists/" + "arg_"  #resets the output hist name
           
            #checks which parameter needs to be updated for the inner loop and updates it
            #also checks if the correct answer for the inner lies between current val and next increment, if so sets do_correct2
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct2 = para_init(para2, counter2, intv2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
            
            
            output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"  #appends the current parameters to the output hist name
            
            nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)  #runs the sim with these parameters
            
            f.write("%s\t%s\n" % (name1, name2))  #writes the value to the value files.
            
            
            if(do_correct2 == True):  #if the correct answer is between the interval for the inner loop, run the correct answer
                write_correct(f, para2, name1)  #writes the correct answers to the value file
                
                output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"  #sets the output hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                
                do_correct2 = False  #resets do_correct2
            
            
            counter2 += intv2  #increment the inner loop value
            name2 = str(counter2)
        
        
        if(do_correct1 == True):  #if the outer loop correct answer was found in the interval
            name1_save = name1  #save the current iterated value for the outer loop
            
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name1 = correct_set(para1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)  #set the correct values for the outer loop
                
            
            counter2 = start2  #run the same inner loop as above
            name2 = str(counter2)
            while counter2 < end2 + intv2:
                output_hist = folder + pipe_name + "_hists/" + "arg_"  #resets the output hist name
                
                #checks which parameter needs to be updated for the inner loop and updates it
                #also checks if the correct answer for the inner lies between current val and next increment, if so sets do_correct2
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, do_correct2 = para_init(para2, counter2, intv2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )
                
                
                output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"  #appends the current parameters to the output hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                
                f.write("%s\t%s\n" % (name1, name2))  #writes the correct values to the value file
                
                
                if(do_correct2 == True):  #if the correct answer for the inner loop was found 
                    write_correct(f, para2, name1)  #write the correct answers to the value file
                    
                    output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"  #sets the output hist name
                    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, pipe_name, sweep_name)
                    do_correct2 = False  #resets do_correct2

                
                counter2 += intv2  #iterates the inner loop value
                name2 = str(counter2)
            
            name1 = name1_save  #once the correct value was put in, reset the counter to previous value so that iteration continues
            do_correct1 = False  #reset do_correct1
        
        counter1 += intv1  #iterates the outer loop value
        name1 = str(counter1)
    f.close()#close the files
    return 0





def random_iteration_sweep(start1, end1, N1, para1, start2, end2, N2, para2):
    counter1 = 0.0
    counter2 = 0.0
    #sweep name
    sweep_name = "_2d_rand_iter"
    #name of the files
    pipe_name = para1 + "_" + para2
    hist_path = folder + pipe_name + "_hists/" + "arg_"
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_name)
    data_vals   = folder + "parameter_sweeps" + sweep_name + "/" + pipe_name + "_vals.txt"
    f = open(data_vals, 'w')
    
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    para = parameters(ft_c, bt_c, r_c, rr_c, m_c, mr_c, hist_path, sweep_name, pipe_name)
    
     #this iterates over one parameter on the outside and another on the inside
    while counter1 < N1:
        if(counter1 == 0.0):#since this has random iteration, put the correct value first
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name1 = correct_set(para1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)  #sets the correct value for the outerloop

            counter2 = 0.0#reset the inner loop counter
            while counter2 < N2:#runs the inner loop iteration
                if(counter2 == 0.0):#put the correct value for the inner loop first
                    ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name2 = correct_set(para2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)  #sets the correct value for the inner loop
                    output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"  #sets the name of the output hist
                    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, pipe_name, sweep_name)
                    f.write("%s\t%s\n" % (name1, name2))  #write values to value file
                
                output_hist = folder + pipe_name + "_hists/" + "arg_"  #reset output file name
                
                name2 = random.uniform(0.0, 1.0) * (end2 - start2) + start2  #randomly select a value in the sweep range of inner loop parameter
                name2 = str(name2)
                
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp = para_init_rand(para2, name2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )  #set the values for the correct parameter for the inner loop
                
                output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist" #append the values to the hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                f.write("%s\t%s\n" % (name1, name2)) #write values to value file
                
                counter2 += 1 #iterate counter. want a certain number of points
        
        name1 = random.uniform(0.0, 1.0) * (end1 - start1) + start1  #after putting correct answer, randomly select value from sweep range for outer loop parameter
        name1 = str(name1)
        
        ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp = para_init_rand(para1, name1, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )  #set the values for the correct parameter for the inner loop
        
        counter2 = 0.0  #reset the counter for the inner loop
        while counter2 < N2:
            if(counter2 == 0.0):#put the correct value for the inner loop first
                ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, name2 = correct_set(para2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp)
                
                output_hist = folder + pipe_name + "_hists/" + "arg_" + ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist" #set the hist name
                nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
                
                f.write("%s\t%s\n" % (name1, name2)) #write values to value file
                
            
            output_hist = folder + pipe_name + "_hists/" + "arg_" #reset the name of the hists
            
            name2 = random.uniform(0.0, 1.0) * (end2 - start2) + start2 #randomly select a value within the sweep range for the inner loop
            name2 = str(name2)
           
            ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp = para_init_rand(para2, name2, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp )  #assign values to the correct parameter for the inner loop
                
            output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
            nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, pipe_name, sweep_name)
            f.write("%s\t%s\n" % (name1, name2))
            counter2 += 1
        counter1 +=1
        
    f.close()
    return 0