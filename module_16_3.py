from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
# Создал новое приложение FastAPI
app = FastAPI()
# Создал словарь users = {'1': 'Имя: Example, возраст: 18'}
users = {"1": "Имя: Example, возраст: 18"}
# get запрос по маршруту '/users', который возвращает словарь users
@app.get("/users")
async def get_all_messages() -> dict:
    return users
# post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению
# ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered"
@app.post("/user/{user_name}/{age}")
async def create_message(user_name: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя",
                        example="Andrei")],age: Annotated[int, Path(ge=1, le=100, description="Введите возраст",
                        example=55)]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    mess = f"Имя: {user_name}, возраст: {age}"
    users[current_index] = mess
    return f"Пользователь {current_index} зарегистрирован!"
# put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users
# под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
@app.put("/user/{user_id}/{user_name}/{age}")
async def update_message(user_id: Annotated[int, Path(ge=0)], user_name: str = Path(min_length=5, max_length=20,
                        description="Введите имя", example="Andrei"), age: int = Path(ge=1, le=100,
                        description="Введите возраст", example=55),) -> str:
    users[user_id] = f"Имя: {user_name}, возраст: {age}"
    return f"Информация о пользователе id# {user_id} обновлена!"
# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару
@app.delete("/user/{user_id}")
async def delete_user(user_id):
    if user_id in users:
        users.pop(user_id)
        return f"Пользователь с id# {user_id} удален."
    raise HTTPException(status_code=404, detail="Пользователь не найден.")
