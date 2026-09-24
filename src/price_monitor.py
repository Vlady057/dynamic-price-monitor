def calculate_price_change(old_price, new_price):
    difference = new_price - old_price
    percentage = difference / old_price * 100

    return difference, percentage


def get_price_status(old_price, new_price):
    if new_price < old_price:
        return "decreased"

    elif new_price > old_price:
        return "increased"

    return "unchanged"


def format_price_change(difference, percentage):
    if difference > 0:
        return (
            f"+{difference:.2f} UAH",
            f"+{percentage:.2f}%"
        )

    elif difference < 0:
        return (
            f"{difference:.2f} UAH",
            f"{percentage:.2f}%"
        )

    return (
        "0.00 UAH",
        "0.00%"
    )


def check_price(old_price, new_price):
    difference, percentage = calculate_price_change(
        old_price,
        new_price
    )

    status = get_price_status(
        old_price,
        new_price
    )

    formatted_difference, formatted_percentage = (
        format_price_change(
            difference,
            percentage
        )
    )

    return {
        "status": status,
        "difference": difference,
        "percentage": percentage,
        "formatted_difference": formatted_difference,
        "formatted_percentage": formatted_percentage
    }