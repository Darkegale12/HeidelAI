# Producer–Consumer Pattern using Wait/Notify (Java)

## Overview
- This project implements the classic Producer–Consumer problem using Java threads.
- It demonstrates thread synchronization and inter-thread communication using `wait()` and `notify()`.
- The solution is written in a modular manner for clarity and easy understanding.

---

## Problem Statement
- A Producer thread reads data from a source container and puts items into a shared queue.
- A Consumer thread reads data from the shared queue and stores items into a destination container.
- The shared queue has a fixed capacity.
- Producer waits if the queue is full.
- Consumer waits if the queue is empty.

---
```
 Project Structure
src/
└── jan3/com/vcm
         ├── SharedQueue.java
         ├── Producer.java
         ├── Consumer.java
         └── ProducerConsumerWaitNotify.java
```


## Class Responsibilities

### SharedQueue.java
- Acts as the shared bounded buffer between producer and consumer.
- Handles all synchronization logic using `synchronized`, `wait()`, and `notify()`.
- Blocks producer when the queue is full.
- Blocks consumer when the queue is empty.

---

### Producer.java
- Implements `Runnable`.
- Reads items from the source container.
- Produces items into the shared queue.
- Sends a termination signal (`-1`) after all items are produced.

---

### Consumer.java
- Implements `Runnable`.
- Consumes items from the shared queue.
- Stores consumed items into the destination container.
- Stops execution when the termination signal (`-1`) is received.

---

### ProducerConsumerWaitNotify.java
- Contains the `main()` method.
- Initializes source and destination containers.
- Creates the shared queue.
- Starts producer and consumer threads.

---

## How the Program Works
1. The Producer and Consumer threads start concurrently.
2. The Producer adds items from the source list into the shared queue.
3. If the queue is full, the Producer waits.
4. The Consumer removes items from the shared queue and stores them in the destination list.
5. If the queue is empty, the Consumer waits.
6. After producing all items, the Producer sends a termination signal.
7. The Consumer receives the signal, stops execution, and the program ends safely.
