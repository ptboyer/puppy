
function venvup {
    rm -rf venv
    virtualenv -p python3 venv
    activate
}

function venvdown {
    deactivate
}

venvup
v2_start=$(($(date +%s%N) / 1000 ))
pip install bcrypt flask flask-script flask-restful flask-migrate flask-cors pyjwt webargs marshmallow requests psycopg2 git+http://github.com/nickw444/flask-sqlalchemy.git redis celery boto3
v2_end=$(($(date +%s%N) / 1000 ))
v2_diff=$(($v2_end - $v2_start))
venvdown

# venvup
# v1_start=$(($(date +%s%N) / 1000 ))
# pip install bcrypt
# pip install flask
# pip install flask-script
# pip install flask-restful
# pip install flask-migrate
# pip install flask-cors
# pip install pyjwt
# pip install webargs
# pip install marshmallow
# pip install requests
# pip install psycopg2
# pip install git+http://github.com/nickw444/flask-sqlalchemy.git
# pip install redis
# pip install celery
# pip install boto3
# v1_end=$(($(date +%s%N) / 1000 ))
# v1_diff=$(($v1_end - $v1_start))
# venvdown

# echo "Serial   $v1_diff"
# echo "Parallel $v2_diff"

# if [[ $v1_diff < $v2_diff ]]; then
#     echo "SERIAL WINS"
# else
#     echo "PARALLEL WINS"
# fi
