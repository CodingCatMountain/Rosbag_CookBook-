#!/usr/bin/env python
#coding=utf-8
import os,sys

from rosbag.bag import Bag
os.chdir(sys.path[0])

# Rewrite bag with header timestamps:
import rosbag

with rosbag.Bag('./data/test2_.bag','w') as outbag:
    for topic,msg,t in rosbag.Bag('./data/test1_.bag').read_messages():
        if topic=='/joint_states' and msg:
            outbag.write('/iiwa_pos',msg,msg.header.stamp)
        else:
            outbag.write(topic,msg,msg.header.stamp if msg._has_header else t)