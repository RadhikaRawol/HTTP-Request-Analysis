import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# GET - Retrieve all posts

response = requests.get(BASE_URL)

print("Request Method:", response.request.method)
print("Request URL:", response.request.url)
print("Status Code:", response.status_code)

print("\nResponse Headers:")
print("Content-Type:", response.headers.get("Content-Type"))

print("\nResponse JSON:")

posts = response.json()

# Display first 2 posts only

print(posts[:2])

# GET - Retrieve one post

url = BASE_URL + "/1"

response = requests.get(url)

print("Request Method:", response.request.method)
print("Request URL:", response.request.url)
print("Status Code:", response.status_code)

print("\nResponse JSON:")

post = response.json()

print(post)

# POST - Create a new post

new_post = {
"title": "Radhika New Post",
"body": "I am learning HTTP and REST API",
"userId": 10
}

response = requests.post(BASE_URL, json=new_post)

print("Request Method:", response.request.method)
print("Request URL:", response.request.url)
print("Status Code:", response.status_code)

print("\nResponse JSON:")

created_post = response.json()

print(created_post)

# PUT - Update an existing post

updated_post = {
"id": 1,
"title": "Updated Radhika Post",
"body": "I updated this post using Python PUT request",
"userId": 10
}

url = BASE_URL + "/1"

response = requests.put(url, json=updated_post)

print("Request Method:", response.request.method)
print("Request URL:", response.request.url)
print("Status Code:", response.status_code)

print("\nResponse JSON:")

updated_data = response.json()

print(updated_data)

# DELETE - Delete a post

url = BASE_URL + "/1"

response = requests.delete(url)

print("Request Method:", response.request.method)
print("Request URL:", response.request.url)
print("Status Code:", response.status_code)

print("\nResponse JSON:")

try:
    deleted_data = response.json()
    print(deleted_data)

except ValueError:
    print("No JSON response body")

