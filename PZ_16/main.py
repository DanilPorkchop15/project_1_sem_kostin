import modules
from figures import triangle, circle
modules.get_set()
modules.lessons_list.get_list()
print(modules.get_txt())

print(modules.list_doc.doc)

print(dir(modules))
print(triangle.triangle_perimeter(10, 4, 11))
print(circle.circle_area(10))
