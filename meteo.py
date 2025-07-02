import requests
import json
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt

def get_hourly_temperatures(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&hourly=temperature_2m"
    )
    response = requests.get(url)
    data = response.json()
    hours = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]
    hourly_data = [{"time": t, "temperature_2m": temp} for t, temp in zip(hours, temperatures)]
    return hourly_data

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def plot_hourly_temperatures(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    times = [entry["time"] for entry in data]
    temps = [entry["temperature_2m"] for entry in data]

    plt.figure(figsize=(12, 5))
    plt.plot(times, temps, marker="o")
    plt.xticks(rotation=45)
    plt.xlabel("Heure")
    plt.ylabel("Température (°C)")
    plt.title("Températures heure par heure")
    plt.tight_layout()
    plt.savefig("graphique_températures.png")
    print("Graphique sauvegardé dans graphique_températures.png")

if __name__ == "__main__":
    latitude = 48.8566
    longitude = 2.3522
    hourly_temps = get_hourly_temperatures(latitude, longitude)
    save_to_json(hourly_temps, "historique_températures.json")
    print("températures enregristrées !")
    plot_hourly_temperatures("historique_températures.json")