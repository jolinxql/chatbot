"""
@time       : 2021/8/19 12:36 上午
@author     : JolinXia
@description:
    
"""
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()