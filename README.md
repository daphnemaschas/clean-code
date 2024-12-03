# <span style="color:#5D6D7E;">Set Up</span>

Follow these steps to set up the project on your machine.

## <span style="color:#5D6D7E;">Step 1: Clone the Repository</span>

First, download the repository to your local machine. Open your terminal or command prompt and run:

```bash
git clone https://github.com/louis-marx/clean-code.git
````

Then navigate to the project folder:

```bash
cd clean-code
```

## <span style="color:#5D6D7E;">Step 2: Install uv</span>

uv is used to manage dependencies and environments. If you don’t have uv installed, follow the instructions below:

### <span style="color:#F5C078;">For macOS and Linux</span>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### <span style="color:#F5C078;">For Windows</span>

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, verify that uv is installed by running:

```bash
uv --version
```

You should see the installed version of uv.

## <span style="color:#5D6D7E;">Step 3: Set Up the Environment</span>

Inside the project folder, follow these steps to set up your environment:

1. Create and activate a new environment using uv:

```bash
uv env install
```

2. Install all the project dependencies:

```bash
uv install
```

This command ensures that all required libraries are installed and ready to use.

## <span style="color:#5D6D7E;">Step 4: Run Tests</span>

This project uses pytest for testing. To verify that everything is set up correctly, run:

```bash
pytest
```


# <span style="color:#5D6D7E;">Gilded Rose Requirements Specification</span>

Hi and welcome to team **Gilded Rose**. As you know, we are a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in quality as they approach their sell-by date. We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

- All items have a `SellIn` value which denotes the number of days we have to sell the item.
- All items have a `Quality` value which denotes how valuable the item is.
- At the end of each day our system lowers both values for every item.

Pretty simple, right? Well this is where it gets interesting:

- Once the sell-by date has passed, <span style="color:#F5C078;">`Quality` degrades twice as fast</span>.
- The <span style="color:#F5C078;">`Quality` of an item is never negative</span>.
- `"Aged Brie"` actually <span style="color:#F5C078;">increases in `Quality`</span> the older it gets.
- The <span style="color:#F5C078;">`Quality` of an item is never more than 50</span>.
- `"Sulfuras"`, being a legendary item, <span style="color:#F5C078;">never has to be sold or decreases in `Quality`</span>.
- `"Backstage passes"`, like `"Aged Brie"`, <span style="color:#F5C078;">increase in `Quality`</span> as their `SellIn` value approaches:
  - <span style="color:#F5C078;">`Quality` increases by 2</span> when there are 10 days or less.
  - <span style="color:#F5C078;">`Quality` increases by 3</span> when there are 5 days or less.
  - <span style="color:#F5C078;">`Quality` drops to 0</span> after the concert.

We have recently signed a supplier of `"Conjured"` items. This requires an update to our system:

- `"Conjured"` items <span style="color:#F5C078;">degrade in `Quality` twice as fast</span> as normal items.

Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything still works correctly. However, do not alter the `Item` class or `Items` property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership (you can make the `UpdateQuality` method and `Items` property static if you like, we'll cover for you).

Just for clarification, an item can <span style="color:#F5C078;">never have its `Quality` increase above 50</span>, however `"Sulfuras"` is a legendary item and as such its `Quality` is 80 and <span style="color:#F5C078;">it never alters</span>.
