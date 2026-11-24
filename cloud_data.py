
import pandas as pd
import random

def get_cloud_data():

    data = {
        "Cloud": ["AWS", "Azure", "Google Cloud"],
        "Resource": [
            "EC2 Server",
            "Virtual Machine",
            "Compute Engine"
        ],
        "CPU": [85, 45, 65],
        "Memory": [78, 60, 55],
        "Storage": [90, 50, 70],
        "Cost": [5000, 3500, 4000],
        "Status": ["Running", "Running", "Running"]
    }

    return pd.DataFrame(data)


def refresh_cloud_data():

    data = get_cloud_data()

    data["CPU"] = [
        random.randint(20, 95) for i in range(3)
    ]

    data["Memory"] = [
        random.randint(20, 95) for i in range(3)
    ]

    data["Storage"] = [
        random.randint(20, 95) for i in range(3)
    ]

    return data
