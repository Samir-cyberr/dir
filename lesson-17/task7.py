import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['skyblue', 'orange', 'green', 'red', 'purple']

plt.figure(figsize=(8, 5))
plt.bar(products, sales, color=colors)

plt.title('Sales Data of Products')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
