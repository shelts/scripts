

function get_rscale()
    tmp_r = 0.001
    cutoff = mass_l / 2.0
    while true do
        tmp_mass_enc_l = mass_l * tmp_r ^ 3.0 / (tmp_r * tmp_r + rscale_l * rscale_l ) ^ (3.0 / 2.0)
        
        if(tmp_mass_enc_l >= cutoff) then
            break
        else
            tmp_r = tmp_r + 0.001
        end
    end
    print( 'MASSENCL = ', tmp_mass_enc_l)
    tmp_mr = (mass_d_enc / mass_d) ^ (2.0 / 3.0)
    tmp_rs = (tmp_r * tmp_r) * ( 1.0 - tmp_mr) / tmp_mr
    tmp_rs = tmp_rs ^ (1.0 / 2.0)
    return tmp_rs
end

function get_md()
    tmp_r = 0.001
    cutoff = mass_l / 2.0
    while true do
        tmp_mass_enc_l = mass_l * tmp_r ^ 3.0 / (tmp_r * tmp_r + rscale_l * rscale_l ) ^ (3.0 / 2.0)
        
        if(tmp_mass_enc_l >= cutoff) then
            break
        else
            tmp_r = tmp_r + 0.001
        end
    end
    print( 'MASSENCL = ', tmp_mass_enc_l)
    
    tmp_md = mass_d_enc * (tmp_r * tmp_r + rscale_d * rscale_d ) ^ (3.0 / 2.0)
    tmp_md = tmp_md / tmp_r ^ 3.0
    return tmp_md
end