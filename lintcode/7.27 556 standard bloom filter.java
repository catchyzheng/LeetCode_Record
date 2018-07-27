/*
7/27 [556. Standard Bloom Filter](https://www.lintcode.com/problem/standard-bloom-filter/description)<br>
Implement a standard bloom filter. Support the following method:<br>

1 StandardBloomFilter(k),The constructor and you need to create k hash functions.<br>
2 add(string). add a string into bloom filter.<br>
3 contains(string). Check a string whether exists in bloom filter.
解答：需要用到hash，和BitSet这个数据结构，其实很像布尔数组。。当然这道题主要是检查自己是否理解标准布隆过滤器的实现方法.

首先哈希函数需要一个类，而且需要有hash_size和seed，seed用于构造哈希函数。
后面需要一个list存放k个哈希函数对象，以及一个bitset对象，将哈希值对应的下标的元素置为true。
*/

class BloomHash{
    private int hash_size;
    private int seed;
    public BloomHash(int c, int ss){hash_size = c; seed = ss; }
    public int getHash(String s){
        long res = 0;
        for (char c: s.toCharArray()){
            res = (res * seed + c) % hash_size;
        }
        return (int)(res);
    }
}

public class StandardBloomFilter {
    /*
    * @param k: An integer
    */
    private int capacity = 100000;
    private List<BloomHash> hashCollections;
    private BitSet bits = new BitSet(capacity);
    public StandardBloomFilter(int k) {
        hashCollections = new ArrayList<>();
        for(int i=0; i<k; ++i){
            hashCollections.add(new BloomHash(capacity, 2*i + 37));
        }
        bits.clear();
    }

    /*
     * @param word: A string
     * @return: nothing
     */
    public void add(String word) {
        for(BloomHash hash_func: hashCollections){
            bits.set(hash_func.getHash(word), true);
        }
    }

    /*
     * @param word: A string
     * @return: True if contains word
     */
    public boolean contains(String word) {
        for(BloomHash hash_func: hashCollections){
            if(bits.get(hash_func.getHash(word)) == false) return false;
        }
        return true;
    }
}