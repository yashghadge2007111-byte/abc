import csv
import json
import xml.etree.ElementTree as ET

# Text File
try:
    print("\n--- Text File ---")
    with open("data.txt","r") as f:
        print(f.read())
except:
    print("Text file not found")

# CSV File
try:
    print("\n--- CSV File ---")
    with open("data.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except:
    print("CSV file not found")

# JSON File
try:
    print("\n--- JSON File ---")
    with open("data.json","r") as f:
        data = json.load(f)
        print(data)
except:
    print("JSON file not found")

# XML File
try:
    print("\n--- XML File ---")
    tree = ET.parse("data.xml")
    root = tree.getroot()
    for child in root:
        for item in child:
            print(item.tag,":",item.text)
except:
    print("XML file not found")
