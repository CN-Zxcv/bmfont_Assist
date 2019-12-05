
# -*- coding: UTF-8 -*-

import os
import sys
import ctypes
import shutil
import re
from PIL import Image
import fileinput
import codecs
import math

def generateFont(path):
    fontname = os.path.basename(path)
    configFileName = fontname + '_bmfont.bmfc'
    shutil.copy2('bmfont.bmfc', configFileName)

    configFile = open(configFileName, 'r+', encoding='utf-8')
    configFileData = configFile.readlines()

    files = []
    lines = []
    for _, _, t in os.walk(path):
        for filename in t:
            t = os.path.splitext(filename)
            if t[1].lower() in ['.png', '.jpg', '.tga', '.dds', '.bmp']:
                filepath = path + '/' + filename
                files.append(filepath)

                fontID = getFontID(t[0])
                line = 'icon="{0}", {1}, 0, 0, 0\n'.format(filepath, fontID)
                lines.append(line)

    # change output size
    size = getTextureSize(files)
    print('TextureSize', size)
    for k, line in enumerate(configFileData):
        replaceLine(configFileData, k, 'outWidth', size['w'])
        replaceLine(configFileData, k, 'outHeight', size['h'])
        replaceLine(configFileData, k, 'fontSize', size['maxH'])
        # replaceLine(configFileData, k, '', size['maxH'])
        # if 'outWidth' in line:
        #     configFileData[k] = re.sub(r'^.*$', 'outWidth={0}'.format(size['w']), line)
        # if 'outHeight' in line:
        #     configFileData[k] = re.sub(r'^.*$', 'outHeigt={0}'.format(size['h']), line)
        # if 'lineHeight' in line:
        #     configFileData[k] = re.sub(r'^.*$', 'lineHeight={0}'.format(size['maxH'], line))
    
    configFile.seek(0)
    configFile.writelines(configFileData)
    configFile.writelines(lines)
    configFile.close()

    os.system('bmfont64.exe -c {0} -o {1}'.format(configFileName, fontname + '.fnt'))
    os.remove(configFileName)

def replaceLine(configFileData, k, s, val):
    if s in configFileData[k]:
        configFileData[k] = re.sub(r'^.*$', '{0}={1}'.format(s, val), configFileData[k])

# 取文件名最后一个字符作为编码
# 无法作为文件名的特殊字符以编号形式命名文件
# 比如 \92, /47, :58, ?63, "34, <60, >62, |124
def getFontID(name):
    r = re.match('(\D+)(\d+)$', name)
    if r:
        (h, t) = r.groups()
        # print(h, t)
        if h:
            return int(t)
    #     print('re', name, r.groups())
    # if (r):
    #     return int(r[0])
    else:
        char = name[len(name) - 1]
        return ord(char)

def getTextureSize(files):
    area = 0
    minW = 0
    minH = 0
    maxW = 0
    maxH = 0
    for path in files:
        img = Image.open(path)
        (w, h) = img.size
        area += (w * h)
        if minH == 0 or h < minH:
            minH = h
        if minW == 0 or w < minW:
            minW = w
        if maxH == 0 or h > maxH:
            maxH = h
        if maxW == 0 or w > maxW:
            maxW = w
    
    num = math.ceil(math.sqrt(len(files)))
    w = num * maxW
    h = num * maxH
    realArea = w * h

    while realArea < area:
        w += maxW
        w += maxH
        realArea = w * h
    return {'w':w, 'h':h, 'maxH':maxH}

def main():
    if not os.path.exists('bmfont.bmfc'):
        ctypes.windll.user32.MessageBoxW(0, '修改为想要的配置后关闭软件以继续', '生成默认配置', 1)
        os.system("bmfont64.exe")

    for path in sys.argv[1:]:
        generateFont(path)

if __name__ == "__main__":
    main()