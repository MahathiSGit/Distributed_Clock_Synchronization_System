#  Distributed Clock Synchronization System

A lightweight implementation of the Network Time Protocol (NTP) algorithm using UDP sockets in Python. This project demonstrates how distributed systems synchronize clocks across a network by estimating clock offset and round-trip delay.

---

##  Overview

In distributed systems, different machines have independent clocks that drift over time. Clock synchronization is critical for consistency in operations like logging, transactions, and coordination. This project simulates the **NTP clock sync algorithm** between a client and server over UDP.

---

##  Project Structure

```
Distributed_Clock_Synchronization_System/
├── server.py       # UDP server that timestamps incoming requests
├── client.py       # UDP client that calculates clock offset and delay
└── README.md
```

---

##  How It Works

The system uses **four timestamps** to calculate clock offset and network delay — modeled after the NTP algorithm:

| Timestamp | Description |
|-----------|-------------|
| `t1` | Time at which the client sends the request |
| `t2` | Time at which the server receives the request |
| `t3` | Time at which the server sends the response |
| `t4` | Time at which the client receives the response |

### Formulas

```
Clock Offset  = ((t2 - t1) + (t3 - t4)) / 2
Round-trip Delay = (t4 - t1) - (t3 - t2)
```

The client runs **5 iterations**, collects offsets and delays, then computes:
- **Average Offset** — how far the client clock is from the server
- **Average Delay** — the average round-trip network latency
- **Drift-Corrected Time** — client's adjusted local time

---

##  Getting Started

### Prerequisites

- Python 3.x
- No external libraries required (uses built-in `socket` and `time`)

### Running the Project

**1. Start the server** (in one terminal):
```bash
python server.py
```

**2. Start the client** (in another terminal):
```bash
python client.py
```

### Expected Output

**Server:**
```
====================================
 UDP Clock Sync Server Started
 Listening on port 12345...
====================================
Request from ('127.0.0.1', <port>)
t2: 1700000000.123, t3: 1700000000.128
```

**Client:**
```
====================================
 UDP Clock Sync Client Started
====================================

--- Iteration 1 ---
t1 (Client Send)    : 1700000000.120
t2 (Server Receive) : 1700000000.123
t3 (Server Send)    : 1700000000.128
t4 (Client Receive) : 1700000000.131
Offset              : 0.001
Delay               : 0.008

====================================
 FINAL RESULTS
====================================
Average Offset        : 0.0009
Average Delay         : 0.0082
Drift Correction      : 1700000000.9
```

---

##  Concepts Demonstrated

- **UDP Socket Programming** — lightweight, connectionless communication
- **NTP Algorithm** — industry-standard clock synchronization logic
- **Clock Drift Correction** — adjusting local time based on computed offset
- **Round-trip Delay Estimation** — measuring network latency

---

##  Contributors

| Name | Role |
|------|------|
| [Mahathi S] | PES2UG24AM084 |
| [Nethra Manoj] | PES2UG24AM101 |
| [P Samreen] | PES2UG24AM108 |

---

