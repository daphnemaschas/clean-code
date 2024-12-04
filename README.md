# <span style="color:#5D6D7E;">Set Up</span>

Follow these steps to set up the project on your machine.

## <span style="color:#5D6D7E;">Step 1: Install uv</span>

uv is used to manage dependencies and environments. If you don’t have uv installed, follow the instructions from the [official documentation](https://docs.astral.sh/uv/getting-started/installation/)

After installation, close your terminal and open a new one to verify that uv is installed by running:

```bash
uv
```
```bash
An extremely fast Python package manager.

Usage: uv [OPTIONS] <COMMAND>

...
```

## <span style="color:#5D6D7E;">Step 2: Clone the Repository</span>

Then, navigate to your desired directory and download the repository to your local machine by running:

```bash
git clone https://github.com/louis-marx/clean-code.git
````

Then navigate to the project folder:

```bash
cd clean-code
```

## <span style="color:#5D6D7E;">Step 3: Run Tests</span>

This project uses pytest for testing. To verify that everything is set up correctly, run:

```bash
uv run pytest
```
```bash
Using CPython 3.12.7
Creating virtual environment at: .venv
Installed 4 packages in 7ms
=================================== test session starts ====================================
platform darwin -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /path/to/project/directory
configfile: pyproject.toml
collected 11 items                                                 

tests/test_gilded_rose.py ...........                                                 [100%]

==================================== 11 passed in 0.01s ====================================
```

You should also try to run the testtest fixture, for e.g. 10 days:

```
uv run src/texttest_fixture.py 10
```

# <span style="color:#5D6D7E;">Gilded Rose Requirements Specification</span>

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in `Quality` as they approach their sell by date.

We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that
we can begin selling a new category of items. First an introduction to our system:

- All `items` have a `SellIn` value which denotes the number of days we have to sell the `items`
- All `items` have a `Quality` value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

Pretty simple, right? Well this is where it gets interesting:

- Once the sell by date has passed, `Quality` degrades twice as fast
- The `Quality` of an item is never negative
- __"Aged Brie"__ actually increases in `Quality` the older it gets
- The `Quality` of an item is never more than `50`
- __"Sulfuras"__, being a legendary item, never has to be sold or decreases in `Quality`
- __"Backstage passes"__, like aged brie, increases in `Quality` as its `SellIn` value approaches;
	- `Quality` increases by `2` when there are `10` days or less and by `3` when there are `5` days or less but
	- `Quality` drops to `0` after the concert

We have recently signed a supplier of conjured items. This requires an update to our system:

- __"Conjured"__ items degrade in `Quality` twice as fast as normal items

Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything
still works correctly. However, do not alter the `Item` class or `Items` property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the `UpdateQuality` method and `Items` property static if you like, we'll cover
for you).

Just for clarification, an item can never have its `Quality` increase above `50`, however __"Sulfuras"__ is a
legendary item and as such its `Quality` is `80` and it never alters.
