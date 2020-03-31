#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:24:30 2020

@author: ed
"""
import re

json = open("/Users/ed/Documents/GitHub/Buchnearer/labelme_output/all.json", 'r')
json = str(json)
regex = (r"\"bbox\": \[\n"
	r"                .{2,}\\n"
	r"                .{2,}\\n"
	r"                .{2,}\\n"
	r"                .{2,}\\n"
	r"            \].")
bboxes = re.findall(searchterm, json, re.MULTILINE)
for bbox in bboxes:
    print(bbox)
    