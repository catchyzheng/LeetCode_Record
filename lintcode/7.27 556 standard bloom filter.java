/*
7/27 [556. Standard Bloom Filter](https://www.lintcode.com/problem/standard-bloom-filter/description)<br>
Implement a standard bloom filter. Support the following method:<br>

1 StandardBloomFilter(k),The constructor and you need to create k hash functions.<br>
2 add(string). add a string into bloom filter.<br>
3 contains(string). Check a string whether exists in bloom filter.
�����Ҫ�õ�hash����BitSet������ݽṹ����ʵ���񲼶����顣����Ȼ�������Ҫ�Ǽ���Լ��Ƿ�����׼��¡��������ʵ�ַ���.

���ȹ�ϣ������Ҫһ���࣬������Ҫ��hash_size��seed��seed���ڹ����ϣ������
������Ҫһ��list���k����ϣ���������Լ�һ��bitset���󣬽���ϣֵ��Ӧ���±��Ԫ����Ϊtrue��
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