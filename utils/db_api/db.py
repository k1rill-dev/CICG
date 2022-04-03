from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
        database="postgres",
        user="postgres",
        password="KOKI___KLAVY123",
        host="localhost",
        port="5432"
    )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS PLAYERS
     (ID SERIAL PRIMARY KEY,
     TG_ID BIGINT NOT NULL UNIQUE,
     NAME VARCHAR (100) NULL,
     PROG_COUNT BIGINT,
     TESTER_COUNT BIGINT,
     ANALYSE_COUNT BIGINT,
     ADMIN_COUNT BIGINT,
     PROFESSION VARCHAR (100),
     FINISH VARCHAR (100));'''
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, username, telegram_id):
        sql = "INSERT INTO PLAYERS (NAME, TG_ID) VALUES($1, $2) returning *"
        return await self.execute(sql, username, telegram_id, fetchrow=True)

    # async def autoriz_data(self, full_name, username, telegram_id):
    #     sql = "UPDATE Users SET full_name=$1, username=$2 WHERE telegram_id=$3"
    #     return await self.execute(sql, full_name, username, telegram_id,  fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM PLAYERS"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM PLAYERS WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM PLAYERS"
        return await self.execute(sql, fetchval=True)

    async def delete_users(self):
        await self.execute("DELETE FROM PLAYERS WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE PLAYERS", execute=True)