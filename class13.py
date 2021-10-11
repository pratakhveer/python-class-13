import statistics
from numpy import result_type
import pandas as pd
import csv

df = pd.read_csv("height.csv")

height = df["Height"].to_list()
weight = df["Weight"].to_list()

Hmean = statistics.mean(height)
Wmean = statistics.mean(weight)

Hmedian = statistics.median(height)
Wmedian = statistics.median(weight)

Hmode = statistics.mode(height)
Wmode = statistics.mode(weight)

print("mean, median, mode of height is {},{} and {} respectively".format(
    Hmean, Hmedian, Hmode))
print("mean, median, mode of weight is {},{} and {} respectively".format(
    Wmean, Wmedian, Wmode))

Hstd = statistics.stdev(height)
Wstd = statistics.stdev(weight)

# 1,2,3 standard deviation for height

height1sdStart, height1sdEnd = Hmean - Hstd, Hmean + Hstd
height2sdStart, height2sdEnd = Hmean - (2*Hstd), Hmean + (2*Hstd)
height3sdStart, height3sdEnd = Hmean - (3*Hstd), Hmean + (3*Hstd)

# 1,2,3 standard deviation for Weight

weight1sdStart, weight1sdEnd = Wmean - Wstd, Wmean + Wstd
weight2sdStart, weight2sdEnd = Wmean - (2*Wstd), Wmean + (2*Wstd)
weight3sdStart, weight3sdEnd = Wmean - (3*Wstd), Wmean + (3*Wstd)

# percentage of data within 1,2 and 3 standard deviation of height

height1sd = [result for result in height if result >
             height1sdStart and result < height1sdEnd]
height2sd = [result for result in height if result >
             height2sdStart and result < height2sdEnd]
height3sd = [result for result in height if result >
             height3sdStart and result < height3sdEnd]

# percentage of data within 1,2 and 3 standard deviation of Weight

weight1sd = [result for result in weight if result >
             weight1sdStart and result < weight1sdEnd]
weight2sd = [result for result in weight if result >
             weight2sdStart and result < weight2sdEnd]
weight3sd = [result for result in weight if result >
             weight3sdStart and result < weight3sdEnd]

# printing the data for height and weight

print("{}% of data for height lies within 1 standard deviation".format(
    len(height1sd)*100.0/len(height)))
print("{}% of data for height lies within 2 standard deviation".format(
    len(height2sd)*100.0/len(height)))
print("{}% of data for height lies within 3 standard deviation".format(
    len(height3sd)*100.0/len(height)))

print("{}% of data for weight lies within 1 standard deviation".format(
    len(weight1sd)*100.0/len(weight)))
print("{}% of data for weight lies within 2 standard deviation".format(
    len(weight2sd)*100.0/len(weight)))
print("{}% of data for weight lies within 3 standard deviation".format(
    len(weight3sd)*100.0/len(weight)))
