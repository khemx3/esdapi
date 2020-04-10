from app.api.models import BookSchema
from app.db import books, database


async def post(payload: BookSchema):
    query = books.insert().values(title=payload.title, description=payload.description, price=payload.price)
    return await database.execute(query=query)


async def get(id: int):
    query = books.select().where(id == books.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = books.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: BookSchema):
    query = (
        books
        .update()
        .where(id == books.c.id)
        .values(title=payload.title, description=payload.description, price=payload.price)
        .returning(books.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = books.delete().where(id == books.c.id)
    return await database.execute(query=query)
