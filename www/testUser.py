# -*- coding: utf-8 -*-

'''
测试模块User
'''

__author__ = 'Jerry Tu'

import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', database='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()