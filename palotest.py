import asyncio

from scrapli import AsyncScrapli
from scrapli.logging import enable_basic_logging

enable_basic_logging(file=True, level="debug")
device = {
    "host": "172.28.6.6",
    "auth_strict_key": False,
    "ssh_config_file": True,
    "platform": "paloalto_panos",
    "transport": "asyncssh",
    "auth_username": "admin",
    "auth_password": "G0lfc0urs3",
}
conn = AsyncScrapli(**device)


async def main():
    await conn.open()
    p = await conn.get_prompt()
    print(p)
    await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
