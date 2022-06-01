from views import Index, About, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList

routes = {
    '/': Index(),
    '/about/': About(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create_course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList()
}
