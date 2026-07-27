from swoop import (
    Passengers,
    SearchLeg,
    SORT_CHEAPEST,
    TransportConfig,
    search_legs,
)


def get_cheapest(departure_date, return_date):
    results = search_legs(
        [
            SearchLeg(
                date=departure_date,
                from_airport="TLV",
                to_airport="KIX",
                max_stops=1,
            ),
            SearchLeg(
                date=return_date,
                from_airport="NRT",
                to_airport="TLV",
                max_stops=1,
            ),
        ],
        passengers=Passengers(
            adults=2,
            children=0,
        ),
        cabin="economy",
        sort=SORT_CHEAPEST,
        transport=TransportConfig(
            country="IL",
            retries=3,
        ),
    )

    valid_results = [
        item
        for item in results.results
        if item.price is not None
    ]

    if not valid_results:
        return "No priced results found"

    cheapest = min(
        valid_results,
        key=lambda item: item.price,
    )

    currency = cheapest.currency or results.currency or ""

    return f"{cheapest.price} {currency}"


price_1_20 = get_cheapest(
    "2027-04-01",
    "2027-04-20",
)

price_3_22 = get_cheapest(
    "2027-04-03",
    "2027-04-22",
)

print("OPEN JAW FLIGHT PRICE UPDATE")
print()
print(f"1 April 2027 -> 20 April 2027: {price_1_20}")
print(f"3 April 2027 -> 22 April 2027: {price_3_22}")
print()
print("Route: TLV -> KIX | NRT -> TLV")
print("Travellers: 2 adults")
print("Maximum stops: 1 per direction")
