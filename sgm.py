#!/usr/bin/env python

import configparser
import shutil
import os
import sys
import fileinput
from glob import glob

SOURCE = os.path.dirname(os.path.realpath(__file__)) + '/source/'

def sed(files, f, t):
    for file in glob(files):
      for line in fileinput.input(file, inplace = 1):
          print(line.replace('%' + f + '%', t).rstrip('\n'))

def add_android(config):
    shutil.copytree(SOURCE + 'android', 'sgm/android')
    name = config['name']
    package = config['package']
    _package_ = package.replace('.', '_')
    package_path = package.replace('.', '/')
    sed('sgm/android/AndroidManifest.xml', 'name', name)
    sed('sgm/android/AndroidManifest.xml', 'package', package)
    sed('sgm/android/java/*.java', 'package', package)
    sed('sgm/android/jni/jni.c', '_package_', _package_)
    shutil.move('sgm/android/java', 'sgm/android/src/' + package_path)

def build_android():
    src = ['jni.c', 'hook.cpp']
    for file in glob('src/*.cpp'):
        src.append('../../../' + file)
    for line in fileinput.input('sgm/android/jni/Android.mk', inplace = 1):
        if line.startswith('LOCAL_SRC_FILES'):
            print('LOCAL_SRC_FILES := ' + (' '.join(src)))
        else:
            print(line.rstrip('\n'))

def init():
    os.mkdir('sgm')
    os.mkdir('src')
    shutil.copy(SOURCE + 'app.h', 'sgm')
    config = configparser.ConfigParser()
    config.read('config')
    platforms = config.sections()
    for platform in platforms:
        globals()["add_" + platform](config[platform])

if sys.argv[1] == 'init':
    init()
elif sys.argv[1] == 'build':
    if sys.argv[2] == 'android':
        build_android()
else:
    print('unknown cmd')