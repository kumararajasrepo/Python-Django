import pandas as psObject
import numpy as npy
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table
from reportlab.platypus import Table, TableStyle

#Process initialization
def Init(properyInfo):
    data = psObject.read_csv(properyInfo);
    
    locationwiseData = data.groupby(['Location'])['SquareFootage','Price'].mean()
    propertywiseData = data.groupby(['PropertyType'])['BedroomsCount','BathroomsCount'].mean()
    overallAverageData = data.groupby(['PropertyType', 'Location'])['BedroomsCount','BathroomsCount','SquareFootage','Price'].mean()   
    
    lstColumns=['Location']
    table_data=PrepareData(locationwiseData,lstColumns)
    GenerateReport("Locationwise_Average_Report.pdf","Locationwise Average Report",table_data);

    lstColumns=['PropertyType']
    table_data=PrepareData(propertywiseData,lstColumns)   
    GenerateReport("Propertywise_Average_Report.pdf","Propertywise average Report",table_data);

    lstColumns=['PropertyType','Location']
    table_data=PrepareData(overallAverageData,lstColumns)
    GenerateReport("Overall_Average_Report.pdf","Overall Average Report",table_data);
   
#PrepareData is created for preparing report data
def PrepareData(data,columName):
    lcolumns=[]
    for cindex in range(0,len(columName), 1):
        lcolumns.append(columName[cindex]);

    for column in data.columns:
        lcolumns.append(column)
    
    ltable_data = [lcolumns]          
    
    for index, row in data.iterrows():
        processedrow=[]
        for cindex in range(0,len(columName), 1):            
            if len(columName) > 1:                
                processedrow.append(index[cindex]);
            else:
                processedrow.append(index)      
        
        for rowindex in range(0, len(row), 1):
            processedrow.append(npy.round(row[rowindex],2))
        ltable_data.append(list(processedrow))
    return ltable_data;

#GenerateReport is created for generating property average report in PDF format    
def GenerateReport(reportName,reportHeader,table_data):
    table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkcyan),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
])
    pdf = canvas.Canvas(reportName, pagesize=letter)
    pdf.drawString(inch, 10 * inch, reportHeader);
    table=Table(table_data);
    table.setStyle(table_style)
    table.wrapOn(pdf, inch, inch)
    table.drawOn(pdf, inch, 800-(len(table_data)*50))
    pdf.save()

Init('C:\Python Apps\PropertyAnalyzer\PropertyAnalyzer\Data\PropertyInfo.csv')