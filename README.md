# Distance Vector Routing Protocol Simulation
This project simulates the Distance Vector Routing Protocol using Python.
It demonstrates how routers exchange routing tables and iteratively update shortest
path costs using the Bellman-Ford algorithm until the network converges.

## Project Structure
```
Distance-Vector-Routing-Simulation/
│
├── routing_protocol_simulator.py
├── .gitignore
└── README.md
```
## Objective

To simulate a dynamic routing environment in which routers:
- Maintain routing tables
- Exchange routing information with neighbors
- Apply the Bellman-Ford formula to compute shortest paths
- Repeat updates until convergence is achieved

## Requirements
- Python 3.x
- Basic understanding of routing protocols
- No external libraries required

## Distance Vector Routing – Bellman-Ford Algorithm

Distance Vector Routing is an adaptive routing algorithm in which each router
stores the minimum cost to reach every other router in the network.

Routers periodically exchange routing tables with neighbors and update their
own tables using the Bellman-Ford equation:
```
D(x, y) = min ( cost(x, v) + D(v, y) )
```
This process continues until all routers have the correct shortest paths.

## How the Program Works

- User enters the number of routers.
- A random cost matrix is generated.
- Each router initializes its routing table with direct link costs.
- Routers exchange distance vectors.
- Routing tables are updated iteratively using Bellman-Ford.
- The process stops when no further updates occur (convergence).
- Final shortest path tables are displayed.

## How to Run
```bash
python routing_protocol_simulator.py
```
## Example Output
```
Enter number of routers: 4

Generated Cost Matrix:
Router 1: [0, 8, 9, 7]
Router 2: [8, 0, '∞', 1]
Router 3: [9, '∞', 0, '∞']
Router 4: [7, 1, '∞', 0]

Initial Routing Tables:
Router 1: [0, 8, 9, 7]
Router 2: [8, 0, '∞', 1]
Router 3: [9, '∞', 0, '∞']
Router 4: [7, 1, '∞', 0]

--- Iteration 1 ---

Routing Tables after Iteration 1:
Router 1: [0, 8, 9, 7]
Router 2: [8, 0, 17, 1]
Router 3: [9, 17, 0, 16]
Router 4: [7, 1, 16, 0]

--- Iteration 2 ---

Routing Tables after Iteration 2:
Router 1: [0, 8, 9, 7]
Router 2: [8, 0, 17, 1]
Router 3: [9, 17, 0, 16]
Router 4: [7, 1, 16, 0]

All routers have converged.

Final Routing Tables (Shortest Path Costs):
Router 1: [0, 8, 9, 7]
Router 2: [8, 0, 17, 1]
Router 3: [9, 17, 0, 16]
Router 4: [7, 1, 16, 0]
```

## Key Concepts Demonstrated

- Distance Vector Routing
- Bellman-Ford Algorithm
- Routing table exchange
- Iterative convergence
- Network path optimization
