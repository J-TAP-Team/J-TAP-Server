# J-TAP-Server

J-TAP의 API 서버입니다.

<hr></hr>

## Getting Start

### 가상환경 생성 및 실행

- MAC OS
```
virtualenv venv
source venv/bin/activate
```

- WINDOWS
```
virtualenv venv
call venv/Scripts/activate
```

### 파이썬 라이브러리 설치
```
pip install -r requirements.txt
```



### db 생성
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### 서버 실행
```
python manage.py run
```

