import pyqrcode


header = "               Invoice Details              \n"
next_line = "\n"

Serial_Number = input("Enter Serial Number :- ")
Client_Name = input("Enter client name :- ")
Invoice_Date = input("Enter invoice date :- ")
Due_Date = input("Enter Due Date :- ")
Invoice_Number = input("Enter Invoice Number :- ")
PO_Number = input("Enter po number :- ")
Item_Description = input("Enter Item description - Quantity :- ")
qr_name = input("Enter QR code name for Generation :- ")
Amount = None
try:
    Amount = input("Enter Overall Amount for Quantity :- ")
except:
    print("please Enter amount in digits only.....")
    exit(0)
string = header + next_line + "Serial Number: " + Serial_Number + next_line + "Client Name: " + Client_Name + next_line + "Invoice Date: " + Invoice_Date + next_line + "Due Date: " + Due_Date + next_line + "Invoice Number: " + Invoice_Number + next_line + "PO Number: " + PO_Number + next_line + "Item Description: " + Item_Description + next_line + next_line + "Total Amount For All Quantity: " + Amount + next_line + next_line + "Payment Method:      Paypal"
qr_code = pyqrcode.create(string)
qr_code.svg(qr_name+".svg",scale=4)
qr_code.png(qr_name+".png",scale=4)