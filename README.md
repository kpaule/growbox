# Growbox

Im Projekt “Klimakontrolle eines Raums“ soll mithilfe eines IoT Geräts eine smarte Gewächskiste angesteuert werden. Die Pflanzen sollen eine artgerechte Umgebung bekommen, um ein optimales Wachstum zu ermöglichen.

## Versioning
### Clone the project
`git clone https://gitlab.com/mthaithanh/growbox.git`

### Checkout branch
`git checkout <branch_name>`

### Create and checkout branch
`git checkout -b <branch_name>`

### Create branch
`git branch <branch_name>`

### List branches
`git branch`

### View status
`git status`

### Add changes
`git add <file_name>`

### Commit changes with message
`git commit -m "<meaningful_message>"`

### Push changes to remote
`git push -u`

## Workflow
1. Clone branch
2. Create and checkout new branch
3. Make changes
4. Add changes
5. Commit changes with meaningful message
6. Push changes to remote repository
7. Create merge request
8. Resolve conflicts

## Folder structure
```
< PROJECT ROOT >
   |
   |-- app/
   |    |-- home/                                # Home Blueprint - serve app pages (private area)
   |    |-- base/                                # Base Blueprint - handles the authentication
   |         |-- static/
   |         |    |-- <css, JS, images>          # CSS files, Javascripts files
   |         |
   |         |-- templates/                      # Templates used to render pages
   |              |
   |              |-- includes/                  #
   |              |    |-- navigation.html       # Top menu component
   |              |    |-- sidebar.html          # Sidebar component
   |              |    |-- footer.html           # App Footer
   |              |    |-- scripts.html          # Scripts common to all pages
   |              |
   |              |-- layouts/                   # Master pages
   |              |    |-- base-fullscreen.html  # Used by Authentication pages
   |              |    |-- base.html             # Used by common pages
   |              |
   |              |-- accounts/                  # Authentication pages
   |                   |-- login.html            # Login page
   |                   |-- register.html         # Registration page
   |
   |-- requirements.txt                          # Development modules - SQLite storage
   |-- requirements-mysql.txt                    # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt                    # Production modules  - PostgreSql DMBS
   |
   |-- .env                                      # Inject Configuration via Environment
   |-- config.py                                 # Set up the app
   |-- run.py                                    # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

## Docker
### Build
`sudo docker build -t python-growbox .`
### Run
`sudo docker run -p 5000:5000 python-growbox`

## DB usage
```
# create db
from growbox import db, create_app
app = create_app()
app.app_context().push()
db.create_all()

# add row
from growbox.models import User
u = User(username="admin", password="$2b$12$aTjB4dj.K2t67gUJgSn4vu5uSxthhabnAbOUFyhIKhBgs6CgtxkpO") # pw = admin
db.session.add(u)
db.session.commit()

# query data
User.query.all()
User.query.first()
User.query.filter_by(username="admin").first()
```

## Password hash usage
```
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# generate password hash
hashed_pw = bcrypt.generate_password_hash("testing").decode("utf-8")

# check password hash
bcrypt.check_password_hash(hashed_pw, "testing")

```