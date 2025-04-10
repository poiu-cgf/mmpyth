# PYTHON ....
# Telegram : @ndmmo - @zlzflf 
# instagram : ****
# Codeder : B7E | ابن بابل 

# هذه الاداة - بوت مجانية وليست للبيع الرجاء عدم بيعها ..
# عدم ازالة الحقوق تقديرا لتعبنا وجعلنا نستمر في تقديم مثل هكذا (ادوات او بوتات)..

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import json
import uuid
import time
import webbrowser
webbrowser.open(f'https://t.me/ndmmo')
bot = telebot.TeleBot("7908862338:AAGKmY9TtLwZlaHnHJ30Qsp9OMPG1dAtGHY")
VOICES_PER_PAGE = 30
ff = None  
bb = None  

def Fix():
    try:
        url = "https://ai-voice.nyc3.cdn.digitaloceanspaces.com/data/data.json"
        headers = FOU()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('voices', [])
        else:
            print(f"Error fetching voices. Status Code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching voices: {e}")
        return []

def Fox():
    Id_B7E1 = uuid.uuid4().hex
    start_time = str(int(time.time() * 1000))
    Id_B7E9 = uuid.uuid4().hex + ":APA91b"
    return Id_B7E1, start_time, Id_B7E9

def FOU():
    return {
        'User-Agent': "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.100 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        'sec-ch-ua-mobile': "?1",
        'origin': "http://localhost",
        'x-requested-with': "com.leonfiedler.voiceaj",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "http://localhost/",
        'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i"
    }

@bot.message_handler(commands=['start'])
def SpS(message):
    bot.reply_to(message, "- اهلا بك في بوت الاصوات مدفوع 🤖")
    VoV(message, page=1)

def VoV(message, page=1):
    voices = Fix()
    if not voices:
        bot.send_message(message.chat.id, "- لا توجد اصوات حاليا ⛔️")
        return
    start_idx = (page - 1) * VOICES_PER_PAGE
    end_idx = start_idx + VOICES_PER_PAGE
    current_voices = voices[start_idx:end_idx]
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(f"{voice['name']} (بالعربية)", callback_data=f"voice_{idx}") for idx, voice in enumerate(current_voices, start=start_idx)]
    markup.add(*buttons)
    pagination_buttons = []
    if start_idx > 0:
        pagination_buttons.append(InlineKeyboardButton("🧚‍♀️ السابق 🧚‍♀️", callback_data=f"page_{page-1}"))
    if end_idx < len(voices):
        pagination_buttons.append(InlineKeyboardButton("🧚‍♀️ التالي 🧚‍♀️", callback_data=f"page_{page+1}"))
    if pagination_buttons:
        markup.add(*pagination_buttons)
    bot.send_message(message.chat.id, "- اختر صوتاً:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("voice_") or call.data.startswith("page_"))
def handle_callback_query(call):
    if call.data.startswith("voice_"):
        H0(call)
    elif call.data.startswith("page_"):
        page = int(call.data.split("_")[1])
        VoV(call.message, page)

def H0(call):
    global ff, bb
    try:
        Id_B7Ex = int(call.data.split("_")[1])
        voices = Fix()
        B7E = voices[Id_B7Ex]
        ff = B7E.get('category') 
        bb = B7E.get('id')  
        if Id_B7Ex >= 183:
            bot.send_message(call.message.chat.id, f"لقد اخترت: {B7E['name']}\nالصورة تم حضرها من قبل الصانع B7E الصوت.")
        else:
            image_url = f"https://ai-voice.nyc3.cdn.digitaloceanspaces.com/voice_images/{B7E['image_ios'].split('/')[-1]}"
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                bot.send_photo(call.message.chat.id, image_response.content, caption=f"لقد اخترت: {B7E['name']}")
        bot.send_message(call.message.chat.id, "هلا عزيزي المتابع ادخل نص فقط ")
        bot.register_next_step_handler(call.message, process_text_input, B7E)
    except Exception as e:
        print(f"Error in H0: {e}")

def process_text_input(message, B7E):
    text = message.text
    if len(text) > 200:
        bot.send_message(message.chat.id, "عذراً، لقد تجاوزت الحد المسموح به للنص المجاني. يرجى الانتظار للتحديثات المستقبلية.")
        return
    while True:
        try:
            Id_B7E1, start_time, Id_B7E9 = Fox()
            token2, Id_B7E2, C9 = ABC()
            if token2 and Id_B7E2 and C9:
                EFG(Id_B7E2, token2, Id_B7E1)
                audio_data = HIG(Id_B7E2, token2, C9, Id_B7E1, Id_B7E9, B7E['voiceId'], text, B7E['name'])
                bot.send_audio(message.chat.id, audio_data, title=f"{B7E['name']} @ndmmo")
                break
        except Exception as e:
            print(f"Error in process_text_input loop: {e}")

def ABC():
    try:
        U0 = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser"
        P0 = {'key': "AIzaSyDk5Vr0fvGX3AF3mNfMghP6Q-ECoBYT7aE"}
        P1 = json.dumps({"clientType": "CLIENT_TYPE_ANDROID"})
        B7E_com = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Build/RKQ1.201004.002)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'X-Android-Package': "com.leonfiedler.voiceai",
            'X-Android-Cert': "F6D71619262E74DC6BADD005D596BA9EC6543814",
            'Accept-Language': "ar-EG, en-US",
            'X-Client-Version': "Android/Fallback/X23000000/FirebaseCore-Android",
            'X-Firebase-GMPID': "1:444011263758:android:acbabc2d1f24666531495f",
            'X-Firebase-Client': "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA"
        }
        while True:
            O0O = requests.post(U0, params=P0, data=P1, headers=B7E_com)
            data_signup = O0O.json()
            token2 = data_signup['idToken']
            Cc0 = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo"
            T0T = json.dumps({"idToken": token2})
            R0R = requests.post(Cc0, params=P0, data=T0T, headers=B7E_com)
            D0 = R0R.json()
            Id_B7E2 = D0['users'][0]['localId']
            C9 = D0['users'][0]['createdAt']
            return token2, Id_B7E2, C9
    except Exception as e:
        print(f"Error in ABC: {e}")
        return None, None, None

def EFG(Id_B7E2, token2, Id_B7E1):
    try:
        url = "https://api.getvoices.ai/api/v1/user"
        payload = json.dumps({
            "uid": Id_B7E2,
            "isNew": True,
            "uuid": f"android_{Id_B7E1}",
            "platform": "android",
            "appVersion": "1.10.1"
        })
        headers = FOU()
        headers['authorization'] = token2
        requests.post(url, data=payload, headers=headers)
    except Exception as e:
        print(f"Error in EFG: {e}")

def HIG(Id_B7E2, token2, C9, Id_B7E1, Id_B7E9, Id_B7E, text, voice_name):
    try:
        url = "https://connect.getvoices.ai/api/v1/text2speech/stream"
        payload = json.dumps({
            "voiceId": Id_B7E,
            "text": text,
            "deviceId": Id_B7E1,
            "uid": Id_B7E2,
            "lang": "ar",
            "platform": "android",
            "voice": bb,
            "voiceCategory": ff,
            "subscribed": 50000,
            "startTime": C9,
            "translate": None,
            "fcmToken": Id_B7E9,
            "appVersion": "1.10.1"
        })
        headers = FOU()
        headers['authorization'] = token2
        response = requests.post(url, data=payload, headers=headers)
        return response.content
    except Exception as e:
        print(f"Error in HIG: {e}")
        return None

if __name__ == "__main__":
    bot.polling()
