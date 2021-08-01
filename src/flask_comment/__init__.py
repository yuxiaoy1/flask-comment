"""
    flask_comment
    ~~~~~~~~~~~~~~
    Create comment component in Flask/Jinja2 template.

    :author: Frank Yu <withyuxiaoy@gmail.com>
    :copyright: (c) 2021 by Frank Yu.
    :license: MIT, see LICENSE for more details.
"""
import sys
import typing as t

from flask import Blueprint
from flask import current_app
from flask import Flask
from flask import Markup
from flask import request

# sanity checking
try:
    assert sys.version_info >= (3, 6, 0)
except AssertionError:  # pragma: no cover
    raise RuntimeError('Flask-Comment required Python 3.6+!')

__version__ = '0.1.0'

DISQUS = 'disqus'
CUSDIS = 'cusdis'
VALINE = 'valine'
UTTERANCES = 'utterances'
GITALK = 'gitalk'


class Comment:
    def __init__(
        self,
        app: t.Optional[Flask] = None,
        platform: str = DISQUS,
    ) -> None:
        if app is not None:  # pragma: no cover
            self.init_app(app, platform=platform)

    def init_app(
        self,
        app: Flask,
        platform: str = DISQUS,
    ) -> None:
        if not hasattr(app, 'extensions'):  # pragma: no cover
            app.extensions = {}
        app.extensions['comment'] = self

        blueprint = Blueprint('comment', __name__)
        app.register_blueprint(blueprint)

        app.jinja_env.globals['comment'] = self

        app.config.setdefault('COMMENT_PLATFORM', platform)

    def load(
        self,
        page_url: t.Optional[str] = None,
        page_indentifier: t.Optional[str] = None,
    ) -> Markup:
        """
        Load comment component resources.

        Examples:
        
        ```py
        from flask import Flask
        from flask_comment import Comment
        
        app = Flask(__name__)
        comment = Comment(app)
        ```
        
        Arguments:
            page_url: The [page url](https://help.disqus.com/en/articles/1717084-javascript-configuration-variables) for Disqus, 
                default to [`flask.request.base_url`](https://flask.palletsprojects.com/en/latest/api/?highlight=base_url#flask.Request.base_url).
            
            page_indentifier: The [page indentifier](https://help.disqus.com/en/articles/1717084-javascript-configuration-variables) for Disqus, 
                default to [`flask.request.path`](https://flask.palletsprojects.com/en/latest/api/?highlight=request%20path#flask.Request.path).
        """
        if current_app.config['COMMENT_PLATFORM'] == DISQUS:
            return self._load_disqus(page_url, page_indentifier)
        if current_app.config['COMMENT_PLATFORM'] == CUSDIS:
            return self._load_cusdis()
        if current_app.config['COMMENT_PLATFORM'] == VALINE:
            return self._load_valine()
        if current_app.config['COMMENT_PLATFORM'] == UTTERANCES:
            return self._load_utterances()
        if current_app.config['COMMENT_PLATFORM'] == GITALK:  # pragma: no cover
            return self._load_gitalk()

    @staticmethod
    def _load_disqus(
        page_url: t.Optional[str] = None,
        page_indentifier: t.Optional[str] = None,
    ) -> Markup:
        """
        Load Disqus resources.

        Reference: https://disqus.com/
        """
        page_url = page_url or request.base_url
        page_indentifier = page_indentifier or request.path
        short_name = current_app.config['COMMENT_DISQUS_SHORTNAME']

        return Markup(
            """<div id='disqus_thread'></div>
            <script>
                var disqus_config = function () {{
                this.page.url = '{}';
                this.page.identifier = '{}';
                }};

                (function() {{ // DON'T EDIT BELOW THIS LINE
                var d = document, s = d.createElement('script');
                s.src = 'https://{}.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
                }})();
            </script>
            <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">
            comments powered by Disqus.</a></noscript>""".format(
                page_url, page_indentifier, short_name
            )
        )

    @staticmethod
    def _load_cusdis() -> Markup:
        """
        Load Cusdis resources.

        Reference: https://cusdis.com/
        """
        app_id = current_app.config['COMMENT_CUSDIS_APP_ID']
        page_id = request.path
        return Markup(
            """<div id="cusdis_thread"
                        data-host="https://cusdis.com"
                        data-app-id="{}"
                        data-page-id="{}"
                        data-page-url="{}"
                        data-page-title=""
                        >
                        <script>
                        (function(){{
                            const cusdis = document.getElementById('cusdis_thread')
                            cusdis.setAttribute('data-page-title', document.title)
                        }})()
                        </script>
                        <script async src="https://cusdis.com/js/cusdis.es.js"></script>
                      """.format(
                app_id, page_id, page_id
            )
        )

    @staticmethod
    def _load_valine() -> Markup:
        """
        Load Valine resources.

        Reference: https://valine.js.org/
        """
        app_id = current_app.config['COMMENT_VALINE_APP_ID']
        app_key = current_app.config['COMMENT_VALINE_APP_KEY']

        return Markup(
            """<script src='https://unpkg.com/valine/dist/Valine.min.js'></script>
            <div id='vcomments'></div>
            <script>
                new Valine({{
                    'el': '#vcomments',
                    'appId': '{}',
                    'appKey': '{}',
                }})
            </script>""".format(
                app_id, app_key
            )
        )

    @staticmethod
    def _load_utterances() -> Markup:
        """
        Load Utterances resources.

        Reference: https://utteranc.es/
        """
        repo = current_app.config['COMMENT_UTTERANCES_REPO']

        return Markup(
            """<script src="https://utteranc.es/client.js"
                                repo="%s"
                                issue-term="pathname"
                                theme="github-light"
                                crossorigin="anonymous"
                                async>
                        </script>"""
            % repo
        )

    @staticmethod
    def _load_gitalk() -> Markup:
        """
        Load Gitalk resources.

        Reference: https://github.com/gitalk/gitalk#install
        """
        client_id = current_app.config['COMMENT_GITALK_CLIENT_ID']
        client_secret = current_app.config['COMMENT_GITALK_CLIENT_SECRET']
        repo = current_app.config['COMMENT_GITALK_REPO']
        owner = current_app.config['COMMENT_GITALK_OWNER']
        admin = current_app.config['COMMENT_GITALK_ADMIN']

        return Markup(
            """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">
            <script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>
            <div id="gitalk-container"></div>
            <div id='vcomments'></div>
            <script>
                const gitalk = new Gitalk({{
                clientID: '{}',
                clientSecret: '{}',
                repo: '{}',      // The repository of store comments,
                owner: '{}',
                admin: ['{}'],
                id: location.pathname,      // Ensure uniqueness and length less than 50
                distractionFreeMode: false  // Facebook-like distraction free mode
                }})
                gitalk.render('gitalk-container')
            </script>""".format(
                client_id, client_secret, repo, owner, admin
            )
        )
