#!/usr/bin/env python
#coding=utf-8
import os,sys
#os.chdir(sys.path[0])
import rosbag
bag=rosbag.Bag('./data/test1_.bag')
topics = bag.get_type_and_topic_info()[1].keys()
types=[]
for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
    types.append(bag.get_type_and_topic_info()[1].values()[i][0])