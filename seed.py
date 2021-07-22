from app import db
from app import Post

# Seeder
db.session.add(Post(
    title='Post 1',
    author='wgprtm_',
    content='Content of post 1'
))

db.session.commit()