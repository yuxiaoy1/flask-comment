import pytest
from flask import current_app

from flask_comment import CUSDIS
from flask_comment import GITALK
from flask_comment import UTTERANCES
from flask_comment import VALINE


@pytest.mark.usefixtures('client')
class TestComment:
    def test_extension_init(self):
        assert 'comment' in current_app.extensions

    def test_load_method(self, comment):
        current_app.config['COMMENT_DISQUS_SHORTNAME'] = 'shortname'

        rv = comment.load()
        assert 'disqus' in rv

    def test_default_disqus_comment_platform(self, client):
        current_app.config['COMMENT_DISQUS_SHORTNAME'] = 'shortname'

        rv = client.get('/')
        data = rv.get_data(as_text=True)
        assert rv.status_code == 200
        assert 'disqus' in data
        assert 'shortname' in data

    def test_cusdis_comment_platform(self, client):
        current_app.config['COMMENT_PLATFORM'] = CUSDIS
        current_app.config['COMMENT_CUSDIS_APP_ID'] = 'app-id'

        rv = client.get('/')
        data = rv.get_data(as_text=True)
        assert rv.status_code == 200
        assert 'cusdis' in data

    def test_valine_comment_platform(self, client):
        current_app.config['COMMENT_PLATFORM'] = VALINE
        current_app.config['COMMENT_VALINE_APP_ID'] = 'app-id'
        current_app.config['COMMENT_VALINE_APP_KEY'] = 'app-key'

        rv = client.get('/')
        data = rv.get_data(as_text=True)
        assert rv.status_code == 200
        assert 'valine' in data

    def test_utterances_comment_platform(self, client):
        current_app.config['COMMENT_PLATFORM'] = UTTERANCES
        current_app.config['COMMENT_UTTERANCES_REPO'] = 'username/repo'

        rv = client.get('/')
        data = rv.get_data(as_text=True)
        assert rv.status_code == 200
        assert 'utteranc.es' in data

    def test_gitalk_comment_platform(self, client):
        current_app.config['COMMENT_PLATFORM'] = GITALK
        current_app.config['COMMENT_GITALK_CLIENT_ID'] = 'client-id'
        current_app.config['COMMENT_GITALK_CLIENT_SECRET'] = 'client-secret'
        current_app.config['COMMENT_GITALK_REPO'] = 'repo'
        current_app.config['COMMENT_GITALK_OWNER'] = 'owner'
        current_app.config['COMMENT_GITALK_ADMIN'] = 'admin'

        rv = client.get('/')
        data = rv.get_data(as_text=True)
        assert rv.status_code == 200
        assert 'gitalk' in data
