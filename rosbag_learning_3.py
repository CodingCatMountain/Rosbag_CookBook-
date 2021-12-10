#!/usr/bin/env python
#coding=utf-8
import subprocess,yaml
import os,sys

from yaml.loader import FullLoader
#os.chdir(sys.path[0])

info_dict=yaml.load(subprocess.Popen(['rosbag','info','--yaml','./data/test1_.bag'],stdout=subprocess.PIPE).communicate()[0],Loader=yaml.FullLoader)
print(info_dict)

import yaml
from rosbag.bag import Bag
info_dict=yaml.load(Bag('./data/iiwa.bag','r')._get_yaml_info(),Loader=yaml.FullLoader)
print(info_dict)