import os
import shutil

image = ['jpg', 'png', 'jpeg', 'gif']
document = ['docx', 'doc', 'xlsx', 'ppt', 'txt', 'pptx']
video = ['mkv', 'mp4', 'avi', 'mov']
audio = ['mp3', 'wav', 'aac', 'webm']
program = ['html', 'php', 'c', 'cpp']
s_path = "D:/Source"
d_path = "D:/Arranged_file"
list_dir = os.listdir(s_path)
print(list_dir)
for i in list_dir:
    name, ext = os.path.splitext(i)
    ext = ext[1:]

    if ext in image:
        desti_path = d_path + "/" + "Images" + "/" + ext

        if os.path.exists(desti_path):
            shutil.move(s_path + "/" + i, desti_path + "/" + i)
        else:
            os.makedirs(desti_path)
            shutil.move(s_path + "/" + i, desti_path + "/" + i)

    if ext in document:
        desti_path = d_path + "/" + "Documents" + "/" + ext

        if os.path.exists(desti_path):
            shutil.move(s_path + "/" + i, desti_path + "/" + i)
        else:
            os.makedirs(desti_path)
            shutil.move(s_path + "/" + i, desti_path + "/" + i)

    if ext in video:
        desti_path = d_path + "/" + "videos" + "/" + ext

        if os.path.exists(desti_path):
            shutil.move(s_path + "/" + i, desti_path + "/" + i)
        else:
            os.makedirs(desti_path)
            shutil.move(s_path + "/" + i, desti_path + "/" + i)

    if ext in audio:
        desti_path = d_path + "/" + "Audios" + "/" + ext

        if os.path.exists(desti_path):
            shutil.move(s_path + "/" + i, desti_path + "/" + i)
        else:
            os.makedirs(desti_path)
            shutil.move(s_path + "/" + i, desti_path + "/" + i)

    if ext in program:
        desti_path = d_path + "/" + "Program_files" + "/" + ext

        if os.path.exists(desti_path):
            shutil.move(s_path + "/" + i, desti_path + "/" + i)
        else:
            os.makedirs(desti_path)
            shutil.move(s_path + "/" + i, desti_path + "/" + i)