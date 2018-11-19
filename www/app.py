#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Welcome To My Blog</h1>', content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app)
