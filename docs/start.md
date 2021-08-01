# Quick Start

Once the extension is installed, create an instance and initialize it with the 
Flask application:

```py
from flask_comment import Comment
...
comment = Comment(app)
```

And then you need to add some configurations to make the initialization valid, for this you can refer to [Configuration](configuration.md) for detailed information.

The comment platform is [Disqus](https://disqus.com) by default, and you can set the comment platform by passing a second argument to the `Comment` class:

```py
from flask_comment import Comment, CUSDIS
...
comment = Comment(app, CUSDIS)
```

With this, the [Cusdis](https://cusdis.com) platform has been set, and the supported variable here is `DISQUS`, `CUSDIS`, `VALINE`, `UTTERANCES`, `GITALK`, keep in mind you need to add unique configurations for each comment platform.

If the application uses the [application factory pattern](https://flask.palletsprojects.com/en/latest/patterns/appfactories/), 
the two-step initialization method can be used instead:

```py
from flask import Flask
from flask_comment import Comment, CUSDIS
comment = Comment()

def create_app():
    app = Flask(__name__)
    comment.init_app(app, CUSDIS)
    ...
    return app
```

To complete the initialization, add the following line inside the Jinja template that will use the extension:

```jinja
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask-Comment Example</title>
</head>
<body>
<h1>Flask-Comment Example</h1>

<!-- This would render the comment component in your html -->
{{ comment.load() }}

</body>
</html>
```