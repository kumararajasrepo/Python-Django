from msilib import Table
import pandas as psObject
import numpy as num
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table

def Init(properyInfo):
    data = psObject.read_csv(properyInfo);
    
    locationwiseData = data.groupby(['Location'])['SquareFootage','Price'].mean().astype(float)
    propertywiseData = data.groupby(['PropertyType'])['BedroomsCount','BathroomsCount'].mean().astype(int)
    overallAverageData = data.groupby(['PropertyType', 'Location'])['BedroomsCount','BathroomsCount','SquareFootage','Price'].mean().astype(float)    
    
    lstColumns=['Location']
    table_data=PrepareData(locationwiseData,lstColumns)
    GenerateReport("Locationwise_Average_Report.pdf","Locationwise Average Report",table_data);

    lstColumns=['propertytype']
    table_data=PrepareData(propertywiseData,lstColumns)   
    GenerateReport("Propertywise_Average_Report.pdf","Propertywise average Report",table_data);

    lstColumns=['propertytype','location']
    table_data=PrepareData(overallAverageData,lstColumns)
    GenerateReport("Overall_Average_Report.pdf","Overall Average Report",table_data);
    
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
            processedrow.append(row[rowindex])
        ltable_data.append(list(processedrow))
    return ltable_data;

def PrepareData1(data,columName):
    lcolumns=[columName]   
    for column in data.columns:
        lcolumns.append(column)
    
    ltable_data = [lcolumns]          
    
    for index, row in data.iterrows():
        row[columName]=index;        
        processedrow=[]
        for rowindex in range(len(row)-1, -1, -1):
            processedrow.append(row[rowindex])
        ltable_data.append(list(processedrow))
    return ltable_data;
    
def GenerateReport(reportName,reportHeader,table_data):
    pdf = canvas.Canvas(reportName, pagesize=letter)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(inch, 10 * inch, reportHeader);
    pdf.setFont("Helvetica", 12)
    table=Table(table_data);
    table.wrapOn(pdf, 0, 0)

    table.drawOn(pdf, 0, 800-(len(table_data)*50))
    pdf.save()
Init('C:\Python Apps\PropertyAnalyzer\PropertyAnalyzer\Data\PropertyInfo.csv')