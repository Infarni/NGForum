About
---
Ready-made minimalist forum on Django

___
Installation
---
1. Cloning this repo
2. Install requirements Navigate to the repository folder <code>pip install -r requirements.txt</code>

___
Configure
---
1. Run <code>python manage.py makemigrations && python manage.py migrate</code>
2. If you need to fill the database, then execute the following command <code>python manage.py --command="from handlers import database; database.filling()"</code>


___
Run
---
Run start.sh or start.bat