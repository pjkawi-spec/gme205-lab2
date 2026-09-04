from spatial import Point

p = Point("A", 121.0, 14.6) 
print(p.id, p.lon, p.lat)
print(p.to_tuple()) 

q = Point("X", 121.0, 14.6) 
print(q.id, q.lon, q.lat)

print(p.distance_to(q))

