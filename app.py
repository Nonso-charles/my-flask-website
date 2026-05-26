from flask import Flask, render_template, request

app = Flask(__name__)


# ── Shared data ─────────────────────────────────────────

SERVICES = [
    {"icon": "✂️",  "name": "Classic Cut",          "desc": "A timeless scissor and clipper cut tailored to your face shape and preferred style.",
        "price": "3,500",  "duration": "30 min", "popular": False},
    {"icon": "🪒",  "name": "Hot Towel Shave",       "desc": "A luxurious straight-razor shave with warm towels, pre-shave oil, and cooling balm.",
        "price": "4,000",  "duration": "45 min", "popular": True},
    {"icon": "💈",  "name": "Cut & Shave Combo",     "desc": "The full works — a precise haircut followed by our signature hot towel straight shave.",
        "price": "6,500",  "duration": "70 min", "popular": True},
    {"icon": "🧴",  "name": "Beard Sculpt & Line",   "desc": "Expert beard shaping, line-up, and conditioning to keep your beard sharp and healthy.",
        "price": "2,500",  "duration": "25 min", "popular": False},
    {"icon": "👑",  "name": "The Royal Treatment",   "desc": "Full cut, shave, beard sculpt, scalp massage, and a hot towel facial. The full luxury experience.",
        "price": "12,000", "duration": "120 min", "popular": False},
    {"icon": "🧒",  "name": "Kids Cut (Under 12)",   "desc": "A gentle, fun haircut for the young gents. Clippers or scissors, whatever they prefer.",
     "price": "2,000",  "duration": "20 min", "popular": False},
    {"icon": "💆",  "name": "Scalp Massage",         "desc": "A deep, relaxing scalp massage with essential oils to boost circulation and relieve tension.",
        "price": "2,000",  "duration": "20 min", "popular": False},
    {"icon": "🔦",  "name": "Edge-Up / Line-Up",     "desc": "Precision hairline clean-up along the forehead, temples, and neckline.",
        "price": "1,500",  "duration": "15 min", "popular": False},
]

TEAM = [
    {"emoji": "💈", "name": "Emeka Obi",     "role": "Master Barber & Founder",
        "bio": "Over 20 years behind the chair. Emeka trained in London and Lagos and founded Blade & Grace in 2008."},
    {"emoji": "✂️", "name": "Tunde Adeyemi", "role": "Senior Barber",
        "bio": "Tunde specialises in fades and modern cuts. His precision line-ups are legendary on the island."},
    {"emoji": "🪒", "name": "Chidi Nwosu",   "role": "Shave Specialist",
        "bio": "Chidi is our hot-towel shave expert. He'll have you looking smoother than you thought possible."},
]


# ── Routes ───────────────────────────────────────────────

@app.route("/")
def home():
    stats = [
        {"number": "16+", "label": "Years in Business"},
        {"number": "12K+", "label": "Happy Clients"},
        {"number": "3",   "label": "Master Barbers"},
    ]
    why = [
        {"icon": "🏆", "title": "Award-Winning Craft",
            "desc": "Recognised as Lagos' top barbershop three years running. Our blades speak for themselves."},
        {"icon": "🌿", "title": "Premium Products Only",
            "desc": "We use only the finest grooming products — Baxter of California, Proraso, and house blends."},
        {"icon": "⏱️", "title": "Punctual Every Time",
            "desc": "We respect your time. Book an appointment and walk in to a chair that's ready for you."},
    ]
    return render_template("home.html", active="home", stats=stats, why=why)


@app.route("/about")
def about():
    story = "Blade & Grace was born on the corner of Broad Street in 2008, when Master Barber Emeka Obi returned from a decade of training in London with one vision: to bring world-class barbering to Lagos Island."
    story2 = "What started as a two-chair shop has grown into the most trusted grooming destination in the city — a place where tradition meets precision and every client leaves looking like the best version of himself."

    values = [
        {"title": "Precision Over Speed",
            "desc": "We never rush a cut. Every service is performed with full attention and care, no matter how busy we are."},
        {"title": "Respect in the Chair",
            "desc": "The barber's chair is a place of trust. We listen, we advise, and we always deliver what you ask for."},
        {"title": "Community First",
            "desc": "We're proud to be a Lagos institution. From apprenticeships to sponsorships, we invest in the community we serve."},
        {"title": "Continuous Improvement",
            "desc": "Our barbers train every quarter. New techniques, new products — we are always evolving our craft."},
    ]
    return render_template("about.html", active="about", story=story, story2=story2, team=TEAM, values=values)


@app.route("/services")
def services():
    return render_template("services.html", active="services", services=SERVICES)


@app.route("/booking", methods=["GET", "POST"])
def booking():
    shop_info = [
        {"icon": "📍", "label": "Address",
            "value": "14 Broad Street, Lagos Island, Lagos"},
        {"icon": "🕐", "label": "Opening Hours",
            "value": "Tuesday – Sunday: 9:00am – 8:00pm"},
        {"icon": "📞", "label": "Phone",        "value": "+234 801 234 5678"},
        {"icon": "📧", "label": "Email",        "value": "hello@bladeandgrace.ng"},
    ]

    time_slots = ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
                  "1:00 PM", "2:00 PM",  "3:00 PM",  "4:00 PM",
                  "5:00 PM", "6:00 PM",  "7:00 PM"]

    service_names = [s["name"] for s in SERVICES]
    barber_names = [b["name"] for b in TEAM]

    booked = False
    booked_name = ""
    booked_email = ""

    if request.method == "POST":
        booked = True
        booked_name = request.form.get("first_name", "")
        booked_email = request.form.get("email", "")

    return render_template(
        "booking.html",
        active="booking",
        shop_info=shop_info,
        time_slots=time_slots,
        services=service_names,
        barbers=barber_names,
        booked=booked,
        booked_name=booked_name,
        booked_email=booked_email,
    )


if __name__ == "__main__":
    app.run(debug=True)
