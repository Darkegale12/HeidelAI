package jan3.com.vcm;
import java.util.*;
class Producer implements Runnable {
    private SharedQueue sharedQueue;
    private List<Integer> source;

    public Producer(SharedQueue sharedQueue, List<Integer> source) {
        this.sharedQueue = sharedQueue;
        this.source = source;
    }

    @Override
    public void run() {
        try {
            for (int item : source) {
                sharedQueue.produce(item);
                Thread.sleep(500);
            }
            sharedQueue.produce(-1); // termination signal
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}