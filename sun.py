'''
精确度±30分钟
仅考虑地球为理想球体，未考虑日地距离造成的误差
出现时间均为地方时
'''
import math
import datetime
dec=math.radians(float(input("请输入今日太阳高度角（南纬为负）")))
city=math.radians(float(input("请输入当前城市纬度（南纬为负）")))
sunrise= (math.acos(math.tan(dec)*math.tan(city))/(2*math.pi))*24
# sunrise=(math.acos(-(math.sin(-0.01483529864)-math.sin(dec)*math.sin(city))/(math.cos(dec)*math.cos(city)))/(2*math.pi))*24 #修正公式 来源wiki
sunset=24-sunrise
daytibme=24-2*sunrise
minrise = str(datetime.timedelta(hours=sunrise))
mindaytime=str(datetime.timedelta(hours=daytibme))
minset = str(datetime.timedelta(hours=sunset))
print(f''' 日出：{minrise}
 日落：{minset}
 昼长：{mindaytime}  ''')
