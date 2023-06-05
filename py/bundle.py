import numpy as np


def bundling(data):
    # Set maximum time spent and distance for a bundle
    MAX_TIME_SPENT = 300
    MAX_DISTANCE = 10  # in km

    # Set minimum time_spent and distance for a bundle
    MIN_TIME_SPENT = 120
    MIN_DISTANCE = 5  # in km

    # Set maximum number of attraction in a bundle
    MAX_ATTRACTION = 5
    MIN_ATTRACTION = 2

    #  create a list of Attractions
    attractions = []
    for row in data:
        id = int(row[0])
        lat = float(row[1])
        lng = float(row[2])
        time_spent = int(row[3])
        attractions.append((id, lat, lng, time_spent))
    # Initialize the list of bundles and visited attraction
    bundles = []
    visited = set()

    # Loop through each attraction and try to bundle it with other attractions
    for i, (id, lat, lng, time_spent) in enumerate(attractions):
        if id in visited:
            continue

        # Create a new bundle with the current attraction
        bundle = [(id, lat, lng, time_spent)]
        visited.add(id)

        # Find all nearby attraction within 5km and add them to the bundle
        for j, (other_id, other_lat, other_lng, other_time) in enumerate(attractions[i+1:], start=i+1):
            if other_id in visited:
                continue

            # Calculate the distance between the two attractions in km using the Haversine formula
            lat1, lng1, lat2, lng2 = np.radians(lat), np.radians(lng), np.radians(other_lat), np.radians(other_lng)
            dlat, dlng = lat2 - lat1, lng2 - lng1
            a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlng/2)**2
            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
            distance = 6371 * c

            if distance <= MIN_DISTANCE and len(bundle) < MAX_ATTRACTION:
                bundle.append((other_id, other_lat, other_lng, other_time))
                visited.add(other_id)

        # Calculate the total time spent and distance of the bundle
        total_time = sum(b[3] for b in bundle)
        total_distance = sum(np.sqrt((bundle[i][1]-bundle[i-1][1])**2 + (bundle[i][2]-bundle[i-1][2])**2) for i in range(1, len(bundle)))

        # If the bundle meets the conditions, add it to the list of bundles
        if total_time >= MIN_TIME_SPENT and total_time <= MAX_TIME_SPENT and total_distance <= MAX_DISTANCE and len(bundle) >= MIN_ATTRACTION:
            bundles.append(bundle)

    # Print the list of bundles
    for i, bundle in enumerate(bundles):
        print(f"Bundle {i+1}:")
        for id, lat, lng, time_spent in bundle:
            print(f"- attraction {id}: ({lat}, {lng}), {time_spent} minutes")

    return bundles
