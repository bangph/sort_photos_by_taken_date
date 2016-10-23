# exif_sort[January 2012] / martin gehrke [martin AT teamgehrke.com]
# original source: https://martingehrke.com/2012/02/sorting-files-into-folders-based-on-exif-date-using-python/
# Extended by: Bang Pham Huu to sort with input directory [b.phamhuu@jacobs-university.de] 
# sort almost every images types (add in EXTENSIONS)
# Example to run: python sort_photos.py /home/test/photos/input (it will rename the files: fileName + "-" + taken date) 
 
from PIL import Image
from PIL.ExifTags import TAGS
import sys, os, glob
 
def format_dateTime(UNFORMATTED):
    DATE, TIME = UNFORMATTED.split()
    return (DATE + "-" + TIME).replace(':','')
 
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
    	decoded = TAGS.get(tag, tag)
    	ret[decoded] = value
    return ret
 
def sortPhotos(path):
    PHOTOS = []
    EXTENSIONS =['.jpg','.jpeg','.JPG']
    for EXTENSION in EXTENSIONS:
        PHOTO = glob.glob(path + '/*%s' % EXTENSION)
	if PHOTO:
        	PHOTOS.extend(PHOTO)
 
    for PHOTO in PHOTOS:
        DATE = format_dateTime(get_exif(PHOTO)['DateTime'])
        #if not os.path.exists(DATE):
        #    os.mkdir(DATE)
	file_name = DATE + "-" + os.path.basename(PHOTO)
	dir_path = os.path.dirname(PHOTO)
        os.rename(PHOTO, dir_path + "/" + file_name)
 
if __name__=="__main__":
    PATH = sys.argv[1]
    if PATH == '': PATH = os.getcwd()
    sortPhotos(PATH)
