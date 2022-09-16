# Template
# {1: ['Adarsh', 16, {'Maths': 55, 'Science': 44, 'Social Science': 33, 'English': 22, 'French': 11, 'Computers': 99}, 264, 44.0]}
def func_excel(x):
    # Imports
    import xlsxwriter
    import os
    # Variable
    n = 0
    index = 1
    # While Loop
    while True:
        b = input('Do you want to store the students in an excel workbook(Type in either yes or no)? ').lower()
        if b != 'yes' and b != 'no':
            continue
        elif b == 'no':
            print(x)
            quit()
        elif b == 'yes':
            a = len(x)   # Number of students.
        d = os.getcwd()
        c = input('What do you want to call the excel file(For example: "example_excel_file")? ')
        c = c + '.xlsx'
        print(f'The file "{c}" was created in "{d}"')

        # Creating workbook with name
        workbook = xlsxwriter.Workbook(c)
        # Creating worksheet
        worksheet = workbook.add_worksheet()
        # Setting alignment to center
        cell_format = workbook.add_format()
        cell_format.set_align('center')
        # Merging Subjects
        worksheet.merge_range("F1:L1", "Subjects", cell_format)
        # Creating Headings
        worksheet.write("A1", "Name", cell_format)
        worksheet.write("B1", "Age", cell_format)
        worksheet.write("C1", "Class", cell_format)
        worksheet.write("D1", "Total", cell_format)
        worksheet.write("E1", "Average", cell_format)

        while a != n:
            # Writting Details
            worksheet.write(1+n,0, x[index][0], cell_format)
            worksheet.write(1+n,1, x[index][1], cell_format)
            worksheet.write(1+n,2, x[index][2]['grade'], cell_format)
            worksheet.write(1+n,3, x[index][3], cell_format)
            worksheet.write(1+n,4, x[index][4], cell_format)
            # Writting Marks
            if len(x[index][2]) -1 == 5:
                worksheet.write(1+n,6,  x[index][2]['sub1'], cell_format)
                worksheet.write(1+n,7,  x[index][2]['sub2'], cell_format)
                worksheet.write(1+n,8,  x[index][2]['sub3'], cell_format)
                worksheet.write(1+n,9,  x[index][2]['sub4'], cell_format)
                worksheet.write(1+n,10, x[index][2]['sub5'], cell_format)
            elif len(x[index][2]) -1 == 6:
                worksheet.write(1+n,5,  x[index][2]['sub1'], cell_format)
                worksheet.write(1+n,6,  x[index][2]['sub2'], cell_format)
                worksheet.write(1+n,7,  x[index][2]['sub3'], cell_format)
                worksheet.write(1+n,8,  x[index][2]['sub4'], cell_format)
                worksheet.write(1+n,9,  x[index][2]['sub5'], cell_format)
                worksheet.write(1+n,10, x[index][2]['sub6'], cell_format)
            elif len(x[index][2]) -1 == 7:
                worksheet.write(1+n,6,  x[index][2]['sub1'], cell_format)
                worksheet.write(1+n,7,  x[index][2]['sub2'], cell_format)
                worksheet.write(1+n,8,  x[index][2]['sub3'], cell_format)
                worksheet.write(1+n,9,  x[index][2]['sub4'], cell_format)
                worksheet.write(1+n,10, x[index][2]['sub5'], cell_format)
                worksheet.write(1+n,12, x[index][2]['sub7'], cell_format)
                worksheet.write(1+n,11, x[index][2]['sub6'], cell_format)
            n += 1
            index += 1
        
        workbook.close()
        break
                