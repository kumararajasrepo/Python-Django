from msilib import Table
import pandas as psObject
import numpy as num
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table

def Init(properyInfo):
    data = psObject.read_csv('C:\Python Apps\PropertyAnalyzer\PropertyAnalyzer\Data\PropertyInfo.csv');
    
    locationwiseData = data.groupby(['Location'])['SquareFootage','Price'].mean().astype(float)
    propertywiseData = data.groupby(['PropertyType'])['BedroomsCount','BathroomsCount'].mean().astype(int)
    grouped_data = data.groupby(['PropertyType', 'Location'])['BedroomsCount','BathroomsCount','SquareFootage','Price'].mean().astype(float)    
    
    ltable_data=PrepareData(locationwiseData,'Location')    

    GenerateReport("locationwise_report.pdf","Locationwise Average Report",ltable_data);

    pcolumns=list(propertywiseData.columns)
    pcolumns.append('propertytype')
    ptable_data = [pcolumns]          
    
    for index, row in propertywiseData.iterrows():
        row['propertytype']=index;
        ptable_data.append(list(row))

    GenerateReport("propertwisewise_report.pdf","propertywise average report",ptable_data);  
    
    columns=list(grouped_data.columns)
    columns.append('propertytype')
    columns.append('location')
    table_data = [columns]          
    
    for index, row in grouped_data.iterrows():
        row['propertytype']=index[0];
        row['location']=index[1];
        table_data.append(list(row))

    GenerateReport("average_report.pdf","average report",table_data);
    
def PrepareData(data,columName):
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
    
def GenerateReport(reportName,reportHeader,table_data):
    pdf = canvas.Canvas(reportName, pagesize=letter)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(inch, 10 * inch, reportHeader);
    pdf.setFont("Helvetica", 12)
    table=Table(table_data);
    table.wrapOn(pdf, 0, 0)
    table.drawOn(pdf, 0, 400)
    pdf.save()

Init('C:\Python Apps\PropertyAnalyzer\PropertyAnalyzer\Data\PropertyInfo.csv')