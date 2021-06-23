# -*- coding: cp949 -*- 
import csv

#test1
#test@
#create_merge
#test_branch
#test ttttt

def run_csv_file(open_file_name, write_file_name):

    # open_file_name = 'test_user7.csv'  #?떎?뻾?븷 ?뙆?씪 ?꽑?깮 (CSV)
    # write_file_name = 'write_user7_x.csv'

    save_address_time = []
    save_address_settemp = []
    Pre_csv_f_read_split = 0
    save_count = 0
    csv_f = open(open_file_name, 'r')
    csv_f_read = csv_f.readline()

    while csv_f_read :
        csv_f_read = csv_f.readline()
        
        if csv_f_read != '' :
            csv_f_read_split = csv_f_read.split(',')
            address_time = csv_f_read_split[0]
            address_settemp = csv_f_read_split[21]

        if (Pre_csv_f_read_split != address_settemp) :
            save_address_time.append(address_time)
            save_address_settemp.append(address_settemp)
            save_count += 1
        Pre_csv_f_read_split = address_settemp


    csv_f.close()

    csv_f = open(write_file_name,'a', newline='')
    wr = csv.writer(csv_f)
    wr.writerow(["time", "settemp"])
    #wr.writerow(["-----?떎?궡?삩?룄紐⑤뱶-----"])
    for i in range(0, save_count) :
        wr.writerow([save_address_time[i], save_address_settemp[i]])

    csv_f.close

    # csv_f = open(write_file_name,'a', newline='')
    # wr = csv.writer(csv_f)

    # if check_sum > 0:
    #     in_ave = check_sum / check_count
    #     wr.writerow(["?떎?궡?삩?룄 10遺? ?씠?긽 ?뿰?냽 ?뿰?냼議곌굔?뿉?꽌?쓽 ?떎?궡?삩 1?룄 ?긽?듅 ?룊洹좎떆媛?:"])
    #     wr.writerow([check_count," Case"])
    #     wr.writerow([round(in_ave,2)," Sec(Average)"])

    # if ondol_check_sum > 0 :
    #     ondol_ave = ondol_check_sum / ondol_check_count
    #     wr.writerow(["?삩?룎?삩?룄 10遺? ?씠?긽 ?뿰?냽 ?뿰?냼議곌굔?뿉?꽌?쓽 ?떎?궡?삩 1?룄 ?긽?듅 ?룊洹좎떆媛?:"])
    #     wr.writerow([ondol_check_count," Case"])
    #     wr.writerow([round(ondol_ave,2)," Sec(Average)"])

    # csv_f.close

    #return []


