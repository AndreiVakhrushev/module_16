from fastapi import FastAPI, Path, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
tmpl = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None

@app.get('/')
async def get_main_page(request: Request):
    return tmpl.TemplateResponse("users.html", {'request': request, 'users': users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int):
    try:
        user = next(user for user in users if user.id == user_id)
        return tmpl.TemplateResponse("users.html", {'request': request, 'user': user})
    except Exception:
        raise HTTPException(status_code=404, detail='Пользователь не найден')


@app.post('/user/{username}/{age}')
async def add_user(user: User,
                   username: str = Path(min_length=5, max_length=20, description='Введите имя', example='Andrei'),
                   age: int = Path(ge=1, le=100, description='Введите возраст', example='55')) -> str:
    user.id = 1 if len(users) == 0 else len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return f'Пользователь {user.id} зарегистрирован!'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: str = Path(min_length=5, max_length=20, description='Введите имя', example='Andrei'),
                      age: int = Path(ge=1, le=100, description='Введите возраст', example='55')) -> str:
    try:
        edit_user = next(user for user in users if user.id == user_id)
        edit_user.username = username
        edit_user.age = age
        return f'Информация о пользователе id# {user_id} обновлена!'
    except Exception:
        raise HTTPException(status_code=404, detail='Пользователь не найден')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        del_user = next(user for user in users if user.id == user_id)
        users.remove(del_user)
        return f'Пользователь с ID {user_id} удален.'
    except Exception:
        raise HTTPException(status_code=404, detail='Пользователь не найден')