import pandas as psObject
import numpy as num
from fpdf import FPDF

def ReadData(properyInfo):
    data = psObject.read_csv('C:\Python Apps\PropertyAnalyzer\PropertyAnalyzer\Data\PropertyInfo.csv');
    #for i, row in data.iterrows():
        #PropertyType,Location,Price,BedroomsCount,BathroomsCount,SquareFootage=row
        #print(f"{PropertyType}, {Location}, {Price}, {BedroomsCount}, {BathroomsCount},{SquareFootage}")

    grouped_data = data.groupby(['PropertyType', 'Location'])['Price','SquareFootage','BedroomsCount','BathroomsCount'].mean().astype(float)
    #converteddata=rouped_data.to_frame()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Mean Property Data', 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    
    for index, row in grouped_data.iterrows():
        pdf.cell(0, 10, 'Property Type: ' + str(index[0]) + ', Location: ' + str(index[1]), 0, 1)
        pdf.cell(0, 10, 'Average Price: ' + str(row['Price']), 0, 1)
        pdf.cell(0, 10, 'Average Square Footage: ' + str(row['SquareFootage']), 0, 1)
        pdf.cell(0, 10, 'Average Bedrooms Count: ' + str(row['BedroomsCount']), 0, 1)
        pdf.cell(0, 10, 'Average Bathrooms Count: ' + str(row['BathroomsCount']), 0, 1)
        pdf.cell(0, 10, '', 0, 1)

    pdf.output('mean_property_data.pdf', 'F')

    
    


ReadData('C:\Python Apps\PropertyAnalyzer\PropertyAnalyzer\Data\PropertyInfo.csv')