## Notes:

### Localization:

```bash
python manage.py makemessages -l uk -l en -l en_us -i env/**/locale -i .env/**/locale -i venv/**/locale -i .venv/**/locale

django-admin compilemessages -i env/**/locale -i .env/**/locale -i venv/**/locale -i .venv/**/locale
```
