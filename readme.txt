mkdir apna_avneesh_project
cd apna_avneesh_project
virtualenv apna_env
git clone https://github.com/avneeshkumar/apna_co_project.git
source apna_env/bin/activate
cd apna_co_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

OPEN BROWSER
To create dummy friend1,friend2 connection
http://127.0.0.1:8000/createdummy/

To fetch friend of user with id
http://127.0.0.1:8000/friends/<id>
Example : http://127.0.0.1:8000/friends/5

To fetch friend of user with id at depth k
http://127.0.0.1:8000/friends/<id>?depth=<k>
Example: http://127.0.0.1:8000/friends/4?depth=2
