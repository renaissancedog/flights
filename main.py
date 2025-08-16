import flights_pb2 as PB, base64, requests
from bs4 import BeautifulSoup

trip = [
    ["2025-09-29", "SAT", "TYO"],
    ["2025-10-06", "KIX", "PVG"],
    ["2025-10-22", "PVG", "SAT"]
]
allFlights = []
for leg in trip:
    flight = PB.FlightData(
        date = leg[0],
        from_flight= PB.Airport(airport=leg[1]),
        to_flight = PB.Airport(airport=leg[2])
    )
    allFlights.append(flight)
info = PB.Info()
for flight in allFlights:
    info.data.append(flight)
info.seat = PB.Seat.ECONOMY
info.passengers[:] = [PB.Passenger.ADULT]
if (len(allFlights) > 1):
    info.trip = PB.Trip.MULTI_CITY
else :
    info.trip = PB.Trip.ONE_WAY

info_bytes = info.SerializeToString()
tfs=(base64.b64encode(info_bytes).decode('utf-8'))
url="https://www.google.com/travel/flights/search?tfs="+tfs
print(url)
ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
)
response = requests.get(
        url,
        headers={"user-agent": ua, "accept-language": "en"},
    )

soup = BeautifulSoup(response.content, 'html.parser')
with open("test.html", "w") as f:
  f.write(soup.prettify())