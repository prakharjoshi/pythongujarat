################# Imports ####################

# Python imports
import os

# Framework imports
import jinja2
import webapp2

############## End imports ####################


############# Setup environment ###############

# Jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

########### End environment setup #############


################# Handlers ####################

class FrontPageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("front-page.html")
        self.response.write(template.render())


class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("blog.html")
        self.response.write(template.render())


class GitAndPRHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("git-and-pull-request.html")
        self.response.write(template.render())


class LaunchingWebsiteHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("launching-website.html")
        self.response.write(template.render())


class MeetingHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("meeting.html")
        self.response.write(template.render())


class MembersHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("members.html")
        self.response.write(template.render())


class PostingPolicyHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("posting-policy.html")
        self.response.write(template.render())


class PythonResourcesHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("python-resources.html")
        self.response.write(template.render())


class ResourcesHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("resources.html")
        self.response.write(template.render())


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("welcome.html")
        self.response.write(template.render())

############### End handlers ##################


############### Initialization ################

app = webapp2.WSGIApplication([
    ('/', FrontPageHandler),
    ('/meetings', MeetingHandler),
    ('/blog', BlogHandler),
    ('/members', MembersHandler),
    ('/resources', ResourcesHandler),
    ('/posting-policy', PostingPolicyHandler),
    ('/git-and-pull-requests', GitAndPRHandler),
    ('/welcome', WelcomeHandler),
    ('/launching-website', LaunchingWebsiteHandler)
], debug=True)

############# End initialization ##############

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
