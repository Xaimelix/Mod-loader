import zipfile
from zipfile import ZipFile
import os

with ZipFile('new_zip.zip', 'r') as zip_file:
    zip_file.extractall(r'C:\Users\skyhe\PycharmProjects\Mod-loader')
 #разархиваирует содержимое zip-файла в папку