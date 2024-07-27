from variables import celestial_bodies, celestial_bodies_with_atmosphere_and_water, celestial_bodies_with_atmosphere, situations, situations_recovery, experiments
import pandas as pd

celestial_bodies_with_atmosphere_and_water = ["Kerbin", "Eve", "Laythe"]
celestial_bodies_with_atmosphere = ["Duna", "Jool", "Sun"]
celestial_bodies = ["Kerbin", "Minmus", "Mun", "Duna", "Ike", "Dres", "Eve", "Gilly", "Eeloo", "Moho", "Jool", "Pol", "Bop", "Vall", "Tylo", "Laythe"]

situations = ["SrfLanded", "SrfSplashed", "FlyingLow", "FlyingHigh", "InSpaceLow", "InSpaceHigh"]
situations_recovery = ["Landed", "Splashed", "Flew", "SubOrbited", "Orbited", "Flyby"]

experiments = ["surfaceSample", "evaReport", "crewReport", "mysteryGoo", "mobileMaterialsLab", "temperatureScan", "barometerScan", "gravityScan", "seismicScan", "athmosphereAnalysis", "recovery", "evaScience", "infraredTelescope", "magnetometer", "asteroidSample", "cometSample"]
# df


def main():
    # Einlesen der CSV-Datei
    df = pd.read_csv('C:\\Users\\danie\\OneDrive\\Software\\KSP Science Checklist\\all biomes.csv', delimiter=';')


if __name__ == '__main__':
    main()
