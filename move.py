import os
import shutil
import time
import glob

frmtslst = ["*.jpg", "*.png", "*.gif"]

src_dir = "/home/kunal/Downloads/"

# while True:
#     NumberOfFiles = len(os.listdir("/home/kunal/Downloads"))
#     time.sleep(20)
#     OldNumber = NumberOfFiles
#     NumberOfFiles = len(os.listdir("/home/kunal/Downloads"))

#     if NumberOfFiles != OldNumber:

allimgs = []
allpdfs = []
allsws = []
allvids = []

for frmt in frmtslst:
    allimgs.extend(glob.iglob(os.path.join(src_dir, frmt)))

allpdfs = glob.glob("/home/kunal/Downloads/*.pdf")

allsws = glob.glob("/home/kunal/Downloads/*.deb")

allvids = glob.glob("/home/kunal/Downloads/*.mkv")

print(allimgs)
print(allsws)
print(allvids)

if len(allpdfs) != 0:
    pdfs = [f for f in os.listdir() if ".pdf" in f.lower()]
    if not os.path.exists("pdfs"):
        os.mkdir("pdfs")
    for pdf in pdfs:
        new_path = "pdfs/" + pdf
        shutil.move(pdf, new_path)

if len(allimgs) != 0:
    images = [f for f in os.listdir() if ".jpg" in f.lower()]
    if not os.path.exists("images"):
        os.mkdir("images")
    for image in images:
        new_path = "images/" + image
        shutil.move(image, new_path)

if len(allsws) != 0:
    sws = [f for f in os.listdir() if ".deb" in f.lower()]
    print(sws)
    if not os.path.exists("softwares"):
        os.mkdir("softwares")
    for sw in sws:
        new_path = "softwares/" + sw
        shutil.move(sw, new_path)
