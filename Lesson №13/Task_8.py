def render_input(field):
    return f'<input id="id_{field}" name="{field}">'

def wrap_with_p(func):
    def wrapper(*args, **kwargs):
        return f'<p>{func(*args, **kwargs)}</p>'
    return wrapper

@wrap_with_p
def render_input_with_p(field):
    return render_input(field)

username = render_input_with_p('username')
print(username)