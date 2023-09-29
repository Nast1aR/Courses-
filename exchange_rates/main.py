import asyncio
import argparse
import aiohttp

API_KEY = "RWPDOCB60S5GG7JA"
BASE_URL = "https://www.alphavantage.co/query"


async def fetch_exchange_rate(session, from_currency, to_currency):
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_currency,
        "to_currency": to_currency,
        "apikey": API_KEY,
    }
    async with session.get(BASE_URL, params=params) as response:
        data = await response.json()
        exchange_rate = data["Realtime Currency Exchange Rate"][
            "5. Exchange Rate"
        ]
        return f"{from_currency} to {to_currency}: {exchange_rate}"


async def main():
    parser = argparse.ArgumentParser(
        description="Fetch currency exchange rates."
    )
    parser.add_argument(
        "source_currencies",
        nargs="+",
        help="Source currencies to convert from",
    )
    parser.add_argument(
        "--target", required=True, help="Target currency to convert to"
    )
    args = parser.parse_args()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for source_currency in args.source_currencies:
            task = fetch_exchange_rate(session, source_currency, args.target)
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
