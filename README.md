# more.signals

`more.signals` is an extension for [Morepath](http://morepath.readthedocs.io) that adds [Blinker](https://github.com/jek/blinker) signals support.

### Quickstart

The integration adds two directives to a Morepath App for connecting and disconnecting signals. Once connected you can emit to signal using `request.app.signal('signal.name')` to specify a named signal and then use the `send()` method, or you can combine both using `request.app.signal('signal.name').send(self, **data)`. Please read [Blinker's documentation](https://pythonhosted.org/blinker/) for all the details.

```python
from more.signals import SignalApp

class App(SignalApp):
    pass


@App.connect('hello')
def say_hello(sender, **data):
    print('HELLO {}!'.format(data.get('name')))


@App.path(path='')
class Root(object):
    pass


@App.json(model=Root)
def root_view(self, request):
    name = 'Foo Bar'
    request.app.signal('hello').send(self, name=name)
    return {'name': name}


if __name__ == '__main__':
    morepath.run(App())

```
