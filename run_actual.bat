set file="test5.csv"

REM python task1.py dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" w=3 s=2 r=3

REM python task2.py dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database"

python task3.py dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" f=%file% type="tf"
python task3.py  dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" f=%file% type="tfidf"
python task3.py  dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" f=%file% type="tfidf2"

python task4.py dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" f=%file% type="tf"
python task4.py dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" f=%file% type="tfidf"
python task4.py dir="D:\Google Drive\ASU\CSE 515 Multimedia and Web Databases\Project\database" f=%file% type="tfidf2"