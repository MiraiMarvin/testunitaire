import json
import os
from meteo import save_to_json, plot_hourly_temperatures

def test_save_to_json(tmp_path):
    data = [{"time": "2024-07-02T00:00", "temperature_2m": 20}]
    file_path = tmp_path / "test.json"
    save_to_json(data, file_path)
    with open(file_path, encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == data

def test_plot_hourly_temperatures(tmp_path):
    
    data = [
        {"time": "2024-07-02T00:00", "temperature_2m": 20},
        {"time": "2024-07-02T01:00", "temperature_2m": 21},
        {"time": "2024-07-02T02:00", "temperature_2m": 19}
    ]
    json_file = tmp_path / "test.json"
    save_to_json(data, json_file)
    
    plot_hourly_temperatures(json_file)
    
    assert os.path.exists("graphique_températures.png")
    os.remove("graphique_températures.png")