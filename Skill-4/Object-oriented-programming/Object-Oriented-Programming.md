# Object-Oriented Programming

## Introduction

00:00:00
Hey, guys, and welcome back to another skill in Python from Network Engineers. So this skill is a really, really important topic. Remember how we cover something called Functional Programming pretty recently? Now within this skill, we also drew a reference to something called OOP, this is Object-Oriented programming.

00:00:32
And it's Object-Oriented programming that we are going to be focusing on in the skill right here. So the key thing here to focus on is this concept of objects. Now, the central focus of this skill is going to be how we actually create particular objects.

00:00:46
And we are going to be using something called classes. And we'll talk about classes in a little bit more detail in the very next Nugget. But for now, I want you to grapple with the idea of what an object actually is. So if I had to ask you to conceptualize a human being, a person, as an object within Python, now there are two distinct things that we're really going to focus on about this object.

00:01:10
The first thing is, what are the properties that actually belong to this object? And the other thing is what the person actually does. So what on Earth do I mean here with properties and what they do? So think about properties of a human being. Things that might be a property could be their name.

00:01:29
You could also have their date of birth, or things like, what are the color of their eyes? And also, let's see, height, this could also be another property of a human being. So these are properties with respect to what they actually do. Well, what are some of the things that human beings actually do?

00:01:47
Well, they walk, they also speak. They sometimes run, if you're feeling pretty fit. Hopefully, you laugh. And from time to time, you sneeze. So there obviously are a lot more things that human beings do, but let's just leave it at that just now. So this concept of properties, data about the human being, that is going to be known in the object world as attributes.

00:02:07
And what they actually do, these are going to be known as methods. And these are two huge concepts that we're going to be covering throughout this skill. Now an important thing to note here is that sometimes a method is going to have to have access to the actual attributes.

00:02:24
So say, for example, if a person wanted to see-- what they mostly wanted to use is the speak method, well, they would have to have access to the name property of that human so they could see their own name. This is the link up play between these methods and attributes.

00:02:39
And throughout this skill, we're going to be learning all about these features. So we're going to have to look at classes, how we create them. We're going to have to look at the different types of attributes that we can have. And we'll come to learn that you can have an instance attribute, as well as a class attribute.

00:02:55
Now, these won't make any sense right now, but hopefully as you go through this, this is going to become much, much clearer. Also, actually, on how we can create these attributes and how we can also create our own methods. And not just this, we're also going to be looking at something called Magic Methods.

00:03:12
Now, this sounds pretty mysterious. What on Earth is a magic method? But we'll definitely be getting into that later on within this skill. But they're sometimes known as Dunder methods, and if I can spell "Dunder" correctly. So these are some of the things which you have lined up for this skill.

00:03:26
It's going to be really, really good. But what I will see is that Object-Oriented programming, people often find the concept a little difficult to digest upon first exposure. What I'm pretty much saying to you is that this is a very, very common place where people do get kind of caught up and a little bit confused.

00:03:44
And the solution is, like so many things, is just repetition. Go back over the skill, continually keep working with classes, and then you're going to get to that point where it just clicks, and everything begins to sync in and make sense. Because in my experience, this is one of these topics where so many programmers really do find it a little bit of a hurdle.

00:04:04
So if you find that also, too, then definitely don't be discouraged. It's perfectly normal. The key is is just to keep hammering away at it. So that is what we've got lined up for this skill. The very first thing we're going to be digging into are those Python classes.

00:04:17
Let's check that out in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Classes

00:00:00
Hey guys and welcome back. So let's now talk about classes within Python here. Now ultimately, what a class does within Python, it defines a type. Remember when you use your type function within Python you can say type and then maybe put in an integer that will return back, but the type of this happens to be an int.

00:00:30
Well, int is a type within Python as is a string. A string is also a type within Python. And by using Python classes, we can create our own types. We can create a type for say, a person, or a type for a musician, or a type for a vehicle. Pretty much any type you want to be able to create, you can create within Python using classes.

00:00:51
Now although it may already not quite feel like it, you have actually been using classes all throughout this course already. We have built-in classes within Python. So let me just quickly demonstrate what I mean here. We go into Python-Net-Eng, go into our virtual environment, let's activate it.

00:01:08
Go back out, and we'll create a directory just called class-stuff and go in there, clear the screen, and we'll jump into IPython. So let's just go through the process of creating a variable. So I'll just call the variable my_var. Call it anything you like.

00:01:23
And what I'm going to do is make that equal to the value john. So let's hit Enter. Now what has actually happened here is that this variable, this one here is referencing an object. And as we know, that object has a type. Now in this case here, because I've used quotation marks, this is going to be str for string.

00:01:45
Now how on Earth was this created? How do we create this object here with this particular type? Well like I say, what is happening here is that Python is using a built-in class. And one of the built-in classes is the str class. And in fact, just by specifying this value here within quotation marks, Python under the hood has invoked this built-in class, this str class.

00:02:08
So now, we have this new object called my_var as we see here. And it does have a type, its type is str. See that? So because this is a built-in class, we don't actually have to do anything particular here, its all kind of done automagically. Whereas when we want to create a custom type, we have to be much more explicit.

00:02:28
So how on Earth do we go about creating these custom types with our classes? Well, one of the quick ways to check this out is again, I always recommend going to the Python documentation. Its very comprehensive, and it's very well-written. So if you just search for Python classes and click this top link here, it's going to take you to the documentation right here.

00:02:46
And I certainly would recommend that you read through this page as a supplement to what you see here throughout this skill. And it kind of tells us here the broad overview. Says that classes provides a means of building data and functionality together.

00:03:00
And as we see here, that creating a new class creates a new type. This is exactly what I'm talking about. And it's a new type of object. And it's going to allow new instances of that type to be made. But that might sound a little bit confusing, but hopefully we'll clear this up.

00:03:16
Now if we just scroll on down a little bit here, you're actually going to get to see what the syntax does in fact actually look like. So section 9.3 gives us a first look at classes, and this shows us the syntax we're going to see here. And pretty much the simple definition that they actually give us is this example here.

00:03:34
Basically, we're going to use this keyword here, class, which is going to create a new class, and then we specify our class name. And then indented within, we're going to specify all the things we want to do to associate towards that particular class.

00:03:49
This is where we can specify what our attributes are, as well as the particular methods that we want to associate with this class. So let's jump back to IPython and use what we've just learned here then. So let's close this down. OK, so let's clear this screen here, and we will create a class for a person.

00:04:07
So what we'll do here is use this keyword class, and we can see here that it goes green because this is a known keyword within Python. And now we're going to specify the name of the class you want to create, so we'll just say Dog. Now notice here that I happen to use a capital letter here for Dog.

00:04:23
This is not actually imposed by Python, but it is a convention to use uppercase letters as well as when you're separating out words, capitalization is really quite an important standard within classes. So if I created a class called MyPerson we would say it like this, capitalization.

00:04:39
So we'll see here, class is Person. Now we can pass in arguments, but we don't have to. Right now, I'm just going to say parentheses, and then I'll do my colon, and then hit Enter. And now indented within, I can specify these attributes, as well as the methods I want to associate with this person.

00:04:57
So like we said in the example earlier on in this skill, we would consider things like what other attributes, maybe what is their height, what is their color of hair, so on and so forth. And the methods would be things that they do, their behaviors. People walk, people talk, people saying.

00:05:12
All these things could be denoted as methods. But for now, all we're going to do is just create a really simple class and effectively have nothing in it. We can do this by using the pass keyword. This is going to pretty much create a class, but we're just kind of leaving it for now.

00:05:27
We'll get back to it later. So we have this Person class. Now we read in the documentation just there that we had this concept of a class and an instance of a class. So right now what we've done here is create a class. This part is the class. If I want to create an instance of the class, let me show you how we can do that.

00:05:45
If I say that john is equal to the Person class, and we'll just call this. If I hit Enter now, here's what's happened. We now have a new instance of this class called john. So the class is Person and john is the instance of the class. That means that john is an object, and the type of object that john is, is of the Person type, the newly created type we've just created.

00:06:09
So what I could say here is, is say type and pass in john. And if I hit Enter, its going to tell us that it's not an str, it's not an int. In fact, it is of the Person class, that is the type now. And again, I can create multiple instances using the same class.

00:06:25
Let me create a new instance. Let's just call this paul. Paul is also a person, so we'll say paul is equal to person. And now we've created a new object with the type Person, this time this object is called paul. So really think about the class as like the blueprint.

00:06:41
That's a nice way to conceptualize this. And in fact, it's almost like a cookie cutter, you know when you go to bake some cookies. And with this ring you can just press it into dough. So let's say you've got a big bit of dough here. You can just keep pressing the cookie cutter in and just creating more instances of these cookies.

00:06:59
Well roughly you can kind of conceptualize that as what's going on here. The actual cookie cutter happens to be the class, and we can just keep using the class to create instances, these new instances one at a time. But as of right now, we've not actually created any attributes or methods associated with this class.

00:07:17
We're going to be getting to that very, very shortly. But if we did, then john would have access to all of these methods, such as maybe walking, talking, breathing. As with paul, paul would have access to the exact same methods. And if we had particular class attributes, because john is of the type class, as well as paul, both of these instances of the class would have access to those attributes.

00:07:41
And this is what classes are all about. It allows us to logically group together the data we use, as well as the functionality of that data, the methods and the attributes. And it allows us to group things together in a way that makes sense, such as, if you are a person, it makes sense that you have the attributes and the methods associated with the person, which we can define with any Person class.

00:08:02
Now right now all of this might still seem pretty abstract. So the best thing to do is to dig in to creating some of these attributes. First thing we'll do is look at the different types of attributes that we can create, those are our instance and our class attributes.

00:08:17
And that's what we're going to be talking about in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Class Attributes

00:00:00
Hey, guys, and welcome back. Now previously, we had just found out that our objects can have class attributes, as well as instance attributes. What we will focus on in this Nugget right here, is the first one right now. That is class attributes.

00:00:27
So let's check out how we can actually assign these. So what we'll do here is dive back into a IPython, so IPython. So let's just create a class called, let's say drama. And right now, drama is not going to be taking any arguments. Now intended but then, we're going to create our class attribute.

00:00:44
Now basically, these are just variables which are associated to this particular class. So what do I mean by that? So let's say we want to say that lesson, everyone who is a drama, happens to be a percussionist. We want to associate that with the class of drummer.

00:00:59
And you create a class attribute here called, let's just say maybe member_type. Call it anything you want, like I say. And we'll make this member a percussionist within the band, because if you play drums, you are playing a percussion instrument. So if I hit Enter here, we have now created a class attribute.

00:01:19
That means that anyone who happens to be instantiated with this drummer class, is going to have this attribute associated with them that they are a percussionist. Everyone with that class gets this variable, effectively. To check this out, if I hit Enter one more time, let's create a new object, a new instance of this class.

00:01:37
So let's just say John again. That's me. I do happen to play drums. And we'll say John is a drummer. And let's just call this by using parentheses. So if i hit Enter now, like we see, if I say type, John, this is going to be of the type drummer, but now we're also going to see that we also have this new attribute associated with this instance John.

00:01:57
If I happened to say dir John, hit Enter, look here at the very bottom. We've got this one called member type. This is an attribute now associated with this instance. So lets access this attribute here. So we can see John.member_type, and we can see John as a percussionist.

00:02:17
Now the key thing to note here, is that all instances of this class is going to get this attribute. It's not unique to John. It's not unique to, let's just say, Paul. Let's create one called Paul. Paul's also a drummer. Everyone who is of this type drummer is going to have this attribute, so member type.

00:02:34
Paul is going to have the exact same. He is also a percussionist. So the syntax is really quite simple. It's just like assigning a variable. The difference is that it's indented within your class, as we see here, if we scroll on up right here. And like I say, for everyone that gets instantiated with this drummer class is going to have this member type attribute, as class weight.

00:02:54
So now we know what a class attribute is, let's find out what an instance attribute is. And that's what we're checking out in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Instance Attributes

00:00:00
Hey, guys, and welcome back. So previously, we had just talked about class attributes and how they effectively add class weight. Every one of that class is going to have those attributes, regardless. But we know that we can create an instance of a class like we did with John and we did with Paul.

00:00:29
What if we wanted to give particular attributes of that class to that particular instance? OK, so let's just quickly start afresh so we doing this totally clean. We'll dive back into IPython. OK, so let's recreate your class once again. We'll say class Drummer.

00:00:43
And what we'll do here is we'll recreate our class attribute first. This is going to apply to all instances of the class. Everyone gets this attribute. So we'll say, once again, member_type is percussionist. So if you happen to be a drummer, regardless, you are going to be a percussionist.

00:01:00
But let's now create a type of attribute that is specific to the actual instance. What we're going to do here is to use an initializer. Now, the initializer has a very special method, which is well known in Python, and it's known as the double underscore init method.

00:01:17
This is a magic method. And we'll get to those in a little bit more detail later on. But for now, just understand that this is a very important special type of method within Python. And this is what we're going to be using to create your instance attributes.

00:01:31
Now these instance attributes are unique to each object. It's not like your class attribute. Now, let's quickly look at the syntax we're going to invoke to create this instance attribute. So just like we do when we create a function, we're going to use the same type of syntax.

00:01:47
We're going to say "def". Now we're going to specify the name of our initializer, which is double underscore init double underscore. And now we're going to pass in some arguments. Now this part here is pretty confusing when you first see it. It's one of those things that just takes a few go arounds to get it straight in your head.

00:02:06
So just like with functions, we can pass in arguments. Let's say we wanted to pass in, maybe, the style of drummer they are. We'll pass in a lead hand, whether they're left-handed or right-handed, that is. And we'll pass in the brand of drums that they also happen to use.

00:02:22
Now this looks fairly reasonable right now, but the thing here we have to remember is that when we're creating an instance attribute, we're going to have our first argument that's going to be known as self. Now, notice that this went green straight away.

00:02:35
This is a well known convention within Python. Now, what self is, it's a reference to the instance that is going to be created. So let me just finish this off and I'll circle back and explain just what is going on. What I'm going to do here is to bind the actual arguments I'm passing in to the object that I'm going to create.

00:02:53
So what I'm going to say here is self.style is equal to style. And I'm going to say self.lead_hand is equal to lead_hand. And I'm going to say self.brand is equal to brand. Now what on earth is going on here? This is super confusing, I know. So like I say, self is referenced in the object that we're going to create.

00:03:14
So what I'm saying here is let's say I created an object called John. OK, now John was of the class Drummer. Now, because we're using this constructor here, this initializer, notice that we can't just specify that John is equal to Drummer. We're going to have to specify some type of arguments as well.

00:03:32
We're going to have to pass in the style, the lead hand, and the brand. Now, what is happening within this part of the code here is that we are just taking these arguments we pass in-- the style, the lead hand, and the brand-- and just think of it like we are binding it to the object.

00:03:49
We are attaching it to the object. So let me show you what I mean here so it makes a little bit more sense. OK, so if I hit Enter, we've now created our class. We have a class attribute, a member type called "percussionist", which applies to all drummers.

00:04:03
But for every instance of the Drummer, we're going to have to supply a style, a lead hand, and a brand. Because now if I just say John is equal to Drummer, it's going to tell me that I'm missing three positional arguments. I can't just say Drummer any more.

00:04:17
We're expecting these three arguments. And when I pass in these three arguments-- style, lead hand, and brand-- they're going to be attached to this object here. So let me do this correctly this time. So let's instantiate a Drummer called John. So we'll say John is equal to Drummer.

00:04:34
And let's pass in the style. So let's say John is going to be a rock Drummer. That's the first argument. And let's say John is going to play right-handed. And the last type is going to be let's say John plays Pearl drum. That's a make of drums, a brand.

00:04:48
So now I've passed in the three arguments that are required for the initialization to happen. Now if I hit Enter, we've now successfully created an instance of this class. This is the instance here. This is the class Drummer. And, now, these three arguments here are going to be bound to this instance.

00:05:07
So what I can now say here is I can say john.style. And it now outputs rock because that is the style of drums that John plays. If we say john.lead_hand, we're going to find out that John plays drums right-handed. If we say john.brand, we're going to see that John has the instance attribute "Pearl".

00:05:27
That's the brand of drums that John plays. And notice John also still has the member type. That is the class attribute. So everyone is going to get this attribute. So if I say john.member_type, John is a percussionist. But watch this. If I happen to create a new instance of a Drummer-- let's create a Drummer called "lauren".

00:05:45
So Lauren is also a Drummer. And we're going to have to pass in three positional arguments because that is what the init method takes, our initializer. And we'll say Lauren is going to be a jazz Drummer, Lauren is going to be left-handed, and the type of drums that Lauren plays is going to be DW, which is another brand of drums.

00:06:03
So now, check this out. We've now got two instances of the class Drummer. We've got John and Lauren. Now John and Lauren both share a class attribute. Notice this. If I say, "lauren.member_type", Lauren is going to get the percussionist attribute no matter what, because she is a Drummer.

00:06:19
All Drummers get that. Everyone that belongs to that class gets that class attribute. But Lauren is also an instance of a class. So Lauren has these unique instance attributes. So what are the instance attributes we have? Well Lauren is going to have, and if we check what our class definition was, we've got a style, a lead hand, and a brand here.

00:06:39
So notice that Lauren's style attribute is actually different from John's. It's a jazz style she plays. Similarly, Lauren's lead hand, as left-handed and Lauren's brand is not Pearl. Lauren plays DW drums, even though, like I say, John and Lauren both still have that class attribute.

00:06:57
John member type, Lauren member type. Both the exact same. So that is a critical difference between an instance attribute that is unique to each object created, John, Lauren, and the class attribute applies to all members of that particular class. John and Lauren are both Drummers.

00:07:14
They both get that percussionist class attribute. Now one thing I will just say here on this note about self, is that the important thing to note here is that it's the first positional argument you pass in. You don't actually have to use the word "self".

00:07:28
You can pretty much use any word you want. But, honestly, don't change it. That is a super strong Python convention. Everyone uses self for this. So let me just quickly give you an example of what I mean here. OK. So let's create an example here called class, and we'll make this of a dog.

00:07:43
Now create a class attribute. We'll call this "sound' So all dogs are going to make the sound "WOOF" and depending if it's Spaniel or a Labrador, that are going to say "WOOF" that's something that is applicable across all dogs. Now we'll create an instance attribute.

00:07:58
So we'll say def double underscore init double underscore. And now, traditionally, we would always, always, always be passing in self as the first argument here, OK? But, like I say, you don't actually have to, even though you always should. Let me just show you that you can actually know this.

00:08:14
So I'll just call this maybe, "my instance," OK? So I'll say my instance, and they we'll take their positional argument. So let's just say we're going to pass in an argument of the breed of dog, as well as maybe, fav food. OK, so colon, hit Enter. And now what we want to do is to bind our positional arguments, breed, and fav food to the actual instance itself.

00:08:35
Now, the instance itself has been referenced by the key word "my instance," in this case anyway. So we'll say "my instance.breed" is going to be equal to the breed argument we pass in. And we'll say, "my instance.fav_food" is going to be equal to the fav for the pass in when we are creating this object.

00:08:55
So if I hit Enter and, again, if I create an instance-- let's call it "rover." And we'll say Rover is a dog, now we're going to take two positional arguments. Like I say, the first argument is just referencing the instance. So we can just ignore this here.

00:09:09
We need to pass in breed and fav food. So we'll say Rover is going to be a Spaniel, and we'll also say Rover's favorite food is going to be chicken. So if I hit Enter here, we now have this instance "rover," which is of the type dog. So we'll say "type rover," and we're going to see Rover has got a class attribute, which is WOOF, and Rover has also got these instance attributes which are unique to the actual instance.

00:09:37
So I say, "rover.breed". Rover happens to be a Spaniel, but not all dogs are Spaniel. If I say, "rover.fav_food", Rover's favorite food is chicken. So like I say, we can actually use a different word than "self" as long as it is the first positional argument passed into the constructor, but really do not do this.

00:09:55
I just want to highlight that there's nothing, actually, special about the key word "self." You can use anything, but it's such a strong convention that you never, ever want to change it. But really, ultimately, the key point to remember here is that our instance attributes are unique to each object created.

00:10:10
So if we create rover, it's going to have these instance attributes for passing in. If I happen to create a new dog, let's just say Fido, and I passed in that Fido was a Labrador, and its favorite food happened to be beef, it would have different instance attributes, even though both of them would have the same sound, the class attribute of WOOF.

00:10:31
So that is all for creating instance in class attributes. Now we're focused on the attributes of our objects. These are the properties we associate with these objects. Let us now focus on the behaviors of our objects, what our objects can do, and we're going to be able to define these behaviors in the form of methods.

00:10:48
And that's what we're going to be checking out in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Creating Methods

00:00:00
[LOGO SOUND EFFECTS] Hey, guys, and welcome back. So let's now check out how we can implement methods within our Python classes. So let's this time go into Visual Studio Code. We'll create an example called example1.py. Now, let's just open this up. OK, so let's again create a class of "Drummer," OK?

00:00:28
And we'll have a class attribute. We'll just say member_type as a percussionist, just like we saw before. And what we'll do is we'll create an entrance attribute, just as we saw before. So if I say "def," and then get into a net. Now what should happen here with VS code is automatically it's probably going to fill this in for you.

00:00:46
So I'll just delete this part because I actually want to add things here. So again, the first positional argument is going to be "self." We're going to add a "style," as well as "lead_hand." And again, the "brands" just like we saw before. And what we want to do is to bind these arguments again to our object.

00:01:01
So we'll say self.style = style we pass in. We'll say self.lead_hand = lead_hand we pass in. And we'll say self.brand = brand we pass in. Cool. So that happens to be the actual instance attributes we've created here. Now what we want to do is to create some method, some behavior, some things we can actually do.

00:01:23
Now really, what you're going to notice here is that the methods we're going to see here, it's really just like a function almost. The difference is, it's like a function within a class. So check this out. Let's first create a method. So let's now create a method called "paradiddle." OK, so if you don't actually know a paradiddle is it's the drum rhythm.

00:01:42
And what it does it basically means that you grab your sticks, and then you hit your left hand then the right hand, then the left, then the left. Or you go right hand, left, right, right. So there's a little bit of an alternating pattern. Now what we're going to do here is determine whether we should start with a left hand or a right hand depending on our lead hand, if your left handed, you're going to do it left, right, left, left.

00:02:06
If you are right handed, you're going to do right, left, right, right. So to be able to access these attributes, here, which are bound to the actual object upon construction, we're going to want to pass in "self." This going to allow us to get access to these variables, here-- these instance variables effectively, or instance attributes.

00:02:25
So we'll pass in "self" as an argument, here. And what I'll say here is F self.lead_hand = left. Then what we'll do is we print left, right, left, left. However, if they're not left handed, they're going to be right handed obviously. There's only one of two choices.

00:02:43
So then we'll do the part that'll go the reverse way. We'll start with the right hand, then the left, and we'll do right, right. So now, we've created this little class Drummer will specify some positional arguments we need to pass send an order to create the object via the and initializer.

00:02:59
And now, we've created this paradiddle method. So let's create an actual instance of a Drummer. And we'll say "buddy_rich." Buddy Rich was a very famous jazz drummer. So Buddy will be a Drummer. Buddy happened to be a jazz drummer. His lead hand was his right hand, and the brand of drums that Buddy played was Slingerland.

00:03:17
Cool. So what I'll do here is I'll actually call this method buddy_rich.paradiddle And the way we call a method is by using a parentheses. So if we see this-- and let's try it right now so you can see what happens. So if we say "python3 example1," hit Enter.

00:03:33
And as we can see here, we've actually instantiated the objects, and we've called the paradiddle method, which is printed out right, left, right, right. That happened to be because Buddy Rich with instantiated as having a lead hand of a right handed.

00:03:47
See that? So it was not left handed, so we go to the L statement. And instead, what has happened is we've printed out right, left, right, right. OK so let's print out some of the attributes, as well. We'll say a printout. We'll say "buddy_rich.style." And notice, that when we want to access the attributes, we don't have to do a parentheses like you would with a method.

00:04:05
Just the dot notation is enough to get the attribute. So we'll say print(buddy_rich.style) print(buddy_rich.lead_hand) print(buddy_rich.brand). Cool. So if we save this and we try running that step one more time, let's hit Enter. So we call our paradiddle method that's at the very top.

00:04:23
And as we can see, we'll also be able to access our attributes. OK, so the method we've just created here, this paradiddle was using self as a way to be able to access these attributes so we could actually run a conditional statement on them. So if the lead hand we pass them was left.

00:04:38
Do this, L. Do that. Let's say we then actually need to access any of the attributes. Just watch this, we still need to pass in self here. So let's just do a simple method, just called maybe "introduction." And let's try to pass it in with no arguments, here.

00:04:53
And all we'll do is a simple print statement and just say, "hello. I am a drummer! What do you do for a living?" OK, so what we'll do here is will actually comment out the paradiddle method. OK? So we'll say buddy_rich.introduction. And it's a method, so we'll call this.

00:05:07
Watch what's going to happen, here. So if I try to run this now, hit Enter. It's going to say that introduction takes zero positional arguments but one was given. Well, where was one given? Well, that is effectively self as being inferred. So we all want to do is to be able to handle this by passing in self here as an argument, even though we're not actually explicitly using it here the way we were using it in the above by actually deliberately accessing the attributes.

00:05:32
So now that I've actually passed down self, even I'm not actually using it now, the method is going to handle this positional argument. So if I clear the screen, arrow up, hit Enter. Now we have our introduction methods. And what we can also do is pass in arguments to our method.

00:05:46
So let me show you that. So let's create another method, and this time called maybe, say, "drum_lessons." So we're going to take this argument self, which is going to reference the actual instance. But we're also going to take an additional argument, here.

00:05:59
So the drum lessons is going to be contingent upon the type of grip that the person is using. Now the details of a drum grip really doesn't matter, here. Basically, there are two main types of grip. You can get traditional grip and a matched grip. OK, so Buddy Rich is only going to give drum lessons if the student happens to be traditional grip.

00:06:19
He's very, very strict on traditional grip. So if you try to approach him wanting lessons with a match grip, he's going to tell you to go away. So what we'll say here is, if the grip that you pass in is equal to traditional, then what we'll do is we'll printout, "sure I can teach you no props!" And we'll say, "else," "print," "sorry!

00:06:40
I only teach traditional grip!" So now what we can do here is call this drum lessons method, is Buddy going to give us a drum lesson? We can say buddy_rich.drum_lessons-- if I can get the right one. And we need to pass in this grip argument. So what we'll do, here, is we'll pass in the argument traditional, and we'll comment this out here.

00:06:59
Let's Save here. Clear the screen, arrow up, hit Enter. And because we have a traditional grip, Buddy Rich is happy to teach us. However, if I happen to inquire if I could get a lesson of him and I happen to be matched grip, which is not traditional-- okeydoke-- then what is going to happen is Buddy's going to tell me where to go.

00:07:18
So as you can see here, we didn't actually get the lesson. So notice here is that our methods are very much like our functions. The difference is that we create methods within a class, and we also have this argument self here to take care of. This is going to reference the object itself.

00:07:35
Now notice, that even when we are not actually explicitly referencing the object within the method, such as this here, we are still going to pass it in as an argument. Similarly, as we saw here, this self argument gives us access to our attributes. So self.lead_hand gives us access to the arguments we passed on here.

00:07:55
And as we also saw, with our methods, we can add additional arguments to the methods. And then that means that when we're calling the method, we're going to have to pass in an argument because it's expecting another argument. So these are some of the concepts around attributes and methods within Python.

00:08:11
Like I say, the whole concept of using self is a little bit weird at first. But as you do it a few more times, you get a better familiarity, then it certainly does become a lot, lot clearer. So that is methods within Python. We also have to explore another thing called magic methods, and that is coming up in the very next Nugget.

00:08:29
So I hope this has been informative for you, and I'd like to thank you for viewing.

--

## Magic Methods

00:00:00
 Hey guys, and welcome back. So previously, we had just looked at methods within our Python classes. Let us now discuss something called magic methods. Now that sounds like a pretty interesting term, a magic method. Why exactly is this?

00:00:26
Well, like so many of these type of concepts, the best thing to do is to see and try it. So let's check it out. So let's just first dive into IPython right now. What I'm going to do here is I'll create a list called "my list." And I'll make this equal to, and I'll just say John, Trevor, Bob, Simona.

00:00:42
OK, so now I've created this list. If I happen to say type my list, you can see that it's been instantiated using the built-in list class. We have an object, my list of type list. Now there are some things we can do with this object that we happen to see there in my list.

00:00:59
Check this out. You can see, for example, here, we have this double underscore len. This allows us to be able to calculate the amount of objects within less than five. This is what the len function is actually doing. When we say len my list, and we get four items that are list, which is obviously true here, 1, 2, 3, 4.

00:01:17
And what we can also do here is say my list, and actually call this double underscore len methods. Let's use the parentheses to call it since it's a method. If we hit Enter, we're actually getting the same result. So clearly, we can easily calculate the number of items within our list.

00:01:34
And it is because the built-in list type gives us access to this double underscore len method. So what I want to do is to show you the difference here when we create our own class. So what I'll do is I'll create a class called "friends." And what I'll do here is I'll create a class attribute, which is actually going to be a list object.

00:01:53
I'll say members. And who are the members? We'll say Ross, Rachel, Joey, Phoebe, Chandler, and Monica. And I should actually make the members equal to that, OK. So if I create an instance of this class, let's just call this "my friends", and I'll make that equal to the friends class, kill.

00:02:11
So clearly here, if I happen to see my friends dot members, we're going to have access to this class attribute, which is going to give us all of the friends we have here. Now what if we wanted to be able to get the length of this list, i.e., how many friends do we actually have here?

00:02:30
We can see we have six. So if I say dir and I parse in the My friends object, notice here, we don't actually have access to the double underscore len method here. Notice that is not present at all. What this means then is if I try to take the actual length of my friends, like you would with the regular list, if I Enter, it's going to see that the object actually doesn't have any length.

00:02:54
So what we actually need to do here is to implement the len method within our actual class. So let's try this once again. So clear the screen. I'll create a class again. [INAUDIBLE] That's just so we know we're completely clear. Clear here, back into IPython, let's recreate the class.

00:03:11
We'll say class, friends. And we'll say members is equal to, and just as we did before, say Ross, Rachel, Joey, Phoebe, Chandler, and Monica, cool. So what we want to do here is to implement a magic method here. Now you'll notice we've already actually seen a magic method before.

00:03:29
That was used in the initializer by saying double underscore init. And any time you see those double underscores, that is when we're dealing with a magic method. So in order to be able to access the length of the list, let's create this double underscore len methods.

00:03:45
We're going to have to reference self to reference the actual objects. And all we're going to do is say return the length using the length function. And all we're going to do is access the object by saying self dot. And what do you want to take the length of?

00:03:59
The actual members, which as the list, OK. So if I hit Enter here and again, let's now create a new instantiation of the friends, class or game. We'll say My Friends is equal to, I'm going to say parentheses, perfect. So as you can see here, I've got an object of the type friends.

00:04:16
And now we are going to notice is I can actually now pass this object into the length function. I can say My Friends. And if I Enter, now we can see here that it's actually calculating the amount of friends we have, which is six. Basically, magic method is going to allow us to give us access to Python's built-on syntax features, things like the len function.

00:04:38
So again, let's create another example of a magic method. But before we do that, let me just create a separate list entirely. I'll just call this My Different List of Friends. And that has nothing to do with the class. It's just any example list. I'll just say Trevor, Simona, Knox.

00:04:54
OK, so if I hit Enter, what if I wanted to do a conditional test here and say, if Trevor and my different list of friends, what I can do is print Trevor as in the list. Else, I can say print Trevor as not in the list. If I Enter here and again, going to say Trevor is on the list because Trevor, as we can say here, is within our list right here.

00:05:17
So again, we have created this instance called My Friends, which happens to be of the type friends. And as you know, we have the class attribute members here, which tells us all of our friends. Now let's try to apply the same logic we just did there.

00:05:31
Let's see, if Ross in my friends, or print similar to what we did with Trevor. We'll say Ross is in the list. Else, print Ross is not in the list. So let's hit Enter. And again, on watch this. It says the argument of tight friends is not acceptable. We can't actually use this logic directly on this object right here.

00:05:52
If you want to be able to use this as an operator within Python on a special type that we've just created, we've got to be able to specify this as a magic method. So let's go and revisit our class once again, our friends class. So we want to create a new method, a new magic method.

00:06:09
That's then going to be called underscore, or double underscore contains, I'll Enter pass and self as a reference to the object. And we'll take an argument called friend. And all we're going to do here is return friend in self dot members, which is our list object out here.

00:06:27
See that? So now if I hit Enter and again, let's reinstantiate our objects. So we now have the new definition of friends, which now includes this new magic method. So we'll say my friends is equal to the friends class, which has now got this new contains magic methods.

00:06:43
So now I can actually implement that logic and say if Ross and my friends, what I can do is print Ross as in the list. Else, we'll just print out Ross is not and the list. If I hit Enter, and again, now we can implement this in logic within our actual new object.

00:07:02
So note there's a lot of the built-in functionality in Python, like checking the length, checking if something is in something, that's automatically baked in when we use a built-in class, like, for example, name equals john. That is automatically instantiated by the built-in str class, str.

00:07:20
And they already have all these magic methods built-in, which is data. You can see it's got the contains magic method, has got the greater than if you want to check if something is greater than, or perhaps less than, or check the length of it. These are already built-in.

00:07:36
But in our Custom Objects that we are just creating, if we want to have this type of built-in functionality, we're going to have to specify them as magic methods. And as we can see here, there actually are quite a lot of them, including the one we've already saw, the double underscore in that method.

00:07:52
So as we can see here, these magic method, these Dunder methods as they're sometimes called due to the double underscores, they allow us to apply some cool Python functionality to our Custom Objects that we get automatically with the built-in objects.

00:08:06
So if you want your custom class to be able to do these type of comparisons, greater than, less than, check if something is in the class, what is the length of an object within the class, then implementing these magic methods is where you want to go.

00:08:19
Before we actually wrap this Nugget here, what I want to show you is a very common implementation of the Dunder method, AKA a magic method. Let me show you this. So let's just create a class for each student, let's say. And let's create some instance attributes.

00:08:33
We'll say, def double underscore init double underscore. Our first argument's going to be self. And we'll take the age of the students as well as the course they're actually taking. And what we'll do is we'll say self dot age is equal to the age the person.

00:08:48
We'll say self, and we'll also bind the course of parsing into the object. So I'll say self dot course equals course. So now we have our student class. So if I happen to create a student, let's just say Michelle as a student. OK, so we now have to parse in our two positional arguments-- age and course.

00:09:05
Let's say Michelle is 20 years old. And let's say Michelle is studying computer science. OK cool, to check this out though, what if I happened to just print Michelle, OK? And we get this ugly output here. It says that Michelle is a student object. And it shows Michelle's position and memory.

00:09:24
Now, a common thing people want to do is to be able to make this a little bit more readable. And what they often do here is implement double underscore str. This is going to give us a readable representation of this object. Now there also is another very similar one called double underscore repr.

00:09:41
But we'll not dive into the deep details on those differences right now. Let's just focus on double underscore str. So let me show you how we can make this a little bit more readable then. So what we'll do here is let's recreate this class. So say class students.

00:09:55
Once again, we'll say def underscore init double underscore, same again, self, age and course. Again, we want to bind our arguments to the attributes. So we'll say self dot age is equal to the age that's parsed in. Self dot course is equal to the course that's parsed in.

00:10:11
Now what we want to do here is to create another magic method here. So we'll say def. I'm now going to say double underscore str double underscore. And we're going to parse in self as per usual. And all we're going to do here is return some type of readable statement.

00:10:27
Something that's going to be very easy on the human eye, so that we can easily inspect our object and see exactly what it is. So when we actually use the print function, what it's actually going to do is call double underscore str. And it's going to print out whatever we return here.

00:10:42
So if I happen to return, I am a student because I'm part of the student class. And I'll say age. And in fact, let's make this an F string rather, so we can use our interpolation. So we use our calibrate. And I'll say age is equal to self dot age. Now all I need to access the age attributes that is bound to the object.

00:11:02
And I'll say age actually. A little bit better. And I am studying, self dot course, cool. So now we have this new magic method, double underscore str, really, really common to see this done. So now let's instantiate a new student with this new definition, which now has this double underscore str magic method.

00:11:22
So we'll also create a new student called Julio. And we'll make Julio a student class. Julio is going to be 21 years old. And Julio is going to be studying network engineering, cool. So let's hit Enter. So if we happen to print our Michelle object, remember Michelle was created before the double underscore str magic method.

00:11:41
So this is going to just print out this weird student object and its memory location. However, if we actually print Julio, what it's going to do is going to call this double underscore str. And we're going to get this nice readable output about this object.

00:11:55
So Julio is a student, aged 21. And Julio is studying network engineering. So this is a very, very common use you're going to see about using magic methods. If you happen to inspect code on GitHub, you're going to see this implemented all over the place.

00:12:09
And it really actually is going to give you a nice and readable representation about the object that you've just instantiated. So I can see that is a lot to deal with, but then this scale is very confusing the very first time you see it. I struggled with it.

00:12:22
I think everyone who I know happened to struggle with it a little bit at least. But I really can't stress enough that repetition is the absolute key here. Once you just go through it enough times, then the whole picture is really going to crystallize within your mind.

00:12:35
So if you feel you have to watch this skill just a couple of times, then definitely do that and certainly lap up what you see and experiment in your own way too. Okey-doks, I hope this has been informative for you. And I'd like to thank you for viewing.

00:12:48