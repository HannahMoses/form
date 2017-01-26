#ULC video class2.5 only on GAEL and GIT

import webapp2
form="""
<form method="post">
	What is your birthday?
    <br>
    <input type="text" name="month" > Month <br><br>
    <input type="text" name="day"> Day <br><br>
    <input type="text" name="year"> Year <br><br>
    <br>
    <br>
    <input type="submit">
</form>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)


app = webapp2.WSGIApplication([
	('/',MainPage)
	], debug=True)
