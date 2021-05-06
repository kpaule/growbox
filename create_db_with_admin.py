from growbox import db, create_app
app = create_app()
app.app_context().push()
db.create_all()

from growbox.models import User
u = User(username="admin", password="$2b$12$aTjB4dj.K2t67gUJgSn4vu5uSxthhabnAbOUFyhIKhBgs6CgtxkpO")
db.session.add(u)
db.session.commit()

User.query.all()