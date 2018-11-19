#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>Welcome To My Blog</h1>', content_type='text/html')


async def main(loop):
    server = web.Server(index)
    await loop.create_server(server, "127.0.0.1", 8080)
    print('server is started at http://127.0.0.1:8080')


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.run_forever()
