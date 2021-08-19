#!/usr/bin/python3



print("Content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()


import cgi

details = {
    'KL 65k 7111': '''
                    Owner Name: Yashdeep Singh 
                    Registration Date: 12-Dec-2018
                    Registration Authority: Kerala
                    Maker/Model: SUV
                    Vehicle Class: LMV (Light Motor Vehicle)
                    Chassis No: MJH56278S
                    Engine No: JAF56GH990
                    Fuel: Diesel
                    Insurance Upto: 19-Apr-2024
                    RC Status: ACTIVE''',
    'MH20 DV 2363': '''
                    Owner Name: Aman Kumar
                    Registration Date: 10-May-2020
                    Registration Authority: Maharashtra
                    Maker/Model: Sedan
                    Vehicle Class: LMV (Light Motor Vehicle)
                    Chassis No: HGF4562F
                    Engine No: 9UHGF34LK
                    Fuel: Diesel
                    Insurance Upto: 01-Apr-2025
                    RC Status: ACTIVE''',
    'MH 20  EE 0943': '''
                    Owner Name: Daya Devgan
                    Registration Date: 01-Jan-2020
                    Registration Authority: Maharashtra
                    Maker/Model: Sedan
                    Vehicle Class: LMV (Light Motor Vehicle)
                    Chassis No: HVAF23G62F
                    Engine No: KJ45AN9LK0
                    Fuel: Diesel
                    Insurance Upto: 20-Jan-2025
                    RC Status: ACTIVE''',
    'KA 05 NB 1786': '''
                    Owner Name: Vaibhav Sharma
                    Registration Date: 01-Mar-2020
                    Registration Authority: Karnataka
                    Maker/Model: SUV
                    Vehicle Class: LMV (Light Motor Vehicle)
                    Chassis No: H9000G2F
                    Engine No: 9LK0OPVG07
                    Fuel: CNG
                    Insurance Upto: 30-Dec-2025
                    RC Status: ACTIVE''',
    'KL 21 5 8086': '''
                    Owner Name: Harsh Bhardwaj
                    Registration Date: 13-Jul-2020
                    Registration Authority: Karnataka
                    Maker/Model: SUV
                    Vehicle Class: LMV (Light Motor Vehicle)
                    Chassis No: JBDQU1452
                    Engine No: DFSH0934G
                    Fuel: CNG
                    Insurance Upto: 05-Oct-2025
                    RC Status: ACTIVE'''
}


mydata = cgi.FieldStorage()
x = mydata.getvalue("x")

print(x)


if x in details:
    print(details[x])
else:
	print("Car is not registered.")
