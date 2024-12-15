from fastapi import FastAPI
from fastapi.responses import JSONResponse
# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Создаем маршрут к главной странице - "/".
# По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def welcome() -> JSONResponse:
    return JSONResponse(content={"message": "Главная страница"},
                        media_type="application/json; charset=utf-8")
# Создаем маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def admin() -> JSONResponse:
    return JSONResponse(content={"message": "Вы вошли как администратор"},
                        media_type="application/json; charset=utf-8")
# Создаем маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get("/user/{user_id}")
async def userid(user_id:str) -> JSONResponse:
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"},
                        media_type="application/json; charset=utf-8")
# Создаем маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
@app.get("/user/{user_name}/{age}")
async def user_info(user_name:str, age: str) -> JSONResponse:
    return JSONResponse(content={"message": f"Информация о пользователе. "
                                            f"Имя: {user_name}, Возраст: {age}"},
                        media_type="application/json; charset=utf-8")
