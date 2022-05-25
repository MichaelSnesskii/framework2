from views import Home, About, Contact, Services, Works, Blog

routes = {
    '/': Home(),
    '/index.html/': Home(),
    '/about-agency.html/': About(),
    '/contact-agency.html/': Contact(),
    '/services-agency.html/': Services(),
    '/works-agency.html/': Works,
    '/blog.html/': Blog(),
}
