import os,platform

drc_3 = "/etc/snort/rules"
for dirName, subdirList, fileList in os.walk(drc_3):
    for fname in fileList:
        try:
            if fname.endswith(".rules") and fname.startswith("community-web-client"):
                print fname
                x=fname
                f1 = open(x, 'r+')
                f2 = open(x, 'r+')
                for line in f1:
                    f2.write(line.replace('flowbits:noreject;', ''))
                f1.close()
                f2.close()
        except:
            pass
