#!/usr/bin/env python
#coding=utf-8
import os,sys
#os.chdir(sys.path[0])   #添加当前文件夹路径到系统路径中，让vscode找到文件

# Rewrite bag with header timestamps
import rosbag

with rosbag.Bag('./data/iiwa.bag','w') as outbag:
    for topic,msg,t in rosbag.Bag('./data/test1_.bag').read_messages():
        if topic == "/joint_states" and msg.transforms:
            outbag.write("/iiwa_pos",msg,msg.transforms[0].header.stamp)
        else:
            # merge the input.bag中的msg到output.bag中，如果msg有header则使用msg的header否则使用ros时间
            outbag.write(topic,msg,msg.header.stamp if msg._has_header else t)