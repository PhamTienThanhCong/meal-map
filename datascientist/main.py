import requests
import json

def get_list_res_ids_search_global(city_id=273, token="", foody_services=[5], keyword=""):
    url = "https://gappapi.deliverynow.vn/api/delivery/search_global"
    payload = json.dumps({
        "category_group": 1,
        "city_id": city_id,
        "delivery_only": True,
        "keyword": keyword,
        "foody_services": foody_services,
        "full_restaurant_ids": True
    })
    
    # Updated headers based on working analysis
    headers = {
        'X-Foody-Access-Token': token,
        'X-Foody-Api-Version': '1',
        'X-Foody-App-Type': '1004',
        'X-Foody-Client-Id': '',
        'X-Foody-Client-Language': 'vi',
        'X-Foody-Client-Version': '3.0.0',
        'X-Foody-Client-Type': '1',
        'Content-Type': 'application/json',
        # Additional headers that may be required
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://deliverynow.vn',
        'Referer': 'https://deliverynow.vn/',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Debug information
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    
    if response.status_code == 200:
        json_object = json.loads(response.text)
        print(f"Success! Found {len(json_object.get('reply', {}).get('search_result', []))} service types")
        return json_object
    else:
        print(f"Error: {response.text}")
        return {"error": response.text}

if __name__ == "__main__":
    print("Testing API with Hanoi and keyword 'bami sot':")
    print("="*60)
    
    # Test Hanoi (city_id=218) with keyword "bami sot"
    result = get_list_res_ids_search_global(
        city_id=218,  # Hanoi
        token="",
        foody_services=[1],  # All available services
        keyword="bami sot"
    )
    
    if 'reply' in result:
        search_results = result['reply'].get('search_result', [])
        print(f"Found {len(search_results)} service types with keyword 'bami sot' in Hanoi")
        
        total_restaurants = 0
        for service in search_results:
            service_id = service['foody_service']
            restaurant_count = service['total_items']
            total_restaurants += restaurant_count
            print(f"  Service {service_id}: {restaurant_count} restaurants")
            
            # Show first few restaurant details
            if service.get('restaurants'):
                print(f"    First few restaurants:")
                for i, restaurant in enumerate(service['restaurants'][:3]):
                    restaurant_id = restaurant['restaurant_id']
                    dish_count = len(restaurant.get('dish_ids', []))
                    print(f"      Restaurant {restaurant_id}: {dish_count} dishes")
        
        print(f"\nTotal: {total_restaurants} restaurants found")
        
        # Save result to file
        with open("./shoppe_data/hanoi_bami_sot_result.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        # Print full response for detailed analysis
        print(f"\nFull response saved to './shoppe_data/hanoi_bami_sot_result.json'")
        print(f"First part of response:")
        print(json.dumps(result, indent=2, ensure_ascii=False)[:1000] + "...")
    else:
        print("Error or no data")
        print(result)