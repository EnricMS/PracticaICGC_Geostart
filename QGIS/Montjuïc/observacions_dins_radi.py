punts = iface.activeLayer()
if punts is None or punts.crs().authid() != "EPSG:25831":
    raise ValueError("Selecciona la capa de punts del GeoPackage (EPSG:25831).")
centre = next(punt for punt in punts.getFeatures() if punt["id"] == "P02")
radi = 500

for punt in punts.getFeatures():
    distancia = centre.geometry().distance(punt.geometry())
    if distancia < radi:
        print(punt["id"], punt["nom"])