set -o allexport; source .env; set +o allexport
cd flask_app && . _venv/bin/activate && flask run