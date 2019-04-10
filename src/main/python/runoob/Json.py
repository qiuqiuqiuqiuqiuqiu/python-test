#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

'''
    Python原始类型向json类型的转化对照表：
    Python          JSON
    dict            object
    list,tuple      array
    str,unicode     string
    int,long,float  number
    True            true
    False           false
    None            null
'''


pythonObject = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# json.dumps用于将Python对象编码成JSON字符串
jsonText = json.dumps(pythonObject, sort_keys=True, indent=4, separators=(',', ': '))
print jsonText

jsonText = '{"a":1,"b":2,"c":3}'
# json.loads用于将已编码的JSON字符串解码为Python对象
pythonObject = json.loads(jsonText)
print pythonObject
