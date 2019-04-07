

[222. Getter与Setter](<https://www.lintcode.com/problem/setter-and-getter/description>) 入门

实现一个`School`的类，包含下面的这些属性和方法:

- 一个string类型的私有成员`name`.
- 一个setter方法`setName`，包含一个参数name.
- 一个getter方法`getName`，返回该对象的name。

### 样例

```
Java:
    School school = new School();
    school.setName("MIT");
    school.getName(); // 返回 "MIT" 作为结果 

Python:
    school = School();
    school.setName("MIT")
    school.getName() # 返回 "MIT" 作为结果 
```

```java
/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

public class School {
    /*
     * Declare a private attribute *name* of type string.
     */
    private String name;
    
    /**
     * Declare a setter method `setName` which expect a parameter *name*.
     */
    public void setName(String name) {
        this.name = name;
    }
    
    /**
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
     */
    public String getName() {
        return this.name;
    }
}
```



[456. 引用](<https://www.lintcode.com/problem/reference/description>) 入门

实现一个类 *ReferenceManager* 包含如下两种方法

1.`copyValue(Node obj)` 只拷贝参数*obj*的权值，*obj*和*node*仍然是两个指针

2.`copyReference(Node obj)` *obj*和*node*指向同一个地方

```java
/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

public class ReferenceManager {
    public Node node;

    public void copyValue(Node obj) {
        if (obj == null) {
            return;
        }
        if (node == null) {
            node = new Node(obj.val);
        }
        node.val = obj.val;
    }

    public void copyReference(Node obj) {
        node = obj;
    }
}
```





8/31 review 

8/1 [560. Friendship Service](https://www.lintcode.com/problem/friendship-service/description) 简单

实现好友服务，支持 follow & unfollow, getFollowers, getFollowings方法 。竟然是简单版。example如下：

其实思路就是，维护两个map<int, Set<int>>， 分别存放一个人关注了什么人以及一个人被什么人关注。

```
follow(1, 3)
getFollowers(1) // return [3]
getFollowings(3) // return [1]
follow(2, 3)
getFollowings(3) // return [1,2]
unfollow(1, 3)
getFollowings(3) // return [2]
```

TreeSet用得好。

```java
public class FriendshipService { 

	private Map<Integer, Set<Integer>> followers, followings;

	public FriendshipService() {
		// initialize your data structure here.
		this.followers = new HashMap<Integer, Set<Integer>>();
		this.followings = new HashMap<Integer, Set<Integer>>();
	}

	// @param user_id an integer
	// return all followers and sort by user_id
	public List<Integer> getFollowers(int user_id) {
		if (!followers.containsKey(user_id))
			return new ArrayList<Integer>();

		return new ArrayList<Integer>(followers.get(user_id));
	}

	// @param user_id an integer
	// return all followings and sort by user_id
	public List<Integer>  getFollowings(int user_id) {
		if (!followings.containsKey(user_id))
			return new ArrayList<Integer>();

		return new ArrayList<Integer>(followings.get(user_id));
	}

	// @param from_user_id an integer
	// @param to_user_id an integer
	// from user_id follows to_user_id
	public void follow(int from_user_id, int to_user_id) {
		if (!followers.containsKey(from_user_id))
			followers.put(from_user_id, new TreeSet<Integer>());

		followers.get(from_user_id).add(to_user_id);

		if (!followings.containsKey(to_user_id))
			followings.put(to_user_id, new TreeSet<Integer>());

		followings.get(to_user_id).add(from_user_id);
	}

	// @param from_user_id an integer
	// @param to_user_id an integer
	// from user_id unfollows to_user_id
	public void unfollow(int from_user_id, int to_user_id) {
		if (followers.containsKey(from_user_id))
			followers.get(from_user_id).remove(to_user_id);

		if (followings.containsKey(to_user_id))
			followings.get(to_user_id).remove(from_user_id);
	}
}
```

```python
class FriendshipService:

    def __init__(self):
        # initialize your data structure here.
        self.followers = dict()
        self.followings = dict()

        
    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowers(self, user_id):
        # Write your code here
        if user_id not in self.followers:
            return []
        results = list(self.followers[user_id])
        results.sort()
        return results

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowings(self, user_id):
        # Write your code here
        if user_id not in self.followings:
            return []
        results = list(self.followings[user_id])
        results.sort()
        return results
        
    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id follows to_user_id
    def follow(self, to_user_id, from_user_id):
        # Write your code here
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        self.followers[to_user_id].add(from_user_id)

        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followings[from_user_id].add(to_user_id)

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id unfollows to_user_id
    def unfollow(self, to_user_id, from_user_id):
        # Write your code here
        if to_user_id in self.followers:
            if from_user_id in self.followers[to_user_id]:
                self.followers[to_user_id].remove(from_user_id)

        if from_user_id in self.followings:
            if to_user_id in self.followings[from_user_id]:
                self.followings[from_user_id].remove(to_user_id)
```





8/1 [Shape Factory](<https://www.lintcode.com/problem/shape-factory/description>) 简单

工厂模式是一种常见的设计模式。实现一个形状工厂 `ShapeFactory` 来创建不同的形状类。这里我们假设只有三角形，正方形和矩形三种形状。

Example:

```java
ShapeFactory sf = new ShapeFactory();
Shape shape = sf.getShape("Square");
shape.draw();
 ----
|    |
|    |
 ----
shape = sf.getShape("Triangle");
shape.draw();
   /\
  /  \
 /____\
shape = sf.getShape("Rectangle");
shape.draw();
  ----
 |    |
  ----
```

注意equalsIgnoreCase，这什么鬼。。另外，注意末尾的空格和\的转义。

[完整解答在此。](https://segmentfault.com/a/1190000004970575#articleHeader2)<br>

这道题考了interface & implementation & override，具体概念如下：

**Interface**: A Java interface is a bit like a class, except that it can only contain method signatures and fields, which is saying that it cannot contain any implementation of the methods. You can use interface to achieve polymorphism.

**Implementation**: To declare a class that implements an interface, you have to include an `implements` clause in the class definition. Your class can implement more than one interface.

**Overriding**: If subclass provides the specific/close implementation of the method that has been provided by one of its parent class, it is known as method overriding.

除此之外，还需要注意正则表达式的写法。

```java
/**
 * Your object will be instantiated and called as such:
 * ShapeFactory sf = new ShapeFactory();
 * Shape shape = sf.getShape(shapeType);
 * shape.draw();
 */
interface Shape {
    void draw();
}

class Rectangle implements Shape {
    public void draw(){
        System.out.println(" ---- ");
        System.out.println("|    |");
        System.out.println(" ----");
        return;
    }
}

class Square implements Shape {
    // Write your code here
    public void draw(){
        System.out.println(" ---- "); 
        System.out.println("|    |");
        System.out.println("|    |");
        System.out.println(" ----");
        return;
    }
}

class Triangle implements Shape {
    // Write your code here
    public void draw(){
        System.out.println("  /\\"); 
        System.out.println(" /  \\");
        System.out.println("/____\\");
        return;
    }
}

public class ShapeFactory {
    /**
     * @param shapeType a string
     * @return Get object of type Shape
     */
    public Shape getShape(String shapeType) {
        // Write your code here
        if(shapeType.equalsIgnoreCase("Square")){
            return new Square();
        }
        else if(shapeType.equalsIgnoreCase("Rectangle")){
            return new Rectangle();
        }
        else if(shapeType.equalsIgnoreCase("Triangle")){
            return new Triangle();
        }
        else return null;
    }
}
```

 ```python
"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print "  /\\"
        print " /  \\"
        print "/____\\"

class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print " ----"
        print "|    |"
        print " ----"

class Square(Shape):
    # Write your code here
    def draw(self):
        print " ----"
        print "|    |"
        print "|    |"
        print " ----"

class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == "Triangle":
            return Triangle()
        elif shapeType == "Rectangle":
            return Rectangle()
        elif shapeType == "Square":
            return Square()
        else:
            return None
 ```





**单例**

**单例** 是最为最常见的设计模式之一。对于任何时刻，如果某个类只存在且最多存在一个具体的实例，那么我们称这种设计模式为单例。例如，对于 class Mouse (不是动物的mouse哦)，我们应将其设计为 singleton 模式。

你的任务是设计一个 `getInstance` 方法，对于给定的类，每次调用 `getInstance` 时，都可得到同一个实例。

### 样例

```
在 Java 中:

	A a = A.getInstance();
	A b = A.getInstance();

a 应等于 b.
```

```java
class Solution {
    /**
     * @return: The same instance of this class every time
     */
    public static Solution instance = new Solution();
    public static Solution getInstance() {
        // write your code here
        return instance;
    }
};
```



[208. 赋值运算符重载](https://www.lintcode.com/problem/assignment-operator-overloading-c-only/description) 

实现赋值运算符重载函数，确保：

- 新的数据可准确地被复制
- 旧的数据可准确地删除/释放
- 可进行 `A = B = C` 赋值

### 说明

本题只适用于`C++`，因为 *Java* 和 *Python* 没有对赋值运算符的重载机制。

### 样例

如果进行 `A = B` 赋值，则 A 中的数据被删除，取而代之的是 B 中的数据。

如果进行 `A = B = C` 赋值，则 A 和 B 都复制了 C 中的数据。

### 挑战

充分考虑安全问题，并注意释放旧数据。

```c++
/**
* This reference program is provided by @jiuzhang.com
* Copyright is reserved. Please indicate the source for forwarding
*/

class Solution {
public:
    char *m_pData;
    Solution() {
        this->m_pData = NULL;
    }
    Solution(char *pData) {
        if (pData) {
            m_pData = new char[strlen(pData) + 1];
            strcpy(m_pData, pData);
        } else {
            m_pData = NULL;
        }
    }

    // Implement an assignment operator
    Solution operator=(const Solution &object) {
        if (this == &object) {
            return *this;
        }
        
        if (object.m_pData) {
            char *temp = m_pData;
            try {
                m_pData = new char[strlen(object.m_pData)+1];
                strcpy(m_pData, object.m_pData);
                if (temp)
                    delete[] temp;
            } catch (bad_alloc& e) {
                m_pData = temp;
            }
        } else {
            m_pData = NULL;
        }
        return *this;
    }
};
```



