from django.shortcuts import render, redirect
from .models import Field, Farm, FieldCrop, Irrigation
import xlrd
import os


def create_data(request):

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filePath = os.path.join(desktop, "20170907.xlsx")
    workbook = xlrd.open_workbook(filePath)
    worksheet = workbook.sheet_by_name("LatestOutput") # We need to read the data

    #from the Excel sheet named "Sheet1"
    num_rows = worksheet.nrows  #Number of Rows
    num_cols = worksheet.ncols  #Number of Columns

    result_data =[]
    for curr_row in range(4, num_rows, 1):
        row_data = []

        for curr_col in range(1, num_cols, 1):
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            row_data.append(data)
        farm = row_data[0]
        field = row_data[1]
        variety = row_data[2]
        curr_smd = row_data[3] if row_data[3] else 0.0
        lw_smd = row_data[4] if row_data[4]  else 0.0
        water_use = row_data[5] if row_data[5] else 0.0
        drainage = row_data[6] if row_data[6] else 0.0
        allowable_smd = row_data[7] if row_data[7] else 0.0
        farm_obj, create = Farm.objects.get_or_create(name=farm)
        field_obj, create = Field.objects.get_or_create(name=field, farm=farm_obj)
        fc_obj, create = FieldCrop.objects.get_or_create(name=variety, field=field_obj)
        Irrigation.objects.create(fieldcrop=fc_obj, curr_smd=curr_smd,lw_smd=lw_smd, water_use=water_use,
                                  drainage=drainage, allowable_smd=allowable_smd)

        result_data.append(row_data)
    return redirect('/')