# Load in variables
f = h5py.File("parameters.hdf5", "r")
varname_list = list(f.keys())

for x in range(len(varname_list)):
    var_obj = f[varname_list[x]][()]
    exec(varname_list[x] + '= var_obj')
f.close()

####################################################################################################################################
# * Check the completeness of downloaded files
os.chdir(path_ltdr)
files = sorted(glob.glob('*.nc4'))
# date_seq_late = date_seq[6939:]
files_group = []
for idt in range(13879):
    # files_group_1day = [files.index(i) for i in files if 'A' + date_seq_late[idt] in i]
    files_group_1day = [files.index(i) for i in files if 'A' + date_seq[idt] in i]
    files_group.append(files_group_1day)
    print(idt)

file_miss = []
for idt in range(len(files_group)):
    if len(files_group[idt]) != 8:
        file_miss.append(date_seq[idt])
        print(date_seq[idt])
        # file_miss.append(date_seq_late[idt])
        # print(date_seq_late[idt])
        print(len(files_group[idt]))
    else:
        pass

    
# Find the indices of each month in the list of days between 1981 - 2018    
month_num = np.arange(1, 13)
month_num = [str(i).zfill(2) for i in month_num]
date_seq_mo = [date_seq[i][4:6] for i in range(len(date_seq))] # Create a sequence containing only month names

ind_month_gldas = []
for m in range(len(month_num)):
    ind_month_gldas_1mo = [i for i, s in enumerate(date_seq_mo) if month_num[m] in s]
    ind_month_gldas.append(ind_month_gldas_1mo)
