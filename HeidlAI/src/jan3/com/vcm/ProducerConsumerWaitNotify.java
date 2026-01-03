package jan3.com.vcm;

import java.util.*;

public class ProducerConsumerWaitNotify {
    public static void main(String[] args) {
        List<Integer> source = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> destination = new ArrayList<>();

        SharedQueue sharedQueue = new SharedQueue();

        Thread producer = new Thread(new Producer(sharedQueue, source));
        Thread consumer = new Thread(new Consumer(sharedQueue, destination));

        producer.start();
        consumer.start();
    }
}
