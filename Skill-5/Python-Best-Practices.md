# Python Best Practices

## Introduction

00:00:00
[MUSIC PLAYING] Hey, guys, and welcome back to another skill in Python for Network Engineers. So what we're going to be doing in this skill is a really important subject that's all about writing and maintaining Python codes, whilst adhering to best practices.

00:00:26
Now, best practices are, obviously, very important. But in terms of writing your code, it's going to make your code more modular. It will also make your code cleaner and easier to interpret. This is going to be good for you or for future you when you're looking back at old code that you've written.

00:00:42
Having it be nice and clear and concise is really going to help you retroactively understand what it was you were trying to do. And, of course, when working with teams, when sharing code, having nice, clean, readable code is going to be a very big win for collaboration.

00:00:58
And honestly, these are just some of the reasons why you want to follow best practices within Python. So what we're going to be looking at within this skill is something called PEP 8. This is effectively the Python style guide developed by Python experts and the community so that people understand how to write the most Pythonic code-- as it's termed-- as possible.

00:01:18
We want our code to be clean, readable, and adhering to the rules, I suppose, set out within PEP 8. So we'll have a brief glance of what PEP 8 entails. And then, we'll check out some other things, like maybe, say, naming conventions that we want to be using.

00:01:33
We'll check out how we can properly put in comments within our code. And we'll look at other things, such as importing different modules into our codes, as well as the very important topic of how we're going to actually layout our code when writing it.

00:01:47
So these are just some of the things that we're going to be talking about within this skill, but there certainly are going to be some additional things we're going to look at. But like I said, the very first thing that we should be doing is consulting that PEP 8 style guide so that we can get a rough idea what it is we're actually trying to do.

00:02:03
So how about we check that out next? And that's what we're going to be doing in the very next Nugget. So I hope this has been informative for you. And I'd like to thank you for viewing.

---

## Pep8 Style Guide

00:00:00
Hey, guys and welcome back. So let's now check out this PEP 8 style guide, which is going to help us rate the most Pythonic code possible. OK, so let's go and dive into a browser and find out what this is all about then. OK, as you go to Google and you just search for PEP 8 style guide, the very first hop line should take you to where we want to go.

00:00:32
So let's click on this link here then. And let me just Zoom out a little bit here. So that says, the style guide for writing Python code, this is the rules that we want to follow as Python developers. So, as you can see here, we have our contents here, it tells us about all the different things that we can be dealing with, but let's just have a scan through some of the things that we can see here, so we can get a rough idea.

00:00:52
So if you have been writing out your code, then you've been wondering, hey, how exactly should I lay this out? Well, like I said, this is the best place to go. It's going to tell you exactly the accepted way within the community to do so. So one thing, we're going to see here is an indentation.

00:01:07
If you've been using an editor, such as VS Code, naturally when writing Python code, it should automatically indent four spaces. Even though you can use one space, you can use two, you can use three, you can use as many as you want. But really, the accepted style guide suggests, quite strong, that you should be using it for space and your Python code.

00:01:27
And as you can see here, if you just go down here, we get a nice little example of what we're talking about. We get an example of what the correct code should look like, so this one here. And if you scroll on down, we also get a nice little example of what constitutes, at least, according to the style guide as what you should avoid doing.

00:01:43
So this guide is really, really useful. So let's scroll on down, and let's look at a couple more things then. Here's another one, Maximum Line Length. So it tells us here, that when you're writing your Python code, you really want to be limiting your lanes to a maximum of 70 main characters.

00:01:59
However, you'll notice that for certain blocks of code, that is even further truncated, and to only 72 characters. Now it tells us why this is actually the case. When we follow this type of rules, we're going to be able to have several files open side by side.

00:02:13
And it's also helpful when we're doing code review. So if we can adhere to these type of rules, we can have a decent font size, a nice readable font size and also be able to compare two lines of code or our two blocks of code, side by side, with no problem at all.

00:02:28
So again, just another lateral best practice. Let's see what else we have. Here, we have some examples of using white space. We don't want to be adding in unnecessary superfluous white space that is really not needed. To check this out for example. In this example here, we can see that we have a list element of this list here, as well as a dictionary.

00:02:48
Now notice the spacing in here. This is nice and compact. We don't have an additional space between the parentheses and the list object, as well as, the square brackets and the list position. Instead this is all mixed and compact. The exact same is true here, for-- actually, we don't need to have an extraneous white space here, for example, here.

00:03:07
Instead, we want to tight it up and keep it nice and compact. And again, the style guide gives you more and more examples. It gives you examples, when you're dealing with trailing commas. We get an example of how to correctly format our code here. So again, we're just briefly having a quick look at this style guide.

00:03:24
What I would encourage you to do it is to browse through that yourself and just go through the contents. It really is very, very useful. We've got all these different things that we can adhere to. But a really important one, that I do want to focus in on is going to be Naming conventions.

00:03:37
And this is exactly what we're going to be dealing with in the very next nugget. So I hope this has been informative for you. And I'd like to thank you for viewing.

***Quiz***

**The Pep8 Style Guide details the guidelines and best practices on how to write "Pythonic" code.**  True or False? **TRUE**

---

## Naming Conventions

00:00:00
[MUSIC PLAYING] Hey, guys. And welcome back. So now let's talk about naming conventions within Python. What exactly are the best practices here? So let's talk about this then, shall we? Now an important thing to note is that independent of what you're actually describing, whether it be a function or a variable, it is a really good idea to use descriptive names.

00:00:33
So let's say you had a list of IP addresses. If you're going to look through that list, it would make sense to see something like, say, for ip in ip list. Because just reading this, the actual code itself is very readable, as opposed to saying something like, say, for x in random_thing, which would not be a very descriptive naming convention, it makes much more sense to use this type of format.

00:01:01
But here is the thing. We actually do have different naming styles that we can actually use when writing these descriptive names. So what on Earth am I talking about? Well, think about it. Take an example here. What do we have here? This is the letter a, which is going to be a single lowercase letter.

00:01:19
We could also have a capital A, which would be a single uppercase letter. We could have a lowercase word like, let's just say, address. Or we could have lowercase words separated by underscores. So let's say, maybe, my_ip_address, lowercase plus underscores.

00:01:39
Now we also have, as you would expect, uppercase. So maybe we could say, ACL for access control list. This would be an example of uppercase. And just like with lowercase, we could separate out separate words using underscores. So I could say, ACCESS_CONTROL_LIST, uppercase mixed with underscores.

00:01:59
And we also have something called camel case. And this is commonly seen when writing a class. So let's just, for example, say, MyClass. So every new word begins with a capital letter. Again, this is known as camel case. And the reason why it's known as camel case, by the way, is because of the shape of the lettering.

00:02:16
We have this kind of hump here. And we get to a new word, and we get another hump for the capital letter. So it really is quite easy to remember this format. Now, what I will say is that when you're using camel case, when you do encounter an acronym, then you still want to actually capitalize all the letters of that acronym.

00:02:34
So let me give you an example. Let's say we wrote a class to test our OSPF adjacencies. So when we use camel case, we could say, Test. Now the word, OSPF, that is actually an acronym. So we don't just want to just capitalize the O. We'll capitalize the entire acronym, so TestOSPF, and maybe, say, Neighbors, so capital N, and then small letters here.

00:02:57
So just be aware of that within camel case, we still want to be preserving the acronym as capitalized. And then we also have something called mixed case. Now, the difference here between a mixed-case format as opposed to camel case is that with the mixed case, it's going to be the exact same except for that the very first letter is going to be lowercase.

00:03:17
So that would be lowercase to start with. So we can say test, and then next word's going to be a capital letter. So we can say testNetwork, and then maybe say State. This is an example of mixed case, starting with a lowercase letter, no matter what, and every new word gets a capital.

00:03:34
And the other type, which is quite discouraged within Python, is to use capitalization for every new word and separating those with underscores. So this would be something like, capital M, My_Network_State. Capital letters to start each new word and each new word separated with underscores, again, this is quite discouraged.

00:03:57
People don't really like it. It's kind of seen as ugly on the eyes, which I can kind of agree with, to be honest with you. So these are some of the formats that we can use when writing your names for our variables, or functions, or classes, so on and so forth.

00:04:09
But we do have some additional rules that we want to follow here. First thing, let's talk about our single letters. Remember, we can have a single lowercase, a single uppercase. But there are some letters that we want to avoid. One would be is to have a lowercase L. The reason why is because a lowercase L can look a little bit ambiguous.

00:04:29
Some people thinks it looks like an I. What we also want to avoid is an uppercase I because an uppercase I, well, it just looks like the lowercase L, just like we saw just there. So lowercase L, we don't want to use that. We don't want to use uppercase I. And we also don't want to use uppercase O because what does uppercase O look like?

00:04:51
Well, it looks like the number zero. So the reason why we don't want to be using these characters here is purely because they can be ambiguous. And we want our code to be clear, readable, and free from ambiguities. So we do not want to be used in these letters where we can avoid it.

00:05:08
Now let's talk about writing our module names. So when we happen to create a module that we can import into a code, that we can reuse effectively, we want that module to be written in lowercase. And therefore, modules going to be named with several words.

00:05:23
We want to separate out those words using our underscores, so a lowercase word, separate with an underscore, followed by another lowercase word. Let me show you a quick example. So let's just create a simple module which can add two different values as well as subtract two different values.

00:05:39
Because this is doing some type of mathematical equation, let's just call our module my_maths. So the format we want to use is lowercase letters. And if we happen to have more than one word, we want to separate those words with an underscore. So what we'll do here is we'll say "touch" to create the file, and we'll say, my_, next word, maths, and that will be .py.

00:06:01
And within here, we create our module. So we could do something like, say, def adder(a,b), then, return a plus b, and then, def subtractor(a,b), return a minus b. And if I save this, create a new field called touch example.py. I could open this up. And then I can say, from my_maths import.

00:06:23
And I could import adder, and import subtractor. And I can say x is equal to adder(1,2). And then I can print out x. I'll just run python3 example.py, and that's working. And notice here that this import here is following that convention because that's what we've actually named it.

00:06:41
We've used lowercase, and the separate words have been separated with the underscore. Now like I say, if we're going to happen to create a particular class, and again, let's just say we're going to create a class which is going to test our network state, we want a descriptive name.

00:06:55
And we don't just want to do a lower case, we're not going to say it like, say, test_network_state. That really isn't following the convention. We want to be using camel case when we're creating a class. So we say, TestNetworkState. And in this case, I'll just pass.

00:07:08
I'm not going worry about actually writing the code for the class. But for a class, best practices, we want to be using camel case. This makes it really easy to eyeball what we're actually using when we see a class. Now just like we saw within our my_maths little module here, when we are creating functions, such as adder and subtractor, we want that to be in lowercase.

00:07:29
Classes are going to be camel case, and our functions are going to be lowercase. But just like within our module names, if we happen to have more than one word, we still want to be using lowercases that are functions, but we want to be, again, using that underscore to separate those words.

00:07:47
So if I wanted to create a function called the multiplier, I could say, the_multiplier, and take a and b as an argument, and they just return a times b, so again following that convention. Now here is the thing. We often create variables within our code.

00:08:05
These are values which are effectively variable. The thing is, some values are constant, and we're going to have these things called constants to denote that. Now when we are actually writing these constants, we're going to follow a different format from our variables.

00:08:19
Instead, with constants we want to be using uppercase. So let's just say for the purposes of your script that you're going to have a particular threshold value. This value is an absolute value that is never going to change. Because it's going to be a constant, we would just call it THRESHOLD with capitalization.

00:08:36
And we can maybe make that value, let's just say, zero. So a threshold, this could be absolutely anything. This could be a temperature. It could be a number of errors. I'm just giving you a rough example here. The point here, though, is that the threshold is never going to change.

00:08:48
It's going to be a constant value. Because of that, we want to be denoting that with capitalization, or rather uppercase, should I say not capitalization, uppercase. And again, if we're going to have multiple words, we want to be using our underscores to separate that out.

00:09:03
So I could say, MY_THRESHOLD. So these are just some of the naming conventions that we're going to be dealing with in Python. Now we'll see, if you go through PePy in its entirety, you're going to see more examples of what we've just looked at right here.

00:09:17
But these are some of the most common and, I would say, the most important ones to really focus on. And if you want to be writing good clean Pythonic codes which is easy for others to eyeball and interpret, then we really want to be adhering to these rules, that way we can easily identify classes, we can easily identify constants, so on and so forth.

00:09:36
And we don't want to be bringing in ambiguity and to record. So remember, things like uppercase I, lowercase L, uppercase O, these are ambiguous characters. We don't want to be using them. You can use these characters fine with any words, but don't use them as a single character for a particular variable, for example.

00:09:55
So that is us. From now on naming conventions, certainly follow these rules. They're really, really important. But we also have another important topic to get to, and that is comments. And that's we're going to be talking about in the very next Nugget.

00:10:06
So I hope this has been informative for you. And I'd like to thank you for viewing.

***Quiz***

**Which of the following characters should NOT be used to denote a Python variable?**

+ **```l (lowercase el)```**
+ **```I (uppercase eye)```**
+ ```x (lowercase ex)```
+ **```O (uppercase oh)```**

---

## Code Comments

##### 00:00:00
Hey, guys, and welcome back. So let's now talk about writing comments within our code. So what exactly are the purposes of comments? Well, comments, ultimately, are like little notes to yourself or to others. They serve to act like annotations. So if you can imagine that you are back in school and a teacher handed out particular worksheet to do some work, when that teacher was explaining what to do, you might be scribbling down on the side of that sheet, i.e., making little notes about what you have to do, what is expected to be done.

00:00:43
Ultimately, that is kind of what we're doing when we're writing comments within our code. So these little notes that we're writing, we want to be using them to describe our code. This is going to be very handy for your future self. Because when you begin writing lots and lots of code, it can be a little bit difficult to remember everything you were trying to do in previous iterations.

00:01:06
So to save yourself future headaches, writing these comments can really make it easier for you to eyeball what it is you're trying to do in this particular section of the code and why that code might be here, so you don't just delete it about hastily.

00:01:19
So certainly, describing code is a very important concept. And comments helps us do just that. What we can also add are things like to-do lists. What are our future plans? What other features do we still have to implement? So we can easily eyeball our code.

00:01:34
And remember that it's not the finished article. We can't do everything all at once. We certainly have these future plans that we want to implement. And these little comments can help us annotate exactly what those future plans are and whereabouts in the code we plan to implement them.

00:01:50
Some of the labor not always perfect, certainly not. Sometimes our code is functional, but it is a little bit buggy. Maybe we didn't have time to perfect exactly what we were trying to do. We just have something that works for now. But it's a little bit like a Band-Aid.

00:02:04
So we may have some little bugs within our code, and writing comments to highlight those bugs that we should affect but maybe can't quite get to just yet, these comments can really serve us well to point out these potential bugs. Now, another good reason for commenting is, in fact, for troubleshooting.

00:02:20
And I don't just mean about describing what we expect from our code. What I'm talking about is controlling the execution of our codes. Because when we write a comment using our hashtag, as it's now known, this, in essence, stops a particular piece of code executing.

00:02:36
So if we want to test something, maybe we only want to execute a very particular part of that code. But what we can do here is effectively, as it's known, comment out code. And when we comment out code, effectively, we make that piece of the code nonexecutable.

00:02:53
So it allows us to easily target very particular pieces of the code to execute. Again, this is very, very handy when troubleshooting, when trying to isolate a particular error. Now, an important thing to note is that we do have the concept of comments, and we do have the concept of documentation.

00:03:10
Now, it might sound like documentation is what we're trying to implement within these comments. And I suppose, in a way, maybe it can act like some type of pseudo-documentation in some cases. But basically, you can kind of conceptualize is that when we're writing comments within our code, our target audience is really ourselves and our fellow developers, i.e., people who are actually going to be working with the code, manipulating the code, changing the code.

00:03:37
This is primarily who this target audience is. And we target them using our comments. However, when we're using documentation, our target audience is a little bit different. It's not the developer. It's not ourselves. Our target audience, this time, is really about the end user, someone who's actually going to be using your code.

00:03:58
So the end user isn't so much concerned about future features that we, as developers, are going to be implementing. The end user just wants to know, how can I operate this piece of code? How can I make it work as it is intended to work? OK, so let's look at an example of commenting our codes.

00:04:14
So we'll just say touch. I'll just call this one comment_example.py. So basically, our comments are going to start with this pound sign, or as it's now known, a hashtag. And anything that comes after that symbol is going to be ignored by the Python interpreter.

00:04:30
So what I could say here is, #. And anything I write after this on the same line is going to be accepted as a comment and not executable. So what I could say here is print my name. And below it, I could actually write the code. I can say, print My name is John.

00:04:47
If I save this, I could run this, hit Enter, and it's only going to execute My name is John. It's not going to throw an error about this part here because it's just a annotation effectively. Now what I can also do is I can actually change the location of this comment.

00:05:03
I can actually make it after the code here. So at the very end, I can put this hashtag in. And I can say, print my name. And again, anything that comes after the hashtag is going to be commented. But before it, this is uncommented. What I could do here is save this.

00:05:20
Again, arrow up, try again. Code executes the exact same way. So I could add another comment. And I could say, print my surname. And I could just print My surname is McGovern. And if I save this, arrow up, we're printing our first line and our second line.

00:05:37
And if I go back, as I said with regard to troubleshooting, I can control the execution of this code just by commenting some things out. So if I just wanted to test the first line, which has My name as John, I could comment out the second piece of executable code by just commenting that out.

00:05:53
And suddenly, when I save this, we're only going to get the first piece of code executing. And again, I can remove that comment and then comment out the top piece of code, save here, arrow up, and now only the bottom piece is executing. Really, really handy when troubleshooting.

00:06:07
Now, remember we learned within Python, we don't want to have lines which are too long. I believe it is something like, say, 70 characters long or 72 characters. So because of this limitation that we want to impose, we can't just keep writing a comment that just keeps going on and on and on and on and on, if we just keep adding to it.

00:06:26
Again, this is not going to be Pythonic. What we could do here is move this comment and make it into a multiline comment. So to make this a multiline comment, what I can do here is just put a hashtag at the front of a new line and just move everything down a line below.

00:06:41
So if I hit Enter, and, again, as long as we're starting with the hashtag, these lines are going to be interpreted as comments only. And none of it is going to be deemed as executable. Now, one thing I want to highlight is that we still want our code to be concise, i.e., we don't want to just add unnecessary comments just for the sake of commenting.

00:07:02
Some people are really guilty of this. And it just makes the code cluttered and actually harder to read. It just becomes an eyesore. So really, what we actually want to be doing is writing readable code where possible and not trying to rely on comments.

00:07:17
So say, for example, here, what I wouldn't want to do here is add a comment and say it returns a plus b. Because, as we can see here, this is pretty obvious by the code. Returning a plus b, do we really need this comment? That's what you want to be asking yourself.

00:07:32
Similarly, we don't want to be adding in an additional, say, returns a minus b. We're not serving any real purpose here. We're just adding in more text, more clutter. We just don't need it. So by using things like, say, good variable names, very often, your code should be pretty readable and intuitive as it is.

00:07:52
Say, for example, here, I had a list of IP addresses called my_ip_addresses. And I could say, 192.168.1.1 and 10.0.0.1. If I wanted to look through these IP addresses, by using good variable names, I could say, for ip in my_ip_addresses:. I could say, print ip.

00:08:13
That is pretty descriptive already on its own. We don't have to have an extraneous and unnecessary comment here saying, for every ip address in ip address list, print the ip. Because we've actually used good naming conventions, this is almost inferred by the code itself.

00:08:33
So really do consider that when writing your code. Good variable names is going to be pretty self-descriptive. And last, but certainly not least, when writing your code comments always adhere to the code of professionalism. So if you're collaborating on a project with someone, don't comment on the code and say something like, hey, dumbass, this code is stupid.

00:08:53
Do better. I mean, clearly, this is not the type of language you want to be using in a professional environment. So even though code comments can be pretty informal, they can be relaxed. Just remember, you're representing yourself as a professional. And your code comments really should also reflect that as a best practice.

00:09:12
OK, so that is the general rundown on code comments. It might seem like a small topic, but it really, really isn't. It really does help us when maintaining our code, revisiting old code, and collaborating with others. So I hope this has been informative for you, and I'd like to thank you for viewing.

00:09:28


***Quiz***

**(True or False) It is best practice to comment every line of code in order to ensure maximum clarity.** **FALSE**

---

## Imports

00:00:00
[INTRO LOGO] Hey guys and welcome back. So in the previous Nugget, we had just talked about some of the best practices that we should use when adhering to, well, best practices. [LAUGHTER] Now one of the things we talked about was, rating your own modules.

00:00:26
And we know that when we want to use a module, we have to import that module. And there happens to be some type of best practices that we should be following when dealing with our imports. So let's just briefly talk about what the different types of imports we can have, and then see how we should actually conduct ourselves when using those imports.

00:00:45
So, as you may know, Python has a standard library available to it. And if you've been following along in this course on Python for network engineers, in previous skills, we have saw some of the details around those standard libraries, what we can use and some of the cool features available to us.

00:01:03
Now we also have, what are called third party imports. Again, that could be something like, say, for example, the Scrapli library, which is what we use very often to connect to network and devices. And we also have our own custom, local applications or local modules.

00:01:22
This is just like the my-maths module we just created, an EVS Nugget there. Now when we are importing these different types of modules and packages, we want to follow a particular hierarchy, and it's this type of hierarchy, we are seeing right here. When we're doing it imports at the very top, we want to specify a standard library imports at the very top of our script.

00:01:44
That makes it easier to eyeball our code. It's going to give our imports a nice predictable structure. Now a good thing to do is to add some space between our imports, again, so we can clearly delineate and separate what is standard, what is third party, and what is a local module.

00:02:00
So we can add some space in. And then below are standard imports, we will specify our third party imports. And again, once we have finished our third party imports, we will leave a little bit of space, once again, and then what we can do is, finally, import our local modules.

00:02:17
Now a good rule to follow, as well as, within each letter, or would you say, bracket-- say, for example, standard library and the third party and the local modules-- within each one, it is good to do our import in alphabetical order. That means that if you happen to have lots and lots of imports, it's going to make it quite easy or at least easier to be able to scan through what we're looking for and identify quickly whereabouts our import lies, if we have imported or if we have forgotten to.

00:02:46
So, let's look at a quick example then, so I can just show you what I'm talking about here, then. Like I said, if I do an ls, we have this, My-maths module. And that would be denoted as a local module. That's just locally sitting on my machine. It wasn't installed via PEP, as a third party import, nor is it certainly not part of the Python standard library.

00:03:09
So what I'll do here is, I'll create a script. And I'll just call this, maybe say, import_example.py. And let's open this up, then, we're going to import_example.py. So what we want to do here is if we are going to import anything from the standard library that should come at the very top.

00:03:25
So let's just say we're going to import OS, OK, that's part of the Python standard library. And let's say we wanted to import, maybe say, getpass. That is also part of the standard library source, the import getpass So let's just say this is all we're going to import from the standard library.

00:03:41
Let's just treat this as its own little block. Now, what we should do here, really, to make this a little bit easier to read and to interpret is to switch these around because, alphabetically, getpass comes before OS. So let's just quickly switch that around then, here.

00:03:57
So we'll move OS down, and we'll paste then getpass. OK, so these are our standard library imports. We can actually even use a comment to maybe even denote that, imports. And then let's leave a little bit of space to let us know that here, that is all that we have from a standard library.

00:04:13
And if you want to import from a third party, now we can do our imports here. So what I can maybe do here is, say import rich, which would be the rich library. And I could also import, say Scrapli. And alphabetically R comes before S, so that is the order we would want to use.

00:04:31
And these would be our third party imports. And then at the very bottom, we would want to import from our local modules, which in this case, we only got my-maths created, so I could say import my-maths, say local import. And this is a type of format, we want to be following, standard, third party, local.

00:04:50
And like I say, as we saw before, we don't actually just have to import the entire module, we can import explicit things that we want. So say, for example, as opposed to, importing the entire rich library, I could just say, from rich, import prints. And again, if I want, I can give that an alias, like, rprint.

00:05:11
And that's the style following the same type of convention. And similarly, with Scrapli, what I could say here, is from Scrapli, going to driver, and then core, and then I could import the IOSXEDriver, for example. And similarly, if I just wanted to import something particular from the My-maths module, again, I could as opposed to importing everything, say, from my-maths.

00:05:34
And let's say I wanted to import the multiplier function, I could import the multiplier. And again, this is still following the same convention standard library at the top, third party in the middle, local import at the bottom. And with respect to each section, we are following our alphabetical order, G comes before O, R comes before S.

00:05:55
And this is going to make it nice and readable, and easy to interpret for people using your code, as well as yourself looking back at old codes to identify what is being imported, what should be imported. And this is going to keep things nice and predictable, nice and structured.

00:06:10
So when you're dealing with other people's code or other people are dealing with your code, or even if you're looking back on your old code, yourself, that nice, predictable structure is going to make it really easy for you to eyeball and ensure you have your correct imports as they should be.

00:06:25
So these are some of the best practices when dealing with imports, structuring those imports. And I hope this has been informative for you. And I'd like to thank you for viewing.

***Quiz***

**Which of the following should be imported first?**

+ local imports
+ **standard library imports**
+ third party imports

---

## Structuring Code

00:00:00
Hey, guys, and welcome back. So what we're going to be talking about in this Nugget right here is a really important subject. This is all about how we're going to structure our codes. Because we want our code to be nicely structured, so we want to be adhering to best practices.

00:00:26
Now, the very first thing, which I want to discuss with you, is the concept of code which is importable and code which is executable. Because when you're actually writing code you may be defining a particular function. That should be code which is effectively importable you can reuse that function.

00:00:44
But if you happen to call that function, this would be when you're actually executing that code. Now, what I want to do is to show you a very common Python convention that you're going to see all over the place. And at first, if you haven't seen it before, it may look a little bit confusing.

00:00:59
And what that convention is, it's a conditional statement. It's going to say IF, double underscore, name, double underscore, is equal to, and then the string value, double underscore, main, double underscore going to have this conditional statement. And this conditional statement is actually going to help us separate our executable code from our importable code.

00:01:23
What in eff am I talking about? I know that sounds a little bit abstract. The best thing, as always, is to see it in action. So how about we open up a script and dig in then. So let me create a script called NTP stuff. Super creative. You know me, as per usual.

00:01:38
So let's go and write some code then. We'll go into NTP stuff. Now, what I'm going to do here is to define a function. Now, because it has a function, we're going to be using a lowercase and toolbox here. So let's separate it with an underscore. And I'll just create a function called NTP server.

00:01:54
And I'll give this a default value of all the 99s. OK. All this is going to do here is this function is going to print out an IF string, which says NTP server, colon, and then whatever NTP server is passed down. And of course, if none is passed down, we get the default value of all the 99s.

00:02:12
So this here is code, which is importable. We could say from NTP stuff, and we could import that function, because import NTP under server it's called. Here is the thing. Within this actual script here, this NTP stuff, perhaps I actually wanted to call this function.

00:02:31
So let me show So I go down here. And I'll just call NTP server. And I won't use the default value. I'll actually use the value 1, 2, 3, 4. So if I save this, what we have here is, this is importable code, code which we can pull into other scripts. Whereas, this here is just executable code we're just calling that function.

00:02:53
So we'll actually print this out as 1, 2, 3, 4 value for the NTP server. So check this out then. If I say Python3 NTP stuff. Cool. We'd get out our print statement, which is exactly what we were expecting. However, like I say here, we do have this code here, which is importable.

00:03:12
And let's say, for whatever reason, this is a very useful function, if we want to be able to use within other scripts. Now as it transpires this is a pretty basic function. I can't imagine anyone would really want to import this and reuse this function.

00:03:26
But play along. Let's imagine this as a little bit more complicated and a little bit more useful at least. So we want to be importing NTP stuff. And what I want to do is to show you exactly what happens here. So I'm going to actually go into the Python interpreter.

00:03:41
We're going to IPython. And remember that the module is called NTP, underscore, stuff. And what I'm going to do here is just import that module. So I'll import NTP, underscore, stuff. And if I hit enter, watch what happens. You see that? It's not just importing the importable code, the executable code is also being run.

00:04:01
Because when we do this import statement, in effect, what is happening here is we are importing this file, therefore the entire file as a whole is being evaluated by Python. So when we import it Python sees this function here. But it also sees we have executable code.

00:04:18
So therefore, it means that we're also going to execute this. Now this is not very good if we just want to be able to use particular pieces of code. Say for example, this part right here. We don't actually want to use this part, but it has value here.

00:04:31
So a real neat way to get around this is again, is to be able to cleanly separate out what is importable and what has executable. And we're going to do this using this IF statement. And that's IF, double underscore, name, equals, double underscore, main.

00:04:47
So let me first show you how it's going to look first. And then we'll actually repeat our steps or rather walk back or steps, and evaluate what exactly happened. So I'm going to, as opposed to just running this code here, I'm going to put this part, the executable part, within an if statement, a conditional statement.

00:05:06
I'm going to say if double underscore, name, is equal to the string value, double underscore, main, and a colon. And because we have an if statement, we're going to have to indent this. So let's just move this over a little bit here. There we go. So what I want you to do is to watch what happens now we have added this if statement.

00:05:25
And like I say, the purpose here is to separate out our importable codes from the executable. So this is almost acting like a line. This is just going to break in this in half. I checked what happens. If I tried to run the script NTP stuff, we're actually going to get this printout here, which is exactly what we want when we're running the script itself.

00:05:45
So let's arrow up and run the script. So we're still getting the desired effect when we actually execute the scripts. But watch what happens if we try to import NTP underscore stuff plus go back into IPython. And we just import NTP underscore stuff. Hit enter.

00:06:02
We get to import that code, but notice that the executable part is not running automatically here. So now we could use it. We can say NTP stuff dot NTP server. And we could put in a value like say 22, 33, 44, 55. And if I hit enter , we can now use the function within this.

00:06:23
But just by importing it we're not going to get that sudden execution that we didn't plan for. So what exactly happened here then? Well, Python is going to use this magic variable you can call it, this double underscore name. And this value is automatically going to be assigned a value double underscore, name, double underscore.

00:06:43
When we run this file natively, i.e. when we actually execute NTP underscore stuff. However, when we actually import this file into another file, that's magic variable is not going to be set to main. It's going to be set to the name of the module. Now again, this might be a little bit hard to follow.

00:07:02
It may be a little bit confusing at first. So let me just quickly show you what I mean here. So what I'll do right now is I'll just comment out this part of the code right now. OK? Comment you out. Comment you out. And all I'm going to do here is I'm going to print out this magic variable, OK?

00:07:18
So I'll use an F string and our parentheses. And I'll just print out name. OK, and now that uses it. Make this a string, of course. So all this code is going to do is, we have defined this NTP server. But notice that we're actually not even calling it.

00:07:32
So we're not caring about that right now. All we want to know here is, what is the magic variable here? What's it going to be set to when we run it directly from the script? So check this out. So if I save this. So let's run that script and in effect call the magic variable.

00:07:46
So I have to hit enter. Notice what it's printing out. It's actually printing out double underscore main. So if we run the script directly i.e. we happen to say Python3 NTP stuff. Running it directly, that magic variable has been set to double underscore main.

00:08:03
Check this out, though, what would happen though if I import that code? So again, if I happen to import this entire module onto something else, what it's going to do is we'll go line by line. And you'll notice that we're going to run this exact same call here.

00:08:17
But this time, because it's been imported, the magic variable double underscore name is going to take on a different value. It's going to take on the value of the name of the module. This time it's not going to print out double underscore main. It's just going to print out NTP underscore stuff.

00:08:34
So check this out. So let's go into IPython, so we can get that quick execution. And if it imports NTP stuff, it shouldn't print out double underscore main. It's going to print out-- let's hit enter. As you see here, that variable is now being set to the name of module.

00:08:50
So what is the implication of this then? Well again, let's go back to our script. So let's delete this part here. And we'll un-comment out this part once again. So what we are in effect doing here is saying IF double underscore name is equal to main, then run this executable part of the code.

00:09:06
Basically, we're seeing as, if you run this file directly, like say, Python3 NTP stuff, then we want this part of the code to execute. However, if we just import this into another script, we don't want the executable part to work. We just want access to the importable code, so that we can reuse it.

00:09:25
And this is how we're going to get this nice clean separation. So just to highlight this. Let's see we had more importable code. We wanted more function. Let's say we had one which says VLAN caller. And we'll have an argument VLAN. And again, super simple.

00:09:40
It's just going to print out an IF string. Just say the VLAN is called whatever VLAN we pass in. Now, if we wanted to run this code within the script, well, we could call it, of course. We could just say VLAN caller, and put in a VLAN. Let's see VLAN 5.

00:09:56
And again, if I happen to run this code say Python3 NTP stuff, which is not really a good name anymore because we're now using VLANS as well. But nevertheless, if I hit enter, we have our executable portion of the code executing, because we are running the script directly.

00:10:14
However, if I happen to import this code, print to IPython, and we'll import NTP stuff. Again, which is a pretty poor name now, given we have a VLAN function. So if I import this, nothing has been automatically executed. These parts here don't execute, because the name variable when been imported as the name of the actual module, is not the name double underscore main.

00:10:37
And now, like I say, we can use NTP stuff and a totally different script. And we can get access to all that importable code such as VLAN caller, that function. And we can put in, let's say, VLAN 52. If I hit enter, we can use that function, quite the thing.

00:10:52
And you say NTP stuff, NTP underscore server, six, seven, one, two. Hit enter. So now we have access to all of this importable code without worrying about the original executable code executing where we don't want it. And that's just really how we want to be structuring our codes.

00:11:11
So let me show you a classic example of how you we're actually go into structure a code, generally speaking. Create one called structure example dot POI. Let's open this up. OK. So here is the general layout that we're going to see. At the very top, we're going to have our imports.

00:11:26
Let's just say import OS, maybe from rich, import, print as rprint. So here we have our imports. And again, we know how to structure our imports. Next, we want to specify what would be our constants. So let's say you had the constant value. Let's maybe say we had a DNS server.

00:11:44
Where we say DNS underscore server. And again, because it's a constant, we want to be using uppercase. And this the value which is going to stay the same, we'll use Google's DNS server of all the 8s. And now, under that we want to specify whatever functions we may have and whatever classes we may have.

00:12:02
So I might say def. Let's just have a simple function, which says hello. We'll just print hello. We'll have a function which says goodbye. Print goodbye. And again, we can maybe have classes here, testOSPF. You get the deal. But OK that's the thing. Very often it is good to define a main function.

00:12:21
No there's nothing syntactically important here. Python doesn't actually recognize the word main as some kind of special name. That's just a type of convention, but it's a good way to follow how the code is actually going to execute. So what we would do here is, we would define a main function.

00:12:36
And this is how we actually want the code to execute within our program. So let's say the first thing we wanted to do was to print out with an IF string. Just say DNS server as-- and then I can pass in my constant, DNS server. That's the first thing I want to happen in the script.

00:12:54
The next thing I want to do is to call my say hello. In fact, do you know what I'll do? Let's call say hello first. So we'll say, say hello. And we'll call that. We'll then print out the DNS server as DNS server. And then we're going to call the say goodbye function.

00:13:09
Now, if I happen to save this right now, and I tried to execute this code, nothing is going to happen. Say structured example, hit enter, nothing happens. Why is that? Well, because the code is not actually being called. The main function is what's actually is going to run everything.

00:13:26
But the main function itself has to be called. So what we could do here is we could say main, and just call it. And that would mean that we would execute the codes. We arrow up now. We're going to get that effect. However, we know that we want to separate out our executable codes from our importable codes.

00:13:46
So what we want to do here is to do a little trick. We'll say IF name is equal to double underscore main, then we have a conditional statement. And what do we want to do? Well, we'll just call the main function. And this is a good example of how to structure your actual codes.

00:14:02
Because what it means here is that we have this nice consistent structure. We have our imports at the top. Then we have our constants. We can have our functions and classes. These are things which we can import. But like I say, if we happen to import this module, we're not going to automatically just run the main function.

00:14:20
The main function is only going to be run if we directly run this fail by saying Python3 structured example dot PUI. Before I do anything, I just noticed I should actually make that double underscore as well. Let's save this. OK. So now we have that conditional statement.

00:14:36
If I try to run this, then the main function is going to be called because fname is equal to main is going to evaluate true, when we run it directly like this. However, if we want to import this code, say, for example, touch. Let's call this import stuff.

00:14:51
And I can open this up. I can actually import structure example. And the main function is not automatically going to be run. So if I run import stuff right now, nothing is going to happen. That code is not going to execute because it's being imported now.

00:15:04
See that? Which means that we can just selectively use part of the module we want as opposed to having everything within the main function run. So let's just say I wanted to use the say hello function. I could take structure example dot say hello. And I can call that here.

00:15:20
We'll save you. So I can neatly reuse this part of the code very explicitly. If I hit enter, I'm just getting the say hello function operating. And that's really as a nice, reliable, and well-established way to structure your Python codes, imports, constants, functions, and classes, and then preferably, define a main function to show how the code should actually execute.

00:15:43
We're going to run this function, then print this out, then run this function. And then have that conditional statement to specify IF name equals main, then run the main function. Otherwise, do not run the main function. Just leave this as code, which is effectively importable, which can be imported into other Python modules.

00:16:03
So if this is the first time you saw this. This is certainly going to be a little bit confusing. It took me a few times to get my head around what exactly was going on. If you're finding that yourself, then just rewatch the video maybe two or three times.

00:16:14
And then hopefully it should sink in. But for now that is us on Python code structure. I hope this has been informative for you. And I'd like to thank you for viewing. 

---

## Linting Code

00:00:00
Hey, guys, and welcome back. What we're going to be talking about in this Nugget right here is a really important subject. This is called linting. And what linting is all about is pretty much testing everything that we've put into practice so far. A linter is going to run your codes and basically try to find errors on it, things which you may have done wrong, things which are not holding to the conventions, or simply just point out flat out errors you have in your codes.

##### 00:00:37
Let's check this out and see how this works then. So what I'll do here is I'll create a file called "bad example." That's the stuff you actually shouldn't be doing, OK? So that'll be fun. OK, so at the very top, what we'll do here is we'll import, we'll say, NTP stuff.

##### 00:00:52
So that is a local module. And we'll put that before something like say, something from the standard library like import OS, OK? So our imports are the wrong way around. Let's create a constant. And we'll just say l, and we'll make that equal to the value 7.

##### 00:01:07
In fact, let's make it an integer. And we'll see def and let's write your function in capital letters. And we just call this "capital function." And we'll just print out "bad function." And what I'll do here is I'll also just print out something which says, this is a really, really, really, really long line, OK?

##### 00:01:28
We'll create a class. And let's not follow the convention. Let's just call this "bad class." And we'll just pass on it. And for now, that'll just do. OK, so a few things are wrong here. Like I say, we've got our imports around the wrong way. We have a function which is not following the function name convention.

##### 00:01:45
We have a lane which is far too long and a class that is not following camel case. So let's say you wanted to evaluate this. What we're going to do here is import something called Pylint. That is going to allow us to lint our code. So what we'll say is Python3 m pip install Pylint.

##### 00:02:01
Alternatively, you could say, pip 3 install Pylint. And we're going to install that into our virtual environment-- cool. So what I can do here is a Pylint and lint not fail, just by specifying the name of the code, or rather, the name of the file, should I say.

##### 00:02:18
So let's hit Enter and see what we get. And Pylint has actually rated this as negative 5 of 10. So it's really quite bad. So we can see things like, say for example, our line as too long here. We have trailing new lines. We have a missing docstring module.

##### 00:02:34
The constant name doesn't conform to uppercase. The function name doesn't conform to snake case. Class name doesn't follow Pascal case, a.k.a. camel case. We've got an unused import and unused imports. And our import order is in the wrong way. So we can see some of the things that we need to change to make this code a little bit better.

##### 00:02:54
So let's try and improve some of it then. Let's just call this "my constant," OK? And we'll actually use this constant. We'll print it out. So what we'll do here is we'll save this. And let's try clearing the screen. And we'll arrow up and rerun Pylint to see if we get a better result this time.

##### 00:03:11
Hit Enter. Case or code is still pretty terrible, but now it's only negative 2.2 out of 10. So our previous run was minus 5. We have actually improved it two points or almost three points. But as we can see here, we still have a lot of things to fix.

##### 00:03:24
One of the things we can fix here is using a docstring [INAUDIBLE] function. So what I can do here is have a docstring. So you just see this function prints stuff-- not the best docstring, but you get the deal. And I'll change the name of the function from uppercase down to lowercase.

##### 00:03:38
And I'll use my separation with my underscore. Save this, arrow up, hit Enter. So now our code is only getting a nothing out of 10. It's still getting a little bit better. We've improved two points yet again. Let's improve it again. What we'll do is we'll put the standard library at the top.

##### 00:03:53
We'll say import OS above. We'll also change the name of the class to suit the camel case. We'll call it bad class. And in fact, let's change it to "better class" because we're actually using a better convention though. And actually we'll add a docstring to the top of the module, like we actually should as well.

##### 00:04:10
This module demos linting. Let's save this. We arrow up. Try again. So now we're getting 3 out of 10. We're getting less and less problems. As you can see, we've actually improve in our codes. But as we can see here, we still have an unused import from OS and NTP stuff, plus also call NTP stuff.

##### 00:04:28
So it's not unused. And we'll also add a docstring to the class here. Just say demo docstring. And in fact, before I actually use NTP stuff, I need to actually call a particular function within it. So I'll call the NTP, server function, and have this docstring [INAUDIBLE] past statement.

##### 00:04:45
We don't need that. It's about unnecessary now. Let's save here. And if we run the scripts, we're now getting a rating of 7.27. And as you can see here, Pylint is just going to keep giving us information about solutions that we have to fix. Now here's a thing.

##### 00:04:59
If you want Pylint to lint all of our Python files, what we can say here is Pylint and just say, star for a wild card, i.e. anything that ends in dot py. And if I hit Enter, we can actually get a rating of all of our codes here. So we can see the module structure example.

##### 00:05:15
Here's the problems with this module, NTP stuff. Here's the problems with that and module "my maths". We can see all the problems with it. So linting really should be a part of your tool belt for sure, especially when you're working collaboratively. It allows you to-- or rather, it forces you to follow proper convention so that everyone is singing from the same sheet.

##### 00:05:36
So that is linting within Python. It's so, so useful, so, so vital. Definitely check out Pylint. It's going to improve your codes. And it really is a great learning experience to have all the little errors within your code pointed out to you, so that you can systematically correct them and get a feel for what should be correct.

##### 00:05:54
OK, I hope this has been informative for you. And I'd like to thank you for viewing.

---

## Formatting with Black

##### 00:00:00

Hey guys and welcome back. So in the previous Nugget, we had just checked out Pylint. What we're going to be looking at in this Nugget right here is the Black Code Formatter. That's just going to automatically format your code in a very particular way, and it's very good when working with teams, because if everyone is using the same format, we're going to enforce a little bit more consistency across our code.

##### 00:00:33
So what we'll do here is install Black. I'll say, python3 -m pip install black. Again, you can say, pip3 install black, if you so choose. And that's just going to install Black folders. So if you happen to [INAUDIBLE] for Black, you can find it on GitHub or on PyPI.

##### 00:00:47
And basically, as you can see, Black is designed to save you time and mental energy. So this is a really useful tool. I certainly would recommend that you use it. Let me just show you how we can use this now that we've installed it. So let me show you how that works.

##### 00:01:01
What I've done here is created a pretty poorly formatted file called unform. So look at this we've got some random spacing here. We don't have a space between our function and our imports. We have a rather long line here. And I'm just going to run this through Black.

##### 00:01:17
So look at unform right now as it stands. And if I just say, black unform, we're going to reformat that. Let's check it out now. Look at it now, that is a nice consistent format, and this is effectively all this tool is supposed to do. It's just given us a nice consistent format as to how our code is laid out.

##### 00:01:35
And the good thing about Black is, just like with Pylint, you can run it against all your Python files. So what I could just say here is, I could just say black, could say star .py-- i.e., blacken everything that is a Python file. If I hit Enter, we see eight files have been reformatted.

##### 00:01:52
Three of them are left totally unchanged. And it now means that all of these eight files, we can be sure, are consistent with the Black formatting structure. So using Black and Pylint together is a really powerful combination. It's going to allow you to write code which is error-free, code which is consistent, and code which abides by the best practices of Python.

##### 00:02:14
I hope this has been informative for you, and I'd like to thank you for viewing.