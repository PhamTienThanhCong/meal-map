import requests
import json

def get_list_res_ids_search_global(city_id=273, token="xxx", foody_services=[5]):
    url = "https://gappapi.deliverynow.vn/api/delivery/search_global"
    payload = json.dumps({
    "category_group": 1,
    "city_id": city_id,
    "delivery_only": True,
    "keyword": "",
    "foody_services": foody_services,
    "full_restaurant_ids": True
    })
    headers = {
    'X-Foody-Access-Token': token,
    'X-Foody-Api-Version': '1',
    'X-Foody-App-Type': '1004',
    'X-Foody-Client-Id': '',
    'X-Foody-Client-Language': 'vi',
    'X-Foody-Client-Version': '3.0.0',
    'X-Foody-Client-Type': '1',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_object = json.loads(response.text)
    data_restaurant_ids = []
    return json_object

if __name__ == "__main__":
    token=""
    print(get_list_res_ids_search_global(token=token))