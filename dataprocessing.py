import csv
import os

data = "./data"
outputfile_path = "./formatted_csv"
with open(outputfile_path,"w") as outputfile:
    writer=csv.writer(outputfile)
    header=["sales","date","region"]
    writer.writerow(header)
    for filenames in os.listdir(data):
        with open(f"{data}/{filenames}","r") as input_file:
            reader=csv.reader(input_file)
            row_index=0
            if row_index>0:
                product = input_row[0]
                raw_price = input_row[1]
                quantity = input_row[2]
                transaction_date = input_row[3]
                region = input_row[4]
            if product=="pink morsel":
                price=float(raw_price[1:])
                sales=price*quantity
                output_row=["sales","transaction_date","region"]
                writer.writerow(output_row)
        row_index+=1


