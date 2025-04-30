{
    "key":{
        1: "val",
        2: "strong_val",
        6: "val",
        4: "foo"
    },
    "smtp_password": {
        1: "Pa$$wor",
        3: "fooo",
        2: "reset_admin"
    }
}

class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key, value, timestamp):
        if key not in self.data.keys():
            self.data[key] = {}
        self.data[key][timestamp] = value

    def get(self, key, timestamp):
        key_data = self.data.get(key, None)
        if key_data is None:
            return None
        
        timestamp_data = key_data.get(timestamp, None)
        if timestamp_data is None or len(timestamp_data) < 1:
            return None

        # loop
        max_time, max_value = float("-inf"), float("-inf")
        for time, value in key_data.items():
            if time == timestamp:
                return value
            if max_time < time:
                max_time, max_value = time, value

        return max_value

timeMap = TimeMap()
timeMap.set("alice", "happy", 1)  # store the key "alice" and value "happy" along with timestamp = 1.
print(timeMap.get("alice", 1))           # return "happy"
print(timeMap.get("alice", 2))           # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
print(timeMap.set("alice", "sad", 3))    # store the key "alice" and value "sad" along with timestamp = 3.
print(timeMap.get("alice", 3))           # return "sad"



print(timeMap.get("norbert", 3))
print(timeMap.get("alice", 1))