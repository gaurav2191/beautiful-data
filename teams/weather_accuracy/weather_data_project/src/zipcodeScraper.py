"""
Need to have pyzipcode 0.4 to work
Must change the imports of __init__.py of the pyzipcode to the following:

from settings import db_location
from sqlite3 import dbapi2 as sqlite3
import math
import time
"""
def getZipCodes(source, radius):
    from pyzipcode import ZipCodeDatabase
    zcdb = ZipCodeDatabase()
    zipcodes = [z.zip for z in zcdb.get_zipcodes_around_radius(source, radius)]
    return zipcodes