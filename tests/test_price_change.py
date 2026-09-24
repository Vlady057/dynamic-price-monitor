from src.price_monitor import (
    calculate_price_change,
    get_price_status,
    format_price_change,
    check_price
)


# =========================
# calculate_price_change
# =========================

def test_price_decrease():
    difference, percentage = calculate_price_change(1695, 1599)

    assert difference == -96
    assert round(percentage, 2) == -5.66


def test_price_increase():
    difference, percentage = calculate_price_change(1599, 1695)

    assert difference == 96
    assert round(percentage, 2) == 6.00


def test_price_unchanged():
    difference, percentage = calculate_price_change(1695, 1695)

    assert difference == 0
    assert percentage == 0


# =========================
# get_price_status
# =========================

def test_status_decreased():
    status = get_price_status(1695, 1599)

    assert status == "decreased"


def test_status_increased():
    status = get_price_status(1599, 1695)

    assert status == "increased"


def test_status_unchanged():
    status = get_price_status(1695, 1695)

    assert status == "unchanged"


# =========================
# format_price_change
# =========================

def test_format_price_decrease():
    result = format_price_change(-96, -5.66)

    assert result == ("-96.00 UAH", "-5.66%")


def test_format_price_increase():
    result = format_price_change(96, 6.00)

    assert result == ("+96.00 UAH", "+6.00%")


def test_format_price_unchanged():
    result = format_price_change(0, 0)

    assert result == ("0.00 UAH", "0.00%")


# =========================
# check_price
# =========================

def test_check_price_decreased():

    result = check_price(1695, 1599)

    assert result["status"] == "decreased"
    assert result["difference"] == -96
    assert round(result["percentage"], 2) == -5.66
    assert result["formatted_difference"] == "-96.00 UAH"
    assert result["formatted_percentage"] == "-5.66%"


def test_check_price_increased():

    result = check_price(1599, 1695)

    assert result["status"] == "increased"
    assert result["difference"] == 96
    assert round(result["percentage"], 2) == 6.00
    assert result["formatted_difference"] == "+96.00 UAH"
    assert result["formatted_percentage"] == "+6.00%"


def test_check_price_unchanged():

    result = check_price(1695, 1695)

    assert result["status"] == "unchanged"
    assert result["difference"] == 0
    assert result["percentage"] == 0
    assert result["formatted_difference"] == "0.00 UAH"
    assert result["formatted_percentage"] == "0.00%"