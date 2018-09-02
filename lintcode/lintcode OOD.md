8/31 review 

8/1 [560. Friendship Service](https://www.lintcode.com/problem/friendship-service/description)<br>

实现好友服务。竟然是简单版。example如下：

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





8/1 [Shape Factory]()<br>

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