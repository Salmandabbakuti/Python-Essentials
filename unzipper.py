import sys
from zipfile import PyZipFile

for zip_file in sys.argv[1:]:
    pzf=PyZipFile(zip_file)
    pzf.extractall()
#Salman Dabbakuti
#run "py unzipper.py <zip file you wanted to unZip>"
