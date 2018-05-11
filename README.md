# wipro_digital

HOW TO RUN THE CODE 

The project was built in Python3.6 environment. 
To run the project go to wipro_digital/Wipro_Digital.py and run it. 
The whole process will automatically run through the code and run through wipro_digital.com pages and create a structured xml.

The xml consists of of a field name, name is the name of the sitemap are we parsing and then the value is a url.

you may need to install beautiful soup. pip3 install bs4

Following methodologies were tried:
I explored and built a project using scrapy, it did not work as expected. It scraped through all pages and download all pages, then wanted to use that to build a xml. Then I realised it could be easier to do with beautiful soup and I ended up doing with that. 
It was a great learning curve.
Please let me know if theres any issues.
