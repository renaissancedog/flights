import flights_pb2 as PB, base64

trip = [
    ["2025-08-23", "SAT", "BOS"]
    # ["2025-10-23", "BOS", "SAT"]
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
