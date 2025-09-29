import requests
import re
import json
from urllib.parse import urlparse, quote

def extract_build_id(product_url: str) -> str:
    """
    Extract the dynamic Next.js build ID from the product page HTML.
    """
    parsed = urlparse(product_url)
    safe_path = quote(parsed.path)
    safe_url = f"{parsed.scheme}://{parsed.netloc}{safe_path}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(safe_url, headers=headers, timeout=10)
    response.raise_for_status()

    match = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        response.text,
        re.DOTALL
    )
    if not match:
        raise ValueError("Could not find __NEXT_DATA__ script in page HTML")

    data = json.loads(match.group(1))
    return data.get("buildId")


def build_product_json_url(product_url: str) -> tuple:
    """
    Build the product JSON URL dynamically using the extracted build ID.
    Returns (product_id, json_url)
    """
    build_id = extract_build_id(product_url)
    parsed = urlparse(product_url)
    parts = parsed.path.strip("/").split("/")
    slug, product_id = parts[0], parts[-1]
    json_url = f"https://www.shoppersstop.com/_next/data/{build_id}/{slug}/{product_id}.json"
    return product_id, json_url


def fetch_product_json(product_url: str) -> dict:
    """
    Fetch the product JSON dynamically using build ID.
    """
    product_id, json_url = build_product_json_url(product_url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/140.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }
    response = requests.get(json_url, headers=headers)
    response.raise_for_status()
    return response.json()


def extract_size_map(data: dict) -> dict:
    """
    Extract size -> {sku, stock} mapping from JSON response.
    """
    queries = data["pageProps"]["dehydratedState"]["queries"]
    product = queries[1]["state"]["data"]["data"]["products"]["items"][0]
    variant_status = {v["sku"]: v["status"] for v in product["variants_status"]}

    item_on_page = data["pageProps"]["pdpData"]["data"]["products"]["items"][0]
    options = item_on_page["configurable_options"][0]["values"]

    size_map = {}
    for opt in options:
        sku = opt["value_index"]
        size_label = opt["label"]
        stock = variant_status.get(sku, "UNKNOWN")
        size_map[size_label] = {"sku": sku, "stock": stock}

    return size_map

""" 
sample usage python src/utils/utils.py
"""
if __name__ == "__main__":
    product_url = "https://www.shoppersstop.com/adidas-upvibe-synthetic-lace-up-men's-sports-shoes/p-FMADIU5066"
    data = fetch_product_json(product_url)
    sizes = extract_size_map(data)

    for size, info in sizes.items():
        print(f"Size: {size}, SKU: {info['sku']}, Stock: {info['stock']}")
