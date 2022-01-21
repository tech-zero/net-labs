# Decorators & Generators

## Introduction

00:00:00:00
Hey, guys, and welcome back to another skill in Python for network engineers. OK, so check this out. We have a few kill topics we're going to learn in this skill right here. The very first of which is we're going to learn all about what decorators do within Python.

00:0:00:27
Now, previously, like so many things, we've had a very small exposure to the concept of decorators, but it really has just been a brief surface level exposure. In this skill right here, we're going to be looking at them in a little bit more depth so that we can really understand what is going on under the hood, and how they can help us write our code more efficiently.

00:00:47
And what decorators are going to rely upon is the concept of functions within Python. And because the concept of functions is so deeply intertwined within decorators, then I do think it does make sense to just do a quick recap on what functions are, and what we're actually going to do with them.

00:01:04
So that'll be first on the cards. We'll do a quick recap of what functions are, what they can do. And then we'll parlay that information into creating our first decorator. Now, the first time we actually do this, we're going to be doing it in a kind of long forum way, so that you can see more explicitly about what is really going on under the hood.

00:01:22
But what we're also going to explore is a little bit of syntactic sugar here. Because Python really is all about readability, we're going to actually see that there actually is an easier way to write your decorators using a particular type of syntax.

00:01:36
And quite honestly, this will be the recommended way to implement a decorator, so we'll certainly look at that. And what we're also going to be looking at, like I said, because functions are so deeply intertwined within decorators, we're going to look at how we can actually pass in arguments when we are working with our decorators.

00:01:55
And then we'll maybe do a little bit of exploration and create some example decorators, so that you can get an idea of their utility. So that really will make up the first main chunk of the skill. And then we're going to switch gears onto another topic called generators.

00:02:10

And again, this is something that we have just briefly touched upon in previous skills throughout this course. But once again, we haven't really dug into the details. In this skill, though, we're going to tie all that information together, just like we're going to do with decorators.

00:02:25
So the first thing we'll do is we'll have a nice overview about what a generator is. And then we'll learn how to work with generators, and how we can implement them using comprehensions. And we also, if we've got time, may also look at the advantages when it comes to efficiency, ie what kind of memory footprint they have when used.

00:02:45
So this is the rough blueprint for the skill right here. As per usual, we may take a little bit of a tangent here and there. But that is the core of the skill. And I really do hope that we're going to have some fun learning these concepts together. So with that said, however, I shut up.

00:03:00
Let's get back into the topic. The first thing we'll do is that brief recap on functions within Python. That's going to set us up very nicely to segue directly into the concept of decorators. Okey doke, so function recap, that's coming up next. And I hope this has been informative for you.

---

## Functions Recap

00:00:00
Hey, guys, and welcome back. So like I say one of the core components that we're going to be focusing on when constructing our decorators is the concept of using functions within Python. So before we actually dive into the details here, let's just do a very brief recap of what functions actually are.

00:00:28
Now, really, all a function is is a piece of code that is going to perform a particular task. Typically, what's going to happen is it's going to take some type of inputs. It will then manipulate that input by doing something. That's a very high-level description, do something.

00:00:45
And then after that, we're going to have an output. Now, if you recall from our skill on dealing with Python functions, you'll remember that Python functions, by default, are going to return the value none if nothing is actually explicitly returned. However, the way we can actually explicitly return the value is by using the return keyword.

00:01:05
We're certainly going to see this when we are using, or rather creating our decorators. Now what about this concept of taking inputs into our functions? Well, let's just quickly check this out then. So I'm just going to quickly dive into my director, go into my head in venv, and I'll activate my virtual environment.

00:01:22
Source bin/activate, okeydoke. So if I clear the screen and I go into iPython. So just in case you don't remember, the way we can create a function within Python is by using the keyboard, def. That's how we're going to define a function. So if I press space here, this is going to go green because this is the recognized keyword within the language.

00:01:41
Now, we're going to specify the name of the function. Let me just call this test_example. And then within parentheses, we're going to specify which parameters we want to take as arguments. Now, right now I'm not actually going to accept any arguments.

00:01:56
I'll just say colon. If I hit enter, I get my four spaces indentation. And in this case, all this function is going to do is just print out this as a test function. It's not the most useful function. So the way we can call this function, remember, is just by specifying the name of the function, which is test_example.

00:02:16
And then we call it using parentheses. Remember, we don't have to specify any arguments, because none were actually defined in the function. So if I hit enter now, all that's going to do take this code, execute it, and then print out this is as a test function.

00:02:30
But notice here, like I said, we did not happen to take any arguments. What if we wanted to change this up and we called this function, maybe, nameprinter? So we're actually going to take an argument here. And we'll just say name. And all this function will do-- that will print out an f-string, remember, so we can use our variable substitution.

00:02:47
And I'll just say it name printer, and then we'll specify using curly braces for variable substitution whatever name is passed into the function by the caller. So let's just finish this off here. Now if I say name printer, and I pass in, say, for example, John as an argument, that's going to be name.

00:03:06
Therefore, it's going to say, name printer. And then take that argument as the name variable, and then print out, name printer colon John. OK. That's no problem at all. OK. So clearly here we have the option whereby we can specify no arguments, or we can specify a particular argument.

00:03:24
And this case, we are passing in a string value. But remember, we can also pass in other things such as integers or floats. So if we create a function called adder. And I say num 1 as the first argument and nom 2 as the second argument. And all we'll do is print whatever num 1 is plus whatever num 2 is.

00:03:45
So we'll say plus num 2. There we go. So now if I say adder, I can now pass in-- as opposed to a string value, I can pass in the integer of 2 and the integer of 3. If I now hit Enter, it's going to sum them together, take 2, an add it to 3 in the result and the value of 5.

00:04:02
OK. So that is the brief outline of how functions actually work. But what I want to highlight here is that Python functions are actually referred to in Python, quite comically, as first class citizens. So this means they are going to be handled uniformly no matter what.

00:04:20
So that means they can be passed in as arguments or used in the control structures. Now, one of the cool things about the idea of a function being a first class citizen is that even though we've seen here that we can pass in nothing into a function, or perhaps a string value, or maybe even, say, multiple integers, what we can also pass into a function is another function.

00:04:43
So we can actually pop in a function as an argument to a function. And this leads us directly into your Python decorators. Because what a Python decorator is-- Python decorator is a function that takes another function as an argument. And what it does is it returns another function.

00:05:02
Now, if you're anything like me, when you read this your, head is probably swimming. That's just sounds confusing. It sounds very abstract. And I kind of comically term it as function inception. It's just kind of hard to wrap your head around just seeing this as a dry text on the page.

00:05:21
But ultimately, this is the core philosophy about what we're going to learn about when dealing with our decorators. So now that we've done a brief recap of what a Python function is, what they can do, and why you may perhaps use them, let's now look at passing in functions to our functions, and get our hands dirty by exploring the world of decorators within Python.

00:05:42
And that's what we're going to be doing in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---
## Creating a Decorator

00:00:00
Hey, guys. And welcome back. So in the previous Nugget, we had just learned that a Python decorator is a function which is going to take another function as arguments and returns another function. Now, the real main use case of doing this is that it allows us to basically extend our function, and it allows us to extend it in a way that doesn't actually require we modify the original function.

00:00:37
So this is really nice for writing clean code and being able to manipulate your functions without having to rewrite them entirely. You can just pass in through a decorator, and we're going to have that additional functionality extended onto it. OK, again, so like I say, this all sounds quite abstract, a little bit difficult to conceptualize.

00:00:57
The best thing I recommend, as always, is to dive in and start working with the data. So what we'll do right now is open up IPython and get right to it, then. OK, so let's jump into IPython. And what we'll do here is we'll write a function here. So we'll just say def my_first_function.

00:01:14
Now, like I say, we can take an argument here. So we can say something-- let's say a name or an age or a place-- whatever you want to actually manipulate. But remember, what we actually want to do here is to take in another function. So what I'm going to do here is say func.

00:01:31
Now, there is nothing special about the keyword "func". You could actually still call it "blah". But because it is another function that we're going to be passing into this function, that as per Python convention, it does make sense to make things as readable as possible.

00:01:45
So we'll use the keyword "func" to denote what that is. OK, now here is the thing. What we're going to do here is actually create a function within another function. So let's create one called my_second_function. And this one doesn't have to take any arguments.

00:02:02
We don't have to specify a function to pass into this here. We can just use parentheses. And all we'll do here is we'll just print out a simple statement. We'll just say, "BEGINNING TO EXECUTE THE FUNCTION!" OK, so that's the first thing we'll do is print this out here.

00:02:18
And what we're going to do here is now execute the function that we're going to pass in. So what is that represented by? Well, it's going to be represented by this keyword we've chosen here, "func". Again, there's nothing special about this keyword. But this keyword is going to represent that function.

00:02:33
So what we're going to do here is take whatever it is we pass in, which is going to be this function, "func", and we want to call it, remember, because it's a function. Now, how do we call it? We're going to just specify parentheses. And this means that immediately after we print out "BEGINNING TO EXECUTE THE FUNCTION!" we are going to call the function that we're passing in, OK?

00:02:54
Now, after we call this function, what we'll do is immediately after is we'll print out, just say, "THE FUNCTION HAS FINISHED EXECUTING!" So we have this little wrapper effect here. So what I now need to do here is I'm going to return the inner function.

00:03:09
So I'll say return. And that is going to be my second function. In fact, let me just do a little bit of space here. Cool. So check this out, then. We have a function. We're going to take a function as an argument. We have to find a new function within that function, which is going to print out something before we eventually call the original function that's being passed in.

00:03:30

And then after that's executed, we're going to print out another thing denoting that the function has finished executing. And then after that, we're going to return the inner function. So it's a function which takes another function as an argument and returns a different function.

00:03:46
OK, so let's see how this is actually going to shake out, then. So let's create a new function again. And this is going to be the function we're going to pass in to this up here, as denoted by this part here. So what we'll do here is we'll just call this greeter.

00:04:01
And it'll take no arguments. And all this function is going to do, it's going to print out, "Hello my name is John, very nice to meet you!" OK, so if I just happened to call greeter on its own, so I say the name of this function here, and I just call it by saying parentheses, it's going to execute this function, "Hello my name is John, very nice to meet you!" OK, that's cool.

00:04:21
But like I say, what we actually want to do here is to pass this greeter function here as an argument to this function right here. So what do you think is going to happen, then? Well, think about it. We'll pass in this function, greeter, which will go in here.

00:04:37
And then the inner function is going to say that we're going to print out, "BEGINNING TO EXECUTE THE FUNCTION!" Then we'll call whatever function we're passing in, which is effectively doing this, which means that we'll print out this part here. And after this function has finished, i.e. this, then what we'll do is we'll print out this here.

00:04:57
So let's see this an action, then. What we'll do here is we'll call our first function. We'll say my_first_function. And this is going to take an argument. What is the argument? The argument is going to be another function, which is going to be greeter.

00:05:09
And if I hit Enter here, it's actually going to show us that we have an inner function wrapped within an outer function. Now, what has actually happened here is we have returned the value. So if we remember from our skill on Python functions, when we return the value, we can therefore assign it to a new variable.

00:05:29
And what I'm actually going to do here is I'm going to assign it. Now, this is maybe a little bit confusing. I'm going to assign it to the variable name, which is the same name of the function that is being passed in. Again, this might be a little bit of a headache.

00:05:42
But just watch what I mean. So what I'm going to say here is greeter is equal to the very first function, so my_first_function. And we're going to pass in the function greeter, OK? So this is just a variable. This is a function, and this is a function.

00:05:57
And because it's being returned, this new variable is going to have whatever is returned from all of this here. OK, so what is going to happen here is if I just say greeter, and then I call this, just like it was a function, as it originally was, and I hit Enter, look at this.

00:06:11
The greeter function has actually been wrapped with this new behavior, the new behavior which was defined within my_first_function. And effectively, this is decoration, by passing the function in and assigning it to the same name. So this is the function here we passed in.

00:06:28
And we reassigned all of this behavior back to the same name. In effect, greeter now acts like a function which has been decorated with this new behavior defined within this outer function here, my_first_function. Now, again, this is all a little bit confusing the very first time you see it, because like I say, it's very much like Inception.

00:06:48
You just hear the word "function" almost too many times. So again, if I happen to create another function here, and we just call this one, maybe, dog_talker, and what I'll just do here is print out, "WHO IS A GOOD BOY?" OK, so if I just happened to call dog_talker, it's just going to execute this same print statement.

00:07:09
However, if I follow this decoration principle, and I just say dog_talker is equal to, and I'll say, my_first_function. And what am I going to do? I'm going to pass in the dog_talker function now, and, again, reassign it back to dog_talker. And it will effectively be decorated with this new behavior.

00:07:27
So I'll pass in the dog_talker function now. And now if I call dog_talker once again, we get this additional behavior. We print something else before the actual function is called. And then immediately after the function is called, we do this additional print statement.

00:07:42
So ultimately, what a decorator is doing, it is wrapping a function. It's giving it additional functionality. And this is what is happening under the hood when we create decorators. Now, there actually is a neater way to be able to implement this functionality, something that looks a little bit more readable, a little bit more Pythonic.

00:07:59
And it's just a nice piece of syntactic sugar to make our code much, much better to look at. What on earth am I talking about? Well, that's what we're discussing in the very next Nugget. So I hope this has been informative for you. And I'd like to thank you for viewing.

---

## Decorator Syntax

00:00:00
Hey, guys, and welcome back. So in the previous Nugget, we had just looked at our first decorator that we had just created. And at the end of that Nugget I happened to intimate that there might actually be a nicer way to be able to write all of this out.

00:00:25
Well, the good news is that I was not lying. There is such a thing. Let's check that out. OK. So what I'll do is we'll just start again. Let's just exit out of this, just to have a clean slate. OK. Now, before I actually do anything, what I'll do is I'll just make sure I have the rich library installed.

00:00:38
So I'll say pip install rich, which I already have. So let me go into ipython then. Hit Enter. OK. So let's clear the screen. And what I'm going to say here is from rich import the print function as rprint. This is going to allow me to easily use coloration within my prints.

00:00:54
So as opposed to just saying print john, I could rprint in red john again. OK. So what we'll do here is we'll write a very simple decorator that is just going to give us maybe a little bit of colorful output. So what we'll do here is we'll call this decorator-- let's just call it prettify, because it's going to make things look a little bit prettier.

00:01:15
OK. Now what does our decorator take as an argument? It's going to take a function as an argument. And what we'll do here is create an inner function. So let's just call this wrapper, since it's going to act like a wrapper around the original function we're going to pass in.

00:01:29
And this is going to take no arguments. And all I'll do here is use rprint, and what I'll do here is maybe say the color cyan. And I'll do some pretty stars, and we'll say cyan again. And then what we'll do here is we'll call whatever function that we're going to pass in.

00:01:46
And then immediately after I will rprint out. Let's just do the same thing again. We'll do cyan. And then what we want to do is to return the inner function, which is wrapper. So now we have defined our little decorator here. So let's say that I wanted to create a new function, OK?

00:02:02
So I'll say def. And let's just call this banner. OK. And this function is going to be super simple. All we're going to do is print out DO NOT ACCESS THIS DEVICE UNLESS YOU ARE AUTHORIZED. Cool. So like I say, if I just happen to call banner, it's going to print this out.

00:02:18
So what I could also do here, is I can actually just decorate this function as I'm creating it with the decorator I just created. So let me just show you what I had there. So I've got this prettify here. So what I'm going to do here is rewrite this same function, but what I'm going to do here is to decorate it.

00:02:36
And I'm going to decorate it with the classic syntax that you're very typically going to see. This is the same syntax we saw when we dealt with classes in a previous skill. Remember when we looked at static methods or class methods. Well, there, we were actually using decorators.

00:02:50
So what I'm going to do here is say the @ sign, and I'm going to specify the name of the decorator. So I'll say prettify. OK. And then immediately under it, what I'm going to do is to define my function. So I'll just say def banner. And what I can do here is just print out the same type of message, whatever it was, DO NOT ACCESS THIS DEVICE UNLESS YOU ARE AUTHORIZED.

00:03:13
Cool. So this is very similar to what we saw before. The difference here is that we've added this decorator right above the function right here. So now what I can do here is if I just call banner, we're going to get this exact same behavior. This banner function is going to be decorated with this behavior above here.

00:03:30
So let's call banner, hit Enter. And as we can see here, right above, we're going to get our stars printed with the color cyan. And below it, we're also going to get our stars printed with the color cyan. And what I could probably do here is actually just make this a little bit longer.

00:03:45
OK. Let's just fix that. And again, we'll clear the screen. Let's do the same thing, and we'll just call banner once again. And even then we're still a little bit short. I should actually be using more stars. But you kind of get the drift. What I've done here is, as opposed to just creating this function here, I'm able to neatly reuse additional code that has already been pre-written, this wrapper we have.

00:04:07
And the way we implement that into this function's code is just by using this decorator syntax, this @symbol followed by the name of what is the decorator function, the outer function effectively. So same deal. What you could do here for example is, let's just quickly create another one.

00:04:23
And let's just call this function here double call, and we'll say func to pass in. And we'll just call this one def inner. And all we'll do is we'll take whatever function we're going to pass in, we'll call it once, and then we'll call it twice. So effectively, it's going to be called doubly, OK.

00:04:40
And then we'll return our inner. OK. So what I could do is, for example, create a new function right here. So let's just call this one nuggetlove. And all this one will do is print I LOVE CBT NUGGETS. Cool. So if I call nuggetlove, it will only print it once, no matter how many times I use it.

00:04:59
However, if I happen to rewrite that and decorate it with the double call decorator, then we're actually going to get different functionalities. So lets just quickly rewrite that. We'll say @double_call, and now we'll define our function immediately below it.

00:05:12
So we'll say nuggetlove. Oh, and that would help if I actually used the colon. So we say def nuggetlove. And then what we'll do is I'll print, just as we saw before, I LOVE CBT NUGGETS. This time though it's been decorated with double call, which means that it's going to, in effect, be called twice.

00:05:30
So now, if we just hit Enter, there's that new function defined. If we call nuggetlove this time and we hit Enter, we have easily extended this functionality in this nice, neat, readable format. And this really is the type of syntax that we're going to be using when we are implementing our decorators for real.

00:05:48
This is much preferred than what we saw the rather manual way we saw previously, even though that was quite good to see what was kind of happening under the hood. This is a much more pragmatic and much more popular way to implement decorators within Python.

00:06:01
So now we're getting a rough idea of some of the functionality we can implement with decorators in Python. However, we actually have been a little bit limited, and that limitation refers to accepting arguments into our decorator functions. This is a problem we have not yet solved.

00:06:17
Let's dive right into it in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Passing Arguments

00:00:00
Hey, guys. And welcome back. So in the previous Nugget, we had just explored the preferred syntax to use when implementing decorators within Python. However, I did hint at a type of limitation that we might run up against. And that is accepting arguments within our decorated functions.

00:00:28
What on earth am I talking about? Well, the best thing, as per usual, is to see it in action. So let's dive into IPython and do some more exploration, then. So again, what I'll say here is from rich imports print as rprint. If I can type this correctly, that would be nice.

00:00:43
And what I'll do here is I'll create my decorator. So this decorator, let's just call it, maybe, something like, let's just say politeness, OK? And this is going to be a decorator. What is it going to accept as an argument? It's going to accept the functions.

00:00:57
So we'll say func so it's nice and descriptive. And then within here, what we want to do is to define an inner function. Now, this is just going to be a little wrapper around whatever function we pass in. So we'll just call it wrapper once again. Now, this is not going to accept any arguments quite just yet.

00:01:13
So what I'm going to do here is just hit Enter. And what I'll do here is I'll use rprint. And let's just maybe say yellow. I want to say, "Hello, thank you for using my code!" And we'll just end this with yellow yet again. And we'll just close this off with the color yellow.

00:01:29
Then what we want to do is to call whatever function we're passing in. And then we'll rprint, maybe a different color. Let's say green. And we'll just say, "Thanks, again! Hope to see you soon!" OK, so not exactly the most helpful code. But you get the drift.

00:01:43
We're just trying to highlight the concept here, OK? So what we want to do here is to return our inner function, which is going to be wrapper. So we'll return this. We'll return wrapper. Okeydoke, so we now have this function here called politeness. OK, so let's just create a new function here.

00:01:59
And what we're going to do here is we'll call this one-- let's just call this nameprint or something really simple. And this time, we're actually going to specify an argument we're going to take here for this function. So all we'll do here is we'll print out with an f-string.

00:02:12
And we'll just say, "Your name is" and then just print out whatever name they happen to pass in. Now, what we're going to do here is we're not just going to create this function. We're going to decorate it with this politeness decorator. So what I'll do is just directly about it, I'll say politeness.

00:02:28
OK, so the very big difference here is that we're actually accepting an argument in to the function that we are trying to decorate, OK? So watch what happens now. Everything seems fine. But let's try and use nameprinter then. So I'll say nameprinter.

00:02:43
And I'll just pass in the name Trevor. So if I hit Enter, it says here that wrapper takes 0 positional arguments but 1 was given. That is because we gave one here, but the wrapper accepts none. So you might think, OK, well, we can solve that pretty easily.

00:02:58
Let's do this again. Clear the screen. Arrow up. Let's go back to this politeness. And what we'll say here is we'll say wrapper is going to accept name. And when we call function, we'll say name here, OK, cool. So once again, let's do the same type of thing.

00:03:13
We'll go to nameprinter. And we'll decorate it with the politeness decorator. This time, though, we're going to actually specify that the wrapper inside is going to accept this argument here so we can pass it into the function call. So now if I say nameprinter, and I pass in Trevor once again, A, it looks like everything is working A-OK.

00:03:33
Now there as a big problem, though. This code has suddenly become really quite limited. Let me show you what I mean. So let's say I wanted to create another function, OK? Let's just call this one adder. Just as we did before, we'll set accept num1 and num2.

00:03:49
And all we're going to do is print whatever num1 plus num2 is equal to. So really quite simple, but again, what we want to do is to decorate it with politeness so we get this "hello" and "thank you" after we use this code. So we'll decorate it with politeness.

00:04:04
And once again, what we're going to do is to call this. And we'll say adder. And let's just try to add 3 add 7, which should give us 10. If I hit Enter, and now it's saying is that wrapper only takes one positional argument, which is true. It's only accepting one.

00:04:20
And now we are passing in two from the function. OK, so then maybe you think, what if we just change this to add in another argument so it takes two arguments as opposed to one? So we try that. So let's just call this num1 and then num2. And we pass this into the function-- num1, num2.

00:04:39
OK, so we redefine this. And then we try to rewrite adder once again. So we'll create this one more time. If we try adder, we try adding 1 to 5, everything looks good. However, the problem is here is that if we try to, again, create a function similar to nameprinter, so we say surnameprinter.

00:04:58
So we say politeness. And we'll say def surnameprinter. I'm really not original with these functions right now, am I? And we're just going to take in a surname. And all we're going to do is print, with an f-string, "Your surname is surname". And that should be curly braces for a variable we're passing in.

00:05:16
OK, so if we try to use surnameprinter, we're going to see that we are bound once again with the limitations of our decorated function. Check this out. We're now saying we are missing the positional argument num2, which is defined right here. It says we've got to pass in two arguments to a function.

00:05:34
And this function here is only accepting one. So clearly here, we've got a severe limitation. We've tried it both ways. We've tried it with one and accepting two, and vice versa. So really, we don't have much reusability of this politeness function. We just want to be able to always print out this, have some generic function, no matter how many arguments it takes to be able to use that no problem at all.

00:05:58
And then immediately after, we're going to get the exact same effect. So what we want here is flexibility. Now, we actually can solve this problem with a solution we've already seen when we dealt with our Python functions. This is dealing with, as we saw, ```*arcs```, which allows us to pass in variable length positional arguments, as well as **kwarks, which is for our keyword documents.

00:06:23
So check this out. Let's quickly rewrite politeness, this time to include args and kwarks. OK, so clear the screen. Arrow up. And what we're going to do here is within our wrapper, what we're going to do is as opposed to specifying a particular number, we'll just say *args.

00:06:39
And we'll just say ```**kwarks```. So this is pretty much optional arguments for specifying. So if they exist, we'll take them. If not, we don't need to worry about them. So we'll say **kwarks now, and now if we hit Enter, watch what happens now. Let's create our adder function again.

00:06:55
So we'll just say def adder. Let's call it adder2, whatever. And we'll just say num1 and num2. And all we're going to do is print num1 add num2. Cool. And let's decorate this with politeness. Cool. So if we happen to use adder2, and we pass in 4 add 6, or maybe 4 add 5, hit Enter, this works no problem at all.

00:07:17
Let's create this surnameprinter again. So let's recreate surnameprinter. We'll just say ```surnameprinter```. And that is just going to take a surname as an argument. And all we'll do is we'll print out, with an ```f-string``` string, "Your last name is" and then pass in ```surname```.

00:07:33
And you want to decorate this. So we'll just decorate this with politeness. So now if I try surnameprinter and I pass in the name McGovern, which is my second name, if I hit Enter, now this also works. And lastly, if I just create one-- let's just call it, say_hello-- this is going to take no arguments at all.

00:07:52
And all we're going to do is print, ```"HELLO"```. And we'll decorate this with politeness. So we'll say ```@politeness```. And if we just call say_hello with no arguments, this also works no problem at all. So now our decorator has maximum reusability. It's very flexible.

00:08:12
It can accept no arguments, one argument, or multiple arguments. And it's not going to affect the code. The code is always going to stay the exact same way. And the key thing that saved us here was implementing this concept, once again, of args and kwarks.

00:08:28
So again, if you want to re-brush up on what args and kwarks are, go back to the skill on functions within Python earlier on throughout this course. But ultimately, this is going to allow us to specify a variable length or an optional variable length of positional arguments and keyword arguments as well.

00:08:44
So that is how we can deal with arguments within our decorators. I hope this has been informative for you. And I'd like to thank you for viewing.

---

## Creating a Performance Decorator

00:00:00
Hey, guys and welcome back. So what we'll do in this Nugget right here to wrap up this concept of decorators is we will define and create a decorator which is going to allow us to measure performance of our functions execution. What am I talking about?

00:00:26
Well, what are we waiting for? Let's dig in and find out. So once again, we're going to ipython. And what I'm going to do here is say from time, I'm going to import something called perf_counter. So what I can do here is I actually call perf_counter as a function.

00:00:39
So I'll just say, perf_counter. And what it's doing is giving us a very granular measurement of time. So what I could do here is assign this to a variable. So I could just say start is equal to perf_counter. OK. I could wait a few seconds, and I could say finish is equal to perf_counter once again.

00:00:55
Counter. Call you. So now I have two different values. I have a start and a finish. So what I can do is say the performance is equal to the finish time minus the start time. And then I can say the performance is that end total. It took 7.169 seconds.

00:01:12
So that means I created this variable here called start. And then 7 seconds later, or 7.169 seconds, I had completed finishing the second variable called finish. So the task in total took 7.169 seconds. So how about we implement this type of functionality as a wrapper that we can use to decorate our functions with maximum reusability.

00:01:35
So what I'll do here, is I'll create a function. We'll just call this performance tests. And as per usual, we're going to accept func as an argument to represent our function. We'll create an inner function. We'll just call it wrapper. Let's keep the same type of format.

00:01:47
We want maximum reusability, so we're going to say ```*args``` and ```**kwargs```. Just means we can handle multiple arguments or, if we need, no arguments at all. And all I'll do here is pretty much what you saw above. I'll just say start is equal to perf_counter.

00:02:04
And we call that. So we'll take our timer straight away. Then what we'll do is we'll call our function. We want to use maximum flexibility, so we're going to say ```*args```, ```**kwargs```, which means that we can handle new arguments, a single argument, or multiple arguments.

00:02:20
And then immediately after we have finished calling that function, we'll take perf_counter once again. And then we'll say performance is equal to finish minus start. And then what I'll do is I'll just print out with a F string, execution time is equal to whatever the performance is.

00:02:39
Say curly brace, performance. And then we'll return that inner function, which is wrapper. Cool. So what I can now do here is I'll decorate this function I'm going to create, and I'll decorate it with performance tests. And I'll create this function.

00:02:52
Let's just say print some numbers. And we'll accept-- oh, didn't mean to hit that there. And we'll accept num as an argument, which will be a number. And what I'll do is I'll just look through a particular range. I'll just say, for i in range. And we'll start at 0, and we'll go as high as the number which the person passes into this function.

00:03:14
And then what we'll do is we'll just print out i. But like I say, this print_some_numbers has been decorated with performance test, which means it's going to have this additional functionality built in. So if I say print_some_numbers and I pass in the number five, that means we'll do for i in range 0, 5.

00:03:30
If I hit Enter, it's going to print that out, but we're also going to get this new additional functionality that we've decorated with. And it tells us that this took us 0.0004 seconds. And I could just crank this number up to maybe say 3,245. If I hit Enter, it's going to print out all those numbers.

00:03:50
And as you can see, it took a little bit longer. Still very, very fast. 0.02 seconds to iterate through all those numbers. So decorators, really useful for adding additional functionality to your existing functions. Just remember to be able to handle different types of arguments for maximum flexibility.

00:04:07
So that is us for decorators. The next thing we're going to be looking at is generators. That's coming up in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Generator Overview

00:00:00
Hey, guys, and welcome back. So now let's talk about generators within Python. So what on Earth is a generator, and why is it useful to us? Now what a generator function is, it's a type of function that is known as a lazy iterator, which is quite a funny name.

00:00:28
And basically this is something that you can just iterate over, loop over, just like you can with a list. Here's a cool thing, though. With a list, when you're dealing with very large data sets, well, the list has to store all of this information in memory.

00:00:43
This can become quite bloated, and it can really become quite taxing on your resources. Now, with this lazy iterator that we have here, this object, they don't actually store the entire contents in memory. So the way Python generators are going to work is that they're only going to require memory for only one value that they are yielding.

00:01:03
This is actually going to be the key word we're going to use within Python to get that particular value. We're going to yield it. So really, when comparing, say, generator objects to a list, you really want to be considering using generators when you're going to have that very large data set.

00:01:21
And this is why the concept of generators is really big in things like data science, when working with data science using Python, because things like data science, well, that can be really resource intensive. It can be using very, very large numbers and operating at a very large scale.

00:01:38
So it does in fact make sense to look for a more memory efficient solution. And this is really what we're going to get when we're dealing with a generator. So what on Earth does one of these generators actually look like? Well, how about we find that out in the very next Nugget?

00:01:52
So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Working with Generators

00:00:00
 Hey, guys, and welcome back. So let's check out what these generators actually look like, then. So we'll dive into IPython. So what we'll do right now is we'll create a function called square_me, and what it's going to do-- it's going to take a list of numbers.

00:00:27
And what I'll say here is, for num and list of nums, what I'll do is append this into a list of [INAUDIBLE]. Let me do, in fact, as I'll need to create an empty list here, I'll just say my_list, and I'll initialize it as an empty list. And what I'll do is I'll take my underscore lists, and I will append it with whatever the number is times the number.

00:00:48
So it's effectively squaring it-- 2 times 2, 4 times 4, that type of thing. And then once we've exhausted our iteration, what I'll do is just return my_list. So what I'll now do is I'll create a list called squared_list, and all I'll do is I'll take my square_me function, and I'll pass in a list of values.

00:01:07
So I'll just say 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, and let's maybe go up to 20. And now, if I say squared_lists, all of those values should, in fact, be squared. So 1 squared is 1, 2 squared is 4, 3 squared is 9, 4 squared is 16-- so on and so forth until we get to 20 squared, which is 400.

00:01:28
So this is how we would solve this as a list. Now, like I say, this is not so much a problem when dealing with something like, say, 20 numbers. That really isn't going to cause too big of a memory footprint, but again, let's reimagine this to a similar working in a much larger environment in much larger scale.

00:01:47
Let's try to reimagine our function, this time as a generator function. So this was the original function we had. We had an empty list. We iterated through all the numbers we were going to pass into our function, and then we would gradually append, to the empty list, every single number that we passed in using their squared value.

00:02:06
So let me show you the difference here, but I'm actually going to create a generator function. I actually think it's much more readable and easy on the eye. So what I'm going to do is I'll just recreate this function. I'll just say def square_me. This will overwrite the old one.

00:02:19
And again, we'll pass in list of nums. And all I'll do this time is I'll just say, for num in list of nums that we'll pass in, and what I'm going to do is to use this yield keyword. So I'll say yield, and you see, it goes green because it's a known keyword.

00:02:36
And all I want to do is yield the number I am iterating through, and I want to times it by itself. And that is all we need for our generator function. So let's see the difference, then, when we apply this, then. So once again, if we arrow one up-- and I won't create a squared_list because it's not going to be an actual list.

00:02:55
I'll just call this gen_object, because it's actually going to be a generator object. So we're going to pass this in, and if I hit Enter, [INAUDIBLE] if I just say gen_object, it's going to look a little bit different. It doesn't give us a list of all the values of being squared, and instead, it just returns this generator object, and it tells us its place in memory.

00:03:15
Now, here's the thing-- there actually has been no calculations done just yet. In order for me to be able to get each value, I'm going to have to move through each one, one at a time. So a way I can do this is by using the next keyword, and what this will do, it will give us our first value.

00:03:33
It will yield that first value, and then after that, we'll move to the very next value. So check this out. So it's going to be only one value at a time in memory, as opposed to getting them all at once. So what I'll do is I'll just say next, and I'll pass in gen_object, and we go one arrow up.

00:03:51
We get 4, then 9, and we just keep going until, eventually, we will exhaust all of the objects within the generator object, and then we're going to get this stop iteration error. So the big difference here is that we're not actually getting all of the values at once.

00:04:07
We're only getting them one at a item. Now, as opposed to having to keep using this next keyword, we can still iterate through this generator object just like we would with the lists, so let's try this once again. So let's create a new one called new_gen_object, and what I can do is I can just iterate through that.

00:04:24
I can just say for x in the new_gen_object. I can then print x by iterating through it, and I don't have to worry about that stop iteration error. It's going to be handled automatically. So let's press Enter, and boom, look at this. We've actually got all the values, but like I said, the beauty here is that, at no point, were all of these values having to be held in memory all at once.

00:04:48
Python is just worrying about the next value, and then the next, and the next-- all of these small bite-sized chunks. So this is really the big advantage of using generators. It's all about efficiency when it comes to memory. Now again, whenever you see that yield keyword within a function, you want to be thinking, I'm using a generator function here.

00:05:08
And if you want to move through each value one at a time, you can use the next keyword, or [INAUDIBLE] we still have the option to iterate through the object, the generator object, just like we would a list. So that's how we can construct a very simple generator within Python, but you'll know that, just like with lists, we can have things such as list comprehensions, we can also have comprehensions when using generators.

00:05:32
What on Earth are they going to look like? What is the big difference? Well, that is what we're going to be finding out in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Generator Comprehensions

00:00:00
Hey, guys, and welcome back. So if you recall from our skill previously in this course, dealing with Python list, we understood that we could also introduce the concept of list comprehensions. Ultimately, this was a nice substitute as to having to continually use the append method in Python.

00:00:30
So again, let me just quickly show you the translation here, just for a quick refresher. So what I could first do is create an empty list, just called my_list, similar to what we did before. And I could say for num in range, and I'll just say maybe 5 to 100, whatever.

00:00:48
What I could do is take the empty list, append the value, and append it with just num times num, just as we saw in the previous Nugget right there, so num times num. OK, so now, if I happen to save my list, we have all of these values here. But like I say, we can also do this in the form of a list comprehension, which is actually going to have faster execution.

00:01:09
So the way we could deal with this as a list comprehension, we don't have to create an empty list, initialize it, and then continually use the append methods, just keep calling that and calling that and calling that until we exhaust the range. Instead, what we'll do is we'll just take the list straight off the bat by using a list comprehension.

00:01:28
So I'll just say ```my_list_comp``` is equal to. Now, the way we write this as a list comprehension is using square brackets. That is because we're going to be creating a list object that is denoted with square brackets in Python. And again, if you recall from that scale on list, the logic is a little bit backwards, at least the way you read the list comprehension.

00:01:49
So what I want to do here is to say num times num for num in range 5 to 100. This is effectively going to give us the same output as the previous solution, but this is going to be more efficient. So the way I read this is a little bit backwards. I happen to read this part here first, so for num in range 5 to 100.

00:02:11
For that num value, this is what I want to do with it. I want to say that number times itself. And that is going to populate all of the values in this list. So now, if I just happen to say my_list_comp, we're going to have the exact same output as we saw before, but this is a little bit more efficient.

00:02:29
But again, this is the list object. What is Python doing with having to store all of these values all at once? so it's going to have a rather large memory footprint as we scale the numbers up, as we happen to maybe move the range up to the thousands or millions, whatever it may be.

00:02:46
The more numbers you're going to have in this list, the more numbers Python has to keep track of, the larger the memory footprint. And the more taxing, therefore, it's going to be on your resources. So let's look at the same type of solution, but let's use a generator instead.

00:03:01
So what I'll do here-- and it's actually really a simple translation here-- I'll just call this my_gen_comp because it's going to be a generated comprehension. What we're going to do here is change the outermost characters, that is the square brackets for a list.

00:03:15
And when we're creating a generated comprehension, we're going to use parentheses. So check this out, OK? So this is going to be our generated comprehension. And now, just like as we saw before, if I say ```my_gen_comp```, we're actually getting a generated object, not a big list.

00:03:32
And what I want to do here, is I actually want to show you the difference in the memory footprint we've got here. So what I'm going to do here is say import sys. And what I can say is ```sys.getsizeof```. And I'll pass in the ```list_comp```, which I just created prior to that, so ```my_list_comp```.

00:03:47
So the list comprehension has 904 bytes. If we happen to just pass in the generated comprehension, ```my_gen_comp```, this is only 112. Check that still as we scale this right up, look at the difference. So if I happen to create a list comprehension, and I'll call this ```my_list_comp2```, and I'll really made the value a lot larger.

00:04:10
So I'll just say 1 to 500,000, OK? Much, much larger. If I happen to say ```my_list_comp2```, the value is way, way bigger. And if I happen to test the size of that, so pass in ```my_list_comp2```, this is much, much larger. So this is 4,290,000 bytes. Whereas if we do the same thing and put it into a generator, so what we'll do is we'll say ```my_gen_comp2```, and again, we'll make this parentheses.

00:04:38
But I'm not going to have to store all of these values at once. It's still going to be nice and compact. So let's test my_gen_comp2. Let's see the size of that. And that's still only at 112 bytes because it's only storing one value. And if you want to exit it and get all those values, what we can say is for num in, just as we saw before, ```my_gen_comp2```, ```print num```.

00:05:00
And what Python is going to do, it's going to calculate them on the fly, one by one by one by one, and only storing one in memory. So if we print this out, we get a big large value continually printing out, continually calculating. So the thing is to note here is that this is going to be a little bit slower when it comes to speed performance because we don't actually have it all precalculated, but we're going to get a big, big boost in memory performance because we're not having to store everything all at once.

00:05:29
So really, when considering using large data sets in Python, consider asking yourself, do you really need to store all of your values in, say, for example, a list object, or perhaps maybe a generated object is the best bet. Okey doke, so I hope this has been informative for you.
