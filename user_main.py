
# -*- coding: cp949 -*- 
from user_csv_analyzer import run_csv_file
import os
import csv


for path, dirs, files in os.walk("./input_file"):
    user_files=(files)

#user_file = ['user4.csv', 'test_user7.csv' ]
in_path = "./input_file"
out_path = "./output_file"
# file_name = []
# in_count = []
# in_avev = []
# on_count = []
# on_ave = []
# in_count_sum = 0
# on_count_sum = 0
# in_count_sum_ave = 0
# on_count_sum_ave = 0
# in_count_zero_X = 0
# on_count_zero_X = 0

# in_count_ave = 0
# on_count_ave = 0

#result = []
if __name__ == '__main__':
    
    for i in user_files :
        run_csv_file(in_path+'/'+i,(out_path+'/'+'write_.csv'))
        #run_csv_file(in_path+'/'+i,'result.csv')
        # file_name.append(i)
        # in_count.append(result1)
        # in_avev.append(result2)
        # on_count.append(result3)
        # on_ave.append(result4)
    
    # print (file_name)
    # print (in_count)
    # print (in_avev)
    # print (on_count)
    # print (on_ave)
    # print (user_files)

    # csv_f = open('result.csv','w', newline='')
    # wr = csv.writer(csv_f)

    # wr.writerow(["case: ���濬�Ұ� OFF ���� ON�� �ɶ� �ǳ��µ��� 1�� ����ϴ� �ð��� ����Ͽ�, 10�� �̻� ���� ������ ��ϵ��� ī��Ʈ"])
    # wr.writerow(["----------------------------------------------------------------------------------------------------"])
    # wr.writerow(["���� �̸�", "�ǿ� case", "�ǿ� ��� 1�� ��� �ð�[��]", "�µ� case","�µ� ��� 1�� ��� �ð�[��]"])
    # for i in range(0, len(file_name)) :
    #     wr.writerow([file_name[i],in_count[i], round(in_avev[i],2),on_count[i], round(on_ave[i],2)])
    #     in_count_sum += in_count[i]
    #     on_count_sum += on_count[i]
    #     in_count_sum_ave += in_avev[i]
    #     on_count_sum_ave += on_ave[i]
    #     if in_avev[i] != 0 :
    #         in_count_zero_X += 1
    #     if on_ave[i] != 0 :
    #         on_count_zero_X += 1
    
    # if in_count_zero_X != 0 :
    #     in_count_ave = (in_count_sum_ave / in_count_zero_X)/60
    # if on_count_zero_X != 0 :
    #     on_count_ave = (on_count_sum_ave / on_count_zero_X)/60

    # wr.writerow(["----------------------------------------------------------------------------------------------------"])
    # wr.writerow(["[all]�ǿ� Case", "[all]�ǿ� ��� 1�� ��� �ð�[��]", "[all]�µ� case", "[all]�µ� ��� 1�� ��� �ð�[��]"])
    # wr.writerow([in_count_sum, round(in_count_ave,2), on_count_sum, round(on_count_ave,2)])

    #print (in_count_zero_X)




    
