import xlwt
import xlrd
import pymysql


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='YI.9694482664',
    db="booklist",
    charset="utf8",
    )

c = conn.cursor()
sql = "INSERT INTO booklist (name, position) VALUES ( '%s', '%s')"


def readExcel():
    wookbook = xlrd.open_workbook(r'C:\Users\YI\Desktop\书单.xls')
    sheets = wookbook.sheet_names()
    sheet = wookbook.sheet_by_name(sheets[0])
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows, ncols)
    for i in range(1, nrows):
        for k in range(0, ncols):
            if k == 0:
                name = sheet.cell(i, k).value.replace("\'", '\"')
            elif k == 1:
                position = sheet.cell(i, k).value.replace("\'", '\"')
            data = (name, position)
            c.execute(sql % data)
            conn.commit()


if __name__ == '__main__':
    readExcel()