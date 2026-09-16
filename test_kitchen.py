from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")

def test_multiplication_by_two():
    flour = Quantity(200, "oz")
    assert flour.times(2) == Quantity(400, "oz")

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")
    assert flour.times(2) == Quantity(400, "g")

def test_equality():
    assert Quantity(200, "g") == Quantity(200, "g")
    assert Quantity(200, "oz") != Quantity(300, "oz")

def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")
