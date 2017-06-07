import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Rot(Handler):

    def get(self):
        self.render("rot.html", string = "")

    def post(self):
        s = self.request.get('text')
        new_s = ""
        if(s):
            for x in s:
                x = ord(x)
                if(x >= ord('a') and x <= ord('z')):
                    x = (((x + 13) - ord('a')) % 26) + ord('a')
                if (x >= ord('A') and x <= ord('Z')):
                    x = (((x + 13) - ord('A')) % 26) + ord('A')
                x = chr(x)
                new_s += x
        self.render('rot.html', string = new_s)

app = webapp2.WSGIApplication([
    ('/', Rot),
], debug=True)
