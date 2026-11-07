import requests

def task1():
    """Задание 1: Получение данных из публичного API (JSONPlaceholder)"""
    print("--- Задание 1: Первые 5 постов ---")
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Отправляем GET-запрос
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        # Извлекаем и выводим первые 5 постов
        for i in range(5):
            post = posts[i]
            print(f"\nПост #{post['id']}")
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}")
            print("-" * 40)
    else:
        print(f"Ошибка выполнения запроса. Статус код: {response.status_code}")

if __name__ == "__main__":
    task1()
