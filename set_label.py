import os, sys

root_folder = 'dataset'
label_file = open(root_folder+'_label.txt', 'w')

def reset_file_name(pre_name, reset_name):
	new_name = reset_name + '.' + pre_name.split(".")[-1]
	os.rename(pre_name, os.path.join(os.path.dirname(pre_name), new_name))
	return new_name

def write_file_label(file_path, label):
	label_file.write("%s %d\n" % (file_path, label))

def set_label(classDir, label):
    list_dirs = os.walk(classDir) 
    count = 0
    print list_dirs, classDir
    for root, dirs, files in list_dirs: 

        for f in files: 
            file_name = reset_file_name(os.path.join(root, f), str(count))
            print file_name
            print os.path.join(classDir, file_name)
            write_file_label((classDir + "/" + file_name) , label)
            count = count + 1

def set_class(rootDir):
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs:
        label = 0
        for d in dirs: 
            print os.path.join(root, d)
            print d
            set_label(os.path.join(rootDir,d), label)
            label = label + 1

if __name__ == "__main__":
	set_class(root_folder)



