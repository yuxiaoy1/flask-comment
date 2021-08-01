import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask, render_template
from flask_comment import Comment, DISQUS, CUSDIS, VALINE, GITALK, UTTERANCES

# Initialize multiple Flask instances for different comment platform.
app = Flask(__name__)
app_cusdis = Flask(__name__)
app_valine = Flask(__name__)
app_utterances = Flask(__name__)
app_gitalk = Flask(__name__)

app.config.update(
    {
        'COMMENT_DISQUS_SHORTNAME': 'flask-comment',
    }
)
app_cusdis.config.update(
    {
        'COMMENT_CUSDIS_APP_ID': os.getenv('CUSDIS_APP_ID'),
    }
)
app_valine.config.update(
    {
        'COMMENT_VALINE_APP_ID': os.getenv('VALINE_APP_ID'),
        'COMMENT_VALINE_APP_KEY': os.getenv('VALINE_APP_KEY'),
    }
)
app_utterances.config.update(
    {
        'COMMENT_UTTERANCES_REPO': 'yuxiaoy1/flask-comment',
    }
)
app_gitalk.config.update(
    {
        'COMMENT_GITALK_CLIENT_ID': os.getenv('GITALK_CLIENT_ID'),
        'COMMENT_GITALK_CLIENT_SECRET': os.getenv('GITALK_CLIENT_SECRET'),
        'COMMENT_GITALK_REPO': 'flask-comment',
        'COMMENT_GITALK_OWNER': 'yuxiaoy1',
        'COMMENT_GITALK_ADMIN': 'yuxiaoy1',
    }
)

Comment(app, DISQUS)
Comment(app_cusdis, CUSDIS)
Comment(app_valine, VALINE)
Comment(app_utterances, UTTERANCES)
Comment(app_gitalk, GITALK)

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {
        '/disqus': app,
        '/cusdis': app_cusdis,
        '/valine': app_valine,
        '/utterances': app_utterances,
        '/gitalk': app_gitalk,
    },
)

for _app in (app, app_cusdis, app_valine, app_utterances, app_gitalk):

    @_app.route('/')
    def index():
        return render_template('index.html')
