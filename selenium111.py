# import openpyxl
# from openpyxl import *
from selenium import webdriver


driver=webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/python/python_control_flow.htm")
driver.execute_script("window.scrollBy(0,500)")

driver.close()
# # reading the xlsx data
# path = '/Users/surtaram/Downloads/TESTING.xlsx'
#
# workbook = openpyxl.load_workbook(path)
# sheet = workbook.active
# # sheet1 = workbook.get_sheet_by_name('Sheet2')
# sheet2 = workbook['Sheet2']
# sheet3 = workbook['Sheet3']
# row = sheet2.max_row
# column = sheet2.max_column
# print(row)
# print(column)
#
# for r in range(1, row + 1):
#     for c in range(1, column + 1):
#         print(sheet2.cell(row=r, column=c).value, end='   ')
#     print()
#
# # write data from xlsx
#
# for r in range(1, 5):
#     for c in range(1, 3):
#         sheet3.cell(row=r, column=c).value = 'Welcome'

# workbook.save(path)
