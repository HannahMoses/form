﻿#ULC video class2.5

import webapp2

form="""

<form method="post">
    
	What is your birthday?
   
	 <br>
   
	 <label>Month <input type="text" name="month" ></label> <br><br>
  
	 <label>Day <input type="text" name="day"></label><br><br>
    
	<label>Year <input type="text" name="year"></label><br><br>
   
  	 <br>
   
	 <br>
    
	<input type="submit">

</form>

"""


class MainPage(webapp2.RequestHandler):
  
	def get(self):
       
                		 #self.response.headerscontent-Type'] = 'text/plain'
        
		self.response.out.write(form)
   

	 def post(self):
        
		self.response.out.write("Thanks for a valid day !")



app = webapp2.WSGIApplication([
	('/',MainPage)
	], debug=True)


