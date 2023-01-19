from openpyxl import Workbook, load_workbook
""" Work Book """
wb = load_workbook("Titles.xlsx")
ws = wb.active

departments = ["Management","Finance","Operations", "IT", "I.T",
 "Product","Support","HR","Sales","Marketing"]

personas = ["Founder","Owner","CSuite", "Managing Director",
"Director","VP","Manager","Accounting",'controller',"accounting","accountant",
"Finance","Legal"]


# Initialize a variable to keep track of the number of matching cells
matching_cells = 0
managers= 0
persons = 0

for department in departments:
    # Iterate through the rows in column A
    for row in ws['A']:
        # Define the list of strings to check for
        strings_to_check = department    
        count = row.value.count(strings_to_check)
        managers = managers + count
        if count == 1:
            # row.coordinate data type is string
            print(row.coordinate)
            print(row.value)
            ws[f"D{row.coordinate[1:]}"] = department
            

for persona in personas:
    # Iterate through the rows in column A
    for row in ws['A']:
        # Define the list of strings to check for
        strings_to_check = persona   
        count = row.value.count(strings_to_check)
        persons = persons + count
        if count==1:
            print(f"persona..{row.coordinate}")
            print(f"persona..{row.value}")
            ws[f"C{row.coordinate[1:]}"] = persona

# Iterate through all rows in column C and D, starting from the second row
for row in range(2, ws.max_row + 1):
    # Get the value in cell C and D
    value_c = ws.cell(row=row, column=3).value
    if type(value_c) != type("string"):
        value_c = "_"
    value_d = ws.cell(row=row, column=4).value
    if type(value_d) != type("string"):
        value_d = "_"
    # set the value in column B 
    ws.cell(row=row, column=2).value = value_d + " " + value_c 


# Print the number of matching cells
print(f"{managers} Manager Titles")
print(f"{persons} Personas")

wb.save('Titles.xlsx')
