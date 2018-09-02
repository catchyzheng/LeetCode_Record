8/31 复习

7/30 [549. 最常使用的k个单词(Map Reduce) ](https://www.lintcode.com/problem/top-k-frequent-words-map-reduce/description)<br>

用分布式实现topK。

```java
/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */
class Pair {
    String key;
    int num;
    public Pair(String key, int num) {
        this.key = key;
        this.num = num;
    }
}
public class TopKFrequentWords {
    
    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            StringTokenizer st = new StringTokenizer(value.content);
            while (st.hasMoreTokens()) {
                String word = st.nextToken();
                output.collect(word, 1);
            }
        }
    }
    
    public static class Reduce {
        Queue<Pair> queue = null;
        int size;
        private Comparator<Pair> pairComparator = new Comparator<Pair>() {
            public int compare(Pair left, Pair right) {
                if (left.num != right.num) {
                    return left.num - right.num;
                }
                return right.key.compareTo(left.key);
            }
        };
        public void setup(int k) {
            // initialize your data structure here
            this.size = k;
            queue = new PriorityQueue<Pair>(size, pairComparator);
        }   
    
        public void reduce(String key, Iterator<Integer> values) {
            // Write your code here
            int sum = 0;
            while (values.hasNext()) {
                sum += values.next();
            }
            Pair cur = new Pair(key, sum);
            if (queue.size() < size) {
                queue.offer(cur);
            } else {
                Pair top = queue.peek();
                if (pairComparator.compare(cur, top) > 0) {
                    queue.poll();
                    queue.offer(cur);
                }
            }
        }
    
        public void cleanup(OutputCollector<String, Integer> output) {
            // Output the top k pairs <word, times> into output buffer.
            // Ps. output.collect(String key, Integer value);
            List<Pair> res = new ArrayList<Pair>();
            while (!queue.isEmpty()) {
                res.add(queue.poll());
            }
            for (int i = res.size() - 1; i >= 0; i--) {
                Pair tmp = res.get(i);
                output.collect(tmp.key, tmp.num);
            }
        }
    }
}
```



7/30 [504. 倒排索引](https://www.lintcode.com/problem/inverted-index-map-reduce/description)<br>

输入：

[{"id":1,"content":"This is the content of document1"}, {"id":2,"content":"This is the       content content of document2"}]

正确输出：

{"This":[1,2],"content":[1,2],"document1":[1],"document2":[2],"is":[1,2],"of":[1,2],"the":[1,2]}

**有几个坑人之处**：1 间隔可以多个空格 2 同一句话出现相同单词只能算一次。

```java
/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */
public class InvertedIndex {
    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            Set<String> set = new HashSet<>();
            StringTokenizer st = new StringTokenizer(value.content);
            // 记住tokenizer的写法，可以处理多个空格。。
            while (st.hasMoreTokens()) {
                String word = st.nextToken();
                if(!set.contains(word)) {
                    output.collect(word, value.id); 
                    set.add(word);
                }
            }
        }
    }
    public static class Reduce {
        public void reduce(String key, Iterator<Integer> values,
                           OutputCollector<String, List<Integer>> output) {
            List<Integer> res = new ArrayList<>();
            while(values.hasNext()){
                res.add(values.next());
            }
            output.collect(key, res);
        }
    }
}
```



7/30 [554. 排序(Map Reduce) ](https://www.lintcode.com/problem/sort-integers-map-reduce/description)<br>

样例输入：

1: [14,7,9] 2: [10,1] 3: [2,5,6,3] 4: []

输出：

[1,2,3,5,6,7,9,10,14]

```java
/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 */
public class SortIntegers {

    public static class Map {
        public void map(int _, List<Integer> value,
                        OutputCollector<String, List<Integer>> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, List<Integer> value);
            output.collect("1", value);
        }
    }
        
    public static class Reduce {
        public void reduce(String key, List<List<Integer>> values,
                           OutputCollector<String, List<Integer>> output) {
            List<Integer> res = new ArrayList<>();
            /*
            int row = values.size();
            int [] index = new int[row];
            int smallest = values.get(0).get(index[0]);
            for(int in: index){
                
            }*/
            for(List<Integer> value: values){
                res.addAll(value);
            }
            Collections.sort(res);
            output.collect(key, res);
        }
    }
}
```

