## 해커톤 - 주울런지

1. **참여자**: (팀장)오진수, (팀원)김현중, (팀원)김현정, (팀원)신우철, (팀원)안예지, (팀원)이주용

3. **폴더 구조 및 기능**

   ```text
   venv (가상환경)
   ------------------------------------------------
   juwoolunge (프로젝트)
   ├─ plogging (APP)
   ├─ .gitignore
   ├─ requirements.txt
   ```



3. **초기 세팅**

   - git repo 생성, 팀원 초대, 가상환경 생성

   - .gitignore 생성

     - https://www.toptal.com/developers/gitignore/

   - python, windows, mac, django, VisualStudioCode 추가 후 ignore 파일 생성

   - requirements.txt 생성

   - 설치 패키지

     - [1] django == 3.2.13
     - [2] django-bootstrap5
     - [3] django-shortcuts
     - [4] django-imagekit
     - [5] pillow
     - [6] django-messages
     - [7] django-extensions

   - 프로젝트(juwoolunge), APP(plogging) 생성

   - settings.py 설정

     ```python
     # juwoolunge/settings.py
     ...
     INSTALLED_APP = [
         'plogging',
         'imagekit',
         'django_extensions',
         'django_bootstrap5',
     ]
     ...
     TEMPLATES = [
         {
             ...
             'DIRS': [ BASE_DIR / "static" ]
             ...
         }
     ]
     ```

   - 