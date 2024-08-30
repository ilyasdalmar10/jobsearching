class websites:
        def __init__(self,url,content_div,title_div,salary_div,location_div):
            self.url = url
            self.content_div = content_div
            self.title_div = title_div
            self.salary_div = salary_div
            self.location_div = location_div

        def __str__(self):
            return f"THE LINK {self.url}"




