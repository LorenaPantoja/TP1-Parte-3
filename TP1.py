"""
Este módulo contiene las funciones para el procesamiento de datos del TP2.
Autor: Lorena Pantoja
Fecha: 
"""

# 1. Cargar los archivos CSV en DataFrames de Pandas

import pandas as pd

# Cargar los archivos CSV en DataFrames
customers_df = pd.read_csv('ecommerce_customers_dataset.csv')
orders_df = pd.read_csv('ecommerce_orders_dataset.csv')
order_items_df = pd.read_csv('ecommerce_order_items_dataset.csv')
products_df = pd.read_csv('ecommerce_products_dataset.csv')
payments_df = pd.read_csv('ecommerce_order_payments_dataset.csv')

# Visualizar los primeros registros de cada DataFrame para verificar la carga correcta
print(customers_df.head())
print(orders_df.head())
print(order_items_df.head())
print(products_df.head())
print(payments_df.head())


# 2. Establecer la columna índices de las tablas como la clave primaria

# Establecer las columnas índices
customers_df.set_index('customer_id', inplace=True)
orders_df.set_index('order_id', inplace=True)
order_items_df.set_index('order_id', inplace=True)
products_df.set_index('product_id', inplace=True)
payments_df.set_index('order_id', inplace=True)

# 3. Obtener el número total de clientes únicos en el conjunto de datos

total_customers = customers_df['customer_unique_id'].nunique()
print(f'Número total de clientes únicos: {total_customers}')

# 4. Calcular el promedio de valor de pago por pedido

average_payment_value = payments_df['payment_value'].mean()
print(f'Promedio de valor de pago por pedido: {average_payment_value:.2f}')

# 5. Determinar la categoría de producto más vendida

# Unir las tablas de order_items y products
merged_df = order_items_df.merge(products_df, left_on='product_id', right_on='product_id')

# Contar las ventas por categoría
category_counts = merged_df['product_category_name'].value_counts()
most_sold_category = category_counts.idxmax()
print(f'Categoría de producto más vendida: {most_sold_category}')

# 6. Calcular el número total de pedidos realizados

total_orders = orders_df.shape[0]
print(f'Número total de pedidos realizados: {total_orders}')

# FINAL DEL CODIGO


git remote add origin https://github.com/usuario/nombre-del-repositorio.git
