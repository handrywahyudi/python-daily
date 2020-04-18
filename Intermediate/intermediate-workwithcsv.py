#!/usr/local/bin/python3
import csv

if __name__ == "__main__":
    with open('data/Data-Jumlah-Omzet-Pemasaran-Bunga-dan-Tanaman-Hias-Januari2020.csv') as csv_file:
        # Using csv.reader
        # csv_reader = csv.reader(csv_file, delimiter=',')
        # line_count = 0
        # for row in csv_reader:
        #     if line_count == 0:
        #         print(f'Column names are {", ".join(row)}')
        #         line_count += 1
        #     else:
        #         print(f'Location: {row[0]} Type: {row[1]} Profit: {row[2]}.')
        #         line_count += 1
        # print(f'Processed {line_count} lines.')

        # Using csv.Dictreader
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'Location: {row["lokasi_omset_penjualan"]}, Type of commodity: {row["jenis_komoditi"]}, Profit: {row["omzet"]}')
                line_count += 1
        print(f'Processed {line_count} lines')