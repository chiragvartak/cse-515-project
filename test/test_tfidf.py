from tfidf import *

if __name__ == "__main__":
    db = Database.from_wrd_files("D:\\Google Drive\\ASU\\CSE 515 Multimedia and Web Databases\\Project\\database")
    sensor_series_0 = db.get_gesture('1').get_sensor_series(1)