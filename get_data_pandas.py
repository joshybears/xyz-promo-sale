import sqlite3
import pandas

con = sqlite3.connect("xyz-promo-sale.db")

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

df = pandas.read_sql_query(query, con)

df.to_csv('result_pandas.csv', sep=';', index=False)

print("All done! Data printed to result_pandas.csv")