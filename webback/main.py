"""
@time       : 2021/8/19 12:36 上午
@author     : JolinXia
@description:
    
"""
import web

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    from webback.handle import Handle
    app = web.application(urls, globals())
    app.run()