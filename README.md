# PdftoJpg_v02

*Purpose : 

1. To create jpg from the first page of any pdfs in user-input directory.

2. Not to depend any other programs, or sources. (This is failed)

*Dependancy : Don't think the version is important

1. Ghostscript : Ghostscript 9.16 for Windows (64 bit) (GNU Affero General Public License)

   Download path : http://www.ghostscript.com/download/gsdnld.html


2. imagemagick : ImageMagick-6.9.2-1-Q16-x64-static

   Download path :http://www.imagemagick.org/script/binary-releases.php

*Other Things Future consideration: 

1. UI

2. For PDF, there are vector for characters, For JPG, there are raster, I need a bridge for going back and forth.
That is the reason that I used Ghostscript, Imagemagick.

3. To use this, make sure the environment has imagemagick's path.
 


*Version Update history

1. v01 - nothing special. just run.

2. v02 - tried exceptional, command line flag.

