import flights_pb2 as PB, base64

SAT = PB.Airport(airport="SAT")
TYO = PB.Airport(airport="TYO")

flight1 = PB.FlightData(
    date="2025-09-29",
    from_flight=SAT,
    to_flight=TYO
)
flight2 = PB.FlightData(
    date="2025-10-23",
    from_flight=TYO,
    to_flight=SAT
)
allFlights = [flight1, flight2]
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
