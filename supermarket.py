import unittest

class Supermarket(unittest.TestCase):
    def __init__(self) -> None:
        self.itemCount = {}
        self.itemDiscount = {
            "A" : 3,
            "B" : 2
        }
        self.itemPrice = { 
            "A" : 50,
            "B" : 30,
            "C" : 20,
            "D" : 15
        }
        self.specialPrice = {
            "A" : 130,
            "B" : 45
        }
        self.cart = []

    def addItem(self, item):
        self.cart.append(item)

    def itemCounts(self):
        self.itemCount = {
            "A" : 0,
            "B" : 0,
            "C" : 0,
            "D" : 0
        }
        for item in self.cart:
            self.itemCount[item] += 1

    def getPrice(self):
        price = 0
        self.itemCounts()
        for item in self.itemCount:
            if item in self.itemDiscount:
                discountedPrice = int(self.itemCount[item] / self.itemDiscount[item]) * self.specialPrice[item]
                normalPrice = (self.itemCount[item] % self.itemDiscount[item]) * self.itemPrice[item]
                price += discountedPrice + normalPrice
            else:
                price += self.itemCount[item] * self.itemPrice[item]
        return price

class test_supermarket (unittest.TestCase):
    def test_item_A_returns_price_of_50(self):
        #Arrange
        supermarket = Supermarket()
        item = "A"
        price = 50
        #Act
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()
        #Assert
        self.assertEqual(price, cartPrice)
    
    def test_adds_two_A_items(self):
        supermarket = Supermarket()
        item = "A"
        totalPrice = 100

        supermarket.addItem(item)
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_item_B_plus_item_A(self):
        supermarket = Supermarket()
        firstItem = "B"
        secondItem = "A"
        totalPrice = 80

        supermarket.addItem(firstItem)
        supermarket.addItem(secondItem)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_two_items_of_B_type_with_one_discount(self):
        supermarket = Supermarket()
        item = "B"
        totalPrice = 45

        supermarket.addItem(item)
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_three_items_of_A_type_with_one_discount(self):
        supermarket = Supermarket()
        item = "A"
        totalPrice = 130

        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)
    def test_adds_three_B_items_with_one_discount(self):
        supermarket = Supermarket()
        item = "B"
        totalPrice = 75

        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_two_B_items_plus_item_A_with_one_discount_on_B(self):
        supermarket = Supermarket()
        firstItem = "B"
        secondItem = "A"
        totalPrice = 95

        supermarket.addItem(firstItem)
        supermarket.addItem(secondItem)
        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_four_items_of_A_type_with_one_discount(self):
        supermarket = Supermarket()
        item = "A"
        totalPrice = 180

        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_six_items_of_A_type_with_two_discounts(self):
        supermarket = Supermarket()
        item = "A"
        totalPrice = 260

        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        supermarket.addItem(item)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_a_cart_of_four_different_types_with_various_discounts(self):
        supermarket = Supermarket()
        firstItem = "A"
        secondItem = "B"
        thirdItem = "C"
        forthItem = "D"
        totalPrice = 375

        supermarket.addItem(firstItem)
        supermarket.addItem(firstItem)
        supermarket.addItem(secondItem)
        supermarket.addItem(thirdItem)
        supermarket.addItem(firstItem)
        supermarket.addItem(forthItem)
        supermarket.addItem(firstItem)
        supermarket.addItem(firstItem)
        supermarket.addItem(secondItem)
        supermarket.addItem(thirdItem)
        supermarket.addItem(firstItem)
        supermarket.addItem(forthItem)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

    def test_adds_a_cart_of_four_different_types_with_various_discounts2(self):
        supermarket = Supermarket()
        firstItem = "A"
        secondItem = "B"
        thirdItem = "C"
        forthItem = "D"
        totalPrice = 375

        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(50, cartPrice)
        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(100, cartPrice)
        supermarket.addItem(secondItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(130, cartPrice)
        supermarket.addItem(thirdItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(150, cartPrice)
        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(180, cartPrice)
        supermarket.addItem(forthItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(195, cartPrice)
        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(245, cartPrice)
        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(295, cartPrice)
        supermarket.addItem(secondItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(310, cartPrice)
        supermarket.addItem(thirdItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(330, cartPrice)
        supermarket.addItem(firstItem)
        cartPrice = supermarket.getPrice()
        self.assertEqual(360, cartPrice)
        supermarket.addItem(forthItem)
        cartPrice = supermarket.getPrice()

        self.assertEqual(totalPrice, cartPrice)

if __name__ == "__main__":
    unittest.main()
