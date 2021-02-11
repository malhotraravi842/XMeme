cd src/backend

virtualenv myprojectenv

source myprojectenv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

sudo ufw allow 8000
