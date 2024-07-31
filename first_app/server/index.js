const express = require('express')
const app = express()

//loading node packages 
const cors = require('cors');
const Joi = require('joi'); 

const courses = [
    {id: 1, name: 'math'},
    {id: 2, name: 'science'},
    {id: 3, name: 'public-speaking'}
];

app.use(cors());
app.use(express.json()); //enables parsing of json objects 

app.get('/', (req, res) => { //callback function which takes a request and response 
    res.send("Hello World");
});

//defines another route > this route used to get all of the courses
//we define each route using api.get and then the handling function
app.get('/api/courses', (req, res) => {
    res.send(courses);
});

//used to get a specific course with a route parameter
//add the route handling function > sending the request parameter to the client 
//when you use this route with an id of 1, the response object gets the id from the request object and displays it back 
//to the client 
app.get('/api/courses/:id', (req, res) => {
    //passing c goes to some boolean logic 
    const course = courses.find(c => c.id == parseInt(req.params.id)); 
    //if a course of that id is not found, return 404 status code (object not found)
    if (!course) return res.status(404).send("The course with given ID was not found"); 
    //else clause 
    res.send(course); 
}); 

//if we want to get all of the posts with a given year and a given month 
//sends the entire request paramater object to the client 
//consists of things based on the route parameters 
app.get('/api/posts/:year/:month', (req, res) => {
    //res.send(req.query);  will send the query params back to the client 
    res.send(req.params); //will send the request parameters back to the client 
}); 


//use postman to test whether the request was sent successfully 
//takes the name parameter from the body of the json object 
//sent from the request 
//open postman, send a request body to that URL 
app.post('/api/courses', (req, res) => {
     //input validation 

    const { error } = validateCourse(req.body); //result.error
    if (error) return res.status(400).send(error.details[0].message); //bad request
    
    const course = {
        id: courses.length + 1,
        name: req.body.name 
    };
    courses.push(course); //adds the new course to the courses array 
    res.send(course); 
}); 

//?sortBy=name is a query parameter 

app.put('/api/courses/:id', (req, res) => {
    //look up the course, if it does not exist, 404 error (object not found error)
    const course = courses.find(c => c.id == parseInt(req.params.id)); 
    if (!course) return res.status(404).send("The course with given ID was not found"); 
    //validate the course, if invalid, return 400 error (bad request)

    //const result = validateCourse(req.body); 
    const { error } = validateCourse(req.body); //result.error
    if (error) return res.status(400).send(error.details[0].message); //validation logic can be replaced with joi
    //400 bad request; can use postman to look at the result.error thing and choose a specific part 
    ///of the error message to display to the users      
   
    //update course and return the updated course to the thing 
    course.name = req.body.name;
    res.send(course); 
});

app.delete('/api/courses/:id', (req, res) => {
    //look up the course > if it does not exist return 404 
    const course = courses.find(c => c.id == parseInt(req.params.id)); 
    if (!course) return res.status(404).send("The course with given ID was not found"); 

    //delete logic
    const index = courses.indexOf(course); 
    
    //deletes the item from the courses array by splicing at that index 
    //and removing one object starting fron that index 
    courses.splice(index, 1); 
    res.send(course); 
});

function validateCourse(course){
    const schema = Joi.object({
        name: Joi.string().min(3).required()
    });
    return schema.validate(course); 
}


console.log(app)

//PORT
const port = process.env.PORT || 8080; 
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});