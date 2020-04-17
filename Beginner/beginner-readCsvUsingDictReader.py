import csv

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"], " | ", line["web"])
        #print(line["last_name"])
        #print(line["web"])

if __name__ == "__main__":
    csv_path = "data/us-500.csv"
    with open (csv_path, "r") as f_obj:
        csv_dict_reader(f_obj)
