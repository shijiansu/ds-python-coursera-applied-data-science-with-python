# -*- coding: UTF-8 -*-
from __future__ import division

import pandas as pd
import re

lines = open('data/university_towns.txt').readlines()
df = pd.DataFrame(columns=["STATE", "RegionName"])
for line in lines:
    # print (line)
    # if re.match('.*[edit]', line): # wrong one
    if re.match('.*\[edit\]', line):
        split_res = line.split('[ed')
        states = split_res[0].strip()
        print ("states: " + states)
    else:
        reg_res = line.split('(')
        regions = reg_res[0].strip()
        print ("regions: " + regions)
