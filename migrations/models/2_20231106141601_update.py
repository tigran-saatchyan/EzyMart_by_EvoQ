from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "telegram_user_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "telegram_user_id" SET NOT NULL;"""
