# -*- coding: utf-8 -*-
import json
import os
import traceback
import uuid

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from content import MODULES, get_module
from extensions import db, login_manager
from models import Progress, User

load_dotenv()

try:
    import iyzipay
except ImportError:  # pragma: no cover
    iyzipay = None

IYZICO_API_KEY = os.environ.get("IYZICO_API_KEY")
IYZICO_SECRET_KEY = os.environ.get("IYZICO_SECRET_KEY")
IYZICO_BASE_URL = os.environ.get("IYZICO_BASE_URL", "sandbox-api.iyzipay.com")
PREMIUM_PRICE = "10"  # TL, tek seferlik


def iyzico_options():
    return {
        "api_key": IYZICO_API_KEY,
        "secret_key": IYZICO_SECRET_KEY,
        "base_url": IYZICO_BASE_URL,
    }


def iyzico_ready():
    return bool(iyzipay and IYZICO_API_KEY and IYZICO_SECRET_KEY)


anthropic_client = None
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if ANTHROPIC_API_KEY:
    try:
        from anthropic import Anthropic

        anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)
    except Exception:
        anthropic_client = None

SYSTEM_PROMPT = (
    "Sen 'AI Akademi' adlı Türkiye odaklı bir eğitim platformunda çalışan, "
    "samimi ve sıcakkanlı bir yapay zekâ öğretmenisin. Karşındaki kişi "
    "yapay zekâ konusunda YENİ BAŞLAYAN bir öğrenci. Bir arkadaş gibi, "
    "günlük ve içten bir Türkçeyle konuş — kuru, resmî bir ders kitabı "
    "gibi değil. Emin olmadığın yerde 'harika soru', 'güzel yakaladın' "
    "gibi doğal bir sıcaklık kullanabilirsin ama abartma, samimiyet "
    "yapmacık durmasın.\n\n"
    "Kavramları anlatırken elinden geldiğince Türkiye'den, günlük "
    "hayattan örnekler ve benzetmeler kullan: Trendyol'un ürün "
    "önerileri, Getir'in teslimat süresi tahmini, bankaların anlık "
    "dolandırıcılık uyarıları, İstanbul trafiğinde en kısa yolu bulma, "
    "yerli dil modeli çalışmaları (Trendyol-LLM, Kumru LLM, TÜBİTAK'ın "
    "projeleri) gibi. Emin olmadığın spesifik bir Türkiye örneği "
    "uydurma; genel ve doğru kalan örnekleri tercih et.\n\n"
    "Cevapların kısa ve öz olsun (en fazla birkaç paragraf), karmaşık "
    "terimleri kullanırken kısa bir açıklama ekle. Öğrenciyi asla "
    "küçümseme, 'aptalca soru yok' mantığıyla yaklaş."
)


def is_module_unlocked(user, module, progress_by_module=None):
    """İlk modül herkese açık. Sonrakiler: premium kullanıcıya hep açık,
    normal kullanıcıya ise bir önceki modül tamamlanmışsa açık."""
    idx = MODULES.index(module)
    if idx == 0:
        return True
    if user.is_premium:
        return True
    if progress_by_module is None:
        prev = MODULES[idx - 1]
        row = Progress.query.filter_by(user_id=user.id, module_id=prev["id"]).first()
        return bool(row and row.completed)
    prev_progress = progress_by_module.get(MODULES[idx - 1]["id"])
    return bool(prev_progress and prev_progress.completed)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-degistir")
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "aiacademy.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message = "Bu sayfayı görmek için önce giriş yapmalısın."

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    with app.app_context():
        db.create_all()

    # ---------- Genel sayfalar ----------

    @app.route("/")
    def index():
        return render_template("index.html", modules=MODULES)

    # ---------- Kimlik doğrulama ----------

    @app.route("/kayit", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")

            if not username or not email or not password:
                flash("Lütfen tüm alanları doldur.", "error")
            elif len(password) < 6:
                flash("Şifre en az 6 karakter olmalı.", "error")
            elif User.query.filter_by(username=username).first():
                flash("Bu kullanıcı adı zaten alınmış.", "error")
            elif User.query.filter_by(email=email).first():
                flash("Bu e-posta zaten kayıtlı.", "error")
            else:
                user = User(username=username, email=email)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash("Hoş geldin! Kaydın oluşturuldu.", "success")
                return redirect(url_for("dashboard"))
        return render_template("register.html")

    @app.route("/giris", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for("dashboard"))
            flash("Kullanıcı adı veya şifre hatalı.", "error")
        return render_template("login.html")

    @app.route("/cikis")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("index"))

    # ---------- Panel / ilerleme ----------

    @app.route("/panel")
    @login_required
    def dashboard():
        rows = Progress.query.filter_by(user_id=current_user.id).all()
        progress_by_module = {p.module_id: p for p in rows}
        completed_count = sum(1 for p in rows if p.completed)
        unlocked_by_module = {
            m["id"]: is_module_unlocked(current_user, m, progress_by_module)
            for m in MODULES
        }
        return render_template(
            "dashboard.html",
            modules=MODULES,
            progress_by_module=progress_by_module,
            unlocked_by_module=unlocked_by_module,
            completed_count=completed_count,
            total_modules=len(MODULES),
        )

    # ---------- Modüller ve quiz ----------

    @app.route("/modul/<slug>", methods=["GET", "POST"])
    @login_required
    def module_view(slug):
        module = get_module(slug)
        if module is None:
            return redirect(url_for("dashboard"))

        if not is_module_unlocked(current_user, module):
            flash(
                "Bu modülü açmak için önceki modülü tamamlamalısın — ya da "
                "Premium'a geçip tüm modüllere anında erişebilirsin.",
                "error",
            )
            return redirect(url_for("dashboard"))

        result = None
        if request.method == "POST":
            correct = 0
            for i, q in enumerate(module["quiz"]):
                answer = request.form.get(f"q{i}")
                if answer is not None and int(answer) == q["correct"]:
                    correct += 1
            total = len(module["quiz"])

            row = Progress.query.filter_by(
                user_id=current_user.id, module_id=module["id"]
            ).first()
            if row is None:
                row = Progress(user_id=current_user.id, module_id=module["id"])
                db.session.add(row)
            row.completed = True
            row.score = correct
            row.total = total
            db.session.commit()
            result = {"correct": correct, "total": total}

        idx = MODULES.index(module)
        next_module = MODULES[idx + 1] if idx + 1 < len(MODULES) else None
        return render_template(
            "module.html", module=module, result=result, next_module=next_module
        )

    # ---------- Premium (iyzico) ----------

    @app.route("/premium")
    @login_required
    def premium():
        return render_template(
            "premium.html", price=PREMIUM_PRICE, iyzico_ready=iyzico_ready()
        )

    @app.route("/premium/odeme", methods=["GET", "POST"])
    @login_required
    def premium_odeme():
        if current_user.is_premium:
            flash("Zaten Premium üyesin!", "success")
            return redirect(url_for("dashboard"))

        if not iyzico_ready():
            flash(
                "Ödeme sistemi şu an yapılandırılmamış. Lütfen daha sonra "
                "tekrar dene.",
                "error",
            )
            return redirect(url_for("premium"))

        if request.method == "POST":
            name = request.form.get("name", "").strip()
            surname = request.form.get("surname", "").strip()
            identity_number = request.form.get("identity_number", "").strip()
            address = request.form.get("address", "").strip()
            city = request.form.get("city", "").strip()
            gsm = request.form.get("gsm", "").strip()

            if not all([name, surname, identity_number, address, city]):
                flash("Ödeme için lütfen tüm alanları doldur.", "error")
                return render_template("premium_odeme.html", price=PREMIUM_PRICE)

            conversation_id = str(uuid.uuid4())
            request_body = {
                "locale": "tr",
                "conversationId": conversation_id,
                "price": PREMIUM_PRICE,
                "paidPrice": PREMIUM_PRICE,
                "currency": "TRY",
                "basketId": f"premium-{current_user.id}-{conversation_id[:8]}",
                "paymentGroup": "PRODUCT",
                "callbackUrl": url_for("premium_callback", _external=True),
                "enabledInstallments": [1],
                "buyer": {
                    "id": str(current_user.id),
                    "name": name,
                    "surname": surname,
                    "gsmNumber": gsm or "+905000000000",
                    "email": current_user.email,
                    "identityNumber": identity_number,
                    "registrationAddress": address,
                    "ip": request.remote_addr or "85.34.78.112",
                    "city": city,
                    "country": "Turkey",
                },
                "shippingAddress": {
                    "contactName": f"{name} {surname}",
                    "city": city,
                    "country": "Turkey",
                    "address": address,
                },
                "billingAddress": {
                    "contactName": f"{name} {surname}",
                    "city": city,
                    "country": "Turkey",
                    "address": address,
                },
                "basketItems": [
                    {
                        "id": "premium-uyelik",
                        "name": "AI Akademi Premium Üyelik",
                        "category1": "Eğitim",
                        "itemType": "VIRTUAL",
                        "price": PREMIUM_PRICE,
                    }
                ],
            }

            checkout_form = iyzipay.CheckoutFormInitialize()
            raw_response = checkout_form.create(request_body, iyzico_options())
            result = json.loads(raw_response.read().decode("utf-8"))

            if result.get("status") == "success" and result.get("paymentPageUrl"):
                return redirect(result["paymentPageUrl"])

            flash(
                "Ödeme başlatılamadı: "
                + result.get("errorMessage", "bilinmeyen hata"),
                "error",
            )
            return redirect(url_for("premium"))

        return render_template("premium_odeme.html", price=PREMIUM_PRICE)

    @app.route("/premium/callback", methods=["GET", "POST"])
    @login_required
    def premium_callback():
        token = request.form.get("token") or request.args.get("token")
        if not token or not iyzico_ready():
            flash("Ödeme doğrulanamadı.", "error")
            return redirect(url_for("premium"))

        checkout_form = iyzipay.CheckoutForm()
        raw_response = checkout_form.retrieve(
            {"locale": "tr", "conversationId": str(uuid.uuid4()), "token": token},
            iyzico_options(),
        )
        result = json.loads(raw_response.read().decode("utf-8"))

        if result.get("status") == "success" and result.get("paymentStatus") == "SUCCESS":
            current_user.is_premium = True
            db.session.commit()
            flash("Premium üyeliğin aktifleşti! Artık tüm modüller açık. 🎉", "success")
            return redirect(url_for("dashboard"))

        flash(
            "Ödeme tamamlanamadı: "
            + result.get("errorMessage", "kart onaylanmadı veya iptal edildi."),
            "error",
        )
        return redirect(url_for("premium"))

    # ---------- Chatbot ----------

    @app.route("/sohbet")
    @login_required
    def chatbot():
        return render_template("chatbot.html", api_ready=anthropic_client is not None)

    @app.route("/api/sohbet", methods=["POST"])
    @login_required
    def api_chat():
        if anthropic_client is None:
            return (
                jsonify(
                    {
                        "error": "Sunucuda ANTHROPIC_API_KEY tanımlı değil. "
                        ".env dosyana kendi API anahtarını ekleyip sunucuyu "
                        "yeniden başlat."
                    }
                ),
                503,
            )

        data = request.get_json(silent=True) or {}
        user_message = (data.get("message") or "").strip()
        history = data.get("history") or []  # [{role, content}, ...]

        if not user_message:
            return jsonify({"error": "Boş mesaj gönderilemez."}), 400

        messages = []
        for item in history[-10:]:
            role = item.get("role")
            content = item.get("content")
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": user_message})

        try:
            response = anthropic_client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=600,
                system=SYSTEM_PROMPT,
                messages=messages,
            )
            reply_text = "".join(
                block.text for block in response.content if block.type == "text"
            )
        except Exception as exc:  # pragma: no cover
            return jsonify({"error": f"API hatası: {exc}"}), 500

        return jsonify({"reply": reply_text})

    # GEÇİCİ DEBUG: hatanın gerçek sebebini sitede görmek için.
    # Sorun çözülünce bu bloğu app.py'den sil.
    @app.errorhandler(Exception)
    def _debug_show_error(e):
        return "<pre>" + traceback.format_exc() + "</pre>", 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
