class BlogPost(object):

    def __init__(self, name, title, text, publication_date):
        self.name = name
        self.title = title
        self.text = text
        self.publication_date = publication_date

blog1 = BlogPost("John Doe", "Lorem ipsum", "dolor ipsum dolor sit ament",
"2000.05.04.")
blog2 = BlogPost("Tim Urban", "Wait but why", "A popular long-form,\
stick-figure-illustrated blog about almost everything.", "2010.10.10.")
blog3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon\
 With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to\
 be the center of attention. When I asked to take his picture outside one of \
 IBM’s New York City offices, he told me that he wasn’t really into the whole \
 organizer profile thing.", "2017.03.28.")

print(blog1.name, blog1.title, blog1.text, blog1.publication_date)
print(blog2.name, blog2.title, blog2.text, blog2.publication_date)
print(blog3.name, blog3.title, blog3.text, blog3.publication_date)