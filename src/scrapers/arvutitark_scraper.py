import requests

def scrape_arvutitark(query, per_page=20, page=1):
    """
    Search products on 'https://www.arvutitark.ee' using their public API.
    Returns a list of dictionaries: {'name', 'price', 'url', 'site'}
    """
    # Initialise parameters
    base_url = "https://cms.arvutitark.ee/api/search"
    params = {
        "prices": "",
        "categories": "",
        "brands": "",
        "sort": "top",
        "shops": "",
        "perPage": per_page,
        "page": page,
        "query": query,
        "full": "true"
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Request failed with status code: ", response.status_code)
        return []

    data = response.json()
    products = data.get("products", {}).get("data", [])
    results = []

    for product in products:
        name = product.get("name", {}).get("et") or product.get("name", {}).get("en") or "Unknown"
        price = product.get("price") or 0
        slug = product.get("slug") or ""
        link = f"https://arvutitark.ee/est/tooted/{slug}" if slug else "?"

        results.append({
            "name": name,
            "price": f"{price} €",
            "link": link,
            "site": "arvutitark.ee"
        })

    return results