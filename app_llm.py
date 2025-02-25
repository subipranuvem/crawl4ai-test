import asyncio
import json

from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig, LLMExtractionStrategy
from pydantic import BaseModel


class Pokemon(BaseModel):
    id: str
    name: str
    height: str
    weight: str
    category: str
    abillities: list[str]
    types: list[str]
    weakness: list[str]
    image_src: str


async def main():
    llm_strategy = LLMExtractionStrategy(
        provider="gemini/gemini-2.0-flash",
        api_token="<your_token>",
        schema=Pokemon.model_json_schema(),
        extraction_type="schema",
        instruction="Extract the informations about the pokémon",
        chunk_token_threshold=1400,
        overlap_rate=0.1,
        apply_chunking=True,
        input_format="html",
        extra_args={"temperature": 0.1, "max_tokens": 1000},
        verbose=True,
    )

    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.DISABLED,
        extraction_strategy=llm_strategy,
        simulate_user=True,
        magic=True,
    )

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://sg.portal-pokemon.com/play/pokedex/0981",
            cache_mode=CacheMode.DISABLED,
            config=crawl_config,
        )
        llm_strategy.show_usage()
        data = json.loads(
            result.extracted_content if result.extracted_content is not None else "{}"
        )
        print(json.dumps(data, indent=2) if data else "No data found.")


if __name__ == "__main__":
    asyncio.run(main())
