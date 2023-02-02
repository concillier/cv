from django.db import models

#Articles = Projects

class articles(models.Model): 

    #Mandatory fields
    
    name= models.CharField(max_length=100)
    summary = models.CharField (max_length=300)
    fulltext= models.TextField(default='Text me')

    data = 'Data Analysis'
    coding = 'Coding'
    writing = 'Writing'
    creativity = 'Creativity'
    category_choices = [(data,'Data analysis'), (coding, 'Coding'), (writing ,'Writing'), (creativity, 'DIY/Creative')]
    category = models.CharField(choices=category_choices, default='DIY/Creative', max_length=15)

    #Optional fields

    url= models.URLField (blank=True)

    py = 'Python'
    ht = 'HTML'
    cs = 'CSS'
    ja = 'JAVA'
    csh = 'C#'
    njs = 'Nodejs'
    sq = 'SQL'
    
    stack_choices= [(py,'Python'), (ht,'HTML'),(cs, 'CSS'), (ja,'Java'), (csh,'C#'), (njs, 'NodeJS'), (sq, 'SQL')]
    stack = models.CharField(choices=stack_choices, blank=True, max_length=10)

    image1 = models.ImageField(upload_to='projects/images/', blank=True)
    image2 = models.ImageField(upload_to='projects/images/', blank=True)
    image3 = models.ImageField(upload_to='projects/images/', blank=True)
    image4 = models.ImageField(upload_to='projects/images/', blank=True)
    image5 = models.ImageField(upload_to='projects/images/', blank=True)

    #To ensure admin shows the actual title strings
    def __str__(self): 
        return self.name

    
    
    



