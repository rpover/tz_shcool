from src.server.database import models as database_models
from src.server.database.pydantic_models import *
from src.server.service import *

routers = (
    RouterManager(
        database_model=database_models.Student,
        pydantic_model=Student,
        prefix='/student',
        tags=['Student']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Staff,
        pydantic_model=Staff,
        prefix='/staff',
        tags=['Staff']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Lesson,
        pydantic_model=Lesson,
        prefix='/lesson',
        tags=['Lesson']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Class,
        pydantic_model=Class,
        prefix='/class',
        tags=['Class']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.LessonTime,
        pydantic_model=LessonTime,
        prefix='/lesson_time',
        tags=['LessonTime']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.LessonTable,
        pydantic_model=LessonTable,
        prefix='/lesson_table',
        tags=['LessonTable']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Mark,
        pydantic_model=Mark,
        prefix='/mark',
        tags=['Mark']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Visit,
        pydantic_model=Visit,
        prefix='/visit',
        tags=['Visit']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Truancy,
        pydantic_model=Truancy,
        prefix='/truancy',
        tags=['Truancy']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Event,
        pydantic_model=Event,
        prefix='/event',
        tags=['Event']
    ).fastapi_router,
)
