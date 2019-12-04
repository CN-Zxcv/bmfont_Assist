# bmfont_Assist
bmfont pack helper

inspired by one vbs file named `bmfont_Assistant by Jerryjin 2015-11-27`

but it could not work properly with chinese，and i`m not familiar with vbscript，so i rewrote it with python and changed outWidth outHeight calc

## what is it

a helper use bmfont to make a font,  usually like make games，

## how to use

make a directory to store all font character files, drag the fontname dir to bmfont_Assist.exe .

like this

├── bmfont64.exe
├── bmfont_Assist.exe
└── fontname
    ├── uni_58.png
    ├── I.png
    └── 帮.png



it will open bmfont at first time if there`s no bmfont.bmfc, change the export setting and close to generate a config file,

we use that config as template to add icons in fontname diretory and output the fnt file.

after run, we got a fontname.fnt and a png file if we output as png

111
├── bmfont64.exe
├── bmfont_Assist.exe
├── bmfont.bmfc
├── fontname
│   ├── uni_58.png
│   ├── I.png
│   └── 帮.png
├── fontname_0.png
└── fontname.fnt



## icon naming

some chars can`t be named as filename,  so use unicodeID name it

as uni_58.png / uni58.png / 58.png / endwith number

【 \ : 92 】 【 / : 47 】 【 : : 58 】 【 * : 42 】 【 ? : 63 】 【 "" : 34 】 【 < : 60 】 【 > : 62 】 【 | : 124 】



### ps

only tested with png , with a small number of chars, not sure the calc of outWidth outHeight is ok