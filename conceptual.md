### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python works based on indentation and spacing, whereas JS works primarily using symbols.

JS is good for working with client-side browsers, Python is good for working with back-end data.

Python is a bit clearer and simpler to understand, but JS seems like it can do more sometimes.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.


      try:
        dict["c"]
      except:
        print("didn't crash")
  
  'c' in dict
  returns false

- What is a unit test?
A unit test is a test that tests the particular functions and processes of a single unit of the program.

- What is an integration test?
An integration test tests how the different units interact with each other, including data-types, error-handling, user-errors, etc.

- What is the role of web application framework, like Flask?

This helps to integrate all the pieces together and do things like manage the http requests between different files in different languages.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

Generally you'd want more independent routes to get their own URL, like specific items being shopped for (vs variations of color of the item) or areas of a website.

Specific variations of those routes might get search params, or any other aspect that allows for user-customization (naming, searching, a calculator, etc)

- How do you collect data from a URL placeholder parameter using Flask?

@app.route('/page/<param>')
def handle(param):
    param = param

- How do you collect data from the query string using Flask?

request.args.get("name-of-data")

- How do you collect data from the body of the request using Flask?

data = request.form("name-of-data"s)

- What is a cookie and what kinds of things are they commonly used for?

Cookies are tiny bits of data that help maintain state when a user is browsing a website. They might show you have a certain cart item, etc

- What is the session object in Flask?

The session object exists on the browser-side 

- What does Flask's `jsonify()` do?

Turns a dict passed into it into json
