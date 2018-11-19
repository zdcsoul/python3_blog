#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aiohttp import web


async def index(request):
    return web.Response(body=b'<h1>Welcome To My Blog</h1>', content_type='text/html')


async def test(request):
    return web.Response(body=b'<h1>test</h1>', content_type='text/html')

app = web.Application()
app.router.add_get('/', index)
web.run_app(app, host='127.0.0.1', port=8080)
