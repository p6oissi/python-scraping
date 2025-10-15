import requests

def scarpe_yaga(keyword, limit=20):
    """
    Search products on 'https://www.yaga.ee' using their public API.
    Returns a list of dictionaries: {'name', 'price', 'url', 'site'}
    """
    # Initialise parameters
    base_url = "https://www.yaga.ee/api/product/search/"
    params = {
        "query": keyword,
        "offset": 0,
        "limit": limit,
        "mode": "multi"
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Request failed with status code", response.status_code)
        return []

    data = response.json()
    products = data.get("data", {}).get("list", [])
    results = []

    for product in products:
        name = product.get("description") or "Unknown"
        price = product.get("price", 0)
        currency = product.get("currency", "€")
        slug = product.get("slug")
        shop = product.get("shop", {})

        shop_slug = (
                shop.get("active_slug")
                or shop.get("activeSlug")
                or "unknown-shop"
        )

        link = f"https://www.yaga.ee/{shop_slug}/toode/{slug}" if slug else "?"

        results.append({
            "name": name,
            "price": f"{price} {currency}",
            "link": link,
            "site": "yaga.ee"
        })

    return results