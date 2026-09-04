import math 

class Point:
    def __init__(self, id, lon, lat, name=None, tag=None): 
        if not (-180 <= lon <= 180): 
            raise ValueError("Longitude must be between -180 and 180") 
        if not (-90 <= lat <= 90): 
            raise ValueError("Latitude must be between -90 and 90") 
        
        self.id = id 
        self.lon = lon 
        self.lat = lat 
        self.name = name
        self.tag = tag
# ------------------------------------------------------------------ 
# Instance methods (behavior belongs to the object) 
# ------------------------------------------------------------------ 
    def to_tuple(self) -> tuple[float, float]: 
        """ 
        Return the coordinate as a (lon, lat) tuple. 
        """ 
        return (self.lon, self.lat) 
    def distance_to(self, other): 
        return Point.haversine_m(self.lon, self.lat, other.lon, other.lat) 
# ------------------------------------------------------------------ 
# Static method (pure spatial math) 
# ------------------------------------------------------------------ 
    @staticmethod 
    def haversine_m( 
        lon1: float, lat1: float, lon2: float, lat2: float 
    ) -> float: 
        """ 
        Compute the Haversine distance between two lon/lat pairs in meters. 

        Static method because it does not depend on object state. 
        """ 
        R = 6_371_000.0  # Earth radius in meters 

        phi1 = math.radians(lat1) 
        phi2 = math.radians(lat2) 
        dphi = math.radians(lat2 - lat1) 
        dlambda = math.radians(lon2 - lon1) 

        a = ( 
            math.sin(dphi / 2) ** 2 
            + math.cos(phi1) 
            * math.cos(phi2) 
            * math.sin(dlambda / 2) ** 2 
            ) 
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) 
        return R * c 
# ------------------------------------------------------------------ 
# Class method (constructing objects from data) 
# ------------------------------------------------------------------ 
    @classmethod 
    def from_row(cls, row): 
        return cls( 
            id=str(row["id"]), 
            lon=float(row["lon"]), 
            lat=float(row["lat"]), 
            name=row.get("name"), 
            tag=row.get("tag"), 
        ) 
# ------------------------------------------------------------------
# Semantic method (behavior depends on object state)
# ------------------------------------------------------------------
    def is_poi(self): 
        return (self.tag or "").lower() == "poi"

class PointSet:
    def __init__(self, points: list[Point]): 
        self.points = points
# ------------------------------------------------------------------ 
# Class method (constructing objects from data) 
# ------------------------------------------------------------------
    @classmethod 
    def from_csv(cls, path): 
        import csv 
        points = [] 
        with open(path, newline="") as csvfile: 
            reader = csv.DictReader(csvfile) 
            for row in reader: 
                points.append(Point.from_row(row)) 
        return cls(points)
        
# ------------------------------------------------------------------ 
# Instance methods (behavior belongs to the object) 
# ------------------------------------------------------------------ 
    def count(self): 
        return len(self.points)

    def bbox(self): 
        """ 
        Return the bounding box of the points as a tuple: (min_lon, min_lat, max_lon, max_lat) 
        """ 
        min_lon = min(p.lon for p in self.points) 
        max_lon = max(p.lon for p in self.points) 
        min_lat = min(p.lat for p in self.points) 
        max_lat = max(p.lat for p in self.points) 
        return (min_lon, min_lat, max_lon, max_lat)

    def filter_by_tag(self, tag): 
        """ 
        Return a new PointSet containing only points with the given tag. 
        """ 
        filtered_points = [p for p in self.points if p.tag == tag] 
        return PointSet(filtered_points)