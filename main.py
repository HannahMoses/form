#ULC video class2.5
#C:\Users\brown\Downloads\git\gitcode\LC101\form\myform
#ONLY ON GIT

import webapp2
			# form="""
			# <form method="post">
			# 	What is your birthday?
			# 	<br>
			# 	<label>Month <input type="text" name="month" ></label> <br><br>
			# 	<label>Day <input type="text" name="day"></label><br><br>
			#     <label>Year <input type="text" name="year"></label><br><br>
			#   	<br>
			# 	<br>
			#     <input type="submit">
			# </form>
			# """
class MainPage(webapp2.RequestHandler):
	def get(self):
    #    self.response.out.write(form)
	self.response.write("Form")

    def post(self):
        self.response.out.write("Thanks for a valid day !")

app = webapp2.WSGIApplication([
	('/',MainPage)
	], debug=True)
'''
#Failed code with error display
#ULC video class2.5
import webapp2
form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month <input type="text" name="month" ></label> <br><br>
    <label>Day <input type="text" name="day"></label><br><br>
    <label>Year <input type="text" name="year"></label><br><br>
    <div style="color":red>%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self,error=""):
        self.response.out.wrote(form%{"error":error})
    def get(self):
        #self.response.headerscontent-Type'] = 'text/plain'
        self.write_form
    def post(self):
        if month=="January" :
            self.write_form("Thanks for a valid day !")
        else:
            self.write_form("Invalid month")

app = webapp2.WSGIApplication([('/',MainPage)], debug=True)
