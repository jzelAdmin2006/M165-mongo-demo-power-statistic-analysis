import datetime
import os
import time
import matplotlib.pyplot as plt

import psutil
from pymongo import MongoClient
from matplotlib.animation import FuncAnimation


def draw_graph(i):
    cursor = db.power_usage.find().sort("timestamp", -1).limit(10000)
    data = list(cursor)
    data.reverse()
    times = [x["timestamp"] for x in data]
    cpu_usage = [x["cpu"] for x in data]
    ram_usage = [x["ram_usage"] for x in data]
    plt.cla()
    plt.plot(times, cpu_usage, label='CPU Usage (%)')
    plt.plot(times, ram_usage, label='RAM Usage (bytes)')
    plt.legend(loc='upper left')
    plt.tight_layout()


connection_string = os.environ['MONGODB_CONNECTION_STRING']
client = MongoClient(connection_string)
db = client["power_statistics"]

ani = FuncAnimation(plt.gcf(), draw_graph, interval=1000)
plt.show()
