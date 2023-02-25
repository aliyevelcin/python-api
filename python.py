import requests




# film = input()
# pre_result = requests.get(f'https://imdb-api.com/API/Search/k_iek5x25t/{film}')
# result = pre_result.json()
# films = result["results"]
# print(films)
# for film in films:
#     print(f'Adi: {film["title"]}')
#     print(f'Kino haqqinda: {film["description"]}')
#     print(f'Shekili: {film["image"]}')
#     print("\n")



# states = input()
# pre_result = requests.get(f'http://universities.hipolabs.com/search?country={states}')

# salam =  pre_result.json()
# for uni in salam:
#     print(f'name: {uni["name"]}')
#     print(f'Domains: {uni["domains"]}')
#     print(f'web_pages: {uni["web_pages"]}')
#     print(f'Country: {uni["country"]}')
#     print(f'Kodlar: {uni["alpha_two_code"]}')
#     print("\n")

    


pre_result = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

result = pre_result.json()
print(f'{result["chartName"]}')

print(f"USD: {result['bpi']['USD']['rate']} Dollar,   Updated: {result['time']['updateduk']}")
print(f"GBP: {result['bpi']['GBP']['rate']} Pound, Updated: {result['time']['updatedISO']}")
print(f"EUR: {result['bpi']['EUR']['rate']} Euro, Updated: {result['time']['updated']}")

 