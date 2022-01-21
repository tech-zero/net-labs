# The Jinja Templating Engine

## Introduction

00:00:00
Hey, guys, and welcome back to another Skill and Python for Network Engineers. So throughout this course, what we've been doing is learning the fundamentals of what Python is all about. Now admittedly, sometimes learning these fundamentals, it's not quite so obvious how they may apply to the network.

00:00:31
These fundamentals are really important. We have to understand them. But I must say, it really is much easier to get enthused about learning something when you can see its applicability straight off the bat. And this skill right here, I think we're going to be able to have an obvious connection between what we're doing here and what we want to be able to do on the network.

00:00:52
So what on earth am I talking about here? This skill is going to be all about using the templating engine, known as Jinja2. Now Jinja2 is really, really useful with a network automation. I happen to use it all the time. And it really is very, very popular when you're trying to automate legacy devices.

00:01:12
Because legacy devices effectively have to be accessed over the CLI, like something like, say, SSH, as opposed to connecting them through some, maybe, modern API, such as, connecting to a device over HTTP using the RESTCONF protocol. Now if you don't know what the RESTCONF protocols is, do not worry about that at all.

00:01:31
That's just a modern way to be able to automate your network. But suffice to say, most networks are still kind of living in the dark ages. We're going to be used in the CLI, just automating the CLI effectively. But what does this actually mean? Well, think about.

00:01:47
If we log on to a device and we want to say, well, we want to configure this device with an ntp server. So you'd log in. And we would say, ntp-- I think, it's hyphen server, I think, if it's Cisco. And you would type in the address. So maybe just say 1.1.1.1.

00:02:04
OK. So this is what you would do by hand on the keyboard, plugging into a console cable. This is the command you will type on. Now when you're automating these legacy devices over SSH, this is, in essence, what you have to do. You've got to be able to take the command and send off to the device.

00:02:21
Well, how are we going to do this using Python? Well, the answer is, we're going to be able to template out our configurations. And in order to template out our configurations, we need some type of templating engine that's going to do that. And the type that we're going to be using for Python is legacy Jinja2.

00:02:40
And this is what we're going to be using within the scale here. Here's the thing. We're not just going to be learning about Jinja2, because Jinja2 is only one part of the equation, albeit a big part. What we've got to learn to do is how we can separate out configuration that can be templatized, like say, for example, this configuration here, ntp-server.

00:03:02
This will always be what we take when we are configuring a ntp-server. But what about this part here? This can be a unique value, which maybe differs across different devices. And to be able to reliably manage devices in such a way that we can automate these configurations, what we want to do is to split this apart.

00:03:21
Things, which can have variable values, we're going to store them as variables in something called, YAML. This is very, very common with a network automation. And ultimately, what we're going to do is just manage these YAML files to make changes in our network.

00:03:37
So when we make a change to a YAML file, for example, we change 1.1.1.1 to maybe be 8.8.8.8. We update that file. And then, we push that new value through a template engine, which is going to regenerate a new configuration, once again, which would be ntp-server.

00:03:57
And in this case, we would use the new configuration within the YAML file. This would be 8.8.8.8. So that's just really what we have planned for this skill right here, introducing how we can use these YAML files in conjunction with Jinja2 to be able to generate a configuration.

00:04:16
So the first thing we'll be looking at is what is YAML? What does it actually look like? How can we work with this data format? And then, the rest of the skill will be more focused on Jinja2 explicitly, because Jinja2 is a little bit like a language in and of itself.

00:04:30
Really, it's the same type of concepts we get in Python. We're going to be able to see how we can do variable substitution. We're going to see how we can implement loops within Jinja2, how we can implement conditional logic, which is pretty much your if statements.

00:04:45
If this equals this, do that, or else do something else, that type of thing. And we'll also look at other cool things, such as, maybe C filtering, as well as, a couple of other little cool tricks. So I do think what we learn in this skill is going to be immediately applicable for us, as network engineers.

00:05:03
And for that reason, I really am quite excited to get into. But like I say, the first thing that we've got to learn about is this concept of YAML. What exactly is it? What does it do? What does it look like? All those questions will be answered in the very next Nugget.

00:05:17
So I hope this has been informative for you. And I'd like to thank you for viewing.

---

## YAML Overview

00:00:00
Hey, guys, and welcome back. In the introduction, we briefly mentioned this concept of YAML. YAML is effectively what is known as a data serialization format. That's just the way to store data programmatically with a big emphasis on readability and writability.

00:00:32
This is the advantage that YAML really does bring us. It's very readable and very writable. And for that reason, this is why it's chosen as the de facto format of choice when it comes to network automation for managing or configuration files. Because when we're working with these configuration files, they may be some pretty complex configurations.

00:00:54
For example, they may have some access control lost information or perhaps, say, BGP information, so on, and so forth. Well, as a network engineer that this can get pretty involved. It can be sometimes confusing, so we don't want to make it any more confusing than it needs to be if we want to work with those data and store those data programmatically.

00:01:13
This is where YAML comes in. Because unlike other data serialization formats, such as maybe, say, XML, YAML is so much easier on the human eye to be able to interpret this. So this really is the strategy here. You want to have your configuration files written in YAML.

00:01:30
And when it comes to actually using configuration data, if you want to, maybe, say, make a change on the network, what we want to do is to suck all that data out of the YAML file and then push it through the template to actually generate the CLI configuration.

00:01:48
So this part here as all about writing your data so that we can store it, and then manipulate as we change it. And we want to be able to do so in a way that as, like I say, again, readable and writable. Now, I don't want to go into too much detail about all the ins and outs of a YAML, but I do want to give you a brief sense of what it's all about and how we can leverage it for our needs.

00:02:10
Now the benefit of using YAML for us, as network engineers using Python, is that YAML is going to support different data types things, such as dictionaries, which we know all about now, and things like lists. Now the way we write a dictionary and the way we write a list in YAML looks a little bit different than we do so in Python.

00:02:32
Again, like I say, YAML's focus is all about readability. But you're going to see that we can actually use a module within Python to just convert what we have in YAML, and it's going to translate it nicely into our Python native syntax. Now here are some broad strokes that we have to understand about YAML.

00:02:53
Now, you're going to be able to tell a YAML file because at the very top of the file, you're going to see three hyphens. When you see that, that is when you should be thinking I am working with a YAML file here, and the YAML rules are going to apply.

00:03:08
Now another very important thing is that YAML is very sensitive to white space. So white space does matter, and it's important to note that when you're working with YAML, you want to be using spaces and not tabs. And just like Python, we're going to be using things such as indentation.

00:03:27
Indentation as important when it comes to working with YAML. And using indentation, just like with Python, is going to allow us to be able to nest our actual data. Another key concept when working with YAML is the concept of mapping. And this is really analogous to working with Python that you're going to have a key on the value.

00:03:47
So you might have something like a key that says device, and then a colon to separate the key, and then the value. The value might be, say, a string value, and it's going to be R1. Now a really important thing here is that between the key and the value, you've got to have a space here.

00:04:03
You can't just have the value immediately after the colon. Space is super, super important. So that's type of syntax is really going to be analogous to your Python dictionaries. When it comes to your Python lists, what we're going to be doing is using a hyphen.

00:04:19
So let's say we had something like, say, a BGP configuration, and we wanted to have a BGP peers. We could say peers. That should be the key. As opposed to having a single value, let's say we had multiple peers we could denote this with the use of the hyphen.

00:04:36
So again, we would have an indentation and then do a hyphen. Then we can maybe, say, something like, say, neighbor, and that could be a key. And we can maybe just say, I don't know, 1.1.1.1. And we could say that as an ASN, so we can map that from a key to a value.

00:04:51
Let's say 65001. And if we wanted another neighbor because that's about like [INAUDIBLE] less. We want to repeat the same key. We're going to, say, neighbor again, the key, and then a value. This time it could be 2.2.2.2. And let's ASN-- could be a little bit different.

00:05:08
We can say ASN 65002, so on, so forth. So these hyphens here, this is how we're going to get out list objects within YAML. So what we're going to do here is write a short configuration file in YAML, and then we'll see how we can work with that programmatically in Python.

00:05:27
So in order to do this, we're going to install something called PyYAML. So this is going to be one of the first things we're going to have to do. So right now, let's go into a directory, activate a virtual environment, install PyYAML, and then we'll begin writing our YAML definition file.

00:05:42
OK, let's try this then. So I'll see into my directory-- Python-Net-Eng. I'll go into my virtual environment. Let's activate this, and let me go back. And what I'll do is I'll create a new directory just maybe call it templates stuff. So let's go in here.

00:05:57
OK, so what I want to do is to install PyYAML. So I'll say, pip install PyYAML. And again, if you want, you can use, [INAUDIBLE] of our answer, and as you can see here I already have installed pyyaml, but if you haven't, then it's going to quickly run through the installation.

00:06:13
So what I'll do first here, as I'll create a little YAML definition file. So I'll just say, touch and let's just call this R1.yaml. This is going to represent our configuration for a non-existent device R1, but let's pretend it does exist. So what we're going to do here, is we're going to go into VS code, I will manipulate this file and start writing it.

00:06:36
So we got into R1.yaml. Now, another thing I would suggest you do is if you go to File, and then go to Preferences, and then to Extensions, if you happen to search for YAML you should get some YAML support. Here we have one bio-rater so I just uninstall this.

00:06:51
And we know we have this Extension, so let me just go back out here, and let's write our very first YAML file then. So let's do a mock configuration for BGP. So like I say, at the very top of the YAML file we're going to be using 3 hyphens, 1, 2, 3. And now what we're going to do here is have some type of key value pair, this is going to be like a little dictionary for us.

00:07:14
So let's say we're going to do some BGP configuration. Let's just play a key called BGP for example. So because it's a key, we're going to specify a colon here, and you see the color change? That is going to be a key as we can see here. Now if I hit Enter, now nested within this I want to have another key, that belongs here.

00:07:36
So like I say, YAML is white space sensitive, and we're going to use indentations-- I'm going to use 4 spaces indentations, so I hit the Spacebar 4 times, 1, 2, 3, 4, and now I can specify indented within my next key. So I'll say ASN and I'll see colon, and now I'll give this ASN a values, so within my quotation marks will have a string value of "65001" And if hit Enter , what I want to do is to denote the pills which I have, which belong to this BGP configuration.

00:08:11
So I'll say a key called peers and I'll say colon, so now another key here, and again, we don't just have one peer like this, we're going to have multiple peers, so because of this we're going to use a last object to hit Return again, and I do 1, 2, 3, 4, now I hit a hyphen for a last object and do another space.

00:08:32
And now I'm going to specify my next key, so let's have a key called neighbor. And let's say the neighbor as "10.0.0.1" and then if I hit Return, and make sure I'm at the correct indentation, we guess this is also going to be within this last object, I'm going to say peer_asn and I'll make this "65002" because our ASN is "65001".

00:08:57
And now if I go down, and at the same indentation level as this hyphen here, I'm going to create another hyphen, so I can create another block of neighbor and peer_asn keys. To check this out, if I do a hyphen and then a space, and now I specified neighbor once again, this time the value is going to be a little bit different.

00:09:17
I'll say "10.0.0.2" in fact, I don't want make that "10.0.0.2" because it's "65002" and I'll make this "10.0.0.3" just so it's a little bit easier to read, or to follow should I say. And I'll say the peer_asn key is going to be "65003" and we'll maybe do one more.

00:09:36
So same indentation level will do a hyphen, and we'll say neighbour is equal to "10.0.0.4" and the peer_asn is going to be "65004" and for now, this can be an example of a BGP configuration in YAML. Now look at this, what I want to highlight is how readable this actually is.

00:09:57
Now maybe you find the structure of being able to write it a little bit confusing and first you've got to work on the indentation, so on and so forth. But realistically just looking at this, if I ask you to create a new neighbor, it wouldn't be too much bother.

00:10:11
So you could just say, I'm going to copy hear, copy that, I could just paste this in, and I could just create a new neighbor quite easily. It's very, very human readable, we could just say "10.0.0.5" and create a new one, and suddenly a new neighbor can be configured on our network.

00:10:26
So it's nice and clean and easy on the eye. And like I say, we want to be able to work with this data programmatically using Python, so let's see how we can do this then. So what I'll do here is I'll in new file, and I'll save this as, let's just say, yamlexample.py.

00:10:45
Now because we installed pyyaml what I'm going to say here is, import YAML. So here's what I'm going to do, I'll create a lot of function here, which is going to pull the configuration, so let me just call this function maybe pull_yaml or whatever, and for now we don't take any arguments.

00:11:01
This will be a little custom function, let's just do a little doctoring here for good habits, and we'll just Function to pull YAML data. So all I'm going to do here, is I'm going to create a variable which is going to represent this data, so let us just say, config_data, that will be the variable name, call it anything you choose.

00:11:20
And now what I want to do is use the YAML module, and I'm going to safe_load the information which I have here. That's the function we want to do, so what I want to do here is open parentheses and say, open and now within parentheses here, I'm going to specify the name of the file, which I want to open.

00:11:38
So what is the file is called? It's called R1.yaml, and because this is on the same directory I do want have to specify that here, so I can just say R1.yaml. And for now that should effectively pull out that YAML information and transform it into Python native syntax, so if I just print, let's print(config_data) and now what I'll do is just call my functions I'll say, pull_yaml() and because it's a function, let's call it with parentheses.

00:12:04
If I save this, and I try running this script then so I'll say, python3 yamlexample.py Enter, and look at this, this looks much more like generic Python. And in fact, to make this a little more readable, let's just make sure we have rich installed, so we'll say pip install rich library, which I already have, so make sure you have it.

00:12:24
And let's go back to illustrate more too here as, I'll just say, from rich import print as rprint. And as opposed to just printing this here we'll have rprint this, just to make us look a lot neater. Let's see if that's once again, let's clear the screen if we arrow up and hit Enter, there we go.

00:12:42
And look at this, know this looks much more like Python native data, this is like a dictionary key, a dict key, a value and then now we have a dictionary key, and within that dictionary we have a square brackets, where is a square bracket? And Python, that is the last object, so we have a last of neighbors with peer_asns.

00:13:02
And if you wanted you could work with us programmatically quite the thing. So we could go back in and if I could call the BGP key, that should strip that away, so we'll just say BGP_stuff is equal to config_data. And name it key, which is BGP, just like the word, and Python and then the print BGP_stuff.

00:13:23
And in fact let's rprinted so we get our nice formatting using rich, so if you Save this, let's go back, if we arrow up, we're now peeling that key away just like we would in Python, and if it wanted to get the ASN we could call that ASN key. Let's Save this arrow up, but it's going to get "65001" and we could also do is say the peer is equal to BGP_stuff, and encode the peers key, knock at rprint the peer's, Save here, let's go back.

00:13:52
If we arrow up what now we'll just get? The peers as the last object. So therefore, we could iterate through all the individual peers, and we can say for peer in peers, we must rprint the peer, let's arrow up again, was tucked away, our last object, we don't have a square bracket, so we can now access the keys and the individually.

00:14:11
So let's key a variable called nbor for the neighbor and we'll make them equal to the peer, and we'll call the neighbor key and we'll say, asnumber is equal to the peer and the key is going to be peer_asn and then we can print with an f string, use a re-calibration will say, the neighbor and we'll pass in nbor, which is going to be the neighbor, has an ASN of an ampersand asnumber variable.

00:14:40
So let's Save this and try again. Let's clear the screen, arrow up Enter. And as we can see here, we're able to easily pull out our data programmatically from this Nash readable format, just like here, and we can work with it programmatically using in Python.

00:14:57
So the goal as a network automation is, to separate out our variable information, such as the different neighbors we might have, the different peer numbers we might use, from the actual hard coded syntax that we need to use within our CLI configurations.

00:15:13
So now we have one part of the equation, we know how to store those variable data, let's see how we can generate our configurations from this data. And like I say, how we're going to do that, is going to be using the Jinja templating engine. So the very first thing we'll look at as variable substitution within Jinja that is coming up next, and I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Variable Substitution

00:00:00
Hey guys and welcome back. So let's now dig in to using Jinja2 then. And in this Nugget right here, we're going to explore how we can install Jinja2 to be able to use it within Python and focus on the concept of variable substitution, how we can actually substitute our variables using Jinja2.

00:00:30
OK, so let's dive in and get to it then, shall we? So what I'm going to do here first is install Jinja2 using pip. So what I'll say is python3 -m pip install Jinja2. And again, you could just say pip3 install Jinja2 if you prefer, both work. So let's hit Enter.

00:00:48
Now as you can see here, I've already got Jinja2 installed in my system. But again, if you don't, then it's going to run through the installation really quite straightforward. OK, so what I'll do here is I'll actually go into my directory once again.

00:01:00
And what I'll do here is I'll create a new example file. So I'll just say example2.py. OK, so let's open this up then, shall we? So we're going to example2.py. OK, so what we're going to do right now is to import YAML once again. That's because that's going to host our variables.

00:01:18
And we want to suck them out from YAML and then run them through our template. So that in order to be able to have access to YAML or rather to our YAML files, let's import YAML. OK, now because I have installed Jinja2, what I'm going to see is from Jinja2.

00:01:34
And what I'm going to do is import two things. The first one is Environment, and the second one is FileSystemLoader, cool. So now what I'm going to do here is just create a little custom function. So just like before, I'll just say something like say generate_config.

00:01:50
We don't take any arguments right now. I undercut dot string for good practice and just say load in host variables. And then just say Generate config from template. OK, so the first thing we want to be able to do is to pull out the information from a YAML file.

00:02:05
Now the YAML file I'm going to use is the same as we saw previously. That's going to be R1.yaml right here. So let's follow the same type of format. Let's just say config_data is equal to-- and I'm going to take the YAML module. And I'm going to say safe_loads.

00:02:19
And I want to open the name of this file. So I'll just say R1.yaml. So config_data is going to be-- in fact, let me just change the name of that just so I can maybe make it a little bit more explicit. I'll just say my_vars for my variables. OK, so now what I want to be able to do is to tell Jinja where to look to find my template.

00:02:40
So I'm going to do here is specify whereabouts my templates are going to be stored. And what I'm going to do is take the environment class, which I just imported, and I'm going to give some type of arguments. I'm going to say loader is equal to. And the loader is equal to the FileSystemLoader, which I just imported here.

00:02:57
Now the argument we have to give is effectively what directly do we want to look into to find our templates. So we actually haven't created a directory quite just yet, but we will in a little second. So I'll just say start from the current directory and go into the templates folder.

00:03:15
This is the directory we'll create. Now in order to control some white space and some indentation, I'm going to add two additional arguments. You don't have to worry about these too much. I'm just going to say trim_blocks is equal to True, and lstrip_blocks is equal to True as well.

00:03:29
OK, So let me now create a variable which is going to represent our template. So I'll just say maybe templates. And I'm going to take this env object I've just instantiated, and I'm going to use the get_template methods. And now effectively, what I've got to do here is pass in the name of the temp I want to get.

00:03:49
So let's just maybe say the template is going to be bgp.j2. So what's happening here is a quick recap. We're using YAML to pull out that information from our R1.yaml file. We want to open that. We've created this env object from the environment class.

00:04:07
We're specifying whereabouts our templates can be found, i.e., you look in the templates directory, which we're going to create. And then once we're inside of that directory, the actual file we want to look at this time is going to be called bgp.j2. So that field is going to be in /templates/bgp.j2.

00:04:25
That is effectively what we're saying here. We're saying, hey Jinja, look in here to find our template that we're going to write. Now that's not all. We also want to effectively blend together our host variable files, which is coming from the R1.yaml, and push that through the actual template.

00:04:46
So it's not enough to just locate the template. We've got to link this file with this file. Let's create a variable called configuration. And we're going to take our template variable we've just created above right here. And then I'm just going to say render.

00:05:01
What do we want to render with our template? But what we want to render is my-vars because that is effectively the variable files we're getting from R1.yaml. To check this out, we just type in my_vars. And that is all we need to do to be able to effectively pull out our host variable files, push it through Jinja2, and generate our configuration.

00:05:23
So we'll just print our configuration. We're not going to send it to any device quite just yet. We just wanted to see what the result will be. And of course, we're going to have to call our function generate_config to execute all of this and then the code.

00:05:35
Now right now, we don't have a template directory. We don't have a bgp.j2 template. So we have to go and create these right now. So that's what we'll just do. Let me just save this. And then from within the directory, and then I'm just going to say mkdir and create this templates folder, because this is where Jinja is going to look in.

00:05:54
So I go into this folder. And it's also going to look for a file called bgp.j2, so let's just create that. And if we do an ls, that is now created. And it resides within then the template directory. OK, this is all very well, but how do we actually write the Jinja2 template?

00:06:08
Well, that's what we're going to get to right now. What I will say, though, is if you haven't already installed the Jinja2 extension within VS Code, I would recommend you do that. If you go to File, and then Preferences, and then Extensions-- like I said, I've already got it here.

00:06:22
But if you just say Jinja2-- there's one here better. Jinja as the one I recommend install. And it's going to give you some syntax highlighting when you're doing F statements and lifts and whatnot. OK, so let's go and write this file then. So let's open up this bgp template.

00:06:38
So we're to templates folder and into bgp.j2. OK, so let's first look at our YAML file. And we'll think about what we actually want to do here. Let's just mock up our basic-- very basic BGP configuration. So let's just simply say, router bgp, which is what you always see in Cisco iOS when you're going to configure BGP.

00:07:00
Now the next value as a variable value. It depends on what you want to input. You can see it with our bgp4. You could see it with our bgp99. Or you could see it with our bgp65001. So this part changes. This part always remains the same. So this is what we're trying to do here.

00:07:18
We're trying to separate this from the variable value. So let's hard code this part right here, because this is always going to be the same. And the way we do that is really, really simple. We just type as we would automatically type it with our BGP.

00:07:32
Now what we have to do here is to do our variable substitution. Now within Jinja, the way we do our variable substitution is using double curly braces on both sides of the variable. And within these curly braces, we specify the variable we want to actually use within our template.

00:07:51
So I could say, what do we actually want to do here? We want to see a little BGP. And we want to substitute whatever value we've got as our ASN, which is this value here. So here's the thing, we are telling Jinja2 to render this file here. So we've got access to all of these variable files.

00:08:09
We just have to access the keys programmatically here. So what we're first going to do is specify the out of key. So that is BGP. OK so within our curly braces, we'll say BGP. And that's going to be capital letters because that's what the key is. And then to go in one level the indentation, we can use dot notation.

00:08:29
So we can say BGP dot. And then what's the next key? Do we want ASN, or do we want peers? But we want, in our case, ASN. So we can just say BGP.ASN. And again, these are capital letters because that's what the keys are. So if we happen to put this within our double curly braces, what Jinja is going to do, it's going to say, look for this key, and then that's key.

00:08:53
And then what is the value? This is the value here, 65001. That is what I'm going to put within my double curly braces. So effectively, we should actually render this as a router bgp 65001. And we have no substitute of this variable from whatever happens to reside within this neat, nice, readable YAML file into our configuration template.

00:09:18
So let's try this out and see if this actually works then. So let's do a double curly brace. And the first key is BGP. And that is capital letters. And the next key is ASN, cool. So this is now our little template. So if I save this, and I try running this code we're going to, like I said, pull out all these values from this file here.

00:09:39
We're going to have access to them and memory. And then we're going to tell Jinja2 to look through the BGP key, the ASN key. OK, so let's try running this script then. So let's go back one directory, and we clear the screen. And we try python3 example2.py.

00:09:55
Let's hit Enter. And, look at what's been rendered, router bgp 65001. And if we want to change our BGP configuration, we don't need worry about fat fingering our router bgp or something. But just effectively, modify what is within our host available file.

00:10:12
So let's go into R1.yaml. If we happen to change this value to, let's just say, 99. And I save this, there we go. So now for R1 and just enter to again. We'll now rendering a new type of configuration. Again, the variables have been removed and separated from the hardcore DCLI syntax.

00:10:32
So this is variable substitution in a nutshell within Jinja2. Double curly braces is what we're going to do. And effectively, we want to be able to access our data programmatically. And we can do that just by accessing the keys and ultimately walking the tree.

00:10:48
Now that sounds all very well. That's how we can access quite simple data like we just saw there. But what if, in the case of something like, say, RFPS here, we have multiple neighbors here, how are we going to be able to access all these different neighbors with their correlating peer_asn?

00:11:05
Well, you may be able to guess that we do have a lost object here. How are we going to solve that? We're going to have to solve that by looping through or iterating through all of these values. Now how can we implement loops within our Jinja2 logic? Well, that's what we're going to find that out in the very next Nugget.

00:11:21
So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## Working with Loops

00:00:00
Hey, guys, and welcome back. So in the previous Nugget, we had just learned how we could do variable substitution using Jinja2. But the variables that we were actually substituting were really quite simple and easy to access. What if we have to access multiple values?

00:00:28
Say, for example, different values through list objects. Well, the key to this is to understand how we can use loops with then Jinja2. And that is what are going to be focused on in this Nugget right here. So what are we waiting for? Let's get to it.

00:00:42
So check this out then. Let's try to advance our little script a little bit farther then. So like I say, if we go in, and check out our YAML file, what we want to do is to render some configuration data using our neighbors and our peer ASN. So if you know Cisco IOS syntax, the syntax is going to look something like, say, router bgp, and then you'll have the ASN, so in this case it's 99 at the moment.

00:01:08
And then if you want to be able to specify a neighbor you want to peer with, you will say the word neighbor. And then you'll have some type of a variable value, whatever the neighbor happens to be. Let's just say 1.1.1.1. And then you're going to have to write the words, remote-as for remote autonomous system number.

00:01:27
And then you specify the remote ASN. So let's just maybe say 65001, whatever. So this is how we could do one neighbor. And just like we saw here, this part will be variable substitution. This part here will also be variable substitution. But we want to be able to implement, or at least have the option to implement multiple neighbors.

00:01:48
So we could also say, neighbor, whatever, 2.2.2.2 remote-as 65002, and add many, many more, if we need to. So like I say, the solution to this problem is to be able to implement loops within Jinja2. So let's dig in and see how we can actually implement this so we can render a configuration for these four neighbors and their four definitely autonomous system numbers then.

00:02:15
OK. So let's go back into our little template here. So like I say, the first thing we would do here is write the word neighbor. This would be hard coded. And then we would specify whatever neighbor we want. So we'd have some type of variable in here.

00:02:28
And for now we'd just say somevar. That is going to change, obviously. And then I'll say a remote-as. That's going to be hard coded. And then let's just say, anothervar. Cool. And what we want to do here is to do this multiple times. So here's the thing.

00:02:42
What we want to do here is to implement some type of logic. So when we have to do this here, what we're going to do is, say, curly brace followed by a percent sign, and then end with a percent sign and the curly brace. And now we can implement our for loop.

00:02:59
So let's think about how we can actually do this then. So let me just get a little bit of space here just now, just so we can focus on the for loop. So what I want to do is say curly brace percent sign. And now I want to implement my for loop. This is going to look pretty much just like we do with Python.

00:03:15
I'm going to say for. And if you're using the Jinja2 extension, you should get red highlighting here, which makes it a little bit easier to read. And now we have to pick a variable name. We can say any name we choose. It doesn't actually matter. Let's just say nbor for the neighbor.

00:03:30
And it's for the neighbor. And what? What are we actually trying to loop through? Well, let's consult our YAML file then. So where is your list object we're trying to loop through? We go to the BGP key, and then the peers key. The peers key is where we have all of our list items.

00:03:46
So think about this. What we want to do is to go through BGP.peers. And this is going to give us access to this object here. And this is what we want to loop through. So let's check this out then. So I'll say for nbor in, and the outer key is BGP in capital letters, and then we're going to say dot peers to get the next key.

00:04:09
And for now what I'll just do is I'll just print out the neighbor. So how do we get the variable that we've just created? We're going to do a variable substitution. We'll say double curly brace, and I'll just say nbor. If I can type that correctly-- nbor.

00:04:22
OK. Now, here's the thing. if I try to actually run this here, we're going to get an error. Let me just quickly show you what this error is going to be. So if I just scroll up, try to run my script once again, look at this. TemplateSyntaxError, unexpected end of template.

00:04:38
It says that Jinja was looking for an endfor, or an else statement. This is because the innermost block has to be closed off. So this is a little bit different than what you do with Python. Python, you can just say for something and something, and you can just iterate through.

00:04:54
With Jinja2, we want to close off that loop. So the way we do this in Jinja syntax, if I just go back, is once we are done with our loop, we are going to implement that same type of logic. We'll say curly brace percent. And then we're going to use the keyword endfor.

00:05:10
And you'll notice that is actually highlighting in red because the Jinja plugin recognizes this as a Jinja keyword. So now if I just print this out this time, we should actually be able to get access to that variable. So try again. But clearly, this is not quite what we want most.

00:05:26
We've still got this kind of dictionary effect here. We want to be able to access this value and this value, and then access this value, and then this value, and then this, and then this, so on and so forth. We don't want the keys involved because that is not going to be any good for us when we're actually rendering your template.

00:05:46
So let's check this out. So like I say, if we want to be able to access the value, say, for example, 10.0.0.2 here, well, what is its corresponding key? Well, the key is just the word neighbor. And if I want to be able to access this value here, what is the key?

00:06:01
Well, the corresponding key is peer_asn. Let's see how we can implement this then. Let's go back to our templates. And what I'll say here is-- so let me first hard code neighbor, because this is what we're going to rate within our syntax. Neighbor, and now we want to populate the value of the neighbor.

00:06:18
So 10.0.0.2, whatever it may be. So what we have to do is to take the variable that we are looping through, which is nbor. And now we have to call the key we want. So what was the key we were trying to get? The key we're trying to get here is the neighbor key.

00:06:33
And we can do this using square brackets. And just like an ordinary dictionary, we can just an inverted comma. Just say the name of the key. So neighbor nbor. And then if we just save this right now, and try it running a script. Try again. And that totally failed because I forgot to do variable substitution because it's going to be a variable.

00:06:53
So of course, what I need to do is enclose this in double curly braces. That was a little bit silly, John. So there we go. If we try this one more time, hopefully we'll get a better result. Let's arrow up. Try again. And now we're actually rendering those values.

00:07:07
That's just the first value we want. We actually want to specify the remote ASN. So again, let's go and do that. Go back to our template. And we will say the keyword remote-as, because that's what Cisco syntax expects. And then we'll do variable substitution.

00:07:23
And our variable we're looping through is nbor. And the next key we want to call is peer_asn. So now this should be our loop. If I go back here, arrow up, hit Enter, look at the configuration we're now rendering. And like I say, maybe you want to add something, let's say, an update source for your BGP configuration.

00:07:43
This would, again, be part of-- within the same loop, we would just say neighbor, and use the same nbor value. So neighbor. We'll call the same key. And let's just say update-source loopback0. This is just Cisco syntax right here-- update-source loopback0.

00:08:00
So now if I happen to save this once again, and I clear the screen, arrow up, look at the configuration we are rendering. Neighbor 10.0.0.2, and then we're getting the same value again. So we have a little block configuration for this part here, and then a lot of block configuration for this value here, and then this, and then this.

00:08:20
They're all enclosed within the same for loop. And just to tidy this up, let's get rid of this white space here that we see. Finally, let's just delete the white space, and that should be our configuration rendered. So one final try. Clear the screen.

00:08:33
Arrow up. Hit Enter. Bam. So this is how we can do our for loops within Jinja2. We're going to be using a single curly brace followed by a percentage sign to implement our logic for our actual loop. We're still going to be using variable substitution.

00:08:48
As we saw here, we're still going to use our double curly braces when we're trying to pass out a particular variable within the loop. And then remember when the loop ends, we're going to have to be pretty explicit and use an endfor statement, or an else statement, something that indicates that the loop is no more.

00:09:05
So that is for loops. Within Jinja2, it really is very, very useful. In network automation, you're going to use this so often. Because like I say, [INAUDIBLE] devices are everywhere, and this is really the way you're going to be automating those devices.

00:09:18
So that is one type of Pythonic logic that we saw within Jinja2. The next one we're going to look at is conditional statements. That's coming up in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

00:09:31
Quiz
Which of the following is used in jinja2 to terminate a for loop?
```{% endfor %}```

---

## Conditional Logic

00:00:00
Hey, guys. And welcome back. So let's now check out how we can introduce conditional statements within Jinja2. Now, again, if you're familiar with control flow in Python, this is going to look really, really familiar. We're going to have our if statements, our elifs, and our else statements.

00:00:29
So really nothing special here. We're just going to see how we implement that using Jinja syntax, as well as some of the comparison operators we can use. So let's check this out, then. So let's go into our templates and bgp once again. So let's add in some conditional logic, then.

00:00:46
So let's say that instead of just-- in fact, let me just quickly run this script one more time so you can see what we're actually printing out. Let's say for whatever reason we didn't want to include the neighbor 10.0.0.4. We wanted to remove this from our configuration.

00:01:02
How could we introduce this conditional logic in our template? Well, check this out. So after we do our for loop, just like in Python, we're going to have this test. We want to test that the value of the neighbor key is not 10.0.0.4. So how do we do this logic?

00:01:21
Well, again, we're going to say curly brace percent. And now within here, we're going to specify whatever our actual logic is. So we will say if whatever nbor. And let's parse out the neighbor value. And know what we need to do is use one of our comparisons.

00:01:37
We could say is equal to, and then pop in, maybe say some type of value, like 10.0.0.1 10.0.0.4. And right now, the only condition that would meet this would be one actual neighbor. That would be the 10.0.0.4 neighbor. That would be the only one which would actually match this.

00:01:53
Here's the thing, though. If I try to run this script once again, watch what's going to happen. This is something you have to be wary of. Let's arrow up. Try again. Look at this. Again, we have this syntax error. The issue here is we've got to close the if statement here.

00:02:08
Here is the thing. Where do you think the if statement has got to be enclosed? Are we going to put it after the for loop or before the for loop ends? Well, it's going to be before the for loop actually ends, believe it or not. We're going to have to go in here, and we'll do our percentage sign.

00:02:24
And we'll say endif, OK? So this is inside of the for loop. So you've got to close it inside it. And then outside it, you actually close the for loop itself. So check this out now. Let's try this. Save you. Clear the screen. Arrow up. Hit Enter. And look at this.

00:02:42
The only one we're printing right now is the neighbor which is 10.0.0.4. Here is the thing, though. We can actually invert this logic by saying exclamation mark, because this is effectively a not equals. So anything that is not 10.0.0.4 is going to be templated, or rendered, should I say.

00:03:01
And the 10.0.04 will not be rendered. Check this out once again. Let's arrow up. And now we have effectively inverted that logic. We've removed the 10.0.0.4. And we can add in additional logic. So this is not going to make much sense in the case of networking.

00:03:18
But just so you can get a rough idea how you can also add in more logic. What I could say here is instead of the endif, I can close it with an else statement. So I can say else print. And I'll just say, I AM NEIGHBOR. And I'll say nbor. And again, you need to put this as a variable because I'm going to substitute this value, AND I'M NOT SUPPOSED TO BE CONFIGURED.

00:03:42
And even after our else statement, we're going to close off this if block. So that's definitively closing it. So we'll say endif. And now if we try to rerun this, if we arrow up, we're now seeing different logic. Once we hit 10.0.0.4, we're getting something totally different.

00:03:56
Now, obviously, this is not the type of thing you would configure on a network. But you get the idea. If you have to have some type of, maybe, say, access control list, which applies to one thing, maybe a deny. Maybe some values get some type of configuration, other values get other types of configuration.

00:04:11
You can implement this logic quite easily in Jinja using this logic. And again, we can just invert this one more time. So basically, 10.0.0.4 will be the only one that will get the BGP configuration. All the other ones are not going to be configured.

00:04:26
So again, let's save this. Try it one more time. Arrow up. Hit Enter. And the only one that is getting configured now is 10.0.0.4. Now, like I say, there is many more operators we can be using. We don't need to do the comparison. We can do things like if it's greater than or if something is less than.

00:04:44
So it really is the same type of logic that you know within Python. You have your if statement, your elif, your else statement. So this is a really powerful tool within your Jinja templating. It's going to be used all over the place when you're making real configurations on real networks based on a particular condition.

00:05:02
But that is not all Jinja2 can do. We also have the option to do some filtering. That's what we're checking out in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

Quiz
In jinja2, ```!=``` denotes the "does not equal" operator?


___

## Jinja Filters

00:00:00
Hey guys, and welcome back. So in this Nugget right here, what we're going to be doing is checking out filters within Jinja2. So to see what filters we have available, let's go to the Jinja website then. So if you just happen to Google for Jinja2 filters, if you click on this top link here, if we click on filters at the left, what you're going to see here is that we have this link.

00:00:33
You'll see the list of built-in filters. When we click this, here are the built-in filters which we have available to us in Jinja2. So much of this is very like what you will see in regular old Python. Now what I'll say is that you can actually create your own custom filters within Jinja2.

00:00:49
That is allowed outside the scope of this scale right here. Listen, but let's not worry about that. Let's just quickly focus on these built-in filters and do a little bit of explanation then. So like I said, we have all of these things available to us.

00:01:02
Let's check them out and see how they work. So let's maybe pick, let's just say I don't know, capitalize. That's a quite a straightforward one. We'll go with that one. So let's see how we can implement the capitalized feature into Jinja2 then. So what I'll do here is I'll go in, and I will open my file.

00:01:18
And let's go back, and I'll go into my R1.yaml. And let me add another key here. Let me just say-- let's just say SNMP. And we'll go 1, 2, 3, 4. And we'll say community. And let's just call this maybe john, super simple, OK? Not very creative, but we'll go with it.

00:01:34
So that's going to be the name of the SNMP community. And also let's go and create the new file then. So we'll create a template just for SNMP. We'll see snmp.j2. And if we go back to our script-- so we'll copy example2, and we'll say example3.py. If we just modify this, let's go into example3.

00:01:56
And we'll just change-- the name of the template we're going to look into this time is going to be snmp.j2, OK? Same host profile is going to be used, R1.yaml. Just pushing it through a different template. So what I'll do is, if I go and open up SNMP, so enter templates, enter the snmp.j2, all will render as SNMP community, I think, the syntax says.

00:02:18
We'll go with that anyway. And then what we want to do is to effectively populate the value that we have in our YAML file. So it's going to be the SNMP key in capital letters. SNMP dot, and then we'll go into the next nested value, which is going to be the word community.

00:02:35
And that should return the value john. So we'll say community. And let's just save this from now. And if I go and try running this script, let's see what's going to be rendered. So I'll say example3.py, hit Enter. And lo and behold, we're rendering that configuration.

00:02:48
But what if you wanted to add then, like I said, some type of filtering. Let's do this capitalization then. Well, it's quite simple. All we're going to have to do is use the cap symbol, and then specify the filter that we want to use. So let's say I wanted to use some capitalization.

00:03:02
No matter what the variable name was, I could see cap. And then the name of that built-in filter happened to be capitalized. And that is with our zed, or a z if you're American. And let's just save this. And if we arrow up, then it would helpful then to spell it capitalize.

00:03:18
If I spell it correctly, that would be super helpful. Capitalize, that'll be a little bit better. Let's try that one more time. And as you can see here, it doesn't matter what the value is. It's always going to be capitalized. So if I change the value once again, let's say Trevor.

00:03:33
And I'll put this all in capital letters. Let's see what happens. If we Arrow up, notice that the trailing letters are all lowercase. Capitalize only capitalizes the very first letter. This is a good way to have some nice in-built standardization, regardless of how they may be stored within our host files.

00:03:52
So again, not that you would want to actually use this filter in this context, but just as an example to highlight how easily you can use this. Again, let's just use, for example, the reverse filter, which is built-in. Just use the pip, and then specify the filter.

00:04:06
So now if we save this, and we go back to our screen, and we run the script, suddenly, the ones which are not supposed to be configured, the variable has actually been reversed. You see that? And again, that is not something you would do with a network automation.

00:04:20
It's just to highlight how we can invoke those filters. So I really would encourage you to explore the built-in filters. And then I should get more comfortable. You can, like I say, even create your own custom Jinja filters. But for now, you've been able to do a variable substitution, your loops, your conditional statements, and implementing some type of filtering.

00:04:40
That is going to make up the vast majority of your use of Jinja and network automation. And these types of templates, which we are seeing rendered, this is a type of template that you're going to eventually see then to say, for example, the Scrapli library, which is actually going to push these templates as actual configurations to target devices.

00:05:00
So that is it for Jinja2. I would just encourage you to keep learning, keep practicing. And I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**The pipe ```|``` symbol is used to invoke a jinja filter.**