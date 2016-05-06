from tethys_sdk.base import TethysAppBase, url_map_maker


class MyFirstApp(TethysAppBase):
    """
    Tethys app class for my first app.
    """

    name = 'My First App'
    index = 'my_first_app:home'
    icon = 'my_first_app/images/byu.png'
    package = 'my_first_app'
    root_url = 'my-first-app'
    color = '#990000'
    description = 'This is a demo app.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='my-first-app',
                           controller='my_first_app.controllers.home'),
                    UrlMap(name='info',
                           url='info',
                           controller='my_first_app.controllers.info'),
                    UrlMap(name='map',
                           url='map',
                           controller='my_first_app.controllers.map'),

        )

        return url_maps