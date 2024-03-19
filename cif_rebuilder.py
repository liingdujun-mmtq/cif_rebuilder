cif_file="D:\python\cif_rebuilder\W-bcc.cif"
cif_data=[]
# read_data
reduilder_signal=0
with open(cif_file) as raw_data:
    lines=raw_data.readlines()
    for i in lines:    
        if reduilder_signal==1:
            rebuild_i=i.split(' ')
            del rebuild_i[0]
            output_i=''
            for j in rebuild_i:
                output_i+=j
            cif_data.append(output_i)
        if reduilder_signal==0:
            cif_data.append(i)
        if '_space_group_symop_operation_xyz'in i:
            reduilder_signal=1
        elif 'loop_' in i:
            reduilder_signal=0
 
with open(cif_file[0:-4]+'-rebuild'+'.cif','w') as file:
    for i in cif_data:
        file.writelines(i)
print("Reduild Finished!")