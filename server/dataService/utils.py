#  from server.models.XXX import XXX

import subprocess
import csv


def get_class_instance(dataname):
    last_module_name = dataname
    class_name = dataname
    module = __import__('server', fromlist=['models', str(dataname)]).models
    last_module = getattr(module, last_module_name)
    _class = getattr(last_module, class_name)
    return _class()

def readProfilesFromCsvFile(file_path):
    with open(file_path, 'rb') as f:
#        headerLine = next(f) # ignore the first header line
#        allCsvContent = csv.reader(f, delimiter=',')
#        for row in allCsvContent:
        allCsvContent = csv.DictReader(f)
        profiles_tmp = []
        for row in allCsvContent:
            profiles_tmp.append(row)
        print profiles_tmp
        return profiles_tmp

def unzipAndloadAllCsvFile(unzip_src, unzip_dest):
    subprocess.call('mkdir ' + unzip_dest, shell=True)
    unzip_return_code = subprocess.call('unzip -o ' + unzip_src + 'profiles.zip' + ' -d ' + unzip_src, shell=True)
    if unzip_return_code == 0:
        print 'unzip successfully!'
        subprocess.call('ls -al ' + unzip_src, shell=True)
        subprocess.call('mkdir ' + unzip_dest + 'faces', shell=True) #It does not matter if it already exists
        subprocess.call('mv -f ' + unzip_src + 'profiles/profile.csv ' + unzip_dest, shell=True)
        mv_return_code = subprocess.call('mv -f ' + unzip_src + 'profiles/faces/* ' + unzip_dest + 'faces/', shell=True)
        if mv_return_code == 0:
            print 'mv files successfully!'
            return readProfilesFromCsvFile(unzip_dest + 'profile.csv')

def clearAllContentOfSrcFolder(unzip_src):
    subprocess.call('rm -rf ' + unzip_src, shell=True)
    subprocess.call('mkdir ' + unzip_src, shell=True)
    print "the src folder is cleaned!!!"
