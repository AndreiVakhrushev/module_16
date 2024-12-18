from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
# Создал новое приложение FastAPI
app = FastAPI()
# Создал пустой список
users = []
# Создал класс(модель) User, наследованный от BaseModel
class User(BaseModel):
    id: int = None
    username: str
    age: int
# get запрос по маршруту '/users' теперь возвращает список users
@app.get("/users")
def get_users() -> List[User]:
    return users
# post запрос по маршруту '/user/{username}/{age}', теперь:
# 1. Добавляет в список users объект User.
# 2. id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# 3. Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# 4. В конце возвращает созданного пользователя.
@app.post('/user/{username}/{age}')
def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Введите имя', example="Andrei")],
                age: Annotated[int, Path(ge=1, le=100, description='Введите возраст', example=55)]) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user
# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# 1. Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# 2. В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: Annotated[int, Path(ge=1, le=1000, description='Введите ID пользователя', example="1")],
                username: Annotated[str, Path(min_length=5, max_length=20, description='Введите имя', example="Andrei")],
                age: Annotated[int, Path(ge=1, le=100, description='Введите возраст', example=55)]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        raise HTTPException(status_code=404, detail='Пользователь не найден')
# delete запрос по маршруту '/user/{user_id}', теперь:
# 1. Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# 2. В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.delete("/user/{user_id}", response_model=str)
async def delete_user(user_id: int = Path(ge=0)) -> str:
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users.pop(index)
            return f"Пользователь с ID {user_id} удален."
    raise HTTPException(status_code=404, detail="Пользователь не найден.")
