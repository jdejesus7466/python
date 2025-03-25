import csv

if __name__ == "__main__":

    best_seller = None
    highest_sales = 0.0

    with open('bestsellers.csv', 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for row in csv_reader:
            sales = float(row[4])
            if sales > highest_sales:
                highest_sales = sales
                best_seller = row
    
    with open('bestseller_info.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        
        csv_writer.writerow(header)  
        csv_writer.writerow(best_seller)
