package jan3.com.vcm;
import java.util.*;
class Consumer implements Runnable {
    private SharedQueue sharedQueue;
    private List<Integer> destination;

    public Consumer(SharedQueue sharedQueue, List<Integer> destination) {
        this.sharedQueue = sharedQueue;
        this.destination = destination;
    }

    @Override
    public void run() {
        try {
            while (true) {
                int item = sharedQueue.consume();
                if (item == -1) break;
                destination.add(item);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}