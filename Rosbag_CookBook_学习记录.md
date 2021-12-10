### Rosbag_CookBook 学习记录

---------------

_language:中文_

_programed by: Python_



#### The Demo #1 in the CookBook

-------------

```python
import rosbag
with rosbag.Bag('output.bag','w') as outbag:
    for topic,msg,t in rosbag.Bag('input.bag').read_messages():
        # 这将以"all transforms in the message share the same timestap"
        # 为假设代替tf的时间戳
        if topic == "/tf" and msg.transform:
            outbag.write(topic,msg,msg.transforms[0].header.stamp)
        else:
            outbag.write(topic,msg,msg.header.stamp if msg._has_header else t)
```

_官方解析:这将在消息的接收时间与生成时间有巨大差异时非常有用，例如在消息的接收时需要经过不可靠或者是缓慢的连接。_

_注意:这将可能导致消息在通过rosbag play播放时发布的顺序。_

==My demo==

```python
#!/usr/bin/env python
#coding=utf-8
import os,sys
os.chdir(sys.path[0])	#用于vscode无法读取当前文件夹内的文件时
import rosbag

with rosbag.Bag('test2_.bag','w') as outbag:
    for topic,msg,t in rosbag.Bag('test1_.bag').read_message():
        if topic=='/joint_states' and msg:
            outbag.write('/iiwa_pos',msg,msg.header.stamp)
        else:
            # merge the input.bag 中的msg到output.bag中，如果msg中有header则使用
            # msg.header时间否则使用ROS时间。
            outbag.write(topic,msg,msg.header.stamp if msg._has_header else t)
```

