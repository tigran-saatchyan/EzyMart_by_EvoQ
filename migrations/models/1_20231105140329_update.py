from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "is_superuser" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "user" ADD "is_verified" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "user" ALTER COLUMN "is_active" SET DEFAULT False;
        ALTER TABLE "user" ALTER COLUMN "telephone" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "is_superuser";
        ALTER TABLE "user" DROP COLUMN "is_verified";
        ALTER TABLE "user" ALTER COLUMN "is_active" SET DEFAULT True;
        ALTER TABLE "user" ALTER COLUMN "telephone" SET NOT NULL;"""
