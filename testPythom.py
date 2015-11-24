# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime
 
def read_excel():
  # 打开文件
  workbook = xlrd.open_workbook(r'C:\Users\cc\Desktop\CRM-Test\temp.xls')
  #workbook2 = xlrd.open_workbook(r'C:\Users\cc\Desktop\CRM-Test\tt.xls')

  workbookTemp = xlwt.Workbook(encoding='utf-8')
  booksheet = workbookTemp.add_sheet('Sheet 1', cell_overwrite_ok=True)

  # 根据sheet索引或者名称获取sheet内容
  sheet = workbook.sheet_by_index(0) # sheet索引从0开始
  #sheet2 = workbook2.sheet_by_index(0)
 
  # sheet的名称，行数，列数
  #print(sheet.name,sheet.nrows,sheet.ncols)
  rows=sheet.nrows

  for i in range(2,rows) :
      #获取A列的值
      colA="OOTB-"+sheet.row(i)[5].value+"-"+sheet.row(i)[6].value
      print(colA)
      #获取Q列的值
      value41 = sheet.row(i)[7].value
      value42 = sheet.row(i)[8].value
      value43 = sheet.row(i)[9].value
      if value42.strip()!='':
          value42="."+value42
      if value43.strip()!='':
          value43="."+value43    
      colQ=value41+value42+value43
      print(colQ)
      #获取AJ列的值
      valueAJ=sheet.row(i)[35].value
      print(valueAJ)
      booksheet.write(i-1,0,colA)
      booksheet.write(i-1,1,valueAJ)
      booksheet.write(i-1,2,colQ)
  workbookTemp.save('workbookTemp.xls') 
if __name__ == '__main__':
  read_excel()
