#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:30:27 2021

@author: ed
"""
#%%

def pixel_dict_build(output):
    #takes string of path where I have each file name with a list of the pixel areas of all Buchnera. Returns the file as a dictionary - file names as key, list of buch as values
    pixel_values = {}
    with open(output) as file:
        for line in file:
            name, b_list = line.split(':')
            pixel_values[name] = b_list
    return pixel_values

dictionary = pixel_dict_build('/Users/ed/Downloads/PIPE_len2.txt')
#%%
def pixel_to_micron(dictonary): #Conversion dict is a dictionary of the name of each image, and its pixels:micron ratio
    conversion_dict = {"qc20210607_LSR1_N2_flat_1_DAPI.png" :21.1058,
"qc20201113_LSR1_N2_flat_5_4x_DAPI.png" :36.3714,
"qc20201216_LSR1_N2_flat_9_DAPI.png" :15.1274,
"qc20201216_LSR1_N2_flat_2_DAPI.png" :23.6861,
"qc20201216_LSR1_N2_flat_3_DAPI.png" :25.6488,
"qc20201216_LSR1_N2_flat_5_DAPI.png" :19.8101,
"qc20201216_LSR1_N2_flat_1_DAPI.png" :24.708,
"qc20201216_LSR1_N2_flat_6_DAPI.png" :19.8101,
"qc20210709_LSR1_N2_flat_14_DAPI.png" :26.5819,
"qc20210709_LSR1_N2_flat_3_DAPI.png" :19.9068,
"qc20210709_LSR1_N2_flat_2_DAPI.png" :24.9906,
"qc20210709_LSR1_N2_flat_9_DAPI.png" :19.1144,
"qc20210709_LSR1_N2_flat_8_DAPI.png" :19.1144,
"qc20210709_LSR1_N2_flat_12_DAPI.png" :22.5228,
"qc20210709_LSR1_N2_flat_13_DAPI.png" :22.1239,
"qc20210709_LSR1_N2_flat_4_DAPI.png" :22.1239,
"qc20210709_LSR1_N2_flat_5_DAPI.png" :22.1239,
"qc20210709_LSR1_N2_flat_1_DAPI.png" :20.2657,
"qc20210709_LSR1_N2_flat_11_DAPI.png" :20.2657,
"qc20210709_LSR1_N2_flat_10_DAPI.png" :23.3044,
"qc20210709_LSR1_N2_flat_7_DAPI.png" :25.3999,
"qc20210709_LSR1_N2_flat_6_DAPI.png" :26.5819,
"qc20200831_LSR1_N3_10_DAPI.png" :15.9865,
"qc20200831_LSR1_N3_11_DAPI.png" :15.1274,
"qc20210629_LSR1_N3_flat_6_DAPI.png" :19.6818,
"qc20210629_LSR1_N3_flat_7_DAPI.png" :19.6818,
"qc20200831_LSR1_N3_9_DAPI.png" :16.6221,
"qc20210629_LSR1_N3_flat_1_DAPI.png" :20.6312,
"qc20200831_LSR1_N3_6_DAPI.png" :16.8395,
"qc20200831_LSR1_N3_7_DAPI.png" :16.8395,
"qc20210629_LSR1_N3_flat_11_DAPI.png" :19.6818,
"qc20210629_LSR1_N3_flat_10_DAPI.png" :19.6818,
"qc20210629_LSR1_N3_flat_5_DAPI.png" :26.9736,
"qc20210629_LSR1_N3_flat_4_DAPI.png" :26.9736,
"qc20210607_LSR1_N3_flat_4_DAPI.png" :16.6762,
"qc20210629_LSR1_N3_flat_2_DAPI.png" :13.0485,
"qc20210629_LSR1_N3_flat_3_DAPI.png" :13.0485,
"qc20210607_LSR1_N3_flat_2_DAPI.png" :19.3017,
"qc20210629_LSR1_N3_flat_8_DAPI.png" :19.6818,
"qc20210629_LSR1_N3_flat_9_DAPI.png" :19.6818,
"qc20200812_LSR1_N4_vecta_10_DAPI.png" :15.5922,
"qc20210614_LSR1_N4_flat_5_DAPI.png" :13.147,
"qc20210614_LSR1_N4_flat_2_DAPI.png" :13.5233,
"qc20210614_LSR1_N4_flat_6_DAPI.png" :13.147,
"qc20200812_LSR1_N4_vecta_13_DAPI.png" :13.7365,
"qc20210614_LSR1_N4_flat_1_DAPI.png" :15.4755,
"qc20200812_LSR1_N4_vecta_14_DAPI.png" :11.3587,
"qc20200812_LSR1_N4_vecta_15_DAPI.png" :14.0069,
"qc20200812_LSR1_N4_vecta_8_DAPI.png" :11.4142,
"qc20210705+LSR1_N4_flat_10_DAPI.png" :14.5726,
"qc20210705+LSR1_N4_flat_5_DAPI.png" :13.3704,
"qc20210705+LSR1_N4_flat_4_DAPI.png" :11.7409,
"qc20210705+LSR1_N4_flat_9_DAPI.png" :14.5726,
"qc20210705+LSR1_N4_flat_3_DAPI.png" :11.7409,
"qc20210705+LSR1_N4_flat_6_DAPI.png" :11.8366,
"qc20210705+LSR1_N4_flat_7_DAPI.png" :14.1526,
"qc20210705+LSR1_N4_flat_14_DAPI.png" :17.9119,
"qc20210705+LSR1_N4_flat_1_DAPI.png" :13.678,
"qc20210630_LSR1_D9_flat_15_DAPI.png" :14.62,
"qc20210630_LSR1_D9_flat_14_DAPI.png" :16.1956,
"qc20210630_LSR1_D9_flat_2_DAPI.png" :24.4683,
"qc20210630_LSR1_D9_flat_9_DAPI.png" :15.4503,
"qc20210630_LSR1_D9_flat_8_DAPI.png" :14.2218,
"qc20210630_LSR1_D9_flat_12_DAPI.png" :16.6221,
"qc20210630_LSR1_D9_flat_13_DAPI.png" :18.0286,
"qc20210630_LSR1_D9_flat_4_DAPI.png" :17.0321,
"qc20210630_LSR1_D9_flat_5_DAPI.png" :16.9218,
"qc20210614_LSR1_D9_flat_1_DAPI.png" :13.1763,
"qc20210115_LSR1_flat_5_DAPI.png" :11.8752,
"qc20210630_LSR1_D9_flat_16_DAPI.png" :14.62,
"qc20210630_LSR1_D9_flat_1_DAPI.png" :13.1763,
"qc20210115_LSR1_flat_7_DAPI.png" :13.1763,
"qc20210614_LSR1_D9_flat_2_DAPI.png" :15.2261,
"qc20210630_LSR1_D9_flat_10_DAPI.png" :15.4503,
"qc20210630_LSR1_D9_flat_6_DAPI.png" :14.2218,
"qc20200929_LSR1_D13_8_DAPI.png" :12.0697,
"qc20200929_LSR1_D13_9_DAPI.png" :12.3073,
"qc20210614_LSR1_D13_flat_4_DAPI.png" :15.5006,
"qc20210614_LSR1_D13_flat_15_DAPI.png" :16.4878,
"qc20210614_LSR1_D13_flat_12_DAPI.png" :19.1457,
"qc20210614_LSR1_D13_flat_13_DAPI.png" :16.1432,
"qc20200929_LSR1_D13_12_DAPI.png" :12.4683,
"qc20210614_LSR1_D13_flat_5_phal_DAPI.png" :15.5006,
"qc20210614_LSR1_D13_flat_8_DAPI.png" :13.2623,
"qc20210614_LSR1_D13_flat_9_DAPI.png" :17.5092,
"qc20210614_LSR1_D13_flat_17_DAPI.png" :17.0323,
"qc20210614_LSR1_D13_flat_6_DAPI.png" :15.5006,
"qc20210614_LSR1_D13_flat_7_DAPI.png" :16.6222,
"qc20210614_LSR1_D13_flat_11_DAPI.png" :14.2914,
"qc20210614_LSR1_D13_flat_10_DAPI.png" :15.5007,
"qc20200929_LSR1_D13_11_DAPI.png" :12.4683,
"qc20200929_LSR1_D13_10_DAPI.png" :12.4683,
"qc20201216_LSR1_D16_flat_13_DAPI.png" :16.1432,
"qc20201216_LSR1_D16_flat_5_DAPI.png" :10.931,
"qc20201216_LSR1_D16_flat_4_DAPI.png" :12.2674,
"qc20200910_LSR1_D16_9_DAPI.png" :17.4807,
"qc20201216_LSR1_D16_flat_16_DAPI.png" :19.1767,
"qc20200910_LSR1_D16_14_DAPI.png" :13.091,
"qc20201216_LSR1_D16_flat_11_DAPI.png" :17.8828,
"qc20201216_LSR1_D16_flat_10_DAPI.png" :9.9804,
"qc20201216_LSR1_D16_flat_2_DAPI.png" :15.5006,
"qc20200910_LSR1_D16_5_DAPI.png" :10.6505,
"qc20201216_LSR1_D16_flat_8_DAPI.png" :12.4278,
"qc20201216_LSR1_D16_flat_9_DAPI.png" :13.3921,
"qc20200910_LSR1_D16_11_DAPI.png" :15.7962,
"qc20200910_LSR1_D16_10_DAPI.png" :12.6237,
"qc20201216_LSR1_D16_flat_15_DAPI.png" :19.1767,
"qc20201216_LSR1_D16_flat_14_DAPI.png" :17.8828,
"qc20201216_LSR1_D16_flat_6_DAPI.png" :14.2681,
"qc20201216_LSR1_D16_flat_12_DAPI.png" :15.1029,
"qc20210629_LSR1_D23_flat_4_DAPI.png" :18.2645,
"qc20210128_LSR1_D23_flat_9_DAPI.png" :10.9132,
"qc20210128_LSR1_D23_flat_15_DAPI.png" :9.4748,
"qc20210629_LSR1_D23_flat_7DAPI.png" :17.1989,
"qc20210128_LSR1_D23_flat_13_DAPI.png" :12.2873,
"qc20210629_LSR1_D23_flat_10_DAPI.png" :15.152,
"qc20210629_LSR1_D23_flat_11_DAPI.png" :15.152,
"qc20210629_LSR1_D23_flat_3_DAPI.png" :15.2756,
"qc20210629_LSR1_D23_flat_2_DAPI.png" :13.5894,
"qc20210629_LSR1_D23_flat_9_DAPI.png" :15.152,
"qc20210629_LSR1_D23_flat_8_DAPI.png" :16.7576,
"qc20210629_LSR1_D23_flat_6_DAPI.png" :10.3603,
"qc20210629_LSR1_D23_flat_12_DAPI.png" :13.8794,
"qc20210629_LSR1_D23_flat_1_DAPI.png" :16.0646,
"qc20210128_LSR1_D23_flat_10_DAPI.png" :10.3604,
"qc20210128_LSR1_D23_flat_11_DAPI.png" :9.3525
}
    output_dictionary ={}
    for key in dictionary.keys():
        print(key)
        ratio = conversion_dict[key]
        print(ratio)
        micron_list =[]
        print(dictionary[key])
        nospace = dictionary[key].replace(" ", "") #removes spaces from Buchnera pixel area list
        nobracket = nospace.strip('][\n,') #removes square brackets from list, they are added later by the split function below.
        aslist = nobracket.split(',') #Hoping this gives a list of integers that I can iterate over.
        aslist = list(aslist)
        print(aslist) #print to see how far through loop we're getting
        for i in aslist:
            micron_value = int(i)/(ratio**2)
            micron_list.append(micron_value)         
        output_dictionary[key] = micron_list
    return output_dictionary
        
#%%
Result = pixel_to_micron(dictionary)

#%%
N2 = []
N3 = []
N4 = []
D9 = []
D13 = []
D16 = []
D23 = []
lol = [N2, N3, N4, D9, D13, D16, D23]

import re

for key in Result.keys():
    if bool(re.search('N2', key)):
        N2.append(key)
    elif bool(re.search('N3', key)):
        N3.append(key)
    elif bool(re.search('N4', key)):
        N4.append(key)
    elif bool(re.search('D9', key)):
        D9.append(key)
    elif bool(re.search('D13', key)):
        D13.append(key)
    elif bool(re.search('D16', key)):
        D16.append(key)
    elif bool(re.search('D23', key)):
        D23.append(key)
    else:
        D9.append(key)
        

#%% - Use these lists of keys to make lists of list of values, and then sum across
        
def combine(age, agevalue):
    for im in age:
        for i in Result[im]:
            agevalue.append(i)
            
#%%
import statistics
N2value = []
N3value = []
N4value = []
D9value = []
D13value = []
D16value = []
D23value = []
lovl = [N2value, N3value, N4value, D9value, D13value, D16value, D23value]

combine(N2, N2value)
combine(N3, N3value)
combine(N4, N4value)
combine(D9, D9value)
combine(D13, D13value)
combine(D16, D16value)
combine(D23, D23value)


for i in lovl:
    mean = sum(i)/len(i)
    sd = statistics.pstdev(i)
    print(str(mean) + '  ' + str(sd))
    
#%%Anova and tukey andswarm plots
import scipy.stats as stats

result = stats.f_oneway([N2value], [N3value], [N4value], [D9value], [D13value], [D16value], [D23value])

print(result)
    