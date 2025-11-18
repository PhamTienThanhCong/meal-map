import requests
import json

def get_restaurant_infos(restaurant_ids, token=""):
    """Get detailed information about restaurants using get_infos API"""
    url = "https://gappapi.deliverynow.vn/api/delivery/get_infos"
    payload = json.dumps({
        "restaurant_ids": restaurant_ids
    })
    
    # Headers based on successful main.py configuration
    headers = {
        'X-Foody-Access-Token': token,
        'X-Foody-Api-Version': '1',
        'X-Foody-App-Type': '1004',
        'X-Foody-Client-Id': '',
        'X-Foody-Client-Language': 'vi',
        'X-Foody-Client-Version': '3.0.0',
        'X-Foody-Client-Type': '1',
        'Content-Type': 'application/json',
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
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    
    if response.status_code == 200:
        json_object = json.loads(response.text)
        result = json_object.get('result', '')
        if result == 'success':
            print(f"Success! Got restaurant info")
            return json_object
        else:
            print(f"API returned result: {result}")
            return json_object
    else:
        print(f"Error: {response.text}")
        return {"error": response.text}

def load_bami_sot_restaurants():
    """Load restaurant IDs from the search result"""
    try:
        with open("./shoppe_data/hanoi_bami_sot_result.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        restaurant_ids = []
        if 'reply' in data and 'search_result' in data['reply']:
            for service in data['reply']['search_result']:
                restaurant_ids.extend(service.get('restaurant_ids', []))
        
        return restaurant_ids
    except FileNotFoundError:
        print("File hanoi_bami_sot_result.json not found!")
        return []

def analyze_restaurant_details():
    """Analyze restaurant details from the get_infos API"""
    
    print("Loading restaurant IDs from search results...")
    restaurant_ids = load_bami_sot_restaurants()
    
    if not restaurant_ids:
        print("No restaurant IDs found!")
        return
    
    print(f"Found {len(restaurant_ids)} restaurants")
    print(f"Restaurant IDs: {restaurant_ids[:10]}..." if len(restaurant_ids) > 10 else f"Restaurant IDs: {restaurant_ids}")
    
    # Test with first 4 restaurants as in the example
    test_ids = restaurant_ids[:4]
    print(f"\nTesting with first 4 restaurants: {test_ids}")
    
    # Get restaurant info
    restaurant_info = get_restaurant_infos(test_ids)
    
    if 'reply' in restaurant_info:
        infos = restaurant_info['reply'].get('delivery_infos', [])
        print(f"\nGot info for {len(infos)} restaurants:")
        
        for info in infos:
            restaurant_id = info.get('restaurant_id', 'Unknown')
            # Try different possible fields for restaurant name
            restaurant_name = info.get('restaurant_name') or info.get('name') or 'Unknown'
            address = info.get('address', 'Unknown')
            rating = info.get('rating', {}).get('avg', 'No rating')
            delivery_fee = info.get('delivery', {}).get('fee_text', 'Unknown')
            
            print(f"\n🏪 Restaurant ID: {restaurant_id}")
            print(f"   Name: {restaurant_name}")
            print(f"   Address: {address}")
            print(f"   Rating: {rating}")
            print(f"   Delivery Fee: {delivery_fee}")
        
        # Save detailed results
        with open("./shoppe_data/restaurant_details.json", "w", encoding="utf-8") as f:
            json.dump(restaurant_info, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Full details saved to './shoppe_data/restaurant_details.json'")
        
        # Test with all restaurants if first batch works
        if restaurant_info.get('result') == 'success' and len(restaurant_ids) > 4:
            print(f"\n🔄 Getting info for all {len(restaurant_ids)} restaurants...")
            
            # Split into batches of 10 to avoid overwhelming the API
            batch_size = 10
            all_results = []
            
            for i in range(0, len(restaurant_ids), batch_size):
                batch = restaurant_ids[i:i+batch_size]
                print(f"Processing batch {i//batch_size + 1}: restaurants {i+1}-{min(i+batch_size, len(restaurant_ids))}")
                
                batch_info = get_restaurant_infos(batch)
                if 'reply' in batch_info:
                    all_results.extend(batch_info['reply'].get('delivery_infos', []))
            
            print(f"\n📊 SUMMARY - Found {len(all_results)} restaurants with 'bami sot' in Hanoi:")
            print("="*80)
            
            for info in all_results:
                # Try different possible fields for restaurant name
                restaurant_name = info.get('restaurant_name') or info.get('name') or f"Restaurant {info.get('restaurant_id', 'Unknown')}"
                rating = info.get('rating', {}).get('avg', 'No rating')
                print(f"• {restaurant_name} - Rating: {rating}")
            
            # Save complete results
            complete_data = {
                "keyword": "bami sot",
                "city": "Hanoi",
                "total_restaurants": len(all_results),
                "restaurants": all_results
            }
            
            with open("./shoppe_data/complete_bami_sot_restaurants.json", "w", encoding="utf-8") as f:
                json.dump(complete_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Complete results saved to './shoppe_data/complete_bami_sot_restaurants.json'")
    
    else:
        print("❌ Failed to get restaurant info")
        print(restaurant_info)

if __name__ == "__main__":
    analyze_restaurant_details()