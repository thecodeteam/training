__author__ = 'mcowger'

import zipfile
import StringIO
import os





def create_bits_zip(path):
    buffer = StringIO.StringIO()
    zip = zipfile.ZipFile(buffer,'w')
    for root, dirs, files in os.walk(path):
        for file_obj in files:
            arcname = "{}/{}".format(root,file_obj)
            relpath = os.path.relpath(arcname,path)
            zip.write(os.path.join(root, file_obj),arcname=relpath)
    zip.close()
    return buffer