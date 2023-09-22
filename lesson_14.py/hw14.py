import asyncio
import aiohttp
import aiofiles
import logging


urls_to_scrape = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def scrape_and_save(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.text()
                async with aiofiles.open(
                    f'{url.split("/")[-1]}.html', "w"
                ) as file:
                    await file.write(data)
                logger.info(f"Saved data from {url}")
        except (aiohttp.ClientError, IOError) as e:
            logger.error(f"Error while scraping {url}: {str(e)}")


async def main():
    tasks = [scrape_and_save(url) for url in urls_to_scrape]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
