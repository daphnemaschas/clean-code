import pytest

from gilded_rose import GildedRose, Item


@pytest.mark.parametrize(
    "name, sell_in, quality, expected_sell_in, expected_quality",
    [
        # Regular item: quality decreases by 1
        ("bread", 20, 40, 19, 39),
        # Regular item past sell date: quality decreases by 2
        ("bread", 0, 40, -1, 38),
        # Regular item: quality never goes negative
        ("bread", 0, 0, -1, 0),
        # Aged Brie: quality increases
        ("Aged Brie", 10, 2, 9, 3),
        # Aged Brie: quality capped at 50
        ("Aged Brie", 10, 50, 9, 50),
        # Sulfuras: unchanging quality
        ("Sulfuras, Hand of Ragnaros", 10, 40, 10, 40),
        # Backstage pass: normal increase
        ("Backstage passes to a TAFKAL80ETC concert", 15, 40, 14, 41),
        # Backstage pass: double increase
        ("Backstage passes to a TAFKAL80ETC concert", 10, 40, 9, 42),
        # Backstage pass: triple increase
        ("Backstage passes to a TAFKAL80ETC concert", 5, 40, 4, 43),
        # Backstage pass: quality drops to 0 after the concert
        ("Backstage passes to a TAFKAL80ETC concert", 0, 40, -1, 0),
        # Backstage pass: quality capped at 50
        ("Backstage passes to a TAFKAL80ETC concert", 5, 49, 4, 50),
    ],
)
def test_update_quality(name, sell_in, quality, expected_sell_in, expected_quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    updated_items = gilded_rose.items
    assert updated_items[0].sell_in == expected_sell_in
    assert updated_items[0].quality == expected_quality
