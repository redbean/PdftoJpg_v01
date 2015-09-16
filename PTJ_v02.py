#! /usr/bin/python
#

import os, sys, getopt



def main(argv):

        path = os.getcwd()
        files = os.listdir(path)
        dpi = "50"
        try:
                opts, args = getopt.getopt(argv, "hi:d:", ["input=", "DPI="])
        except getopt.GetoptError:
                print "PTJ_v01.py -i <path> -d <int DPI>"
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print "PTJ_v01.py -i <path> -d <int DPI>"
                        sys.exit()
                elif opt in ("-i", "--input"):
                        path = arg
                elif opt in ("-d", "--input"):
                        dpi = arg
        for i in files:
                if i[-3:] == "pdf":
                        print ("convert %s\\%s[0] -density %s %s\%s.jpg" % (path,i,dpi,path,i[:-4]))
                        #os.system("convert %s\%s[0] -density %s %s\%s.jpg" % (path,i,dpi,path,i[:-4]))
                        

if __name__ == "__main__":
        main(sys.argv[1:])
 
