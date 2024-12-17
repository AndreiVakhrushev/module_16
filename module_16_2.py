from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return(f"Главная страница")

@app.get("/user/admin")
async def admin() -> str:
    return(f"Вы вошли как администратор")
# '/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id,
# для которого необходимо написать следующую валидацию:
# 1. Должно быть целым числом
# 2. Ограничено по значению: больше или равно 1 и меньше либо равно 100.
# 3. Описание - 'Enter User ID'
@app.get("/user/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> str:
    return(f"Вы вошли как пользователь № {user_id}")
# '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту,
# принимает аргументы username и age, для которых необходимо написать следующую валидацию:
# 1. username - строка, age - целое число.
# 2. username ограничение по длине: больше или равно 5 и меньше либо равно 20.
# 3. age ограничение по значению: больше или равно 18 и меньше либо равно 120.
# 4. Описания для username и age - 'Enter username' и 'Enter age' соответственно.
@app.get("/user/{user_name}/{age}")
async def user_info(user_name: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    return(f"Информация о пользователе. Имя: {user_name}, Возраст: {age}")