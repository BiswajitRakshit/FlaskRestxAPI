# Description of Flask Aplicataion Programming Interface

### This API is created using Flask restx following Model View Controller Pattern
MVC Pattern stands for Model-View-Controller Pattern. This pattern is used to separate application's concerns.

**Model** - Model represents an object or json carrying data. It can also have logic to update controller if its data changes.

**View** - View represents the visualization of the data that model contains.

**Controller** - Controller acts on both model and view. It controls the data flow into model object and updates the view whenever data changes. It keeps view and model separate.

### This API returns json files and this files are tested in Postman

Postman is an application used for API testing. It is an HTTP client that tests HTTP requests, utilizing a graphical user interface, through which we obtain different types of responses that need to be subsequently validated. 

Postman offers many endpoint interaction methods. The following are some of the most used, including their functions:

GET: Obtain information 

POST: Add information

PUT: Replace information

PATCH: Update certain information

DELETE: Delete information

### When testing APIs with Postman, we usually obtain different response codes. Some of the most common include:

100 Series > Temporal responses, for example, ‘102 Processing’.

200 Series > Responses where the client accepts the request and the server processes it successfully, for instance, ‘200 Ok’.

300 Series  > Responses related to URL redirection, for example, ‘301 Moved Permanently.’

400 Series  > Client error responses, for instance, ‘400 Bad Request’.

500 Series > Server error responses, for example, ‘500 Internal Server Error.’

### json Responces are formatted as 'Status-Massage-Data'  
