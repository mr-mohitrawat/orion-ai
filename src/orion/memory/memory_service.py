from psycopg_pool import ConnectionPool

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

pool = ConnectionPool(DATABASE_URL)

class MemoryService:

    def save(self, user_id: str, key: str, value: str):

        with pool.connection() as conn:
            with conn.cursor() as cur:

                cur.execute(
                    """
                    INSERT INTO user_memory
                    (user_id, memory_key, memory_value)

                    VALUES (%s,%s,%s)

                    ON CONFLICT(user_id, memory_key)

                    DO UPDATE
                    SET memory_value = EXCLUDED.memory_value
                    """,
                    (user_id, key, value),
                )

            conn.commit()

    def get(self, user_id: str, key: str):

        with pool.connection() as conn:
            with conn.cursor() as cur:

                cur.execute(
                    """
                    SELECT memory_value
                    FROM user_memory

                    WHERE user_id=%s
                    AND memory_key=%s
                    """,
                    (user_id, key),
                )

                row = cur.fetchone()

                return row[0] if row else None


memory_service = MemoryService()