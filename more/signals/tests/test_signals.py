from webtest import TestApp as Client

from more.signals import SignalApp


def test_connect_signal_app():
    class App(SignalApp):
        pass

    @App.path(path='/hello')
    class Model(object):
        pass

    @App.connect('hello')
    def say_hello(sender, **data):
        print('HELLO {}!'.format(data.get('name')))

    @App.json(model=Model)
    def hello_view(self, request):
        request.app.signal('hello').send(
            self,
            name='Foo Bar'
        )
        return {}

    app = App()
    c = Client(app)
    c.get('/hello', status=200)


def test_disconnect_signal_app():
    class App(SignalApp):
        pass

    @App.path(path='/hello')
    class Model(object):
        pass

    @App.connect('hello')
    def say_hello(sender, **data):
        print('HELLO {}!'.format(data.get('name')))

    @App.json(model=Model)
    def hello_view(self, request):
        return {}

    App.disconnect('hello')(say_hello)

    app = App()
    c = Client(app)
    c.get('/hello', status=200)
