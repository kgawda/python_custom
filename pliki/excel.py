import openpyxl

def main():
    workbook = openpyxl.Workbook()
    #ws = workbook.worksheets[0]
    ws = workbook.active
    cell = ws.cell(row=1, column=1)
    cell.value = "Hello World"
    cell.font = openpyxl.styles.Font(color="EE5555")
    # cell.fill = openpyxl.styles.PatternFill("solid", fgColor="DDDDDD")  # do sprawdzenia

    ws["B2"].value = 5
    ws["B2"].comment = openpyxl.comments.Comment("To jest komentarz", "kurs")
    ws["B3"].value = "link"
    ws["B3"].hyperlink = "https://www.google.com"

    ws.column_dimensions["A"].width = 50
    assert openpyxl.utils.get_column_letter(1) == "A"

    workbook.save("test.xlsx")
    workbook.close()

if __name__ == "__main__":
    main()