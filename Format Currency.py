def lkr(value):
    """Format value as LKR."""
    return f"Rs {value:,.2f}"
formattedValue= lkr(50000)
print(formattedValue)
