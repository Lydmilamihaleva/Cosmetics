from pyramid.config import Configurator
from pyramid.security import Everyone, Allow
from pyramid_sacrud import PYRAMID_SACRUD_HOME, PYRAMID_SACRUD_VIEW


class BearFactory(object):

    def __init__(self, request):
        self.__acl__ = [
            (Allow, Everyone, PYRAMID_SACRUD_HOME),
            (Allow, Everyone, PYRAMID_SACRUD_VIEW),
            (Allow, Everyone, 'test'),
        ]

def test_factory(request):
    pagename = request.matchdict['pagename']
    if request.dbsession.query(Page).filter_by(name=pagename).count() > 0:
        next_url = request.route_url('edit_page', pagename=pagename)
        raise HTTPFound(location=next_url)
    return BearFactory(pagename)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=BearFactory)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.scan()
    return config.make_wsgi_app()
