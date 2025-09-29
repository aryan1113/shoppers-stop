from utils.utils import extract_size_map, fetch_data, pre_process_url


def main():
    supplied_by_user = """
    https://www.shoppersstop.com/adidas-duramo-sl-m-wide-mesh-low-tops-lace-up-men-s-sports-shoes/p-FMADIG0309/colorChange/FMADIG0309_BLACK
    """

    processed_url = pre_process_url(supplied_by_user)
    data = fetch_data(processed_url)
    size_map = extract_size_map(data)

    for size, info in size_map.items():
        print(f"Size: {size}, SKU: {info['sku']}, Stock: {info['stock']}")


if __name__ == "__main__":
    main()
