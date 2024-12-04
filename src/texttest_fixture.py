import argparse

from gilded_rose import GildedRose, Item


def parse_arguments():
    """
    Parse command-line arguments for the number of simulation days.
    """
    parser = argparse.ArgumentParser(
        description="Simulate the Gilded Rose inventory system."
    )
    parser.add_argument(
        "days",
        type=int,
        nargs="?",
        default=2,
        help="Number of days to run the simulation (default: 2).",
    )
    return parser.parse_args()


def create_items():
    """
    Create the list of initial items for the Gilded Rose shop.
    """
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]


def simulate_gilded_rose(items, days):
    """
    Simulate the Gilded Rose inventory system for a given number of days.

    Args:
        items (list of Item): List of items to simulate.
        days (int): Number of days to simulate.
    """
    for day in range(days):
        print(f"-------- Day {day} --------")
        print(f"{'Name':<45} {'Sell In':<10} {'Quality':<10}")
        print("-" * 65)
        for item in items:
            print(f"{item.name:<45} {item.sell_in:<10} {item.quality:<10}")
        print("")
        GildedRose(items).update_quality()


def main():
    """
    Main function to run the Gilded Rose simulation.
    """
    args = parse_arguments()
    items = create_items()
    simulate_gilded_rose(items, args.days + 1)


if __name__ == "__main__":
    main()
