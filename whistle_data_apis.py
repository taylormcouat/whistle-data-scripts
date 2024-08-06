import requests
import json
import csv

# Define API URLs
production_url = 'https://app.whistle.com'

# Replace these with your actual tokens
auth_token = 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMzM1MjAyLCJleHAiOjE3MTY0Njc4MTh9.lHvlhKb4j0UXaY27iphnKR_k-w_iwbaWbe6CNlzNFiA'
refresh_token = 'dd1ec00782cabf451d076680fecae0be'
serial_number = 'AM6-7117F3F'
NUM_DAYS = 20

# Authentication headers
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.whistle.com.v9+json',
    'Authorization': f'Bearer {auth_token}'
}

# Function to get a new bearer token using the refresh token
def refresh_bearer_token(refresh_token):
    url = f'{production_url}/api/login'
    data = {
        'refresh_token': refresh_token
    }
    response = requests.post(url, headers={
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.whistle.com.v9+json'
    }, json=data)
    if response.status_code in [200, 201]:
        return response.json().get('auth_token')
    else:
        print("Failed to refresh token. Response code:", response.status_code)
        print("Response content:", response.content.decode())
        raise Exception('Token refresh failed')

# Function to handle API requests with automatic token refresh
def api_request(url, headers, params=None):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 401:  # Token expired
        new_token = refresh_bearer_token(refresh_token)
        headers['Authorization'] = f'Bearer {new_token}'
        response = requests.get(url, headers=headers, params=params)
    return response

# Function to get pet ID by device serial number
def get_pet_id(auth_token, serial_number):
    url = f'{production_url}/api/devices/{serial_number}/pet'
    headers['Authorization'] = f'Bearer {auth_token}'
    response = api_request(url, headers)
    if response.status_code == 200:
        return response.json().get('pet').get('id')
    else:
        raise Exception('Failed to get pet ID')

# Function to get daily health trends
def get_health_trends(auth_token, pet_id):
    url = f'{production_url}/api/pets/{pet_id}/health/trends'
    headers['Authorization'] = f'Bearer {auth_token}'
    response = api_request(url, headers)
    return response.json() if response.status_code == 200 else None

# Function to get wellness index
def get_wellness_index(auth_token, pet_id, num_of_days=NUM_DAYS):
    url = f'{production_url}/api/pets/{pet_id}/health/graphs/wellness_index'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'num_of_days': num_of_days}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get sleeping data
def get_sleeping_data(auth_token, pet_id, num_of_days=NUM_DAYS):
    url = f'{production_url}/api/pets/{pet_id}/health/graphs/sleeping'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'num_of_days': num_of_days}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get scratching data
def get_scratching_data(auth_token, pet_id, num_of_days=NUM_DAYS):
    url = f'{production_url}/api/pets/{pet_id}/health/graphs/scratching'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'num_of_days': num_of_days}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get licking data
def get_licking_data(auth_token, pet_id, num_of_days=NUM_DAYS):
    url = f'{production_url}/api/pets/{pet_id}/health/graphs/licking'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'num_of_days': num_of_days}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get drinking data
def get_drinking_data(auth_token, pet_id, num_of_days=NUM_DAYS):
    url = f'{production_url}/api/pets/{pet_id}/health/graphs/drinking'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'num_of_days': num_of_days}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get eating daily trends
def get_eating_daily_trends(auth_token, pet_id, num_of_days=NUM_DAYS):
    url = f'{production_url}/api/pets/{pet_id}/health/graphs/eating_daily_trends'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'num_of_days': num_of_days}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get dailies
def get_dailies(auth_token, pet_id, start_date, end_date):
    url = f'{production_url}/api/pets/{pet_id}/dailies'
    headers['Authorization'] = f'Bearer {auth_token}'
    params = {'start_date': start_date, 'end_date': end_date}
    response = api_request(url, headers, params=params)
    return response.json() if response.status_code == 200 else None

# Function to get daily acitivty
def get_daily_activity(auth_token, pet_id, day_number):
    url = f'{production_url}/api/pets/{pet_id}/dailies/{day_number}'
    headers['Authorization'] = f'Bearer {auth_token}'
    response = api_request(url, headers)
    return response.json() if response.status_code == 200 else None


