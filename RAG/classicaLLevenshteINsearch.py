# pip install fuzzywuzzy python-Levenshtein

# https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/
# https://habr.com/ru/articles/491448/

from fuzzywuzzy import fuzz, process

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)
#Выводит в консоль: 100

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт, наш мир!')
print(a)
#Выводит в консоль: 97

# string to search in file
with open(r'sda2enall50texts.txt', 'r') as fp:
    # read all lines using readline()
    lines = fp.readlines()
    for row in lines:
        # check if string present on a current line
        word = 'tHe techNology coNpany'
        #print(row.find(word))
        # find() method returns -1 if the value is not found,
        # if found it returns index of the first occurrence of the substring
        if fuzz.WRatio(row, word) >= 80:
            print('string exists in file')
            print('line Number:', lines.index(row))

# string exists in file
# line Number: 2
# string exists in file
# line Number: 23
# string exists in file
# line Number: 29
# string exists in file
# line Number: 78
# string exists in file
# line Number: 113
# string exists in file
# line Number: 124
# string exists in file
# line Number: 128
# string exists in file
# line Number: 134
# string exists in file
# line Number: 148
# string exists in file
# line Number: 156
# string exists in file
# line Number: 185
# string exists in file
# line Number: 218
# string exists in file
# line Number: 220
# string exists in file
# line Number: 240
# string exists in file
# line Number: 241
# string exists in file
# line Number: 255
# string exists in file
# line Number: 258
# string exists in file
# line Number: 270
# string exists in file
# line Number: 288
# string exists in file
# line Number: 298
# string exists in file
# line Number: 303
# string exists in file
# line Number: 313
# string exists in file
# line Number: 331
# string exists in file
# line Number: 337
# string exists in file
# line Number: 358
# string exists in file
# line Number: 381
# string exists in file
# line Number: 391
# string exists in file
# line Number: 395
# string exists in file
# line Number: 403
# string exists in file
# line Number: 404
# string exists in file
# line Number: 405
# string exists in file
# line Number: 406
# string exists in file
# line Number: 407
# string exists in file
# line Number: 408
# string exists in file
# line Number: 413
# string exists in file
# line Number: 419
# string exists in file
# line Number: 431
# string exists in file
# line Number: 439
# string exists in file
# line Number: 445
# string exists in file
# line Number: 451
# string exists in file
# line Number: 457
# string exists in file
# line Number: 469
# string exists in file
# line Number: 471
# string exists in file
# line Number: 475
# string exists in file
# line Number: 488
# string exists in file
# line Number: 492
# string exists in file
# line Number: 494
# string exists in file
# line Number: 528
# string exists in file
# line Number: 530
# string exists in file
# line Number: 554
# string exists in file
# line Number: 564
# string exists in file
# line Number: 579
# string exists in file
# line Number: 587
# string exists in file
# line Number: 591
# string exists in file
# line Number: 599
# string exists in file
# line Number: 607
# string exists in file
# line Number: 613
# string exists in file
# line Number: 643
# string exists in file
# line Number: 648
# string exists in file
# line Number: 668
# string exists in file
# line Number: 678
# string exists in file
# line Number: 686
# string exists in file
# line Number: 690
# string exists in file
# line Number: 700
# string exists in file
# line Number: 712
# string exists in file
# line Number: 720
# string exists in file
# line Number: 724
# string exists in file
# line Number: 738
# string exists in file
# line Number: 748
# string exists in file
# line Number: 770
# string exists in file
# line Number: 774
# string exists in file
# line Number: 794
# string exists in file
# line Number: 806
# string exists in file
# line Number: 812
# string exists in file
# line Number: 413
# string exists in file
# line Number: 832
# string exists in file
# line Number: 864
# string exists in file
# line Number: 873
# string exists in file
# line Number: 875
# string exists in file
# line Number: 882
# string exists in file
# line Number: 886
# string exists in file
# line Number: 888
# string exists in file
# line Number: 894
# string exists in file
# line Number: 938
# string exists in file
# line Number: 940
# string exists in file
# line Number: 976
# string exists in file
# line Number: 978
# string exists in file
# line Number: 1000
# string exists in file
# line Number: 1013
# string exists in file
# line Number: 1033
# string exists in file
# line Number: 1041
# string exists in file
# line Number: 1043
# string exists in file
# line Number: 1057
# string exists in file
# line Number: 1085
# string exists in file
# line Number: 1095
# string exists in file
# line Number: 1101
# string exists in file
# line Number: 1107
# string exists in file
# line Number: 1125
# string exists in file
# line Number: 1135
# string exists in file
# line Number: 1141
# string exists in file
# line Number: 1157
# string exists in file
# line Number: 1161
# string exists in file
# line Number: 1167
# string exists in file
# line Number: 1171
# string exists in file
# line Number: 1175
# string exists in file
# line Number: 1183
# string exists in file
# line Number: 1187
# string exists in file
# line Number: 1189
# string exists in file
# line Number: 1033
# string exists in file
# line Number: 1201
# string exists in file
# line Number: 1219
# string exists in file
# line Number: 1225
# string exists in file
# line Number: 1229
# string exists in file
# line Number: 1231
# string exists in file
# line Number: 1237
# string exists in file
# line Number: 1257
# string exists in file
# line Number: 1265
# string exists in file
# line Number: 1269
# string exists in file
# line Number: 1285
# string exists in file
# line Number: 1301
# string exists in file
# line Number: 1303
# string exists in file
# line Number: 1321
# string exists in file
# line Number: 1327
# string exists in file
# line Number: 1341
# string exists in file
# line Number: 1355
# string exists in file
# line Number: 1359
# string exists in file
# line Number: 1361
# string exists in file
# line Number: 1367
# string exists in file
# line Number: 1369
# string exists in file
# line Number: 1379
# string exists in file
# line Number: 1385
# string exists in file
# line Number: 1397
# string exists in file
# line Number: 1413
# string exists in file
# line Number: 1419
# string exists in file
# line Number: 1425
# string exists in file
# line Number: 1443
# string exists in file
# line Number: 1449
# string exists in file
# line Number: 1457
# string exists in file
# line Number: 1465
# string exists in file
# line Number: 1467
# string exists in file
# line Number: 1471
# string exists in file
# line Number: 1503
# string exists in file
# line Number: 1532
# string exists in file
# line Number: 1544
# string exists in file
# line Number: 1554
# string exists in file
# line Number: 1558
# string exists in file
# line Number: 1562
# string exists in file
# line Number: 1564
# string exists in file
# line Number: 1580
# string exists in file
# line Number: 1586
# string exists in file
# line Number: 1594
# string exists in file
# line Number: 1613
# string exists in file
# line Number: 1621
# string exists in file
# line Number: 1631
# string exists in file
# line Number: 1637
# string exists in file
# line Number: 1639
# string exists in file
# line Number: 1641
