package jan3.com.vcm;

import java.util.*;

class SharedQueue {
    private Queue<Integer> queue = new LinkedList<>();
    private int capacity = 3;

    public synchronized void produce(int item) throws InterruptedException {
        while (queue.size() == capacity) {
            wait(); // wait if full
        }
        queue.add(item);
        System.out.println("Produced: " + item);
        notify(); // notify consumer
    }

    public synchronized int consume() throws InterruptedException {
        while (queue.isEmpty()) {
            wait(); // wait if empty
        }
        int item = queue.poll();
        System.out.println("Consumed: " + item);
        notify(); // notify producer
        return item;
    }
}
