class Product:
  def __init__(self, id, name, price, description, stock):
    self.id = id
    self.name = name
    self.price = price
    self.description = description
    self.stock = stock

class Customer:
  def __init__(self, name, email, address):
    self.name = name
    self.email = email
    self.address = address

class CartItem:
  def __init__(self, product, quantity):
    self.product = product
    self.quantity = quantity

  def get_subtotal(self):
    return self.product.price * self.quantity

class ShoppingCart:
  def __init__(self):
    self.items = []

  def add_item(self, product, quantity):
    if product.stock >= quantity:
      existing_item = next((item for item in self.items if item.product == product), None)
      if existing_item:
        existing_item.quantity += quantity
      else:
        self.items.append(CartItem(product, quantity))
        product.stock -= quantity
    else:
      print(f"Insufficient stock for {product.name}. Only {product.stock} available.")

  def remove_item(self, product):
    item = next((item for item in self.items if item.product == product), None)
    if item:
      product.stock += item.quantity
      self.items.remove(item)

  def get_total(self):
    return sum(item.get_subtotal() for item in self.items)

  def __str__(self):
    if self.items:
      return "\n".join(f"{item.product}: {item.quantity} x ${item.product.price} = ${item.get_subtotal()}" for item in self.items)
    else:
      return "Cart is empty."

class Order:
  def __init__(self, customer, cart):
    self.customer = customer
    self.cart = cart
    self.total_cost = cart.get_total()

  def process(self):
    # Simulate order processing
    print(f"Order placed successfully for {self.customer.name} with a total cost of ${self.total_cost}.")

# Example usage
product1 = Product(1, "T-shirt", 19.99, "Cool T-shirt", 10)
product2 = Product(2, "Mug", 9.99, "Funny mug", 20)

customer1 = Customer("John Doe", "johndoe@example.com", "123 Main St")

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 1)

print("Cart:")
print(cart)

order = Order(customer1, cart)
order.process()
