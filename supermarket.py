import unittest

class Supermarket(unittest.TestCase):
    def __init__(self) -> None:
        self.totalPrice = 0
        self.itemPrice = { 
            "A" : 50,
            "B" : 30,
            "C" : 20,
            "D" : 15
        }
        self.specialPrice = {
            "A" : 30,
            "B" : 15
        }
        self.rawCart = []
        self.itemA = 0
        self.itemB = 0

    def addItem(self, item):
        self.rawCart.append(item)
        if item == "B":
            self.itemB = self.itemB + 1
        elif item == "A":
            self.itemA = self.itemA + 1

    def getPrice(self):
        price = 0
        for item in self.rawCart:
            itemPrice = self.getItemPrice(item)
            price += itemPrice
        self.itemA = 0
        self.itemB = 0
        return price

    def getItemPrice(self, item):
        finalPrice = self.itemPrice[item]
        if self.itemB >= 2:
            finalPrice = self.specialPrice[item]
            self.itemB = self.itemB - 2
        elif self.itemA >= 3:
            finalPrice = self.specialPrice[item]
            self.itemA = self.itemA - 3
        return finalPrice

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

if __name__ == "__main__":
    unittest.main()