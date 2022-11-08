########################################################################################################################
# bp_math.py - Blood Pressure Calculations
########################################################################################################################
# Authors
#   Richard Johnston 
#
# Created Date
#   2022-11-06
#
# Description
#   Calculate blood pressure information
#
########################################################################################################################
# BEGIN WORKING DOCUMENT
########################################################################################################################


def bmi_calc(weight_kg, height_m):
    """Calculate BMI from weight in kg and height in meters"""
    bmi = int(weight_kg / height_m**2)
    return bmi
    
def predict_max_HR(age):
    """Age predicted maximal heart rate"""
    max_HR = 208 - 0.7 * age
    return max_HR
    
def bp_risk(systolic, diastolic):
    """Categorises whether blood pressure is elevated, 
 stage 1 hypertension or stage 2 hypertension"""
    if systolic >= 120 and systolic < 130 and diastolic < 80:
        bprisk = 'elevated BP'
    elif (systolic >= 130 and systolic < 140) or (diastolic >= 80 and diastolic < 90):
        bprisk = 'stage 1 hypertension'
    elif systolic >= 140 or diastolic >= 90:
         bprisk = 'stage 2 hypertension'
    else:
        bprisk = 'invalid values'
    return bprisk
    
def print_results(initials, weight, height, age, systolic, diastolic):
    bmi = bmi_calc(weight, height)
    max_HR = predict_max_HR(age)
    bprisk = bp_risk(systolic, diastolic)
    print("\n\t" + initials)
    print("\tweight = {}kg".format(weight))
    print("\theight = {}m".format(height))
    print("\tage = {} years old".format(age))
    print("\tblood pressure = {}/{}".format(systolic, diastolic))
    print("\n\tbmi = {}".format(bmi))
    print("\tpredicted maximal heart rate = {} bpm".format(max_HR))
    print("\tblood pressure = " + bprisk)
    print("\n")
    
# subject =  [initials, height, weight, age, systolic, diastolic]
subject1 = ['GA', 80, 1.6, 70, 120, 80]
subject2 = ['KT', 69, 1.5, 65, 136, 75]
subject3 = ['MN', 80, 1.6, 89, 113, 75]
subject4 = ['PW', 80, 1.7, 55, 141, 96]

subjects = [subject1, subject2, subject3, subject4]

for sub in subjects:
    initials, weight, height, age, systolic, diastolic = sub
    print_results(initials, weight, height, age, systolic, diastolic)