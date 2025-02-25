import asyncio
import base64
import json

from crawl4ai import (
    AsyncWebCrawler,
    CacheMode,
    CrawlerRunConfig,
    JsonXPathExtractionStrategy,
)


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        schema = {
            "name": "Pokémon information",
            "baseSelector": "//div[@class='pokemon-detail']",
            "fields": [
                {
                    "name": "id",
                    "selector": ".//p[@class='pokemon-slider__main-no size-28']",
                    "type": "text",
                },
                {
                    "name": "name",
                    "selector": ".//p[@class='pokemon-slider__main-name size-35']",
                    "type": "text",
                },
                {
                    "name": "height",
                    "selector": ".//span[@class='pokemon-info__title size-14'][text()='Height']/following-sibling::span",
                    "type": "text",
                },
                {
                    "name": "weight",
                    "selector": ".//span[@class='pokemon-info__title size-14'][text()='Weight']/following-sibling::span",
                    "type": "text",
                },
                {
                    "name": "category",
                    "selector": ".//div[contains(@class,'pokemon-info__category')]//span[2]/span",
                    "type": "text",
                },
                {
                    "name": "abillities",
                    "selector": ".//div[@class='pokemon-info__abilities']//span[contains(@class,'pokemon-info__value')]",
                    "type": "list",
                    "fields": [
                        {
                            "name": "item",
                            "type": "text",
                        },
                    ],
                },
                {
                    "name": "abillities_info",
                    "selector": ".//p[@class='pokemon_abillity_created_by_js']",
                    "type": "list",
                    "fields": [
                        {
                            "name": "item",
                            "type": "text",
                        },
                    ],
                },
                {
                    "name": "types",
                    "selector": ".//div[contains(@class,'pokemon-type__type')]//span",
                    "type": "list",
                    "fields": [
                        {
                            "name": "item",
                            "type": "text",
                        },
                    ],
                },
                {
                    "name": "weakness",
                    "selector": ".//div[contains(@class,'pokemon-weakness__btn')]//span",
                    "type": "list",
                    "fields": [
                        {
                            "name": "item",
                            "type": "text",
                        },
                    ],
                },
                {
                    "name": "image_src",
                    "selector": ".//img[@class='pokemon-img__front']",
                    "type": "attribute",
                    "attribute": "src",
                },
            ],
        }

        result = await crawler.arun(
            url="https://sg.portal-pokemon.com/play/pokedex/0981",
            cache_mode=CacheMode.BYPASS,
            config=CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                simulate_user=True,
                magic=True,
                extraction_strategy=JsonXPathExtractionStrategy(schema, verbose=True),
            ),
        )

        data = json.loads(
            result.extracted_content if result.extracted_content is not None else "{}"
        )
        print(json.dumps(data, indent=2) if data else "No data found.")


if __name__ == "__main__":
    asyncio.run(main())
