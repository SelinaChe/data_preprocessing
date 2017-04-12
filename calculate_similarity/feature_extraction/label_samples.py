import os, sys

rootdir = "/home/chm/deep_learning/image_retrieval/model/101_ObjectCategories"
wf = open('/home/chm/deep_learning/image_retrieval/model/101_ObjectCategories.txt', 'w')

count = 0
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in  dirnames:
        print "parent is: " + parent
        print  "dirname is: " + dirname

        for _parent,_dirnames,_filenames in os.walk(os.path.join(parent, dirname)):
            for _filename in _filenames:
                print os.path.join(_parent,_filename), count
                wf.write(str(os.path.join(_parent, _filename) + ' ' + str(count) + '\n'))
        count = count + 1


