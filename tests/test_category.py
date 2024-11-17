def test_category(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации."
    assert len(first_category.products) == 2
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Комфорт и эстетика."
    assert len(second_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
