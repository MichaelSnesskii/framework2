from framework.templator import render


class Home:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', render('about-agency.html')


class Contact:
    def __call__(self):
        return '200 OK', render('contact-agency.html')


class Services:
    def __call__(self):
        return '200 OK', render('services-agency.html')


class Works:
    def __call__(self):
        return '200 OK', render('works-agency.html')


class Blog:
    def __call__(self):
        return '200 OK', render('blog.html')
