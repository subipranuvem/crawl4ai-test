import asyncio

from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://sg.portal-pokemon.com/play/pokedex/0981",
            cache_mode=CacheMode.DISABLED,
            config=CrawlerRunConfig(
                cache_mode=CacheMode.DISABLED,
                simulate_user=True,
                magic=True,
            ),
        )

        if result.markdown_v2:
            print(result.markdown_v2)


if __name__ == "__main__":
    asyncio.run(main())
