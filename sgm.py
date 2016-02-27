#!/usr/bin/env python

import configparser
import shutil
import os
import sys
import fileinput
from glob import glob

SOURCE = os.path.dirname(os.path.realpath(__file__)) + '/template/'

def sed(files, f, t):
    for file in glob(files):
      for line in fileinput.input(file, inplace = 1):
          print(line.replace('%' + f + '%', t).rstrip('\n'))

def add_x11(config):
    shutil.copytree(SOURCE + 'sgm/x11', 'sgm/x11')
    x11_cpp = 'sgm/x11/src/x11.cpp'
    sed(x11_cpp, 'name', config['name'])
    sed(x11_cpp, 'width', config['width'])
    sed(x11_cpp, 'height', config['height'])

def add_android(config):
    shutil.copytree(SOURCE + 'sgm/android', 'sgm/android')
    name = config['name']
    package = config['package']
    _package_ = package.replace('.', '_')
    package_path = package.replace('.', '/')
    sed('sgm/android/AndroidManifest.xml', 'name', name)
    sed('sgm/android/AndroidManifest.xml', 'package', package)
    sed('sgm/android/java/*.java', 'package', package)
    sed('sgm/android/jni/jni.c', '_package_', _package_)
    shutil.move('sgm/android/java', 'sgm/android/src/' + package_path)

def build_x11():
    objects_text = ["OBJECTS_LOCAL= "]
    for file in glob('src/*.cpp'):
        file = file[4:]
        objects_text.append(os.path.splitext(file)[0] + '.o ')
    for file in glob('src/*.cpp'):
        file = file[4:]
        objects_text.append('\n' + os.path.splitext(file)[0] + '.o: $(SRC_DIR)/' + file + '\n\t$(CXX) -c $(CXXFLAGS) $(INCPATH) $(SRC_DIR)/' + file)
    objects = open('sgm/x11/build/Objects.mk', 'w')
    objects.write(''.join(objects_text))
    objects.close()

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
    shutil.copy(SOURCE + 'sgm/app.h', 'sgm')
    shutil.copytree(SOURCE + 'src', 'src')
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
    elif sys.argv[2] == 'x11':
        build_x11()
else:
    print('unknown cmd')
