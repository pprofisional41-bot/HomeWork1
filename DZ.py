import csv
import json

target_date = input("Введите дату (0000-00-00): ")

daily_products = {}
store_revenue = {}

with open('sales_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Date'] == target_date:
            product = row['Product']
            store = row['Store']
            qt = int(row['Quantity'])
            price = float(row['Price'])

            daily_products[product] = daily_products.get(product, 0) + qt

            store_revenue[store] = store_revenue.get(store, 0) + (qt * price)

if not store_revenue:
    print(f"За дату {target_date} данных не найдено. Проверьте CSV-файл.")
else:

    best_store = max(store_revenue, key=store_revenue.get)
    print(f"Наибольшие продажи за {target_date}: {best_store} с объёмом продаж {store_revenue[best_store]}")

    report_list = []
    for prod, qt in daily_products.items():
        report_list.append({"product": prod, "total_sales": qt})

    final_report = {target_date: report_list}
    with open('report.json', 'w', encoding='utf-8') as f:
        json.dump(final_report, f, indent=4, ensure_ascii=False)
    print("Отчет report.json успешно создан.")

