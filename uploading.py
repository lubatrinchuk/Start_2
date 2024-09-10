import shutil

def uploading_files(source):
    destination = r"C:\Users\luba2\PycharmProjects\Start_2"
    return shutil.move(source, destination)                     #перемещаем файлы из папки пользователя в папку с программой
