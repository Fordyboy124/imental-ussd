from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", "")
    service_code = request.values.get("serviceCode", "")
    phone_number = request.values.get("phoneNumber", "")
    text = request.values.get("text", "")

    response = ""

    if text == "":
        response = "CON Welcome to iMental\n1. Book a session\n2. Talk to therapist\n3. Exit"
    elif text == "1":
        response = "CON Choose a date:\n1. Tomorrow\n2. Next Week"
    elif text == "2":
        response = "CON Therapist available now\n1. Yes\n2. No"
    elif text == "3":
        response = "END Thank you for using iMental"
    else:
        response = "END Invalid choice"

    return Response(response, mimetype="text/plain")

@app.route('/')
def index():
    return "iMental USSD is running"

