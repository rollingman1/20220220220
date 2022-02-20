import os
from datetime import datetime

from pyfiglet import Figlet # pip install pyfiglet

f = Figlet(font='ntgreek', width=130)
print(datetime.now())

while(True):
    this_is_the_moment = datetime.now()
    time_20220220220220220220 = datetime(2022, 2, 20, 22, 2, 20, 220220)

    if this_is_the_moment == time_20220220220220220220:
        print('이 컴퓨터는 지금 이 순간', this_is_the_moment,'입니다.')
        print(f.renderText("{:%Y%m%d%H%M%S%f}".format(this_is_the_moment)))
        os.system("afplay " + "this_is_the_moment.mp3")
        break
    elif this_is_the_moment > time_20220220220220220220:
        break