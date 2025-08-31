import requests


def pre_process_url(
    url: str,
    base_url: str = "https://www.shoppersstop.com/_next/data/cOvKwJilpXWjxUCkIBzz3/"
) -> str:
    """
    Clean URL and construct JSON endpoint URL.
    """
    no_param_url = url.split("?")[0]
    no_fragment_url = no_param_url.split("#")[0]
    stripped_url = no_fragment_url.rstrip("/")

    after_com = stripped_url.split(".com/")[1]
    parts = after_com.split("/")

    product_identifier = ""
    for i, part in enumerate(parts):
        if part.startswith("p-"):
            product_identifier = "/".join(parts[:i+1])
            break

    return f"{base_url}{product_identifier}.json"


def fetch_data(url: str) -> dict:
    """
    Fetch JSON from given URL with headers.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


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
