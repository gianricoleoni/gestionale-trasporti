from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_KEY = "AIzaSyAI1p00jSenVAcgtHYfKskdQokCgJwljVs"

storico = []

def get_distance(orig, dest):
url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={orig}&destinations={dest}&key={API_KEY}"
r = requests.get(url).json()
try:
return r['rows'][0]['elements'][0]['distance']['value'] / 1000
except:
return 0

@app.route("/", methods=["GET", "POST"])
def index():
risultato = None

```
if request.method == "POST":
    cliente = request.form["cliente"]
    partenza = request.form["partenza"]
    scarico = request.form["scarico"]
    rientro = request.form["rientro"]
    
    km1 = get_distance(partenza, scarico)
    km2 = get_distance(scarico, rientro)
    tot_km = km1 + km2
    
    costo_km = 1.2
    consumo = 3
    gasolio = 1.8
    telepass = 0.15
    
    totale = (tot_km * costo_km) + (tot_km/consumo * gasolio) + (tot_km * telepass)
    
    risultato = {
        "cliente": cliente,
        "km": round(tot_km,2),
        "totale": round(totale,2)
    }
    
    storico.append(risultato)

return render_template("index.html", risultato=risultato, storico=storico)
```

if __name__ == "__main__":
    app.run()
