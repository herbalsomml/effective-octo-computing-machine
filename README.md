# Catalog of webcam studios
## Version 1.0.2

Catalog of webcam studios with search, filtering and display priority


📚 Libs:
-
- Django
- Jazzmin
- Pillow
- django-bootstrap5
- postgres
- docker
- nginx
- gunicorn


## 👨🏻‍💻 How to install:

#### 1️. Copy .env.example as .env and fill it

#### 2. Run docker-compose.yml
```bash
  docker-compose up --build
```

#### 3. Migrate DB
```bash
  sudo docker compose -f docker-compose.yml exec backend python manage.py migrate
```

#### 4. Collect Static
```bash
  sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic
```

#### 5. Create Superuser
```bash
  sudo docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```

#### Path to logo and fav icon:
```website/main/static/assets/img```

## 💀 Reach Me Here
[![Telegram](https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ihatemylifebutiluvmoney)
[![Instagram](https://img.shields.io/badge/Instagram-purple?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/herbalsomml)
[![email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:herbalsomml@gmail.com)