from swoop import SearchLeg, SORT_CHEAPEST, search_legs

results = search_legs(
    [
        SearchLeg(
            date="2027-04-03",
            from_airport="TLV",
            to_airport="KIX",
            max_stops=1,
        ),
        SearchLeg(
            date="2027-04-22",
            from_airport="NRT",
            to_airport="TLV",
            max_stops=1,
        ),
    ],
    adults=2,
    children=0,
    cabin="economy",
    sort=SORT_CHEAPEST,
    country="IL",
    retries=3,
)

if not results.results:
    raise RuntimeError("No matching Open Jaw results were found.")

cheapest = results.results[0]
currency = cheapest.currency or results.currency or ""

print(f"Cheapest total price: {cheapest.price} {currency}")
print("Route: TLV → KIX | NRT → TLV")
print("Dates: 3 April 2027 → 22 April 2027")
print("Travellers: 2 adults")
print("Maximum stops: 1 per flight")
