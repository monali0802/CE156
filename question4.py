# Question 4:
# The NHS has given you a project to develop a data analysis task, which you will deliver in the
# form of a software (i.e. .py file).
# The data of this project are housekept under an excel file (.xlsx).

# A. Your first objective is to compute the total length of treatment for each patient. You can use
# Pandas dataframes and/or NumPy arrays to perform this. Print the results in a separate excel
# file called “Question4A”. (13 marks)

import pandas as pd
# get data from sheet2
df = pd.read_excel('PatientData_ProgrammingAssignment.xlsx', sheet_name='Sheet2', header=0, skiprows=3, usecols="B:C")
df.columns = ['Patient_ID', 'Drug_admin_date']
df_new = pd.DataFrame(df)

patient_id_array = []
new_sheet = []
p_id = ''
previous_index = ''
last_row = len(df_new['Patient_ID'])
for index, patient_id in df_new['Patient_ID'].items():
    new_row = []
    if p_id == '':
        p_id = patient_id
    if p_id != patient_id or last_row == (index+1):
        end_date = df_new['Drug_admin_date'][index-1].date()
        # find date diff in days and append in sheet row
        date = end_date - start_date
        new_row.append(p_id)
        new_row.append(date.days)
        new_sheet.append(new_row)
    if patient_id not in patient_id_array:
        start_date = df_new['Drug_admin_date'][index].date()
        previous_index = index
        p_id = patient_id
        patient_id_array.append(patient_id)

df_new = pd.DataFrame(new_sheet, columns=['Patient_ID', 'Length'])
df_new.to_excel('Question4A.xlsx')


# B. List separately the length of treatment for patients who use drug 390 vs. the generic. Print
# the results in a separate excel file called “Question4B”. (6 marks)
df1 = pd.read_excel('PatientData_ProgrammingAssignment.xlsx', sheet_name='Sheet1', header=0, skiprows=3, usecols="B:C")
df1.columns = ['Patient_ID', 'drug_390_admin_flag']
df_new1 = pd.DataFrame(df1)
new_sheet1 = []

for index1 in df_new1['Patient_ID'].keys():
    if df_new1['drug_390_admin_flag'][index1] == 0:
        new_sheet1.append('generic')
    else:
        new_sheet1.append('drug_390')

# Add column which drug used in precious dataframe
df_new['Drug'] = new_sheet1
df_new.to_excel('Question4B.xlsx')


# C. Compare the length of treatment by drug 390 vs. the generic by HR/HER2 status patients.
# Print the results in a separate excel file called “Question4C”. In total, there can be 4 different
# groups based on HR/HER2 status: (6 marks)
# HER2(+)_HR(+),
# HER2(+)_HR(-)
# HER2(-)_HR(+)
# HER2(-)_HR(-)

df1 = pd.read_excel('PatientData_ProgrammingAssignment.xlsx', sheet_name='Sheet1', header=0, skiprows=3, usecols="B,D:F")
df1.columns = ['Patient_ID', 'ER_positive', 'PR_positive', 'HER2_positive']
df_new2 = pd.DataFrame(df1)

new_sheet_both_positive = []
new_sheet_both_negative = []
new_sheet_herp_hrn = []
new_sheet_hern_hrp = []
for index2 in df_new2['Patient_ID'].keys():
    flag_p = flag_hern_hrp = flag_herp_hrn = flag_n = 0
    if (df_new2['ER_positive'][index2] == 1 or df_new2['PR_positive'][index2] == 1) and df_new2['HER2_positive'][index2] == 1:
        flag_p = 1
    elif(df_new2['ER_positive'][index2] == 0 and df_new2['PR_positive'][index2] == 0) and df_new2['HER2_positive'][index2] == 1:
        flag_herp_hrn = 1
    elif(df_new2['ER_positive'][index2] == 1 or df_new2['PR_positive'][index2] == 1) and df_new2['HER2_positive'][index2] == 0:
        flag_hern_hrp = 1
    else:
        flag_n = 1
    new_sheet_both_positive.append(flag_p)
    new_sheet_hern_hrp.append(flag_hern_hrp)
    new_sheet_herp_hrn.append(flag_herp_hrn)
    new_sheet_both_negative.append(flag_n)

# Add 4 column in precious dataframe
df_new['HER2(+)_HR(+)'] = new_sheet_both_positive
df_new['HER2(+)_HR(-)'] = new_sheet_herp_hrn
df_new['HER2(-)_HR(+)'] = new_sheet_hern_hrp
df_new['HER2(-)_HR(-)'] = new_sheet_both_negative

df_new.to_excel('Question4C.xlsx')