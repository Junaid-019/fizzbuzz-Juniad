# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XxNUKUp83MSwBFFVjN61VxAse9rNlwqf
"""

#copied from https://stackoverflow.com/questions/15343743/copying-from-one-text-file-to-another-using-python
#!/usr/bin/env python

f = open('list1.txt')
f1 = open('output.txt', 'a')

doIHaveToCopyTheLine=False

for line in f.readlines():

    if 'tests/file/myword' in line:
        doIHaveToCopyTheLine=True

    if doIHaveToCopyTheLine:
        f1.write(line)

f1.close()
f.close()