import io
import contextlib

PRODUCTS = [
    ("Laptop", 1200.0, "electronics"),
    ("Headphones", 200.0, "electronics"),
    ("Coffee Beans", 15.0, "food"),
    ("Notebook", 5.0, "stationery"),
    ("Water Bottle", 10.0, "food"),
    ("Monitor", 300.0, "electronics"),
    ("Pen", 2.0, "stationery"),
]
TAXRATE = 0.07
foodtax = 0.0
ORDERS = [
    ("Alice", "gold", [(0, 1), (1, 2), (2, 3)]),
    ("Bob", "none", [(3, 10), (6, 5)]),
    ("Charlie", "platinum", [(5, 2), (4, 6), (2, 2)]),
    ("Dana", "silver", [(1, 1), (3, 3), (6, 10)]),
]


def calc(o):
    global TAXRATE
    n = o[0]; t = o[1]; items = o[2]
    sub = 0.0; tax = 0.0
    print("Receipt for " + n + " (" + t + ")")
    print("-" * 40)
    for it in items:
        pi = it[0]; q = it[1]
        p = PRODUCTS[pi][1]; nm = PRODUCTS[pi][0]; cat = PRODUCTS[pi][2]
        line = p * q
        sub = sub + line
        if cat == "food":
            tax = tax + line * foodtax
        else:
            tax = tax + line * TAXRATE
        print(nm + " x" + str(q) + " = " + str(line))
    d = 0.0
    if t == "none":
        d = 0.0
    elif t == "silver":
        if sub > 100: d = sub * 0.05
        else: d = sub * 0.02
    elif t == "gold":
        if sub > 100: d = sub * 0.10
        else: d = sub * 0.05
    elif t == "platinum":
        if sub > 100: d = sub * 0.15
        else: d = sub * 0.10
    totalqty = 0
    for it in items:
        totalqty = totalqty + it[1]
    if totalqty >= 10:
        d = d + sub * 0.03
    total = sub - d + tax
    pts = 0
    if t == "none": pts = int(total // 10)
    elif t == "silver": pts = int(total // 10) * 2
    elif t == "gold": pts = int(total // 10) * 3
    elif t == "platinum": pts = int(total // 10) * 5
    print("-" * 40)
    print("Subtotal: " + str(round(sub, 2)))
    print("Discount: " + str(round(d, 2)))
    print("Tax: " + str(round(tax, 2)))
    print("Total: " + str(round(total, 2)))
    print("Points earned: " + str(pts))
    print("")
    return total


def legacy_main():
    grand = 0.0
    for o in ORDERS:
        grand = grand + calc(o)
    print("GRAND TOTAL (all orders): " + str(round(grand, 2)))


def capture(fn):
    """Run fn() and return everything it printed, as a string."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


GOLDEN_OUTPUT = capture(legacy_main)

TAX_RATE = 0.07
FOOD_TAX_RATE = 0.0
FOOD_CATEGORY = "food"
DISCOUNT_THRESHOLD = 100
BULK_QTY_THRESHOLD = 10
BULK_DISCOUNT_RATE = 0.03
POINTS_DIVISOR = 10
RECEIPT_WIDTH = 40


class Product:
    """A store product with its own tax behavior."""

    def __init__(self, name, price, category):
        if not isinstance(name, str) or not name:
            raise ValueError("Product name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Product price must be a non-negative number")
        if not isinstance(category, str) or not category:
            raise ValueError("Product category must be a non-empty string")
        self.name = name
        self.price = price
        self.category = category

    @property
    def tax_rate(self):
        return FOOD_TAX_RATE if self.category == FOOD_CATEGORY else TAX_RATE


class OrderItem:
    """A product and a validated quantity in an order."""

    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Order item product must be a Product")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 1:
            raise ValueError("Order item quantity must be an integer of at least 1")
        self.product = product
        self.quantity = quantity

    def line_total(self):
        return self.product.price * self.quantity


class Customer:
    """Base membership behavior; subclasses provide tier-specific rates."""

    tier = "none"
    points_multiplier = 1
    small_order_rate = 0.0
    large_order_rate = 0.0

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Customer name must be a non-empty string")
        self.name = name

    def discount_rate(self, subtotal):
        if subtotal > DISCOUNT_THRESHOLD:
            return self.large_order_rate
        return self.small_order_rate

    def points_for(self, total):
        return int(total // POINTS_DIVISOR) * self.points_multiplier


class SilverCustomer(Customer):
    tier = "silver"
    points_multiplier = 2
    small_order_rate = 0.02
    large_order_rate = 0.05


class GoldCustomer(Customer):
    tier = "gold"
    points_multiplier = 3
    small_order_rate = 0.05
    large_order_rate = 0.10


class PlatinumCustomer(Customer):
    tier = "platinum"
    points_multiplier = 5
    small_order_rate = 0.10
    large_order_rate = 0.15


CUSTOMER_TYPES = {
    "none": Customer,
    "silver": SilverCustomer,
    "gold": GoldCustomer,
    "platinum": PlatinumCustomer,
}


class Order:
    """An order owns one customer and a collection of product items."""

    def __init__(self, customer, items):
        if not isinstance(customer, Customer):
            raise TypeError("Order customer must be a Customer")
        if not items or not all(isinstance(item, OrderItem) for item in items):
            raise ValueError("Order must contain OrderItem objects")
        self.customer = customer
        self.items = list(items)

    def subtotal(self):
        return sum(item.line_total() for item in self.items)

    def discount(self):
        subtotal = self.subtotal()
        discount = subtotal * self.customer.discount_rate(subtotal)
        if sum(item.quantity for item in self.items) >= BULK_QTY_THRESHOLD:
            discount += subtotal * BULK_DISCOUNT_RATE
        return discount

    def tax(self):
        return sum(item.line_total() * item.product.tax_rate for item in self.items)

    def total(self):
        return self.subtotal() - self.discount() + self.tax()

    def points(self):
        return self.customer.points_for(self.total())

    def receipt(self):
        lines = [
            "Receipt for " + self.customer.name + " (" + self.customer.tier + ")",
            "-" * RECEIPT_WIDTH,
        ]
        for item in self.items:
            lines.append(
                item.product.name + " x" + str(item.quantity) + " = " + str(item.line_total())
            )
        lines.extend([
            "-" * RECEIPT_WIDTH,
            "Subtotal: " + str(round(self.subtotal(), 2)),
            "Discount: " + str(round(self.discount(), 2)),
            "Tax: " + str(round(self.tax(), 2)),
            "Total: " + str(round(self.total(), 2)),
            "Points earned: " + str(self.points()),
            "",
        ])
        return "\n".join(lines)


def build_orders():
    products = [
        Product("Laptop", 1200.0, "electronics"),
        Product("Headphones", 200.0, "electronics"),
        Product("Coffee Beans", 15.0, "food"),
        Product("Notebook", 5.0, "stationery"),
        Product("Water Bottle", 10.0, "food"),
        Product("Monitor", 300.0, "electronics"),
        Product("Pen", 2.0, "stationery"),
    ]
    return [
        Order(CUSTOMER_TYPES["gold"]("Alice"), [
            OrderItem(products[0], 1), OrderItem(products[1], 2), OrderItem(products[2], 3),
        ]),
        Order(CUSTOMER_TYPES["none"]("Bob"), [
            OrderItem(products[3], 10), OrderItem(products[6], 5),
        ]),
        Order(CUSTOMER_TYPES["platinum"]("Charlie"), [
            OrderItem(products[5], 2), OrderItem(products[4], 6), OrderItem(products[2], 2),
        ]),
        Order(CUSTOMER_TYPES["silver"]("Dana"), [
            OrderItem(products[1], 1), OrderItem(products[3], 3), OrderItem(products[6], 10),
        ]),
    ]


def refactored_main():
    """Print every receipt and the grand total — same output as legacy_main()."""
    orders = build_orders()
    grand_total = 0.0
    for order in orders:
        print(order.receipt())
        grand_total += order.total()
    print("GRAND TOTAL (all orders): " + str(round(grand_total, 2)))

def _check():
    try:
        your_output = capture(refactored_main)
    except NotImplementedError:
        print("Solution not implemented yet.\n")
        print("Below is the TARGET output your refactor must reproduce exactly:\n")
        print(GOLDEN_OUTPUT)
        return

    if your_output == GOLDEN_OUTPUT:
        print("PASS - behaviour is unchanged. Your refactor is safe.\n")
    else:
        print("FAIL - the output changed, so this is not yet a valid refactor.\n")
        g = GOLDEN_OUTPUT.splitlines()
        y = your_output.splitlines()
        for i in range(max(len(g), len(y))):
            gl = g[i] if i < len(g) else "<no line>"
            yl = y[i] if i < len(y) else "<no line>"
            if gl != yl:
                print("First difference at line " + str(i + 1) + ":")
                print("  expected: " + repr(gl))
                print("  yours:    " + repr(yl))
                break


if __name__ == "__main__":
    _check()

