### python操作redis时 都是网络IO，所以利用IO等待时提高效率。
### pip install aioredis,支持异步的redis
import asyncio
import aioredis


async def execute():
    redis = await aioredis.from_url("redis://localhost", decode_responses=True)

    await redis.hset("hash", mapping={"key1": "value1", "key2": "value2", "key3": 123})

    result = await redis.hgetall("hash")
    assert result == {
        "key1": "value1",
        "key2": "value2",
        "key3": "123",  # note that Redis returns int as string
    }
    # await redis.set('key', 'value')
    # value = await redis.get('key')
    # print(value)

    await redis.close()


if __name__ == '__main__':
    asyncio.run(execute())
