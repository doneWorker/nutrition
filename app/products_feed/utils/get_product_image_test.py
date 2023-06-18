import json

from .get_product_image import get_product_image

product_json_string = """{
  "id": "011110001986",
  "images": {
    "front": {
      "rev": "5",
      "white_magic": null,
      "sizes": {
        "200": {
          "h": 200,
          "w": 135
        },
        "100": {
          "h": 100,
          "w": 68
        },
        "400": {
          "w": 271,
          "h": 400
        },
        "full": {
          "w": 980,
          "h": 1448
        }
      },
      "imgid": "1",
      "normalize": null,
      "geometry": "980x1448-80-76"
    },
    "1": {
      "uploader": "kp757",
      "uploaded_t": 1425364355,
      "sizes": {
        "100": {
          "w": 100,
          "h": 75
        },
        "full": {
          "h": 1200,
          "w": 1600
        },
        "400": {
          "h": 300,
          "w": 400
        }
      }
    },
    "front_en": {
      "rev": "5",
      "white_magic": null,
      "sizes": {
        "200": {
          "h": 200,
          "w": 135
        },
        "100": {
          "h": 100,
          "w": 68
        },
        "400": {
          "w": 271,
          "h": 400
        },
        "full": {
          "w": 980,
          "h": 1448
        }
      },
      "imgid": "1",
      "normalize": null,
      "geometry": "980x1448-80-76"
    }
  }
}"""


def test_get_product_image():
    input_product = json.loads(product_json_string)
    output_image = "https://images.openfoodfacts.org/images/products/001/111/000/1986/front.5.full.jpg"
    assert get_product_image(input_product) == output_image
