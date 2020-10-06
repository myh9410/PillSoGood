![](doc/images/pillsogood.png)



<p align=center style="line-height: 2;">
<img src="https://img.shields.io/badge/framework-Vue.js 4.4.6-green" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/framework-Django 2.1.15-ff69b4" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/database-SQLite-yellowgreen" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/server-AWS-9cf" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/language-Javascript-important" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/language-HTML5-important" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/language-CSS-important" alt="기술스택" style="zoom:100%;" /><img src="https://img.shields.io/badge/language-Python-important" alt="기술스택" style="zoom:100%;" />
</p>



<p align=center>
  <b>Supported Frameworks</b><br/>
 <img width="50" src="https://cdn.iconscout.com/icon/free/png-512/django-2-282855.png" alt="Django" />&nbsp;&nbsp;
  <img width="45" src="https://naver.github.io/egjs-flicking/images/vue.svg" alt="Vue.js" />
</p>

<hr>

## 📃 Git Flow

#### Git Branch

- Master

  - Develop

    - Front

      - feature/front/{기능}

    - Back

      - feature/back/{기능}

#### Git Commit Message

<p align=center style="line-height: 2;">
    <a>:emoji: | (맨처음 대문자) 이해하기 쉽게 최대한영어로 | Jira 이슈 코드번호</a>
<br>
<img src="https://img.shields.io/badge/최초커밋 🎉-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/기능추가 🆕-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/기능버전업 🆙-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/버그픽스 🐛-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/작업완료 ✅-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/파일/코드제거 🔥-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/코드개선 🔨-yellow" alt="이모지" style="zoom:100%;" /><img src="https://img.shields.io/badge/trash code 💩-yellow" alt="이모지" style="zoom:100%;" />
</p>



## ⚙️ Installation

#### Backend

```bash
$ cd backend
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata categories.json
$ python manage.py loaddata functionals.json
$ python manage.py loaddata nutrients.json
$ python manage.py loaddata supplements.json
$ python manage.py runserver
```

#### Frontend

```bash
$ cd frontend
$ npm install
$ npm run serve
```



## :earth_americas: Supported Browsers

<p align=center>
 <img width="300" src="https://venturebeat.com/wp-content/uploads/2016/10/chrome_firefox_edge_logos.png?w=1200&strip=all" alt="BrowserSupport" />
</p>



## 📼 Demos

Check our [Demos](http://j3a506.p.ssafy.io/). (Coming soon~😎)



## 📖 Documentation

#### ERD

![](doc/images/erd.PNG)

#### Wireframe

- 로그인 x
  - 영양제 제품보기 페이지는 접근 가능
  - 영양제 추천 페이지는 제한

![](doc/images/wireframe1.PNG)

- 로그인 o
  - 모든 페이지 접근 가능

![](doc/images/wireframe2.PNG)
