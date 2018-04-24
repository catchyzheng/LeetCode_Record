[160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)<br>
找到两个链表的交叉处。惊为天人的双指针法！
但实现细节要注意，也就是什么时候改变指针指向的位置。
```
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
	if( null==headA || null==headB )
		return null;
	ListNode curA = headA, curB = headB;
	while( curA!=curB){
		curA = curA==null?headB:curA.next;
		curB = curB==null?headA:curB.next;
	}
	return curA;
}
```
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)<br>
实现链表的加法。相同的思路，但别人有更简洁的代码。
```
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode c1 = l1;
    ListNode c2 = l2;
    ListNode sentinel = new ListNode(0);
    ListNode d = sentinel;
    int sum = 0;
    while (c1 != null || c2 != null) {
        sum /= 10;
        if (c1 != null) {
            sum += c1.val;
            c1 = c1.next;
        }
        if (c2 != null) {
            sum += c2.val;
            c2 = c2.next;
        }
        d.next = new ListNode(sum % 10);
        d = d.next;
    }
    if (sum / 10 == 1)
        d.next = new ListNode(1);
    return sentinel.next;
}
```

[83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)<br>
将链表中所有重复的移除。自己做出来的第一道链表题。。
```
public ListNode deleteDuplicates(ListNode head) {
    ListNode n = head;
    if(n==null || n.next==null) return n;
    while(n!=null){//这里的判断很关键。防止[1,1,1]指针溢出。
        while(n.next!=null && n.val==n.next.val) {
            n.next=n.next.next; 
        }
        n=n.next;
    }
    return head;
}
```

[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)<br>
(self done)原址合并。iteratively。
```
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    if(l1==null && l2==null) return null;
    if(l1==null) return l2; if(l2==null) return l1;
    ListNode start = new ListNode(0);
    ListNode ans=start;
    while(l1!=null || l2!=null){
        if(l1==null){start.next=l2;l2=l2.next; }
        else if(l2==null){start.next=l1;l1=l1.next;}
        else{
            if(l1.val<=l2.val){
                start.next=l1; l1=l1.next;
            }
            else {start.next=l2; l2=l2.next; }
        }
        start=start.next;
    }
    return ans.next;
}
```
(不是自己做的)合并两个链表。类似归并排序。 但可以是原址的。in-place.
```
//recursively
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    if(l1 == NULL) return l2;
    if(l2 == NULL) return l1;
    // ListNode mergehead;
    if(l1->val < l2->val) {
        //mergehead = l1;//nextline: mergehead->next = ...
		l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    } else {
		//mergehead = l2;
        l2->next = mergeTwoLists(l2->next, l1);
        return l2;
    }
	//return mergehead;
}
//iteratively
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    ListNode dummy(INT_MIN);
    ListNode *tail = &dummy;
    while (l1 && l2) {
        if (l1->val < l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy.next;
}
```


[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)<br>
三种解法。。iterative，recursive，以及用栈。然而我哪个都不会打。。
```
public ListNode reverseList(ListNode head) {
    /* iterative solution */
    ListNode newHead = null;
    while (head != null) {
        ListNode pnext = head.next;
        head.next = newHead;
        newHead = head;
        head = pnext;
    }
    return newHead;
}
//
public ListNode reverseList(ListNode head) {
    /* recursive solution */
    return reverseListInt(head, null);
}
//
private ListNode reverseListInt(ListNode head, ListNode newHead) {
    if (head == null)
        return newHead;
    ListNode pnext = head.next;
    head.next = newHead;
    return reverseListInt(pnext, head);
}
```
另一个标准解答。。
```
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
下面这个递归没看懂。。
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
```

[237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)<br>
删除一个给定的节点。不给出链表。
这是一个很巧妙的题！我们可以将本节点a的值设为a.next的值，然后再a.next=a.next.next。这样就间接等于删掉了a节点。
```
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
		node.next = node.next.next; return;
    }
}
```