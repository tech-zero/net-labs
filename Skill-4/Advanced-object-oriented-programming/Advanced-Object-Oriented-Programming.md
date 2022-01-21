# Advanced Object-Oriented Programming

## Introduction

00:00:00
Hey guys, and welcome back to another skill in Python for network engineers. So if you're following along from the previous skill, you'll know that we covered this concept of object-oriented programming. And central to this concept was the idea of creating classes, and these classes had attributes and methods.

00:00:31
Now, the reality is there actually is a lot more to object-oriented programming that we could cover and just one skill. In fact, in this skill, what we've planned to do is to expand upon your knowledge. So what are some of the things that we're going to be learning on this skill right here.

00:00:46
Well, first, what we're going to be focusing on is the concept of private members within our actual classes. The private members are a very common concept within object-oriented programming and languages such as C++ and others. However, what you're going to learn is that Python implements as in a kind of different way.

00:01:05
It's almost like a pretend private member to be honest. What on Earth do I mean by that? Well, we'll get to that very, very shortly. Now, pushing off from this concept of private members, we are going to introduce the property decorator within the skill.

00:01:20
Now, decorators within Python are really just a way to get additional functionality from our functions. That sounds almost a bit like Inception, but that's kind of what it is. It's basically syntactic sugar which allows us to change the behavior of our functions.

00:01:35
Now, this property function is a built-in function-- or rather it's a property decorator should I say-- and we're going to see that it's going to allow us to make our methods act more like attributes. And this is a really nice feature. Now, whilst we're implementing this property concept, we're also going to be exploring the concept of getters and setters.

00:01:56
This is going to tie in nicely with our concept of private membership within our classes. Our getters are going to be able to retrieve those private members. And we're also going to create some setters to be able to change those values. Now, beyond that, we're also going to be looking at a different type of decorator, one called a static method.

00:02:17
Because you'll remember, within our previous skill, we had this concept of methods, just regular methods. Whereas a static method, this is going to act a little bit differently. Similarly, within this skill, we're also going to be looking at the concept of a class method, which, once again, acts differently from a regular method.

00:02:35
No surprises there, but it also acts differently from the static methods. Now, also a very big concept within object-oriented programming that we did not touch upon in the previous skill is the concept of inheritance. Now within Python, very often, you're going to be writing types of classes which are really quite similar.

00:02:54
Now, in order to be able to avoid having to repetitiously keep writing out the same type of classes with the same type of information, just with slight modifications, as opposed to doing that, we can implement this concept of inheritance. This is going to make our code much more manageable and much more scalable.

00:03:12
Now, inheritance is not the only thing we're going to be looking at. We're also going to be covering a concept known as composition. This solves similar problems to inheritance. This is going to solve in many cases, the very same types of problems that inheritance does.

00:03:26
But in particular use cases, you're going to see the composition is actually a much better fit. And lastly, like I say, in the previous skill, I did warn you that object-oriented programming is not the easiest thing to sync in. It does take a little bit of time, and the key here really is practice, practice, practice.

00:03:43
And this skill right here, that applies the exact same way. Really, if you need to watch this skill 2, 3, 4, 5 times, just do so. And certainly, lab up what you see on your time too. But I really am excited to get going. I think we've a lot of good things to learn within this skill.

00:03:58
The first thing we're going to check out is that concept of private members. And that is what we're going to be talking about in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Private Membership

00:00:00
Hey, guys and welcome back. So in this skill, what we're going to be talking about is this concept of private members within our classes. So like I say, in object oriented programming, this is a really big topic. And other languages that impose object oriented programming such as maybe C++.

00:00:29
Private membership is a really big deal. Now, within Python, this can also be implemented but also kinda not, which sounds a little bit strange. But you're certainly going to see what I mean here once we walk through this example. So let's first talk about what exactly this is, then.

00:00:45
So remember from the previous skill, we found out that when we were creating classes, we could have things like attributes and methods. Now here's the deal. What are attributes? Everything we've worked with so far were public attributes, and with methods simply we had public method.

00:01:02
But the reality is, we can also have private methods and attributes. Now what a private member is all about, is that private member can only be accessed internally from within the class. Now, this is how it is traditionally implemented. Here is the deal with Python, though, but it's a little bit strange.

00:01:21
With Python, we can only indicate that as our intention-- that we don't want someone to access it from out of the class. We don't want someone to access a particular attribute and modify it externally. But the key point here is that Python does not implement this.

00:01:35
It is not enforced. It's almost like a traffic light, where we can put up the red light to say, listen, don't go. But it doesn't actually physically stop someone from slamming their foot on the accelerator and running through that light. It still is completely possible to break the rules that we're trying to lay out here.

00:01:51
Even though it definitely is not advised, when we implement these private methods in the private attributes, we are doing so for a good reason. And when you see that within some Python code, that is the assumption that you should make. So what exactly am I talking about that I'm saying you can access an attribute from within the class and accessing it externally?

00:02:09
What is actually going on here? Well, the best way to actually see this is, of course, as per usual, to demonstrate it. So how about we dive into VS code and let's find out what this is all about then. So what I'll do here is I'll clear my screen here.

00:02:22
So let me just create a file called, I don't know, maybe johnmodule.py. And let's go into VS code and edit this. OK, so let's say I'm going to create a class, which is going to allow us to create some emails. So what we'll do here is we'll use the class keyword as we saw before in the previous skill.

00:02:39
And maybe want to name our class. Let's just name it something like, say, create email. Now, that email is going to have some type of suffix i.e. What is the provider? Is it a Gmail account? Is it a Hotmail account? Is it an Outlook account, a proton mail account, and so on and so forth?

00:02:54
So let's say for whatever reason that we wanted to make sure that our user had a particular suffix that was outlook.com outlook.co.uk, and fine. Let's just leave it at that. So what we'll do here is create a class attribute. So let's just call this, let's just say, provider.

00:03:10
OK. And we'll have a list here. So the provider can either be Outlook.com or Outlook.co.uk. Again, the details of the example aren't too important. It's just conceptual here. OK, now what we want to do here is to create an initialization method so that we can have some instance attributes.

00:03:29
So let's just say def init, and we'll say self. And we'll also accept name as an argument, so we'll say name and then colon and if we hit Enter, we get our four spaces indentation. Now just like we learned in the previous skill, what we want to do here is to take the name we are parsing in and to bind it to the object that we are creating.

00:03:49
To represent the object, we're going to say self, which is what we've got here as the first posessional argument. And we're going to say self.name is equal to the name we are parsing in. Now what we want to be able to do here is to be able to generate an email from this class.

00:04:03
So let's create a new method, which is just designed to generate an email. So we'll say def and we'll just call this generates, OK? And again, we're going to parse in self, as per usual. And we will say colon and hit Enter. We get a four spaces indentation once again.

00:04:17
Now like I say, so let's say that we wanted to generate an email account that was used in one of the providers we have, outlook.com or outlook.co.uk. Lets say, however, we don't actually care too much. We just want to assign this on a random basis. So what I'm actually going to do here is I'm going to import the random module within Python, which allows us to easily create a random choice.

00:04:38
I'll just import random here and let's go back down to our methods. Hit Enter again. So the suffix we'll create is going to be equal to-- and if I can spell suffix correctly, that would be nice-- while doing this, I'll take the random module and I'll use the choice function.

00:04:52
And what I want to do is to parse in, what I actually want to choose from. Now I want to choose from is this class attribute here. So the way i can access this is by saying self.provider. So that means that the random choice module is going to randomly choose either outlook.com to be the suffix or outlook.co.uk to be the suffix.

00:05:11
Every time we run the script, it's going to choose one of these two randomly. Now what we want to do is to create an email with this newly generated suffix, that's random suffix. And the way this is going to be is, let's create an F string. And what we want to do is, for the first part of the email we want to take the person's name that we have just instantiated up here, OK?

00:05:29
So we'll take self.name, and we use an F string or curly braces for variable substitution. And then I want to use the @ sign. And then I want to append that to the random choice we've created, which is denoted by this suffix object we've just created.

00:05:44
So basically, we're going to take the user's name as the instantiate, and then when they run the generate method, we're going to take that name and then append it to either randomly outlook.com or outlook.co.uk. And then after that, we want to return the email back to the caller of the method.

00:06:00
OK, so right now, let's just try to use this, then. Like you say, we have this John module. Let me create a new one called example one.py. OK? And what I want to do is to import the create email class from this John module. So what I'll say here is from John module I'm going to import create email, great.

00:06:20
So what I'll do here is, let's just do a simple test. Let's actually create an email for a particular user. Let's just say my email is equal to create email, and we learn that we have to put in a name. So let's just say John. So now we've created this my email with the name John instantiated within the object, and we know can actually run the methods generate plus print, let's say.

00:06:41
We'll say print my email, and we'll use the generate method. And to call a method, as we know, we're going to have to use a parenthesis. So if we save that right now, and I go back to my terminal here-- let's actually run this Python three example one.py.

00:06:54
Hit Enter, and now we've generated john@outlook.co.uk. If I run that again, still the same. And if I run it a few times, there we go. We get the actual .com. Randomly, it chose co.uk the first few times. Then we got a .com. Then we got another .com, then back to co.uk.

00:07:10
So it appears like our actual module here is working quite just fine. Here's the issue, though. Check this out. Let me go back to my example one script. Now that I've created this object, this object has actually got access to those class attributes-- that is, the providers, the .com suffix, and the .co.uk suffix for the Outlook provider.

00:07:30
Now, here's the thing. This object now has access to the class attributes from which it was created-- the create email class. That means that it's got access to the provider attribute, which contains the two email addresses the outlook.com and the outlook.co.uk.

00:07:45
Check this, though. What if I did this? Before I actually generate my email, if I said my_email.provider-- what if I just overwrote that, and I made it something like, say, spam.com. Something that clearly was not the intention of the original code. The code is supposed to be very specific about creating a outlook.com or an outlook.co.uk.

00:08:06
And what we've done here is we've accessed this class attribute, effectively overwritten it. So now when we generate our email, watch what's going to happen. So if I run that again, hit Enter, now we're actually generating the spam module as a .com one, .co.uk.

00:08:21
So this is not the intention of the author of this module of the John module. Now, how can we actually solve this problem? Well, this is what I was talking about with the use of private members. If we happen to go back to our original module-- John module-- we can indicate to the user that a particular attribute or a particular method is not supposed to be modified.

00:08:43
Don't change this. It's there for a reason. Maybe you don't understand the reason, but I've actually put it here for a very good reason. So like I say, well as Python can enforce us. We can actually indicate to someone syntactically that this is the behavior that we are seeking i.e. don't change this.

00:08:58
Now, the way we can do this is by using the syntax of a single underscore before the actual name. So we say _provider, and this is going to denote that as a private attribute-- at least that it should be treated as such. And in fact, before I do anything, let me just say _provider here.

00:09:13
That's we're going to get the random choice between either one of these two. So let's save this and go back. So now if I try running the script once again, we're back to using the outlook.com and .co.uks. . So that doesn't actually give us any hard coded protection.

00:09:28
Like I say, the user can still run the red light if they wish. Watch what they would have to do to do so. In order to do this, if I go back to example one, the way they would have to overwrite that would be to overwrite one that was pre-pinned with an underscore.

00:09:42
That should be an initial signal to them that, hey, I'm using this code incorrectly. I can expect errors. I can expect, well, unexpected consequences, maybe. So if the user is having to change something that has been pre-pinned with this underscore, then the user should know, hey, by the way, I'm actually behaving in the wrong way here.

00:10:02
This is not what the original author intended at all. So let me save this. Add it up. So after I start running this skeptic game, we're back to creating spam emails. Now clearly, this doesn't actually offer us any protection, the fact that we have an underscore.

00:10:15
But it's a very obvious signal to me as a user that hey, maybe this is all my fault here. I'm actually doing something wrong, and that I shouldn't actually be changing this. Now, this is how Python is going to implement, as a little twist on the concept of private membership.

00:10:28
It's not going to be enforced. It's just that the author of the code is going to hint to you and hint to you very strongly by using a single underscore that this is something that should not be changed. OK, though. So know that we have some concept of what a private member is within Python and its limitations, let's now explore the property decorator to see how that fits into the picture.

00:10:46
And that is what we're going to be doing in the very next Nugget. So I hope this has been informative for you, and I would like to thank you for viewing.

---

## Property Decorator

00:00:00
[AUDIO LOGO] Hey, guys, and welcome back. So in this Nugget what we're going to be doing is talking about the property decorator. So to understand what the property decorator does, the first thing we have to understand is, what exactly is a decorator?

00:00:24
So let's first check that out. So I just went to the big old google machine and I searched for Python decorator. Now this is actually a pretty good explanation. What is a decorator in Python? Well, it tells us a decorator within Python is a function that takes another function as its argument and then returns yet another function.

00:00:43
So that sounds like function inception. What is going on here? Well, ultimately this is what it does. It allows us to extend the use of a function, extend its functionality, so to speak. And the crucial point here, it allows you to do so without modifying the original functions source code.

00:01:00
So that is what a decorator does. And you're going to be able spot a decorator within Python with the @ saying, what you do with an email. And what exactly is the property decorator? Well, the property decorator within Python is actually a built-in decorator.

00:01:14
Like it says here, a built-in decorator in Python, which is helpful in defining properties effortlessly without manually calling the inbuilt function property. Now in real terms, this is going to allow us to be able to create methods which are going to do such things like return information about other attributes.

00:01:30
But we'll be able to access those methods like they were actually attributes. So again, this is all very pie in the sky, all very theoretical, all very confusing. How about we actually get to some examples, so you can see an action is going to make things a lot clearer.

00:01:44
So let's dive back into our terminal. And for this one let's dive into ipython. So let's just create a class, and we'll just call this maybe, student, let's say. So if we have colon and Enter, we get four spaces and F What we're going to do is to create our initialization methods.

00:01:59
So we'll say def ```__init__```. We're going to take self as the first argument as per usual. And let's add on two more arguments here. We'll add on the name argument for the student's name. And let's add on one for maybe that identification number, which is called this maybe studentnum, whatever.

00:02:15
So we hit colon. Hit Enter. We've got four spaces indentation once again. Now we have learnt that we know about this concept of private membership. And let's say we wanted to implement this private membership, we could say, bind whatever you're passing in as an attribute appended with the underscore.

00:02:32
So we'll say self._name is equal to whatever name or person. So self._studentnum is equal to whatever student numbers being passed them. So now if I create a new student, let's just say, John is equal to-- if I spelled John correctly, that would be super usefull-- let's say student.

00:02:48
And the name is going to be John. On the student num, let's just set this student num is 1234. Now that's object John. And if we try to access the attributes, clearly, we can't just access it this way, because that is not the way it's been bound to the object.

00:03:03
There's no attribute called name. There is, however, an attribute called ```_name```. Similarly, but also as an attribute called ```_studentnumber```, because that would be bounded within the class definition. So we'll say ```_studentnum```, and that as the student num.

00:03:17
But clearly, this is not the most elegant way to access attributes here. So let's say we decide to implement some type of method. A method which can do this for us a little bit more elegantly. So let's clear this theme, and let's try from scratch. We'll say a class student, once again.

00:03:33
And say def ```__init__```, and again, name, studentnum. And we'll bind that to the object, ```_name``` is ```name```, ```_studentnum``` is equal to student num. And what will now do here is create a method, which is going to return the name and a method, which is going to return the studentnum.

00:03:51
So what we'll do here is to actually call this method, let's name it name. So that means when we say, .name and then parentheses, it's actually going to become this method. So we'll say name as the name of the method, and we're going to take self as an argument as per usual.

00:04:06
And all we're going to do here is return whatever self._name is. You see that? That's the trick within. And similarly, if I say def studentnum, again, take self as an argument, all we're going to do here is return self._studentnum. Let me just add a little bit of space in here to make this a little bit better to read.

00:04:27
OK, so check this out now. Let's create a new student then. We'll have a student called Knox, and we'll use a student class. We'll pass in the name, which is going to be Knox, and Knox's student number can be 5555, cool. Now, if we want to be able to access the attributes of knox._name, we can still do it this way, this kind of clunky way.

00:04:48
But we can also just call the name method, because that's going to return that value anyway. So what we can now do is say knox.name. Now, remember, because it's a method, we're going to have to use parentheses to actually call it. And now we get this private attribute.

00:05:02
Similarly, if we say knox.studentnum and call the method, we also get that attribute. So like I can say, we actually have to explicitly call this as a method. Let's try to introduce the property decorator to see how we can actually change this functionality a little bit and make it a little bit neater, a little bit more Pythonic.

00:05:20
So class-- in fact, let me just arrow up to speed things up a little bit. So what I want to do here is to actually decorate these functions, or rather these methods, should I say, with the property decorator. Now the way we do that is the directly above the methods, as we are going to say at property.

00:05:35
So the @ sign tells we're working with a decorator, and then we just give the name of the decorator. So let's check this out how this actually changes the functionality let's do the same thing for the studentnum. We'll also decorate this method with the property decorator.

00:05:48
OK, so let's save this, cool. So let's now create a new student. Once again, we'll say trevor is equal to Student. And that is going to be Trevor, and that's the student number it's just maybe 9999. Cool, now like I say, just as before, we can still access these attributes by saying trevor._name.

00:06:06
But remember we had this Trevor name method we called. See, because we've now used that property decorator, it's going to act like an attribute almost. So instead, we don't actually have to call this like a method if we just get rid of the parentheses, and just like we would an ordinary attribute, just hit Enter.

00:06:22
It's now going to return that attribute just like it was, a generic attribute. See that? So we can transparently get this information, even though we've appended that with the underscore before the actual name. So again, with trevor.studentnum. That's going to call the studentnum method, which has been decorated with the property decorator.

00:06:41
So we can just say .studentnum, and it's going to return what is effectively the _studentnum attribute, without having to do it that way. Now see what we've implemented right here. This is effectively called a getter. So what we want to also look at here is the concept of a setter, and this is going to allow us to change or update our values.

00:06:59
Now, you might be thinking John, this is an underscore attribute, a private attribute. Why would you try to do this? Well, the thing about setters is that they're going to be implemented with some type of control, some type of condition. So again, let's try this once again, let's go back.

00:07:14
So now, let's create our actual setters then. Now the way this works is, we're going to take the name of the getter method here, which is name. And we want to make a setter for that. So we're going to say at, and then the name here of the getter, and then say .setter.

00:07:31
Now that sounds a bit of a mouthful. Let's just see this in action. So we'll take the getter method, so name, and then we'll just say .setter, and then under that, we're basically going to recreate the same name of the method, we'll say def name once again.

00:07:44
And we're going to say self, but it's not just self, we want to be able to update the values, and we also want to take an argument this time it's going to be name here. So we can say name. And here, that's the thing like I say with setters, we don't just want to just simply set the value.

00:07:58
Let's add in some type of conditions. So let's just maybe say if the length of the name being passed in is less than two, i.e, it's only one character or no characters, and we want to effectively reject that. So let's say colon, and we want to raise something called a value error, saying this is not a valid value, and within parentheses, we'll specify a little custom message back to the user and say: Name must be at least two characters or more.

00:08:27
Cool. Now, if they pass that test, if it is two or more, what we want to do is just simply update self._name with the new name being passed in. You see that? Let me just actually give a little bit more space here, that's a little bit better. Similarly, let's create a setter for the studentnum, so we're going to say @, and then the name of its getter.

00:08:47
So we'll say @studentnum.setter, and then what we'll do here is just create a method with the exact same name. So def studentnum and we'll take self as an argument. Now again, we want you to have the option to update here. So we're going to accept another argument, which is going to be the potential update of the studentnum.

00:09:03
And again, let's add some type of condition. Let's test that the student number has to be an integer. So we know how we can do this. We've done this before previously by using as instance. So if not as instance, and what we do here is pass in the variable first.

00:09:19
So we'll say studentnum, followed by the type of data. So we'll say int, so basically, if it is not an integer, we want to add our condition. So we will say, again, raise ValueError, and we'll just say; Student number must be an integer. Cool. And if we pass that test, what we'll do here is just simply take self._studentnum and update that with the new studentnum that's been fed in, cool.

00:09:45
And again, let me just fix the spacing here, so it's a little bit neater. OK, so there we go. So if I hit Enter now, let's see how all of this shakes out. So let's clear the screen. Let's create a student called simona, and we'll use student class. We'll pass in Simona's name as Simona, and we'll give Simona a student ID number of 441122, whatever as an integer, cool.

00:10:07
So like I say, we can get Simonas' name, we can get Simonas' student number. And if we want to update that, we're going to have to update it through the setter, which has got that nice constraint. So I try to say simona.name is equal to S. It's going to say that the name must be at least two characters or more OK.

00:10:25
Similarly, if I want to update Simona's student ID, I can say simona.studentnum is equal to, and let's just say blah blah blah, which is always a student number. If we hit enter, it's going to say; Student number must be an integer. So this is the concept of the property decorator, how it effectively allows us to access our methods a little bit more elegantly, as well as the use of getters and setters.

00:10:49
Again, this is all about writing and much more pythonic code. It really is very nice, and you're going to see it all over the place-- whenever you're traipsing through GitHub, for examples. But for now, we've got more cool things to get onto. The first one coming up is going to be the static method, and that is what we're going to be talking about in the very next Nugget.

00:11:04
So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Static Methods

00:00:00
[AUDIO LOGO] Hey, guys, and welcome back. So what we're going to be talking about in this Nugget right here is the concept of a static method. Now, one of the important things to remember about the static method is that it can actually modify the state of the actual object.

00:00:27
The instance we create, static method is going to have no effect on that. Similarly, a static method is not actually going to be able to modify the actual state of the class either. This is something really, really important to know about static methods-- really, really limited within its scope here.

00:00:44
Ultimately, a static method is much more like a regular function that you would see within your code. In fact, pretty much any static method can be redefined as a function [INAUDIBLE] a class. So then you might be thinking, why ever even bother using a static method?

00:01:00
But really, a static method is when you want to create something that doesn't have access to an instance, or the class can't really change anything. But you don't want it to be a separate function on its own. You actually just want to conceptually link it to the class.

00:01:14
So as opposed to just redefining it as a regular function whereby it still can access the attributes of the instance or the attributes of the class, but we still want that connection to the class. And that really is a good candidate to implement that static method.

00:01:31
So let's check out how we can rate a static method and see what it's all about then. So once again, let's dive back into IPython. OK, so what I'll do here is I'll create a list of skills right now. So let's just say networking. Let's say we have Linux skills.

00:01:45
Let's say we have cloud skills-- how about Python, Golang, MySQL. And for now, that will do. So what we're going to do here right now is create a class, and this class is going to create a new cbt Nugget trainer, OK? So we'll just call this NewTrainer.

00:02:01
And what we'll say as def ```__init__``` as per usual. And we'll say self. And what we want to do here is to take on a skill, something that the NewTrainer is going to teach. I'm going to say self._skill is equal to the skill of the person. And again, we'll use our technique we've just learned about a property decorator.

00:02:20
And we'll create a method called skill with a reference to self. And all this will do will be to return self._skill. And let's just fix by the space in here to make it a little bit more readable. So let's say we wanted to implement a static method here.

00:02:35
What we can say here is @static-- because it's going to be using a decorator-- and nobody's going to define some type of function, or rather some type of method. Now the key thing here to note is that this method is not going to be contingent upon anything relating to this actual class.

00:02:51
That's just within this class conceptually. So because of that-- let me just give this method a name. We just say it random_skill-- now because this is a static method, we're not actually going to say self here because we don't actually have any kind of access to the instance of this class.

00:03:06
We don't need to say class here or self here. You just leave this empty. And what we're going to do here is to implement something which static methods are very, very useful for. And that is a factory function. Basically, it's going to create an instance of a class for us.

00:03:21
So what is the name of the class? Well, the name of the class is NewTrainer. And NewTrainer has to take an argument called skill. So what we're going to do here is to take one of these skills here and pass it on to the NewTrainer class and their initialization method.

00:03:37
And that is going to create a NewTrainer for us. And like you see, the cool thing here is that we're going to access this directly through the class. We don't have to specify sale for anything like that. So check this out then. Whenever somebody uses the static method, what we want to do is to return the class from NewTrainer.

00:03:54
Now the NewTrainer is going to take a particular skill. That's the argument that it takes. It says that here within their initialization method. Now what we actually want to do is to randomly pick one of these skills here. So what I'm actually going to do here is go to the top.

00:04:07
And I'll just import random once again. So all I'm going to do here is say random.choice once again. Now what is my random choice? Well, my random choice is going to be one of the skills. Now, notice that the skills here are not actually within the class.

00:04:22
They're not the same as in the class. They're actually [INAUDIBLE] the class. So take a random choice from the skills lists whenever we call this static method. Let's just close this off. There we go. So now check this out. So let's create a new cbtn person.

00:04:38
And the way we can do this is just by saying NewTrainer. So we don't have to create a new instantiation of the class here. We just access the class name directly. And then we're just going to call this method random skill. So we can see here randomskill, and just call it [INAUDIBLE] methods.

00:04:53
And it would be helpful if I actually said the correct name. That should be random_skill. So I'll say it random_skill. Try this again, hit Enter. And there we go. So now what I can do here is to find out what that new skill that cbtn person has. We can say new cbtn person, and what I can say is . _skill.

00:05:12
And that's golang. But like I said, because we have that property function, you can actually just say .skill, and it's going to get it through the getter. So we can just say .skill, and we have golang. You see that? So we don't actually have to create an instance of the class beforehand.

00:05:26
We just directly access the class and just called this static methods. So again, if we create a new one, once again, we see cbtn person 2. We just call the class directly. And then, we can just walk in and grab at method, at static method, one again, and we just say new cbtn person 2.

00:05:45
And find out what skill they have. Oh, we have galong again. That's not so cool. Let's try again. I've got a better example for you. Try 3. And the third one actually has MySQL as a skill. So we're not just getting golang. That was just all that we got through in the row there.

00:05:59
OK, so that is the big thing about static methods. They're pretty much like a regular function. But if you want to conceptually tie that function within your class for whatever reason, then a static method is where you want to go. And like I said, a static method is not going to have access or be able to modify the instance state or the class state.

00:06:17
And it's not going to take self as an argument. And that is the big difference between a static method and a regular method. But we also have another method to check out. And that is going to be the class method. And that's what we're going to be checking out in the very next Nugget.

00:06:30
So I hope this has been informative for you. And I'd like to thank you for viewing.

---

## Class Methods

00:00:00
Hey, guys and welcome back. In this Nugget, what we're going to be doing is talking about the class methods. Again, to use a class method, we're going to be using a decorator. Now, the key thing to note here, is that with a class method, we don't actually have access to the instance.

00:00:26
We can't actually modify that, but we do have access to the class itself. So let's check this out. This can be a little bit confusing at first, but let's just follow through. Let me just go back to my directory, activate my venv. OK, so let's dive into IPython.

00:00:42
So let's just create a pretty simple example. Let's say a human class, and we'll have some needs that all humans need. So we'll say needs is equal to, and we'll make this your list object. We'll say air. We'll say water, and we'll say food. Cool. Now, to actually create a human, we'll say def init.

00:00:59
Say self for the reference to the object and we'll also say name. What we'll do here is, say self.name = to name. And what I'll do here is, I'll create a class method. So I'll decorate this by saying classmethod. The method is going to be simply called needs.

00:01:14
Now here's the thing, usually with methods, we're going to have access to self. We notice that with the static method, we don't have access to the class or to self. In this case, pretty similar. We don't have access to self, but we do have access to the class.

00:01:29
So because of this, we're going to be able to have access to class attributes such as the _needs up here. So all we're going to do here is return cls, which is the class, i.e. human. That's all cls is representing, whatever the class name happens to be.

00:01:43
It happens to be Human. So we'll say, return cls _needs. Pretty simple. So if I wanted to create a human, what I could do is say john = a human. And John's name is going to be-- John, so we pass this in. Now, we have created an object called John of the type human.

00:02:01
Now, like I say, John has these attributes. So I can say john._needs and John needs air, water, and food. John probably also needs pizza, but we'll leave that just now. Can I check? Let's see. Watch what happens here. See if I happen to try to overwrite this and say John's needs are actually things that aren't really quite needs-- although sometimes I might argue that they are needs-- say ice cream, pizza.

00:02:26
I'd actually maybe say beer. So whilst I say John._needs appears we have overwritten these, which we have, but these are actually attached to the instance that is John. You see that? What if I actually call this needs method here? Let's check this out.

00:02:44
So I would say john.needs-- call this. That is still the exact same as before, because what we're doing here, in this case here, we have modified the attributes belonging to the instance. Whereas the classmethod is actually pulling back the needs from the actual class itself, which are air, water, and food.

00:03:05
You see that? So we overwrote it here, or so we thought, in the instance. Whereas the needs method actually just calls this, which is the human needs which is just here. So pretty different behavior. Now, let's also check out how we can use a factory function using these classmethods.

00:03:21
So what I'll do here is, let me create a class called-- let me think. Let's call this fashion. What I'll do here also say def_ _ init. We'll say self, and what I need to do is to pass in the actual style-- what is going to be the style. So I'll do here is, I'll just bind this to the object, and we'll make that equal to the style we are passing in.

00:03:41
OK, cool. Now, what I want to do is to create a classmethod, which is going to be a factory function for all these different types of styles. Let's create a style which is going to be-- let me think. Let's say funky. Because this the classmethod, we don't have access to the object, we only have access to the class.

00:04:00
So we can say cls. And all we're going to do here is return whatever the class is. And the class here, as we know, is called fashion and to initialize, we have to pass in a style. All I'm going to do here is to pass in a list of different objects. So if you're funky, maybe you wear bellbottoms.

00:04:19
Let's maybe say a flowery shirt, and we'll just say bike boots. So that is the funky style. So let's create another class method and we'll create this one called maybe gothic style. And again, it's going to have access to the class, which in this case is fashion.

00:04:34
And all we're going to do is return the fashion class and then pass in this type of style. So we'll say-- say trenchcoat, say leather jacket, maybe say Doc Martens boots. Let me just give a little bit separation here to make it look a little bit nicer.

00:04:50
And again let's just create one more classmethod. But let's call this one casual. Again, we'll pass in class. That's what we've got access to. And all we'll do is return the class and this time, we're going to pass in t-shirt, jeans, and sneakers. We call them trainers over here, but I'll say sneakers for my US friends.

00:05:10
So let's just close this off here, and again, let's add a little bit of space. OK, so let's just quickly recapitulate what's going on here. Like I say, if we want to create something using fashion, we specify the name of the class and then we have to give it a style.

00:05:24
So like I say, I could actually create one on the fly here. And I could say maybe swimwear is equal to-- and I'll call the fashion class. Now, based on a person, the style, which is going to be bound to the style. So let's just say maybe trunks and a towel.

00:05:39
So now if I say swimwear.style, swimwear has got trunks and towel, but that is because we did this manually. What we've actually got here are these prebuilt factory functions, effectively, and we can call them just by calling the method. So if I want to say-- let's create someone called Funky Fred.

00:05:57
So Funky Fred is going to have this particularly funky style. So the way we can call this is by calling the name of the class, which is fashion. And now we just in this case, call the name of this method. So we just say .funky. If we say funkyfred.style, Funky Fred's got that style.

00:06:17
You see that we just call it the right with the method really, really handy. It just generates, it straight off the bar So let's say Gothic Gary-- I don't know where I'm getting these names this from, honestly. And I'll just say fashion and we'll just call the gothic method here.

00:06:32
And if I say Gothic Gary-- let's see what his style is. He's got the trench coat, the little jacket, and the Doc Martens boots. Lastly, we say Casual Corey = to fashion and we'll call the casual method. Let's see Casual Corey. Let's see what his style is.

00:06:46
He's wearing a t-shirt, jeans, and sneakers. So very, very different. You see here what the class method again very useful for using factory functions. These kind of prebuilt arguments you want to hand into a class which will allow us to quickly spin up a type of object.

00:07:00
The big difference here is that we don't have access to the object itself, as we saw when we actually tried to modify the object attributes and the class attributes earlier on. And the big thing is that we're going to pass in class as the argument and not self, because we don't have access to that object.

00:07:15
But we do have access to that class. Now, again, I know that is a little bit confusing to get your head around if this is the first time you've seen this. The key here, I really do stress, is practice, practice, practice. OK, folks. I hope this has been informative for you.

00:07:29
I'd like to thank you for viewing.

---

## Inheritance

00:00:00
Hey, guys and welcome back. So now we have a super, super important topic and this is the topic of inheritance. So like I intimated at the very start of this skill, when you're writing classes, sometimes you might be writing lots of them. And very often there might be quite a lot of crossover things which have really strong similarities along those classes.

00:00:33
And the reality is you don't want to have to keep using the old copy pasta to pull the same type of code and just keep pasting it, and pasting it, and pasting it in different areas just because you need similar functionality just with a few little tweaks here and there.

00:00:47
Especially if you want to update something and now, because your initial code has changed, all the times you have pasted it all over the place, you have to modify all them too. This is not very scalable. It's not a good idea. But the good news is, we have this concept of inheritance and it's going to make our lives much, much easier.

00:01:05
So when it comes to inheritance, you want to be using an IS A model. Now, what on Earth am I talking about right here? Well, think about it like this. If I created a class called a dog, and I also created a class called maybe, say, a Labrador, well, a good test to ask yourself if you should be using inheritance or if it might be a helpful solution for you, is to see what the actual interplay between these two classes are.

00:01:32
And if you can say one is another, then it's a good idea that maybe you should be using inheritance. So what I'm talking about? We can say here that a Labrador is a dog. So if we had a class for animal, class for dog, and a class for, let's say, French bulldog, well, a French bulldog is a dog, so it may be an idea to inherit from the class dog.

00:01:55
And a dog is an animal, so it may also be an idea to inherit from the class animal. This is generally the thinking that we want to be implementing when we're talking about inheritance. Now, there also are some type of concepts here. Let me just discuss what they are.

00:02:10
In this example here, the base class would be animal. This is the most broad class, the more general type. As we get more specific, i.e., a dog is a specific type of animal, this would be known as a subclass of the base class. And yet again, even more specific, type of dog is going to be French bulldog.

00:02:31
This is going to be a subclass yet again. And the key thing to note is if we happen to have a clash of attributes, then the most specific is going to win. So let's just say, for example, we set some type of attribute here, like maybe say the sound an animal made, and we just say something general like loud noise-- this is not very helpful an example but just go with me, OK?

00:02:51
If we also say an attribute within the class dog with the exact same name, and we set that to the value of-- let's just say woof. Then if we happen to instantiate an object based on the class dog and we called that attribute, woof would take precedence over loud noise.

00:03:06
It's more specific. Therefore, it's going to win. Similarly, if we happen to instantiate another object with the class French bulldog and we set its sound attribute to be yap yap, even though French Bulldogs don't really yap, if we actually instantiate the object from the French bulldog class, it may inherit all of these other attributes of class dog and class animal.

00:03:28
But if there happens to be a clash, i.e., what sound does it make, woof would overwrite loud noise but yap would overwrite woof. So ultimately, if we derive from this class, the noise it would make would be yap yap. It's the most specific. So again, this might be a little bit abstract to think about right now.

00:03:44
Let's dive into the code and look at some examples then. Let's create a new example here. We'll just say example2.py. Let's open this up. So Example 2. Check this out. Let's create a base class here, and we'll just call this one dog as we just said there.

00:03:59
Keep it quite simple. So just close this down. And what we'll do is we'll create our initialization method. We'll say def init, and we'll say self, and we'll take the name of the dog as well as the age of the dog. And we'll say self.name is equal to whatever name we pass in, and self.age is equal to whatever age we pass in.

00:04:19
Now, this dog is going to have a particular method. Let's just say sounds. Again we'll just say self, and we're going to return the value WOOF. Cool. Let's create another class. Let's create a French bulldog. So we'll say class, and we call this Frenchie.

00:04:34
Now, if you want to actually inherit from the dog class, within parentheses, we're going to specify the name of the class you want to inherit from. So if I say Dog now, this is where we're going to actually inherit whatever the dog is. Here's the thing, we also want to take in those same arguments we took in from the dog-- that is the name and the age as well as self, of course-- because those have to be present for the dog to be initialized, and if we're going to inherit from a dog, they also have to be present.

00:05:02
But as opposed to having to reassign everything once again-- let's say take in self, and age, and name, and bind self.name to name and self.age to age all over again-- what we can do here is use something called super. Now, what the super method is going to do is effectively going to shorthand that for us so we don't have to keep repeating ourself.

00:05:23
Now, within VS Code, this actually does this automatically because I've actually specified that I'm going to inherit from the dog. Watch this. If I just say def_init-- see if I just hit Enter here, actually fills all this in. It gives us a super method and initializes it automatically with just name and age.

00:05:41
What this means is that we don't have to repeat this part here again-- self.name equals name, self.age equals age-- for every time you want to inherit. Pretty much by passing in name and age, it's going to act the exact same way here. This is the super init method.

00:05:56
So basically, we get the same attributes here. We're going to have a name and an age bound in the exact same way. And if you want, we can add additional methods which are not actually accessible to the dog class. So what we can say here is we can say def, and let's just say, I don't know, breathing maybe.

00:06:11
And we'll say self, and we'll return Gremlin because if you ever listened to a French bulldog, they're like little gremlins. I'll say their breathing is like gremlins. So check this out right now. Let's just save this for the moment. And in fact, what I'll do here is I'll initialize a dog.

00:06:27
I'll call a dog called murphy, and I'll make that a Frenchie. And I need to pass in the name and the age. So the name is going to be Murphy, and I'll make Murphy one years old. So here's the thing. If I happen to printout murphy.name, then we're going to get the name.

00:06:44
So if I just save this and run this script-- say python3 example2.py-- we get murphy. So it's the behavior is the exact same. We're getting that from a dog class here. We're just inheriting this behavior, name is equal to self.name. It's been bound automatically.

00:06:58
Same again. We can say .age. Cool. Go back. Rerun the script. Age is 1. Now, here is the thing. Because Frenchie is inheriting from dog, we're also going to get access to all of the dog methods because they are more general. So we can access this sounds methods.

00:07:14
So we can say murphy.sounds and we just call this because is in methods. And if we save this and try running this once again, look at that. Murphy was instantiated as French bulldog, but Murphy's also got the attributes of a dog. And similarly, we can also do Murphy breathing, which is actually just a method only accessible to French bulldogs.

00:07:36
So I can say breathing and call this as a method. Let's save here. And If I arrow up, run this again, the breathing is Gremlin. Now check this out, though. What if I happen to do it the reverse way? I'll comment this out. Comment this out. And let's instantiate an object.

00:07:51
This one will be called zeus. And Zeus is just going to be a dog. We're not going to specify what type of dogs Zeus is. But like I say, we're going to have to specify a name so the name is going to be Zeus and we'll make Zeus two years old. So check this out.

00:08:05
Exact same as before, we can say zeus.name. We'll be able to get that name attribute. Let's save this, arrow up, hit Enter. We have the attribute. Same again for, say, age. Save here. Try again. Arrow up, hit Enter, we get this. But what about these methods?

00:08:20
What methods do you think Zeus is going to have access to? Well, it makes sense that Zeus has access to the sounds method because Zeus is a dog and this is a method defined within the dog class. So if we actually try to call the sounds method, is Zeus going to say woof?

00:08:35
Well, he really should do. So let's save this and arrow up. No problem at all. However, notice that the inheritance only goes one way. If Zeus tries to get the breathing method, that is not going to be accessible. Because like I say, French Bulldogs inherit from dogs, therefore they get all the things that come with a dog.

00:08:54
But a dog does not inherit from a French bulldog. So it doesn't get all the French bulldog-specific things such as the breathing method. So if we tried to call this method here, breathing, Zeus is not a French bulldog, so Zeus is not going to have the gremlin breathing.

00:09:08
So really just think about this when you're are creating your Python classes. Is something related, and how is it related? Is something a type of-- like a French bulldog is a dog. Then really consider using inheritance to solve your problem because you're going to have a lot of overlap of attributes and behaviors, and it might make sense as opposed to trying to copy and paste absolutely everywhere.

00:09:31
Just be aware that the inheritance only goes one way and the more specific things overwrite the less specific. In fact, let me just quickly show you that just once again. So if we create a sounds method within Frenchie-- so let's just say def sounds, and we'll say self.

00:09:46
And let's return again-- not that they say yap yap but let's just say YAP YAP. So now if I comment this out of zeus and we recreate murphy once again, murphy is going to be a French bulldog. So if we happen to say murphy.sounds, there is two sounds methods.

00:10:02
There is a general one for the dog, but a more specific definition is the one for the French bulldog because French bulldog is inheriting from dog. So therefore, dog is more general. That means that when murphy goes to use the sounds method, it's not going to say woof, it's going to say YAP YAP.

00:10:18
So we'll print out murphy.sounds, and we'll call this method. If we save this, arrow up, and notice there's murphy saying YAP YAP, not WOOF now. That method has effectively being overwritten by the more specific method. Okie doke. So that's the general overview of inheritance.

00:10:36
You can really, really expand upon this. This is just really touching the bare bones of what you can do with inheritance. So just be aware of those rules and remember that super init method is really going to help you out. Next topic coming up is going to be composition.

00:10:48
That's coming up in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Composition

00:00:00
Hey, guys, and welcome back. So previously, we had just checked out inheritance within our Python classes. Let's now check out this concept of composition. Here's the big difference, really, when it comes to inheritance and composition. Like I say, when we were invoking inheritance, we were asking ourselves, is something a part of something?

00:00:34
That's not very clear. Let me rephrase that. Let's say, is that an "is a" relationship? So say, for example, a dog and a labrador. We can relate these two together by saying a labrador is a dog. Or you could maybe say musical instrument would be one class, and you could have another class called drums.

00:00:55
You could say drums is a musical instrument. Therefore, it's a good candidate for inheritance. Now, the difference here with composition is, you want to be thinking more on a type of "has a" relationship. So a drum kit doesn't "has a" musical instrument.

00:01:13
That doesn't make any sense. But what if I say something like, say, a human being. We had one class called human, and let's say we had a class called car. Well, we could actually make that relationship saying well, a human being does have a car. That is such a thing.

00:01:28
So then maybe, this might be a good instance to bring about composition to relate these two classes. So really, that is the big difference, you have to think about "has a" versus "is a." So let's do an example of creating a payment structure for an employee of an organization.

00:01:45
Let's check that out then. Let's dive into IPython then. And we'll say IPython. Let's clear the screen. And we'll say class, and we'll create class. And we'll just call this maybe payments. So how you're actually going to be paid. We'll say def init.

00:02:01
And we'll say self. And we'll take in what the wage is, the weekly wage and any type of commission. So what we'll do here is, we'll bind these to the object. So we'll say self.wage is equal to the wage. And we'll say self.commission is equal to whatever commission we pass on.

00:02:19
Now, if you want to create a method which is going to calculate the actual salary, which is the wages for all the weeks in the year, plus the commission-- well, we could do that. Let's just create one called salary, which would get the entire year. And we'll create our self object-- we'll pass on our self object, not create it.

00:02:35
Let me just give a little space here, actually. All we're going to do here is return whatever self.wage is, which is the weekly wages, times 52, because there is 52 weeks in the year. And we'll add on whatever commission that person gets. In fact, let's maybe change this to bonus, as opposed to commission, because a commission would be something you would get regularly, I suppose, wouldn't it?

00:02:57
It doesn't make much sense. Let's just say bonus, because that would be a one-off thing. So we'll make this sales.bonus. Cool. So let's create another class, and we'll just call this person and we'll say def_init_ _ and we'll say self, we'll take in the person's name.

00:03:16
And we'll maybe pass in the person's height. Let's say we want to be able to incorporate this idea of a payment to this person. So we can also person the wage and the bonus as arguments. So what we'll do here is we'll say self.name is equal to the name we pass in, and we'll say self.height is equal to the height we pass in.

00:03:35
Now, here's the thing. What are we going to do here? We already have this class here, which instantiates payment which has this method for calculating the salary. We don't want to have to recreate this once again. In fact, we just want to be able to delegate this operation to this class.

00:03:52
So this class can take care of this for us without us having to redefine anything. So what we can do here is we can say self-- and let's just reference the object here. So we'll say obj_, and we'll just say payments, since that's the name of the class.

00:04:07
Again, you don't have to name it. That's just a general convention I'm using right now. And we're going to make that equal to the name of the class here. That's how we're going to invoke this. So basically, we have in the class, and this class needs to take two arguments, a wage and a bonus.

00:04:22
So person, wage, and bonus. So basically, whenever we instantiate a person, we're going to name, a height, a wage, and the bonus. So whatever wage in bonus is passed then upon creation, we're immediately going to take that wage and bonus and throw it into the payment class here.

00:04:41
You see that? And whatever we get back, we're going to bind it to this object here-- or rather this attribute of the person, object, or rather this attribute of the instance we create from this person class. So what we can do here, is we can create an actual method, which is going to return the person's salary which is related to this person.

00:05:02
Let's just call this a yearly wage for this person. Again, let's just give a little bit of space here, actually. Make it a little bit cleaner. We're going to take self as an argument. I'll just say method here. What we want to do here, is return this attribute here self.obj payments.

00:05:18
So let's return this. This obj payment is basically delegating in this task over to the payment class. And this payment class actually has this salary method which calculates the salary based on the wage and the bonus which is being passed on. OK, so we're passing it straight in here, and it's been accepted up here.

00:05:38
So what we can just do here, in fact, is just call the salary method right here. You see this? Which is going to calculate it based on the wage and the bonus. But it delegating all of this directly to this class here. Check this out. If I just say .salary, and call that method now-- and again, let me just add a little bit more space here-- .

00:05:58
now what's going to happen here is that the person class is going to pretty much act like a container or a gateway for the payment class transparently. So now, if I'm now going to create a person-- and let's just call this person Michael-- and we'll use the person class.

00:06:14
And the person class is going to take a name. So let's just say Michael, it's going to take a height. So let's just maybe say 1.8 meters. You'll have a weekly wage-- let's just say he's got a weekly wage of say $500. And a bonus-- let's just say is a bonus of $5,000.

00:06:31
So if I hit Enter now, what I can do is say, my total wage is equal to Michael. And what we can do is just call this yearly wage method right here, which is transparently going to actually be using this salary method within the payment class. So I can say yearly wage-- just call this.

00:06:50
And then if I print my total wage, we get this value of $31,500 times 52. Add on $5,000. And you notice that we actually created this person class that was that-- we never actually explicitly used the payment class when creating this objects. And this one actually does not have any explicit calculations created.

00:07:10
The calculations are all within a different class completely, this part here, this method. But we were able to hand off that operation to this class transparently using composition. So that really is the big difference here when it comes to composition.

00:07:25
We're not thinking about "is a" relationship, we're thinking about a "has a" relationship. So a person has a payment structure, assuming they have some type of salary or job. So therefore, that was a candidate or a good candidate for use in composition.

00:07:38
And that is exactly what we did in this Nugget right here. So again, the best thing to do throughout that skill is to maybe watch two or three, four times maybe. And go through the labs, all the things we do within the IPython interpreter. And just keep practicing, practicing, practicing.

00:07:53
I hope this has been informative for you, and I'd like to thank you for viewing.

