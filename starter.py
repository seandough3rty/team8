# All inputs will need to be added within " "
# if we have time I will find a way to auto do this so it is not on the user

import os

csv_file_name = input("What is the name of your .csv file? ")
#print(type(csv_file_name))

desired_run_time_in_seconds = input("Desired Run Time (s): ")
#print(type(desired_run_time_in_seconds))

csv_array_in_sec = input("Is your csv aray in microseconds? (t/f) ")
#print(type(csv_array_in_sec))
desired_processing_units = input("Desired number of processing units: ")
desired_processing_units_int = int(desired_processing_units)
#print(type(desired_processing_units))

if desired_processing_units_int == 1:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs

if desired_processing_units_int == 2:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs

if desired_processing_units_int == 3:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs

if desired_processing_units_int == 4:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs

if desired_processing_units_int == 5:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    pu5_pr = input("Desired processing rate for processing unit 5: ")
    pu5_bs = input("Desired buffer size for processing unit 5: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs

if desired_processing_units_int == 6:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    pu5_pr = input("Desired processing rate for processing unit 5: ")
    pu5_bs = input("Desired buffer size for processing unit 5: ")
    pu6_pr = input("Desired processing rate for processing unit 6: ")
    pu6_bs = input("Desired buffer size for processing unit 6: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs

if desired_processing_units_int == 7:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    pu5_pr = input("Desired processing rate for processing unit 5: ")
    pu5_bs = input("Desired buffer size for processing unit 5: ")
    pu6_pr = input("Desired processing rate for processing unit 6: ")
    pu6_bs = input("Desired buffer size for processing unit 6: ")
    pu7_pr = input("Desired processing rate for processing unit 7: ")
    pu7_bs = input("Desired buffer size for processing unit 7: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs

if desired_processing_units_int == 8:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    pu5_pr = input("Desired processing rate for processing unit 5: ")
    pu5_bs = input("Desired buffer size for processing unit 5: ")
    pu6_pr = input("Desired processing rate for processing unit 6: ")
    pu6_bs = input("Desired buffer size for processing unit 6: ")
    pu7_pr = input("Desired processing rate for processing unit 7: ")
    pu7_bs = input("Desired buffer size for processing unit 7: ")
    pu8_pr = input("Desired processing rate for processing unit 8: ")
    pu8_bs = input("Desired buffer size for processing unit 8: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs + " " + pu8_pr + " " + pu8_bs

if desired_processing_units_int == 9:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    pu5_pr = input("Desired processing rate for processing unit 5: ")
    pu5_bs = input("Desired buffer size for processing unit 5: ")
    pu6_pr = input("Desired processing rate for processing unit 6: ")
    pu6_bs = input("Desired buffer size for processing unit 6: ")
    pu7_pr = input("Desired processing rate for processing unit 7: ")
    pu7_bs = input("Desired buffer size for processing unit 7: ")
    pu8_pr = input("Desired processing rate for processing unit 8: ")
    pu8_bs = input("Desired buffer size for processing unit 8: ")
    pu9_pr = input("Desired processing rate for processing unit 9: ")
    pu9_bs = input("Desired buffer size for processing unit 9: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs + " " + pu8_pr + " " + pu8_bs + " " + pu9_pr + " " + pu9_bs

if desired_processing_units_int == 10:
    pu1_pr = input("Desired processing rate for processing unit 1: ")
    pu1_bs = input("Desired buffer size for processing unit 1: ")
    pu2_pr = input("Desired processing rate for processing unit 2: ")
    pu2_bs = input("Desired buffer size for processing unit 2: ")
    pu3_pr = input("Desired processing rate for processing unit 3: ")
    pu3_bs = input("Desired buffer size for processing unit 3: ")
    pu4_pr = input("Desired processing rate for processing unit 4: ")
    pu4_bs = input("Desired buffer size for processing unit 4: ")
    pu5_pr = input("Desired processing rate for processing unit 5: ")
    pu5_bs = input("Desired buffer size for processing unit 5: ")
    pu6_pr = input("Desired processing rate for processing unit 6: ")
    pu6_bs = input("Desired buffer size for processing unit 6: ")
    pu7_pr = input("Desired processing rate for processing unit 7: ")
    pu7_bs = input("Desired buffer size for processing unit 7: ")
    pu8_pr = input("Desired processing rate for processing unit 8: ")
    pu8_bs = input("Desired buffer size for processing unit 8: ")
    pu9_pr = input("Desired processing rate for processing unit 9: ")
    pu9_bs = input("Desired buffer size for processing unit 9: ")
    pu10_pr = input("Desired processing rate for processing unit 10: ")
    pu10_bs = input("Desired buffer size for processing unit 10: ")
    desired_processing_units = str(desired_processing_units)
    caller = "python3 main.py "+ csv_file_name+ " " + desired_run_time_in_seconds + " " + csv_array_in_sec + " " + desired_processing_units + " " + pu1_pr + " " + pu1_bs + " " + pu2_pr + " " + pu2_bs + " " + pu3_pr + " " + pu3_bs + " " + pu4_pr + " " + pu4_bs + " " + pu5_pr + " " + pu5_bs + " " + pu6_pr + " " + pu6_bs + " " + pu7_pr + " " + pu7_bs + " " + pu8_pr + " " + pu8_bs + " " + pu9_pr + " " + pu9_bs + " " + pu10_pr + " " + pu10_bs + " "

#print(caller)

os.system(caller)
