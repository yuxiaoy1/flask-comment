# Examples

> Check the online examples at <https://flask-comment.vercel.app>.

## Installation

### Build the environment

For macOS and Linux:

```bash
$ git clone https://github.com/yuxiaoy1/flask-comment
$ cd flask-comment/examples
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For Windows:

```bash
> git clone https://github.com/yuxiaoy1/flask-comment
> cd flask-comment/examples
> python -m venv venv
> venv\Scripts\activate
> pip install -r requirements.txt
```

### Set enviroment variables

Create a `.env` file by copying the `.evn.template` file, fill out the [configuration values](configuration.md).

## Run, Flask, Run!

Use `flask run` command to run the example application:

```bash
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now check it out on <http://127.0.0.1:5000> in your browser.

**Disqus:**

![](https://flask-comment.readthedocs.io/en/latest/assets/disqus.png)

**Cusdis:**

![](https://flask-comment.readthedocs.io/en/latest/assets/cusdis.png)

**Valine:**

![](https://flask-comment.readthedocs.io/en/latest/assets/valine.png)

**Utterances:**

![](https://flask-comment.readthedocs.io/en/latest/assets/utterances.png)

**Gitalk:**

![](https://flask-comment.readthedocs.io/en/latest/assets/gitalk.png)
