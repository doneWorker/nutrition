def get_max_image_size(sizes: dict):
    if sizes["full"]:
        return "full"

    max_size = 0

    for size in sizes:
        if int(size) > max_size:
            max_size = size

    return str(max_size)


def get_product_id(product: dict):
    if "id" not in product:
        return None
    
    product_id = product['id']
    if len(product_id.lstrip("0")) <= 8:
        return product_id
    else:
        if len(product_id) < 13:
            product_id = "0" + product_id

        groups = [product_id[i:i + 3] for i in range(0, len(product_id) - 4, 3)]
        groups.append(product_id[-4:])
        output_str = "/".join(groups)
        return output_str


def get_product_image(product: dict):
    image_type = "front" or "front_en" or "front_fr"

    if "images" not in product or image_type not in product["images"]:
        return None

    image_id = get_product_id(product)
    rev = product["images"][image_type]["rev"]
    size = get_max_image_size(product["images"][image_type]["sizes"])
    base = "https://images.openfoodfacts.org/images/products/{}/{}.{}.{}.jpg"

    return base.format(image_id, image_type, rev, size)
