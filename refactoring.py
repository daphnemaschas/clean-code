"""Order processing helpers and API.

This module provides a single high-level function `process_order` which
validates order inputs, calculates shipping and discounts, and returns a
summary dictionary. Helper functions are small and pure to make the code
easier to test and read.
"""

from typing import Optional, Dict


def _get_shipping_cost(country_code: str) -> float:
    """Return the flat shipping cost for a given country code.

    Unknown country codes receive a default shipping cost.

    Args:
        country_code: ISO-like country code (e.g. 'FR', 'DE', 'US').

    Returns:
        Shipping cost as a float.
    """
    mapping = {"FR": 10.0, "DE": 15.0, "US": 20.0}
    return mapping.get((country_code or "").upper(), 30.0)


def _get_discount_rate(discount_code: Optional[str]) -> float:
    """Return the discount rate for a discount code.

    The function is tolerant of None and is case-insensitive.

    Args:
        discount_code: Discount code string or None.

    Returns:
        Discount as a fraction (e.g. 0.10 for 10%).
    """
    if not discount_code:
        return 0.0
    return 0.10 if discount_code.strip().upper() == "DISCOUNT10" else 0.0


def process_order(
    customer_name: str,
    product_name: str,
    price: float,
    quantity: int,
    country_code: str,
    discount_code: Optional[str] = None,
) -> Dict[str, object]:
    """Process a single order and return a summary dictionary.

    The function validates the minimal required inputs, computes shipping
    cost and discount, and returns the computed total and a status string.

    Args:
        customer_name: Customer's full name (non-empty).
        product_name: Product name (non-empty).
        price: Unit price (must be >= 0).
        quantity: Quantity ordered (must be >= 1).
        country_code: Country code used to determine shipping cost.
        discount_code: Optional discount code.

    Returns:
        A dictionary with keys: 'customer_name', 'product_name', 'total_price',
        and 'status' where status is 'VIP' for totals > 100, otherwise
        'STANDARD'.

    Raises:
        ValueError: If required fields are missing or numeric values are invalid.
    """
    # Basic validation
    if not customer_name or not customer_name.strip():
        raise ValueError("customer_name must be provided and non-empty")
    if not product_name or not product_name.strip():
        raise ValueError("product_name must be provided and non-empty")
    if price is None or not isinstance(price, (int, float)) or price < 0:
        raise ValueError("price must be a non-negative number")
    if quantity is None or not isinstance(quantity, int) or quantity < 1:
        raise ValueError("quantity must be an integer >= 1")

    shipping_cost = _get_shipping_cost(country_code)
    discount = _get_discount_rate(discount_code)

    subtotal = float(price) * int(quantity)
    total_price = subtotal * (1.0 - discount) + shipping_cost

    status = "VIP" if total_price > 100.0 else "STANDARD"

    return {
        "customer_name": customer_name.strip(),
        "product_name": product_name.strip(),
        "total_price": total_price,
        "status": status,
    }
