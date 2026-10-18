from flask import Flask, request, jsonify, send_from_directory
import requests
import os
import math

app = Flask(__name__)

API_KEY = os.environ.get("OPENCELLID_API_KEY")

if not API_KEY:
    print("\033[91mERROR: OpenCelliD API key missing.\033[0m")
    print("Run:")
    print("export OPENCELLID_API_KEY='YOUR_API_KEY'")
    raise SystemExit(1)


def make_bbox(lat, lon, radius_km=2):
    lat_delta = radius_km / 111.0

    cos_lat = math.cos(math.radians(lat))

    if abs(cos_lat) < 0.01:
        cos_lat = 0.01

    lon_delta = radius_km / (111.0 * cos_lat)

    return (
        lat - lat_delta,
        lon - lon_delta,
        lat + lat_delta,
        lon + lon_delta
    )


@app.get("/")
def home():
    return send_from_directory(".", "index.html")


@app.get("/api/health")
def health():
    return jsonify({
        "ok": True,
        "service": "CellRadar",
        "source": "OpenCelliD",
        "developer": "Dhannjay Uphade",
        "website": "https://dhannjayuphade.github.io/"
    })


@app.get("/api/cells")
def get_cells():

    try:
        lat = float(request.args.get("lat"))
        lon = float(request.args.get("lon"))
    except (TypeError, ValueError):
        return jsonify({
            "ok": False,
            "error": "Valid lat and lon are required"
        }), 400

    try:
        radius = float(request.args.get("radius", "2"))
    except ValueError:
        radius = 2

    radius = max(0.5, min(radius, 2))

    latmin, lonmin, latmax, lonmax = make_bbox(
        lat,
        lon,
        radius
    )

    bbox = f"{latmin},{lonmin},{latmax},{lonmax}"

    url = "https://opencellid.org/cell/getInArea"

    params = {
        "key": API_KEY,
        "BBOX": bbox,
        "mcc": 404,
        "format": "json",
        "limit": 50
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        data = response.json()

    except requests.RequestException as e:
        return jsonify({
            "ok": False,
            "error": f"OpenCelliD request failed: {e}"
        }), 502

    except ValueError:
        return jsonify({
            "ok": False,
            "error": "OpenCelliD returned invalid JSON"
        }), 502

    if "error" in data:
        return jsonify({
            "ok": False,
            "source": "OpenCelliD",
            "error": data.get("error"),
            "code": data.get("code")
        }), 400

    cells = data.get("cells", [])

    result = []

    for cell in cells:
        result.append({
            "lat": cell.get("lat"),
            "lon": cell.get("lon"),
            "mcc": cell.get("mcc"),
            "mnc": cell.get("mnc"),
            "lac": cell.get("lac"),
            "cellid": cell.get("cellid"),
            "radio": cell.get("radio"),
            "range_m": cell.get("range"),
            "samples": cell.get("samples"),
            "signal": cell.get("averageSignalStrength")
        })

    print(
        f"\033[92m[CELLRADAR] "
        f"GPS={lat:.5f},{lon:.5f} "
        f"CELLS={len(result)}\033[0m"
    )

    return jsonify({
        "ok": True,
        "source": "OpenCelliD",
        "center": {
            "lat": lat,
            "lon": lon
        },
        "radius_km": radius,
        "count": len(result),
        "cells": result
    })


if __name__ == "__main__":

    os.system("clear")

    print("\033[92m")
    print(r"""
 ██████╗███████╗██╗     ██╗         ██████╗  █████╗ ██████╗ 
██╔════╝██╔════╝██║     ██║         ██╔══██╗██╔══██╗██╔══██╗
██║     █████╗  ██║     ██║         ██████╔╝███████║██████╔╝
██║     ██╔══╝  ██║     ██║         ██╔══██╗██╔══██║██╔══██╗
╚██████╗███████╗███████╗███████╗    ██║  ██║██║  ██║██║  ██║
 ╚═════╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
    """)

    print("\033[96m")
    print("╔════════════════════════════════════════════╗")
    print("║       CELLULAR INTELLIGENCE SYSTEM         ║")
    print("║              SYSTEM ONLINE                 ║")
    print("╚════════════════════════════════════════════╝")

    print("\033[92m[+] STATUS    : ONLINE")
    print("[+] SOURCE    : OpenCelliD")
    print("[+] API       : /api/cells")
    print("[+] HEALTH    : /api/health")
    print("[+] WEB UI    : http://127.0.0.1:8080")
    print("[+] DEVELOPER : Dhannjay Uphade")
    print("[+] WEBSITE   : dhannjayuphade.github.io")

    print("\033[96m──────────────────────────────────────────────")

    print("\033[93m[SCAN] Waiting for cellular scan request...")
    print("\033[0m")

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )
