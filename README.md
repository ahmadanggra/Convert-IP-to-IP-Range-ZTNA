# convert_ip_to_range
# usage:
# create data as following format:
# [PC] ⮞ cat data.txt
# 10.195.143.24,10.195.143.25,10.195.143.26,10.195.143.27,10.195.143.66,10.195.143.28,10.195.143.93,10.195.143.24,10.195.143.25,10.0.0.1-10.0.0.100
# if we breakdown above ip into new line format the result is like follow:
# 10.195.143.24 -> duplicated
# 10.195.143.25 -> duplicated
# 10.195.143.26 
# 10.195.143.27
# 10.195.143.66
# 10.195.143.28
# 10.195.143.93
# 10.195.143.24 -> duplicated
# 10.195.143.25 -> duplicated
# 10.0.0.1-10.0.0.100
# run the script:
# [PC] ⮞ python3 unique_data.py
# 10.0.0.1-10.0.0.100,10.195.143.24-10.195.143.28,10.195.143.66,10.195.143.93
