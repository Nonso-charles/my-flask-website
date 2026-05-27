from flask import Flask, render_template, request

app = Flask(__name__)

SERVICES = [
    {"icon": "✂️",  "name": "Classic Cut",          "desc": "A precision scissor and clipper cut tailored to your face shape and preferred length.",
        "price": "3,500",  "duration": "30 min", "popular": False},
    {"icon": "🪒",  "name": "Hot Towel Shave",       "desc": "Luxurious straight-razor shave with warm towels, pre-shave oil, and a cooling balm finish.",
        "price": "4,000",  "duration": "45 min", "popular": True},
    {"icon": "💈",  "name": "Cut & Shave Combo",     "desc": "The full works — a precise cut followed by our signature hot towel straight-razor shave.",
        "price": "6,500",  "duration": "70 min", "popular": True},
    {"icon": "🧴",  "name": "Beard Sculpt & Line",   "desc": "Expert beard shaping, edge line-up, and conditioning treatment for a sharp, healthy beard.",
        "price": "2,500",  "duration": "25 min", "popular": False},
    {"icon": "👑",  "name": "The Royal Treatment",   "desc": "Full cut, shave, beard sculpt, scalp massage, and a hot towel facial. Total luxury.",
        "price": "12,000", "duration": "120 min", "popular": False},
    {"icon": "🧒",  "name": "Kids Cut (Under 12)",   "desc": "A fun, gentle haircut for the young gents. Scissor or clipper, whatever they prefer.",
     "price": "2,000",  "duration": "20 min", "popular": False},
    {"icon": "💆",  "name": "Scalp Massage",         "desc": "Deep relaxing scalp massage with essential oils to relieve tension and boost circulation.",
        "price": "2,000",  "duration": "20 min", "popular": False},
    {"icon": "🔦",  "name": "Edge-Up / Line-Up",     "desc": "Precision hairline clean-up along the forehead, temples, and neckline.",
        "price": "1,500",  "duration": "15 min", "popular": False},
]

TEAM = [
    {"emoji": "💈", "name": "Emeka Obi",     "role": "Master Barber & Founder",
        "bio": "20+ years behind the chair. Trained in London and Lagos. Founded Blade & Grace in 2008 with one goal: bring world-class cuts to Lagos Island."},
    {"emoji": "✂️", "name": "Tunde Adeyemi", "role": "Senior Barber",
        "bio": "Tunde specialises in skin fades and modern textured cuts. His precision line-ups are what legends are made of."},
    {"emoji": "🪒", "name": "Chidi Nwosu",   "role": "Shave Specialist",
        "bio": "Chidi is our hot towel shave expert. He'll leave your skin smoother than you thought humanly possible."},
]


@app.route("/")
def home():
    stats = [
        {"number": "16+",  "label": "Years Open"},
        {"number": "12K+", "label": "Happy Clients"},
        {"number": "3",    "label": "Master Barbers"},
    ]
    top_services = [
        {"icon": "✂️", "name": "Classic Cut",     "price": "3,500"},
        {"icon": "🪒", "name": "Hot Towel Shave", "price": "4,000"},
        {"icon": "💈", "name": "Cut & Shave",     "price": "6,500"},
        {"icon": "👑", "name": "Royal Treatment", "price": "12,000"},
    ]
    return render_template("home.html", active="home", stats=stats, top_services=top_services)


@app.route("/about")
def about():
    story = "Blade & Grace was born on the corner of Broad Street in 2008, when Master Barber Emeka Obi returned from a decade of training in London with one clear vision: bring world-class barbering to Lagos Island."
    story2 = "What started as a two-chair shop is now Lagos' most trusted grooming destination — a place where tradition meets precision and every client leaves looking like the best version of himself."

    values = [
        {"title": "Precision Over Speed",
            "desc": "We never rush a cut. Every service gets full attention and care, no matter how busy we get."},
        {"title": "Respect in the Chair",
            "desc": "The barber's chair is a place of trust. We listen, we advise, and we always deliver what you ask for."},
        {"title": "Community First",
            "desc": "We're proud to be a Lagos institution. From apprenticeships to local sponsorships — we invest in our city."},
        {"title": "Always Improving",
            "desc": "Our barbers train quarterly. New techniques, new products — we are always evolving our craft."},
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
            "value": "Tuesday – Sunday · 9:00am – 8:00pm"},
        {"icon": "📞", "label": "Phone",         "value": "+234 801 234 5678"},
        {"icon": "📧", "label": "Email",         "value": "hello@bladeandgrace.ng"},
    ]

    time_slots = ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
                  "1:00 PM", "2:00 PM",  "3:00 PM",  "4:00 PM",
                  "5:00 PM", "6:00 PM",  "7:00 PM"]

    service_names = [s["name"] for s in SERVICES]
    barber_names = [b["name"] for b in TEAM]

    booked = False
    booked_name = booked_email = ""

    if request.method == "POST":
        booked = True
        booked_name = request.form.get("first_name", "")
        booked_email = request.form.get("email", "")

    return render_template(
        "booking.html", active="booking",
        shop_info=shop_info, time_slots=time_slots,
        services=service_names, barbers=barber_names,
        booked=booked, booked_name=booked_name, booked_email=booked_email,
    )


if __name__ == "__main__":
    app.run(debug=True)
