import xlsxwriter

data = [
    {
        'Student' : "Rama",
        'Total Marks' : "95"
    },
    {
        'Student' : "Krishna",
        'Total Marks' : "75"
    }
]

workbook = xlsxwriter.Workbook("marks.xlsx")
worksheet = workbook.add_worksheet("Sheet-1")

worksheet.write(0,0,"Student")
worksheet.write(0,1,"Total Marks")

for index, entry in enumerate(data):
    worksheet.write(index+1, 0, entry["Student"])
    worksheet.write(index+1, 1, entry["Total Marks"])

workbook.close()