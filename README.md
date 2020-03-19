# gtcourseinfo
GT Course Info scrapes RateMyProfessor.com (RMP) as well as Georgia Tech's (GT) Course Critique service to return the average GPA for the class as well as a list of instructors who teach the class with their RMP ratings.
<h3>Files: </h3>

 <h4>main.py </h4>
 <p>
  This file uses a local database of RMP ratings to return the relevant ones. For the list of professors and average GPA, it uses BeautifulSoup to scrape GT Course Critique. 
  </p>
  <h4>updater.py</h4>
  <p>
  This file makes a series of requests to GT's RMP page and creates a list object of dictionary objects, each one corresponding to an instructor. 
  </p>
  <h4>profsList.pkl</h4>
  <p>
  This .pkl file is made using the pickle library. It holds the python list object from which main.py searches for its results. 
  </p>

<h3>Example: </h3>
<p>
The system prompts you to enter the name of the class. 

<a href="https://imgur.com/RjI8EHy"><img src="https://i.imgur.com/RjI8EHy.jpg" title="source: imgur.com" /></a>

Then, it returns all the relevant information. 

<a href="https://imgur.com/okJxHrd"><img src="https://i.imgur.com/okJxHrd.jpg" title="source: imgur.com" /></a>

</p>

