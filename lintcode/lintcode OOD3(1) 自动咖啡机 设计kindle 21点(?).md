[747. 自动咖啡机](<https://www.lintcode.com/problem/coffee-maker-oo-design/description>)

### 描述

中文English

设计一个自动咖啡机，加入一袋咖啡包，简单地煮一杯咖啡。

- 每个**咖啡包**包含有咖啡的配方，如加入了多少牛奶，或加入了多少糖
- 咖啡机可根据咖啡包提供的配方制作咖啡
- 只考虑**两种**成分成分：**糖（sugar）和牛奶（milk）**
- 普通咖啡的成本是**2元**。 加入一份**牛奶**或**糖**会使成本增加**0.5元**
- 考虑使用**Decorator Design Pattern**

您在真实的面试中是否遇到过这个题？  是

题目纠错

### 样例

输入:

```
pack(2, 3)
makeCoffee()
```

输出:

```
Cost for this coffee is: 4.5
Ingredients for this coffee is: Plain Coffee, Milk, Milk, Sugar, Sugar, Sugar
```

Java. 可以跑通！

```java
public class CoffeeMaker {

    public Coffee makeCoffee(CoffeePack pack) {
		Coffee coffee = new SimpleCoffee();

		for (int i = 0; i < pack.getNeededMilk(); i++) {
			coffee = new WithMilk(coffee);
		}

		for (int i = 0; i < pack.getNeededSugar(); i++) {
			coffee = new WithSugar(coffee);
		}

		return coffee;
	}
}

class CoffeePack {
	private int neededMilk;
	private int neededSugar;

	public CoffeePack(int neededMilk, int neededSugar) {
		this.neededMilk = neededMilk;
		this.neededSugar = neededSugar;
	}

	public int getNeededMilk() {
		return neededMilk;
	}

	public int getNeededSugar() {
		return neededSugar;
	}
}

interface Coffee {
	public double getCost();
	public String getIngredients();
}

class SimpleCoffee implements Coffee {

	@Override
	public double getCost() {
		// TODO Auto-generated method stub
		return 2;
	}

	@Override
	public String getIngredients() {
		// TODO Auto-generated method stub
		return "Plain Coffee";
	}

}

abstract class CoffeeDecorator implements Coffee {
	protected final Coffee decoratedCoffee;

	public CoffeeDecorator(Coffee coffee) {
		this.decoratedCoffee = coffee;
	}

	public double getCost() {
		return decoratedCoffee.getCost();
	}

	public String getIngredients() {
		return decoratedCoffee.getIngredients();
	}
}

class WithMilk extends CoffeeDecorator {

	public WithMilk(Coffee coffee) {
		super(coffee);
	}

	public double getCost() {
		return super.getCost() + 0.5;
	}

	public String getIngredients() {
		return super.getIngredients() + ", Milk";
	}
}

class WithSugar extends CoffeeDecorator {

	public WithSugar(Coffee coffee) {
		super(coffee);
	}

	public double getCost() {
		return super.getCost() + 0.5;
	}

	public String getIngredients() {
		return super.getIngredients() + ", Sugar";
	}
}
```



748

[748. 设计kindle](<https://www.lintcode.com/problem/kindle-oo-design/description>)

### 描述

设计一个可以打开三种文件格式的Kindle，文件格式分别为：`PDF`, `MOBI` , `EPUB`。

- 尝试使用 ENUM 处理文件格式。
- 尝试使用 simple factory 设计模式为每种格式创建用户。

### 样例

输入:

```
readBook("EPUB")
readBook("PDF")
readBook("MOBI")
```

输出:

```
Using EPUB reader, book content is: epub
Using PDF reader, book content is: pdf
Using MOBI reader, book content is: mobi
```



java

```java
import java.util.ArrayList;
import java.util.List;

public class Kindle {
    private List<Book> books;
	private EBookReaderFactory readerFactory;

	public Kindle() {
		books = new ArrayList<>();
		readerFactory = new EBookReaderFactory();
	}

	public String readBook(Book book) throws Exception {
		EBookReader reader = readerFactory.createReader(book);
		if (reader == null) {
			throw new Exception("Can't read this format");
		}
		return reader.displayReaderType() + ", book content is: " + reader.readBook();
	}

	public void downloadBook(Book b) {
		books.add(b);
	}

	public void uploadBook(Book b) {
		books.add(b);
	}

	public void deleteBook(Book b) {
		books.remove(b);
	}
}

enum Format {
	EPUB("epub"), PDF("pdf"), MOBI("mobi");

	private String content;

	Format(String content) {
		this.content = content;
	}

	public String getContent() {
		return content;
	}
}

class Book {
	private Format format;

	public Book(Format format) {
		this.format = format;
	}

	public Format getFormat() {
		return format;
	}
}

abstract class EBookReader {
	
	protected Book book;
	
	public EBookReader(Book b){
		this.book = b;
	}
	
	public abstract String readBook();
	public abstract String displayReaderType();
}

class EBookReaderFactory {

	public EBookReader createReader(Book b) {
		if (b.getFormat() == Format.EPUB) {
			return new EpubReader(b);
		} else if (b.getFormat() == Format.MOBI) {
			return new MobiReader(b);
		} else if (b.getFormat() == Format.PDF) {
			return new PdfReader(b);
		} else
			return null;
	}
}

class EpubReader extends EBookReader{

	public EpubReader(Book b) {
		super(b);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String readBook() {
		// TODO Auto-generated method stub
		return book.getFormat().getContent();
	}

	@Override
	public String displayReaderType() {
		// TODO Auto-generated method stub
		return "Using EPUB reader";
	}
}

class MobiReader extends EBookReader {

	public MobiReader(Book b) {
		super(b);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String readBook() {
		// TODO Auto-generated method stub
		return book.getFormat().getContent();
	}

	@Override
	public String displayReaderType() {
		// TODO Auto-generated method stub
		return "Using MOBI reader";
	}

}
class PdfReader extends EBookReader{

	public PdfReader(Book b) {
		super(b);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String readBook() {
		// TODO Auto-generated method stub
		return book.getFormat().getContent();
	}

	@Override
	public String displayReaderType() {
		// TODO Auto-generated method stub
		return "Using PDF reader";
	}
}
```















[714. 二十一点 ](<https://www.lintcode.com/problem/black-jack-oo-design/description>)

### 描述

- 每位玩家起始有`1000`筹码
- 庄家有`10000`筹码
- 如果玩家获胜，双倍获得押注的筹码
- 庄家获胜，玩家押注的筹码归庄家
- 点数相同，庄家获胜
- A 可当做 `1` 或 `11`

### 样例

```
Player(10)
Player(100)
Player(500)
Card([1,4,2,3,1,4,2,3,9,10])
InitialCards()
compareResult()
```

输出:

```
playerid: 1 ;Cards: 1 , 1; Current best value is: 12, current bets: 10, total bets: 990
playerid: 2 ;Cards: 4 , 4; Current best value is: 8, current bets: 100, total bets: 900
playerid: 3 ;Cards: 2 , 2; Current best value is: 4, current bets: 500, total bets: 500
Dealer Cards: 3 , 3; Current best value is: 6, total bets: 10000
playerid: 1 ;Cards: 1 , 1; Current best value is: 12, current bets: 0, total bets: 1010
playerid: 2 ;Cards: 4 , 4; Current best value is: 8, current bets: 0, total bets: 1100
playerid: 3 ;Cards: 2 , 2; Current best value is: 4, current bets: 0, total bets: 500
Dealer Cards: 3 , 3; Current best value is: 6, total bets: 10390
```

Java (不能跑通。。看思路吧)

```java
public class BlackJack {
    private List<NormalPlayer> players;
	private Dealer dealer;

	private List<Card> cards;

	public BlackJack() {
		players = new ArrayList<>();
		dealer = new Dealer();
	}

	public void initCards(List<Card> cards) {
		this.cards = cards;
	}

	public void addPlayer(NormalPlayer p) {
		players.add(p);
	}


	public void dealInitialCards() {
		for (NormalPlayer player : players) {
			player.insertCard(dealNextCard());
		}

		dealer.insertCard(dealNextCard());

		for (NormalPlayer player : players) {
			player.insertCard(dealNextCard());
		}

		dealer.insertCard(dealNextCard());
	}

	public Card dealNextCard() {
		Card card = cards.remove(0);
		return card;
	}

	public Dealer getDealer() {
		return dealer;
	}

	public void compareResult() {
		for (NormalPlayer p : players) {
			if (dealer.largerThan(p)) {
				dealer.updateBets(p.getCurrentBets());
				p.lose();
			} else {
				dealer.updateBets(-p.getCurrentBets());
				p.win();
			}
		}
	}

	public String print() {
		String s = "";
		for (NormalPlayer player : players) {
			s += "playerid: " + (player.getId() + 1) + " ;" + player.printPlayer();
		}
		return s;
	}
}


class NormalPlayer {
	private BlackJack game;
	private int id;
	private Hand hand;
	private int totalBets;
	private int bets;
	private boolean stopDealing;

	public NormalPlayer(int id, int bets) {
		this.id = id;
		hand = new Hand();
		totalBets = 1000;
		try{
		    placeBets(bets);
		}catch(Exception e){
		    e.printStackTrace();
		}
		stopDealing = false;
	}

	public int getId() {
		return this.id;
	}

	public void insertCard(Card card) {
		hand.insertCard(card);
	}

	public int getBestValue() {
		return hand.getBestValue();
	}

	public void stopDealing() {
		stopDealing = true;
	}

	public void joinGame(BlackJack game) {
		this.game = game;
		game.addPlayer(this);
	}

	public void dealNextCard() {
		insertCard(game.dealNextCard());
	}

	public void placeBets(int amount) throws Exception {
		if (totalBets < amount) {
			throw new Exception("No enough money.");
		}
		bets = amount;
		totalBets -= bets;
	}

	public int getCurrentBets() {
		return bets;
	}

	public String printPlayer() {
		return hand.printHand() + ", current bets: " + bets + ", total bets: " + totalBets + "\n";
	}

	public void win() {
		totalBets += (bets * 2);
		bets = 0;
	}

	public void lose() {
		bets = 0;
	}
}


class Hand {
	private List<Card> cards;

	public Hand() {
		cards = new ArrayList<>();
	}

	// Get a list of possible results from hand
	private List<Integer> getPossibleValues() {
		List<Integer> results = new ArrayList<>();

		int aceCount = 0;
		int resultWithoutAce = 0;
		for (Card card : cards) {
			if (card.getValue() == 1) {
				aceCount++;
			} else if (card.getValue() == 11 || card.getValue() == 12 || card.getValue() == 13) {
				resultWithoutAce += 10;
			} else
				resultWithoutAce += card.getValue();
		}

		for (int i = 0; i <= aceCount; i++) {
			int ones = i;
			int elevens = aceCount - i;

			results.add(resultWithoutAce + ones + elevens * 11);
		}

		return results;
	}

	// -1 means went over 21, otherwise means the best value of this hand
	public int getBestValue() {
		List<Integer> results = getPossibleValues();

		int maxUnder = -1;
		for (int result : results) {
			if (result <= 21 && result > maxUnder) {
				maxUnder = result;
			}
		}
		return maxUnder;
	}

	public void insertCard(Card card) {
		cards.add(card);
	}

	public String printHand() {
		String res = "Cards: ";
		for (int i = 0; i < cards.size(); i++){
			res += (cards.get(i).getValue());
			if(i != cards.size() - 1){
				res+=" , ";
			}
			else res+=';';
		}

		res += " Current best value is: " + getBestValue();
		return res;
	}
}


class Card {
	private int value;

	public Card(int value) {
		this.value = value;
	}

	public int getValue() {
		return value;
	}
}


class Dealer {
	private BlackJack game;
	private Hand hand;
	private int bets;

	public Dealer() {
		hand = new Hand();
		bets = 10000;
	}

	public void insertCard(Card card) {
		hand.insertCard(card);
	}

	public boolean largerThan(NormalPlayer p) {
		return hand.getBestValue() >= p.getBestValue();
	}

	public void updateBets(int amount) {
		bets += amount;
	}

	public void setGame(BlackJack game) {
		this.game = game;
	}

	public void dealNextCard() {
		insertCard(game.dealNextCard());
	}

	public String printDealer() {
		return "Dealer " + hand.printHand() + ", total bets: " + bets + "\n";
	}
}
```

c++

```

```



