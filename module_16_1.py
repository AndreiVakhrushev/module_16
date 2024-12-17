from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Создаем маршрут к главной странице - "/".
# По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def welcome() -> dict:
    return{"message": "Главная страница"}
# Создаем маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def admin() -> dict:
    return{"message": "Вы вошли как администратор"}
# Создаем маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get("/user/{user_id}")
async def user_id(user_id:str) -> dict:
    return{"message": f"Вы вошли как пользователь № {user_id}"}
# Создаем маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
@app.get("/user/{user_name}/{age}")
async def user_info(user_name:str, age: str) -> dict:
    return{"message": f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"}
