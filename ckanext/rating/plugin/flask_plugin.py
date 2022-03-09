import ckan.plugins as p

from ckanext.rating.blueprint import rating as rating_blueprint

class MixinPlugin(p.SingletonPlugin):

    p.implements(p.IBlueprint)
    p.implements(p.IClick)

    def get_blueprint(self):
        return [rating_blueprint]