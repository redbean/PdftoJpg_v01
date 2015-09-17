# PdftoJpg_v02

*Purpose : 

1. To create jpg from the first page of any pdfs in user-input directory.

2. Not to depend any other programs, or sources. (This is failed)

*Dependancy : Don't think the version is important

must install below programs. 

1. Ghostscript : Ghostscript 9.16 for Windows (64 bit) (GNU Affero General Public License)

   Download path : http://www.ghostscript.com/download/gsdnld.html


2. imagemagick : ImageMagick-6.9.2-1-Q16-x64-static

   Download path :http://www.imagemagick.org/script/binary-releases.php

*How to use it

1. go to the folder that has pdf
2. just run
3. flag info
   - -i <path> : if you want enter specific path, please use this.
   - -d <dpi>  : To better quality, -d stands for DPI. 


*History of Found Errors

1. the folder Empty or does not have any pdf - Occurs error. please make sure that the folder has any pdf files.
2. the flag "-d" does not work..(cannot see any different between with and without "-d")



*Version Update history

1. v01 - nothing special. just run.

2. v02 - tried exceptional, command line flag.


*Other Things Future consideration: 

1. UI

2. For PDF, there are vector for characters, For JPG, there are raster, I need a bridge for going back and forth.
That is the reason that I used Ghostscript, Imagemagick.

3. To use this, make sure the environment has imagemagick's path.


