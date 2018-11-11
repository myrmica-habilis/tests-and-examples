#!/usr/bin/python
# coding: utf-8

# via https://stackoverflow.com/questions/52291585

from PySide2.QtCore import QByteArray, QBuffer

testByteArray = bytearray([i for i in range(256)])
testQByteArray = QByteArray(testByteArray)
testQBuffer = QBuffer(testQByteArray)

assert(testQBuffer.data().data() == testByteArray)

for name in ["testByteArray", "testQByteArray", "testQBuffer.data()", "testQBuffer.data().data()"]:
    print("{}: type {}".format(name, type(eval(name))))
