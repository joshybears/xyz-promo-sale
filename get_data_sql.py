import sqlite3
import csv

query = """
    SELECT
        c.customer_id as "Customer",
        c.age as "Age",
        i.item_name as "Item",
        sum(o.quantity) as "Quantity"
    FROM
        customers c
    JOIN
        sales s
    ON
        c.customer_id = s.customer_id 
    JOIN
        orders o
    ON
        s.sales_id = o.sales_id 
    JOIN
        items i
    ON
        i.item_id = o.item_id 
    WHERE
        c.age BETWEEN 18 and 35
    GROUP BY
        1,2,3
    HAVING 
        SUM(o.quantity) > 0;
"""

with open('result_sql.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')

    csv_writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])

    with sqlite3.connect("xyz-promo-sale.db") as connection:
        cursor = connection.cursor()

        cursor.execute(query)
        for row in cursor.fetchall():
            csv_writer.writerow(row)

print("All done! Data printed to result_sql.csv")