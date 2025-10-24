"""Gilded Rose kata - refactored version.

This module preserves the original behavior but improves readability by
introducing small helper functions and docstrings. The public API is the
same: an `Item` class and a `GildedRose` class with an `update_quality`
method that mutates the items in place.
"""

from typing import List


class Item:
    """Represents an inventory item.

    Keeps the simple structure used by the kata: `name`, `sell_in`, and
    `quality`. The `__repr__` is kept for backward compatibility with
    existing tests and usages.
    """

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    """Process a list of `Item` objects and update their quality each day.

    The implementation preserves the original rules:
    - "Sulfuras, Hand of Ragnaros" never changes.
    - "Aged Brie" increases in quality the older it gets (max 50).
    - "Backstage passes" increase as the concert date approaches, and
      drop to 0 after the concert.
    - Normal items decrease in quality and degrade twice as fast after
      the sell date.
    """

    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def _increase_quality(self, item: Item, amount: int = 1) -> None:
        """Increase quality without exceeding 50."""
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item: Item, amount: int = 1) -> None:
        """Decrease quality without going below 0."""
        item.quality = max(0, item.quality - amount)

    def _is_aged_brie(self, item: Item) -> bool:
        return item.name == "Aged Brie"

    def _is_backstage(self, item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def _is_sulfuras(self, item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    def update_quality(self) -> None:
        """Update all items for one day.

        The method mutates the `items` in place. It follows the sequence of
        operations from the original implementation: first adjust quality
        depending on current `sell_in`, then decrease `sell_in` (except
        for Sulfuras), and finally apply the accelerated rules when
        `sell_in` has passed (< 0).
        """
        for item in self.items:
            # Skip Sulfuras entirely; it does not change.
            if self._is_sulfuras(item):
                continue

            # Day-before-sell adjustments
            if self._is_aged_brie(item):
                # Aged Brie increases in quality
                self._increase_quality(item, 1)
            elif self._is_backstage(item):
                # Backstage passes increase as the date approaches
                self._increase_quality(item, 1)
                if item.sell_in < 11:
                    self._increase_quality(item, 1)
                if item.sell_in < 6:
                    self._increase_quality(item, 1)
            else:
                # Normal items decrease in quality
                if item.quality > 0:
                    self._decrease_quality(item, 1)

            # Decrease sell_in for non-Sulfuras
            item.sell_in -= 1

            # After sell date has passed
            if item.sell_in < 0:
                if self._is_aged_brie(item):
                    # Aged Brie gains an extra quality point
                    self._increase_quality(item, 1)
                elif self._is_backstage(item):
                    # Backstage passes drop to 0 after the concert
                    item.quality = 0
                else:
                    # Normal items degrade twice as fast after sell date
                    if item.quality > 0:
                        self._decrease_quality(item, 1)
