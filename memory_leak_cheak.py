# -*- coding: UTF-8 -*-

import os

if __name__ == '__main__':
    f = open(r"D:\Users\rtt\Desktop\test.log",'r',encoding='gb18030', errors='ignore')
    malloc = []
    free = []
    had_free = []
    not_free = []
    line = f.readline()
    while line:
        if line.find("<m") >= 0 :
            # print(line)
            malloc.append(line)
        elif line.find("<f") >= 0:
            # print(line)
            free.append(line)
        line = f.readline()

    copy_malloc = malloc.copy()
    copy_free = free.copy()
    # print(copy_malloc)

    for pf in free:
       for pm in copy_malloc:
           if pm[pm.find("r:")+2:pm.find(",")] == pf[pf.find("r:")+2:pf.find(",")]:
                had_free.append(pm)
                copy_malloc.remove(pm.__str__())
                copy_free.remove(pf.__str__())
                break

    # keys = {}
    # keys = keys.fromkeys(not_free)
    # not_free = list(keys.keys())

    fw = open(r"D:\Users\rtt\Desktop\memory-leak.txt",'w')
    fw.writelines("===all malloc===\n")
    for i in malloc:
        fw.writelines(i)
    fw.writelines("===all free===\n")
    for i in free:
        fw.writelines(i)
    fw.writelines("===all copy free===\n")
    for i in copy_free:
        fw.writelines(i)
    fw.writelines("============================================================\n")
    for i in copy_malloc:
        fw.writelines("===not free===")
        fw.writelines(i)
    fw.writelines("============================================================\n")
    for i in had_free:
        fw.writelines("===had free===")
        fw.writelines(i)
    f.close()
    fw.close()
