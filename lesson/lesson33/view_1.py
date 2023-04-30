def index():
    with open('template/index.html') as f:
        return f.read()


def blog():
    with open('template/blog.html') as f:
        return f.read()
