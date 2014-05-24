select concat(
'-   model: gallery.Category\n',
'   pk: ', id, '\n',
'   fields:', '\n',
'       name: ', name, '\n',
'       icon: categories/', id, '.jpg', '\n',
'       pub_date: ', pub_date, '\n'
)
from gallery_category;

select concat(
'-   model: gallery.Picture\n',
'   pk: ', id, '\n',
'   fields:', '\n',
'       category: ', category_id, '\n',
'       title: ', title, '\n',
'       image: pictures/', id, '.jpg', '\n',
'       pub_date: ', pub_date, '\n'
)
from gallery_picture;