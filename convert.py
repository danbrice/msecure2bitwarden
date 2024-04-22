import csv
import sys

file_name = sys.argv[1]

# Open the CSV file
with open(file_name, 'r', encoding = 'utf-8') as file:
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV
    records={}
    for rowNumber,row in enumerate(reader):
        recordId=None
        values={}
        types={}
        for colNumber,col in enumerate(row):
            value=col
            type_=None
            if colNumber == 0:
                name='Record Name'
                value,recordId=col.split('|',1)
            elif colNumber == 1:
                name='Record Type'
            elif colNumber == 2:
                name='Record Category'
            elif colNumber == 3:
                name='Record Note'
            else:
                parts = col.split('|',2)
                if len(parts) == 3:
                    name, type_,value = parts
                    # pipes (|) in value will be escaped:
                    value=value.replace('||','|')
                else:
                    print(f"Unexpected format in column: {col}")
                    print(f"from Row: {row}")
                    continue
            values[name]=value
            types[name]=type_
            #print(f"Record: {recordId} Name: {name} Type: {type_} Value: {value}")
        records[recordId]=[values,types]
    print(f"Records: {records}")