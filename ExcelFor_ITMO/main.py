import xlwings as xw
import pandas as pd


print(xw.__version__)
print(pd.__version__)

wb=xw.Book('Task_1.xlsx')  # Открываем книгу
data_excel = wb.sheets['Лист1']  # Читаем лист Данные
data_pd = data_excel.range('A1').options(pd.DataFrame, header=1, index=False).value  # Создаем DataFrame
# data_pd = pd.DataFrame({342: []})
# data_excel.range('A1').options(index=False).value = data_pd  # Заносим именно
print(data_pd)

print('-----------------------')

# data_pd2 = data_excel.range('B64:C65').options(pd.DataFrame, header=1, index=False).value  # Создаем DataFrame2
# n = int(data_pd2.values[0][0])
# print(n)

print('-----------------------')

letters = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' ,
           'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z', 'AA', 'AB', 'AC', 'AD', 'AE',
           'AF' , 'AG' , 'AH' , 'AI' , 'AJ' , 'AK' , 'AL' , 'AM' , 'AN' ,
           'AO' , 'AP' , 'AQ' , 'AR' , 'AS' , 'AT' , 'AU' , 'AV' , 'AW' , 'AX' , 'AY' , 'AZ',
           'BA' , 'BB' , 'BC' , 'BD' , 'BE' , 'BF' , 'BG' , 'BH' , 'BI' , 'BJ' , 'BK' , 'BL' , 'BM' , 'BN' ,
           'BO' , 'BP' , 'BQ' , 'BR' , 'BS' , 'BT' , 'BU' , 'BV' , 'BW' , 'BX' , 'BY' , 'BZ']
for c in range(2,len(letters)-5):
    for r in range(0,72):
        # adr = "B1:"+(letters[c+10] + str(r+50))
        realadr = "B2:"+(letters[c] + str(r+1))
        # data_pd = pd.DataFrame({i: []})
        # data_excel.range('A1').options(index=False).value = data_pd
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        data_pd2 = data_excel.range('B1:BZ765').options(pd.DataFrame, header=1, index=False).value  # Создаем DataFrame2
        for i in range(c):
            for j in range(r):
                n = int(data_pd2.values[i][j])
                if n > 5000 and n < 7000:
                    c1 += 1
                if n > 6000 and n < 9000:
                    c2 += 1
                if n > 7000 and n < 11000:
                    c3 += 1
                if n > 8000 and n < 13000:
                    c4 += 1
                if n > 9000 and n < 15000:
                    c5 += 1
                if n > 10000 and n < 17000:
                    c6 += 1
                if n > 11000 and n < 19000:
                    c7 += 1
                if n > 12000 and n < 21000:
                    c8 += 1
                if n > 13000 and n < 23000:
                    c9 += 1
                if n > 14000 and n < 25000:
                    c10+= 1
                if n > 15000 and n < 27000:
                    c11 += 1
                if n > 16000 and n < 29000:
                    c12 += 1
                if n > 17000 and n < 31000:
                    c13 += 1
                if n > 18000 and n < 33000:
                    c14 += 1
                if n > 19000 and n < 35000:
                    c15 += 1
                if n > 20000 and n < 37000:
                    c16 += 1
                if n > 21000 and n < 39000:
                    c17 += 1
                if n > 22000 and n < 41000:
                    c18 += 1
                if n > 23000 and n < 43000:
                    c19 += 1
                if n > 24000 and n < 45000:
                    c20 += 1
        if(c1==5 and c2==7 and c3==2 and c4==6 and c5==6
                and c6==6 and c7==6 and c8==6 and c9==4
                and c10==6 and c11==5 and c12==5 and c13==5
                and c14==5 and c15==7 and c16==5 and c17==5
                and c18==5 and c19==5 and c20==5):
            print(realadr)
        if(c20==5): print('Assdsd' , realadr)



