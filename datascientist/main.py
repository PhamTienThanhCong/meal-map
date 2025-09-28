import requests
import json

def search_restaurants(city_id=217, keyword="", sort_type=8, delivery_only=False):
    """
    Search for restaurants using Shopee Food API with proper authentication headers
    
    Parameters:
    - city_id: ID of the city to search in (default: 217)
    - keyword: Search keyword (default: empty string)
    - sort_type: Sort type for results (default: 8)
    - delivery_only: Only delivery restaurants (default: False)
    
    Returns:
    - JSON response data or None if failed
    """
    url = "https://gappapi.deliverynow.vn/api/delivery/search_global"
    
    payload = {
        "category_group": 1,
        "city_id": city_id,
        "delivery_only": delivery_only,
        "keyword": keyword,
        "sort_type": sort_type,
        "foody_services": [1],
        "full_restaurant_ids": True
    }
    
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://shopeefood.vn',
        'Referer': 'https://shopeefood.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15',
        'x-foody-api-version': '1',
        'x-foody-app-type': '1004',
        'x-foody-client-language': 'vi',
        'x-foody-client-type': '1',
        'x-foody-client-version': '3.0.0',
        # Authentication headers - these might need to be updated regularly
        '1c383d76': 'd=3Q<b-qAh`VmU\\b/Jnb[r,^b',
        '1e8c72b7': '\\Z2j>^:.O?Qj3LO_$L1>jPgd0',
        '6de9ea37': '&q[.MSmiS;^EBkg2"CecrbgYO',
        '3753ed4e': 'Qhg#B=k[a%a4bD>iksH0+r=-BTO^*J4EQNAa@@7R6uQm;=(m_":pfi3l%S\\!29%7qad@tqoo,1G4@D%an^6dML)Ch3IEdk#MEgsK+$U+2o^WER7]eqn^D.)!#0;FY=3H*I4n+L?*nk_4rMI?;\'D0herl<K\'RnpR=0>X<lJ;<N!j^hs_V#.jP^9AYVm;Er0W0i[%V#.jP^9AYVm;Er0W0i[%',
        'x-sap-ri': '0f5ad9688f2da52716aa8e3e81ccbc11f49f9dde90b15004'
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                delivery_infos = data.get('reply', {}).get('delivery_infos', [])
                print(f"Found {len(delivery_infos)} restaurants")
                return data
            except json.JSONDecodeError:
                print("Response is not valid JSON")
                print(f"Response: {response.text}")
                return response.text
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Test the function with exact payload from working request
search_data = search_restaurants(city_id=218, keyword="bami sot", sort_type=8, delivery_only=True)

if search_data and isinstance(search_data, dict):
    # Save the data if it's valid JSON
    with open('./shoppe_data/search_results.json', 'w', encoding='utf-8') as f:
        json.dump(search_data, f, indent=4, ensure_ascii=False)
    
    print("Search data saved to search_results.json")
    if 'reply' in search_data:  
        print(f"Top-level reply keys: {list(search_data['reply'].keys())}")