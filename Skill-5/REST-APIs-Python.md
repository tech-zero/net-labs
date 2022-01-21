# ```REST API```s & Python

## Introduction

00:00:00
Hey, guys. And welcome back to another skill in Python from Network Engineers. So in this skill right here, we're going to be focusing on something which is a lot more modern when it comes to network automation, that is dealing with APIs.

00:00:27
Now if you haven't heard about what an API is, an **API** is an **Application Programming Interface**. And in essence, what an API does, it allows two applications to, in effect, talk to each other. So whenever you pull out your phone and you access say, for example, Twitter, and you send someone a DM, ultimately under the hood, you are, in essence, using some form of API.

00:00:52
Now here's the thing about network automation. So many of our devices are classified as legacy devices. These are our devices which were developed way before the age of automation. They aren't exactly built for automation. And in effect, to automate these devices, we have to retrofit our solutions on after the fact.

00:01:14
It's not exactly the most smooth and seamless process. So when we are automating legacy devices, we're going to be sending ```CLI``` commands, typically over ```SSH```. And what we tend to get back is just generic string data. Think of the output of a show IP interface brief.

00:01:34
It's not exactly structured data. It's just, in effect, one big string blob. Now throughout this course, we have learned that there are some ways to mitigate this problem. We can use things like ```TextFSM``` parsers or maybe the ```Genie``` parsers. These are effectively using things like regular expressions to convert that string data into structured data.

00:01:55
Now the thing is with APIs, we can get that data natively off the box in the form of structured data ready to go. This is typically going to come in the form of JSON. This is by far the most popular type of format that you're going to see nowadays. So for us as network engineers wanting to be able to program our networks, being able to interact with our devices in a very programmatic way of getting information as structured data, this is going to make our life much, much easier.

00:02:26
Now there are definitely more than one type of API, but the architectural style that we're going to be focusing on in this skill is something called a ```REST API```. So throughout this skill, we're going to find out what a ```REST API``` actually is. And we're going to be able to see how we can interact with this ```REST API```.

00:02:44
We're going to be using HTTP, which is the Hyper Text Transfer Protocol. This is what you use when you go to access a website in your browser. And we're going to learn that this HTTP protocol actually has some methods of its own. This is how we can perform particular tasks.

00:03:00
If we want to get information, or maybe change information, or a server, we can do that through the use of these HTTP methods. So it is important that we understand what they are and when to use which one. Now the cool thing about working with an API is that we get very explicit communication between the client and the server.

00:03:19
And you're going to see that when we attempt to talk to a server when we try to send a message or retrieve some information, the server is going to return back to us status codes. Now these are very valuable because it allows you to confirm if your request has been successfully taken, or it can provide some really handy troubleshooting information to tell you where exactly the request went wrong, say, for example, maybe the authentication failed or perhaps that the server was just dealing with too much traffic at that time.

00:03:48
These status codes are going to allow us to understand what exactly has happened and easily delineate whether a request has been successful or not. So super, super useful. Now what we'll also cover within this skill is going to be some of the tools that we can use in order to interact with ```REST API```s.

00:04:05
We're going to check a tool called Postman, which has very, very popular when testing APIs. So we're going to have a look at that. But what we're also going to look at is how we can interact directly through Python with a ```REST API```. Now traditionally this was going to be used in the Requests library.

00:04:23
However, there actually is a newer library on the market. The new cat in the block is one called HTTPX. And this is pretty much like the Request library, but with a little bit extra on top. Basically in my opinion, it has an improved version of the Requests library.

00:04:39
So it makes sense that I share with you, what my opinion is, the better solution. So we certainly will be looking at HTTPX. Now what we're also going to do is to dip our toe into what is called the Restconf protocol. This is a protocol developed for network automation, effectively.

00:04:57
It is REST-based, and it allows us to interact with our devices in a programmatic way. This is the protocol we're going to be using to interact with our devices over HTTP. Now there are some things associated with the Restconf protocol which are a little bit difficult to get your head around.

00:05:13
And for the purposes of this skill right here, we're not going to be focusing on that. If you want to look at Restconf a little bit more deeply, then you can follow my skill on Restconf in my Advanced Network Automation course here on CBT Nuggets where we deep dive all the details of this very protocol.

00:05:29
But for the purposes of what we want to learn within this skill, having a brief look of Restconf is going to help you understand what we're learning here and how you can conceptualize where we're trying to go with it, what exactly is on the horizon, how can you actually leverage these skills that we're learning right now.

00:05:45
So I do think getting a glimpse of this protocol is certainly going to be useful to understand the applicability of what we're learning here so that it's just not all in a vacuum. Because the last thing I want you to do is to go and learn all these Python concepts and then think, well, I don't really understand what exactly I can do with them with respect to the networks.

00:06:04
So definitely looking at the Restconf protocol, albeit briefly, will certainly help you identify the target and see where it is we're trying to go. So that is the general overview for what we have planned for this skill right here. The first thing we have to talk about is what exactly is REST?

00:06:20
What are we talking about when we see this word right here? Well, how about we find out that answer. That is what we're going to be doing in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

---

## What is a ```REST API```?

Hey, guys, and welcome back. So let's talk about this thing called ```REST```. What do we mean when we talk about a ```REST API```? Well, what a ```REST API``` is-- it is simply the architectural style for that API. And it stands for **Representational State Transfer**. So that is the name, but what exactly does this mean?

00:00:33
Well, ultimately a ```REST API``` can be characterized by some distinctive attributes. Let's talk about them. Well, the very first thing to note about a ```REST API``` is that it's going to be stateless. This is a common characteristic of this API. So what does that actually mean when we talk about something being stateless?

00:00:52
Well, quite simply, it means that the ```REST API``` server doesn't keep state. So the server here and the client here-- they don't actually have to know anything about each other about the previous state. You can think about this as like the opposite of using cookies in your web browser.

00:01:09
When you use cookies, effectively the server is keeping state about what you've done on the websites. When we're being stateless, we don't really care about what has been sent previously. In effect, if we send a message to the server, the server is going to be able to understand any type of message we send it without having to know or remember any of the previous messages that we have sent.

00:01:31
Now, the purpose of this stateless attribute is that it really does help with things like performance and scalability and allows for things such as updates to happen seamlessly, without disruption. So ultimately, we get this nice, reliable solution. Now we kind of just touched upon this point right here, but another architectural characteristic of your ```REST API``` server is really splitting the client and server apart.

00:01:55
They're not reliant on each other. So like I say, if we happen to change the code on the client side, we can do so. And it's not going to affect the server. And vice versa, if we happen to change some code on the server, it's not going to have any effect on the client.

00:02:09
Basically, as long as the client complies to a particular formatting of a message, which we as the client could find out reading the server documentation-- so long as we abide by those rules, we can send our messages to that server. And we know the server is going to understand our messages, A-OK.

00:02:26
So again, that really does provide us a lot of flexibility. Now when using a ```REST API```, we're going to see this typical structure. The first is going to be some type of HTTP verb or a method. That's the notes if we want to get a resource, like pull information from the server.

00:02:44
Or if you want to maybe, say, change a resource, or if perhaps you want to delete a resource, your ```REST API``` is going to be using very particular verbs to be able to perform these types of operations. And we'll get to talk about what those HTTP methods are very, very shortly.

00:03:00
So what we're also going to send within our message is some type of what is called a header. That's just something that we could send to a server which allows us to specify the type of information we want to pass along during a request. Like what is the actual structure of the data we want?

00:03:16
Do want it in the form of XML? Do we want that structure in the form of, maybe, say JSON? This type of thing can be specified within our header. Now, an important and distinctive thing about a ```REST API``` is that we're also going to specify a particular path to a resource.

00:03:33
So let me give you a rough example. Let's just say that we had some type of ```REST API``` which was going to pull information about the state of our network. Let's say we wanted to retrieve as structured data all of our BGP neighbors. Then maybe we could send an HTTP request to that server.

00:03:51
Let's just maybe say HTTP. Say my network server. Let's just make up a random URL dot com. And if we wanted to, say, for example, get BGP neighbors, we would specify a path to that resource. So we would maybe go into forward slash BGP, which would give us all the BGP information.

00:04:10
And if we just want their neighbors, we would say forward slash neighbors. This would be the path to get the resource of our BGP neighbors. And similarly, if we wanted to get the information of, let's say, maybe, I don't know, the configuration on gigabyte 1, maybe you could say something like, say, forward slash interfaces, which would give us all their interfaces, and then forward slash gig1.

00:04:33
You get the draft. Basically, by specifying a unique path in this request, this HTTP request, we are going to get a unique resource. And this is really the type of way that the RESTCONF protocol works, which we will see a little bit later on in the skill.

00:04:48
Now if we happen to make a request, and we want to change some information about the server-- let's say we wanted to maybe inject a new access control list. We would also have the option of passing in an optional message body. So we could perhaps structure maybe some JSON and define all of our access control lists in this structure, and then send it from the client to the server.

00:05:10
And then the server is going to either accept or deny that change. And depending on what it does, it's going to give us back a particular status code, which lets us as a client know in no ambiguous terms what exactly has happened. Was the operation successful?

00:05:28
Has this access control list been implemented? Or if it failed, why exactly did it fail? This is going to be determined via the status codes. So that's just a very rough overview about how we are going to operate with the ```REST API```s. But like I say, we do have the option when communicating to our servers.

00:05:45
Do we want to delete a resource, change a resource, maybe just get information about a resource? We just mentioned that we had these particular HTTP verbs on how to perform these actions. What exactly are those methods? Well, that's what we're going to be doing in the very next Nugget.

00:06:00
So I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**```REST API```s leverage a stateless connection between client and server.**

---

## Understanding the Methods

00:00:00
Hey, guys, and welcome back. So let's now talk about what these HTTP methods are and what they're all about. So in order to understand the HTTP methods, we have to understand CRUD. No, CRUD doesn't mean something bad. It's just simply an acronym. Basically, when we are dealing with a resource using a REST API, we have the option to create a resource.

00:00:37
We also have the option to read a resource. We also have the option to update an already created resource. And we have the option to delete a particular resource. So to put this in networking terms, let's say we wanted to create a brand new access list.

00:00:55
We could use a create operation. Or, if that access list already existed, and we just wanted to read it from the server, kind of like a show command, we would want to send some type of read operation. Now, if that access list already existed, but we just wanted to add some new policies to it, we could update that resource by using an update operation.

00:01:16
And if we had an outdated access control list that we didn't want to be present anymore, then we would have the option to delete that resource. But here's the thing. We don't actually send a create request, or a read request, or an update, or a delete request.

00:01:31
Instead, these types of operations map to particular HTTP verbs. So let's talk about what those verbs are, and which map to which. So the first one we're talking about is how we can create a particular resource. Now, using HTTP, the type of request that we're going to send here in order to create a resource is going to be what is called a POST request.

00:01:55
So this method is going to create a new resource of a particular type. So again, let's use a networking example. Let's just say we had turned on our networking device, and we wanted to create a look loopback address, loopback0. Now, loopback0 does not exist on this server, i.e, the device, so we could send a POST request to create that loopback.

00:02:18
So the POST request is going to be the type of request which maps to the C of our CRUD operations. A POST request-- that is the method we're actually using-- OK, so creating a resource, but obviously, that is not the only thing we want to be able to do.

00:02:33
Let's talk about how we can read a resource. So if we want to be able to read the resource, the type of HTTP method that we are going to send is going to be known as the GET method. So we send an HTTP GET request. Now, the key thing here is that when we send a GET request, this is a read-only request.

00:02:53
It's not going to have the ability to modify or change any information. It's only going to pull that information from the targeted server or the device. So that would mean that if I happen to send a GET request about this newly created loopback0 interface that we created using a POST request, we could continually send that GET request 50 times, and we should just continually get back the exact same response, over and over and over again.

00:03:20
Because that GET request is not going to modify that information. The only way the GET request would change would be if we happen to make a change to that resource by updating it. So if we just want to read the resource, just like we would using a show command on a Cisco device, the type of HTTP method that we want to use is going to be this GET method.

00:03:41
So that's how we can create a resource, how we can also read a resource. Let's talk about how we can update a resource. Now, in order to update an already created resource, we're not going to send a POST request. Instead, we're going to send a PUT request.

00:03:58
So let's say we had an already existing physical interface on our device, let's just say gigabit1. If gigabit1 originally had an IP address of 10.0.0.1, and we wanted to update gig1 with a new IP address, we could send a PUT request for that resource so that gig1 now has a new IP address of, let's say, 10.0.0.5 maybe.

00:04:21
So we're not creating this resource from scratch, but we are wanting to update the IP address to a new value. In this case, we're not going to be creating the resource, we're going to be updating it. Therefore, we're going to be using a PUT request. This is the method that we're going to send in our HTTP request.

00:04:39
So, as we can see, we have learned how we can create, read, update our resources. Let's see how we can finally delete a resource. Well, this one probably is the easiest one to remember how we can map to our CRUD operation because in order to delete a resource, the actual method we're going to send is also called a DELETE method.

00:04:59
So like I said, this one is super-easy to remember. So again, let's say we had created loopback0 for a particular purpose. Let's say we were using this loopback in order to stand up a BGP peering. And for whatever reason, we wanted to remove that loopback later on.

00:05:15
Well, since that resource, loopback0, has been created on the server, in order to remove that loopback, that resource, then we would want to delete it by sending the DELETE method. And by sending that method, well then, that resource is going to be deleted.

00:05:32
Now, again, just like we say it how can we target a particular resource so that we don't delete all the BGP configuration or all the interface information. Remember, with REST APIs we can specify a particular path. So again as a quick example, let's just say we send the request to http://-- let's just say someexample.com.

00:05:54
And maybe we could go into the interfaces resource and then be a little bit more specific by saying loopback0. If I send a POST request to this path, then it would create that resource. If I send a GET request to this path, then it would get me the information about loopback0, maybe things like what its interface description is or its IP address and subnet mask.

00:06:19
Now, if I wanted to update that resource, then, of course, I could sent a PUT request because that is going to be an update operation. And if I just wanted to totally delete that loopback, well I could just specify a DELETE method using HTTP targeting this address, which would therefore target this particular resource of loopback0 with the method of DELETE, which would in effect remove that resource from the server.

00:06:43
So REST APIs-- it's all about CRUD operations-- creating resources, reading them, updating them, and deleting them. And in order to do so, we have the POST request, the GET request, the PUT request, and the DELETE request. Now, like I say when we interact with our servers, our servers are very helpful and very explicit.

00:06:59
They're going to give us particular status codes allowing us to understand if a POST request has been successful or unsuccessful, so on and so forth. What exactly are those status codes? What are the ones we should be looking out for? Well, that's what we're going to be talking about in the very next Nugget.

00:07:13
So I hope this has been informative for you, and I'd like to thank you for viewing.

***Quiz:***
**Which of the following is an HTTP method used to update an existing resource?**

+ CREATE
+ POST
+ **PUT**
+ UPDATE

---

## Understanding the Status Codes

00:00:00
Hey, guys, and welcome back. So let's now talk about the status codes that the server is going to return to us when we make a particular request. So the first term we're going to note here is that these status codes are going to come in three digits-- something like, say, status code of 100.

00:00:29
Now the very first digit is going to give you a little bit of a hint of what is going on here. So let me talk about it. If we happen to have a 1 as the first digit, and then it doesn't really matter what the next two are, this is going to be denoted as an informational status codes.

00:00:45
So if we happen to get a status code of, say, for example, 1 or 2, this is a status code used to denote processing. So this code here doesn't tell us whether a request was successful, whether it was a failed request. It just gives us some information.

00:01:02
And we can tell that because we have a 1 beginning. Now the status codes that we really do like to see are ones that begin with a 2. If we happen to get a 2, this means that we had a successful request. So here are some of the more common ones we're going to see.

00:01:17
If we get a status code of 200, this one is very, very common. This just means OK. And that's just basically a standard response to denote that your request has been successful. So if we get an OK response, hey, well, everything is OK. We have no problems to worry about.

00:01:34
But like I say, our server can give us a little bit more detail. If we happen to get a 2 or 1-- well, it starts with a 2, so we know we have a successful response. But this actually tells us that something has been created. So if we happen to send a POST request, for example, maybe to add some type of access control list on our server, if the server responds back with a 201, we know it's been successful, because it's a 2.

00:02:00
And 01 means that it's being created. Now we also are going to see a very common one which is a 204, again, because as a 2, we know this is a successful request we have had. But this is known as a no-content response. Simply put, the server has successfully taken a request, but it doesn't actually have to return a particular body.

00:02:21
It's got nothing to send back to us. And these really are the more common ones we're going to see. Now if we happen to get a status code that begins with a 3, this denotes that we have a redirection. So if you happen to get, maybe, say, a 307, this would be a temporary redirect.

00:02:39
This basically means that the resource that we're trying to get is in effect using a different URI temporarily. And because of this, we're going to get a redirect. Same, again, if you happen to get a 301-- this would be a redirect because it is a 3. But this means that something has moved permanently.

00:02:58
So hopefully, you're beginning to get an idea of the utility of these status codes. They are very, very precise. They really do give us a lot of insight into the effect of a request. But quite honestly, the redirects aren't quite so common. What is certainly a lot more common is to get our 4-something-something codes.

00:03:17
These relate to client error. This means when you or I as a client send a bad request to a server, we're going to get some type of client error. Number 4 is going to tell us this is the issue. So if we happen to send a request to a server-- so we have the client.

00:03:34
We send a request to the server. And the server comes back with a 400 status code. We know we have a client error. And a 400 status code basically means that we have a bad request. Basically, whatever we are trying to do-- well, it doesn't really make sense.

00:03:49
It's not been properly formatted. So we've got some bad syntax or something going on. We have to check what we're actually trying to send to the server. Similarly, if we get a 401, again, this is also a client error. But this deals with a lack of authorization.

00:04:04
This means we are unauthorized to make a particular request. Or we're trying to retrieve some type of information from a database, and we get a 401. Perhaps we haven't supplied the correct credentials in order to get that information, so we get back a 401.

00:04:18
Similarly, if we get a 403, this is a forbidden request. What we're doing is, quite simply, not allowed. And a very common one, again, is a 404. This means that what we're trying to do-- the page we're trying to get has not been found. Basically, that request has not been found.

00:04:36
It cannot be fulfilled. And like I say, there are many more of these types of requests in the client/server range. The last range we want to look at is the 5-something-something range. And this deals with a server error. So this time, we're kind of off the hook.

00:04:51
It's not our fault as a client sending a request. It is the server that we're trying to reach that's got the problem. So if we happen to get, let's say, maybe say a 500 request or 500 status code, should I say, this as an internal server error. So maybe the server has stumbled upon some type of weird condition that it's not used to handling.

00:05:12
And it doesn't know how to fulfill the request that you're getting it. So basically, the server has an internal error. It can't deal with that request. And it says, hey, here's a 500 status code. I don't know what to do with this. This is really when a server has an unexpected failure.

00:05:26
And again, just like your 400 status codes, your 500 status codes or server errors-- well, there are a lot more of them. So, for example, we also have, let's say, 501, which means not implemented. So in essence, the server doesn't actually support what it is you're trying to do so.

00:05:43
Maybe a particular request method has not been supported. The server is going to tell us that by sending us a 501 and lets us know that this is not actually implemented-- what we're trying to do. And we can also get things like a 509 which deals with bandwidth limits.

00:05:57
Basically, if we go over a particular bandwidth, an Apache server might send back to us a 509 code. This lets us know exactly what the problem is. It's that bandwidth issue. So as we can see here, all of these different types of error codes really give us quite a bit of detail about what is actually going on-- whether a request has went incorrectly, or whether it has been rejected, and if it has been rejected, why it was rejected-- really, really helpful.

00:06:21
But like I say, we now know about these HTTP methods. The type of requests we can send are GET requests or POST requests or PUT requests and our DELETE request, as well as the type of HTTP status codes that we will receive from our servers when sending these requests.

00:06:37
How about we put these two pieces together and begin sending these requests and receiving these status codes? But one of the best ways to do such a thing is by using the Postman software. And that's what we're going to be doing in the very next Nugget.

00:06:49
So I hope this has been informative for you, and I'd like to thank you for viewing.

***Quiz:***
**A 4xx status code indicates which type of response?**

+ Success
+ Redirection
+ Server Error
+ **Client Error**

---

## Sending Requests with Postman

00:00:00
[MUSIC PLAYING] Hey guys, and welcome back. So previously, we had learned about our HTTP methods as well as our HTTP status codes. Let's now explore one of the most popular tools to use when testing REST APIs and that is Postman. OK, so what are we waiting for?

00:00:27
Let's go and install it. So if you just go to Google and search for Postman, it should be the top link right here. Just click on this. And that should take you to the website. Let me just zoom in a little bit. And if we scroll down to the very bottom here, we're going to get this option, download the app.

00:00:41
So let's download this. And what we're going to do here is, I'm going to download the app. Now, I'm using a Windows machine, so I'm going to be downloading it for Windows and it'll be a Windows 64 bit. Now, if I just save this right here, this is going to download what we need to download.

00:00:56
And then if I just double click this, Postman is going to begin installing. OK, so I've now installed Postman. What I can do now is use this tool in order to craft my request, which I want to send to a particular server. Now the cool thing about Postman is that what you can see here down the left hand side is, you can have an actual collection of particular requests.

00:01:17
Just have them all saved in nice folders. So if you want to have to resend the same request, we don't have to re-craft all the information all over again. It's just neatly saved in a nice little folder, and you can just access it easily. So Postman is really, really nice by having these little workspaces.

00:01:34
You can also create your own APIs. We can specify a particular environment with particular credentials and authentication types, as well as things like creating your own mock servers. So what I can do here is, if I want to create a new request, I can go to this plus sign right here.

00:01:50
So if I click this, now we're going to get the information we need. So we can specify a GET request. Or we can do a POST request or a PUT request, as well as a DELETE request. And you'll notice that we also have additional things such as PATCH request.

00:02:04
We're not going to go into that. The main request, the common requests, at least, are the GET, the POST, the PUT and DELETE request. So check this out. Let's try to get a particular resource. So I'll use a GET request, and now I need to specify a particular URL.

00:02:20
So in order to get a particular resource, I've got to target a particular server now online. There happens to be some mock servers which will serve you mock data that you can access 24/7. Let's go and grab one of them right now. If I go back to my web browser, if you happen to search for gorest, you're going to find an online REST API for testing.

00:02:41
So let's click on this right here. I'll just zoom in a little bit here. We can see some of the resources that we can access. Or say, for example, we can get the users that belong to this resource, the type of posts, their comments, so on and so forth.

00:02:55
So here is the thing. Here, it gives me an example of using something called cUrl. This is another way we can send a particular request. But, for now, what I want to do is to show you how we can do this within Postman. So here is the URL here, that's http://gorest.

00:03:11
So I'm just going to copy this right here. Copy the whole thing. Paste you in. And all I want right now is this right here. So I'll copy this, and this is going to be our endpoint. So this will be our URL. Let's paste this in, and let's get rid of quotation marks.

00:03:26
So notice this is the actual path, we're going into public, version one this appears to be, and our users. And we're sending a GET request, we're going to get the users from the server. Now we can have things like authentication, if the server requires it.

00:03:40
But in this case right here, in order to make a GET request, we need no such thing. The reason why I can tell is because this cUrl request here has no authentication in it at all. The headers it's using-- and these are our headers here. We have an accept header, specifying that the type of data we want is going to be in the JSON format.

00:04:01
Like I said, we can specify maybe XML, if XML is supported. But the common one is to get our information back in JSON. And we're also using a content type header, again, specifying application/JSON. So let's take this information here, this exact header and this content type header.

00:04:19
We'll go back to Postman. So let's go into headers right here, OK? Click on this. So what we'll do here is we'll create an Accept key, and the value in this type is going to be application. And you can see the different options we have here. We've got application Javascript and so on and so forth.

00:04:36
But the one we want is application/JSON. And we also want a content type. We'll say content, and if we just put that in, content type. Again, the value is going to be application JSON. Now, we could specify some type of authentication here. We could go in and maybe say, we could choose some type of basic authentication, if that was required.

00:04:55
Then, we could specify a username and a password. In this case though, it doesn't appear we need any type of authentication, so we'll just say No Auth. We have our headers in place. We have our endpoint or path, and we have the type of request you want, a GET request.

00:05:10
Let's try sending this off and see what we get back. If we say send here, you'll notice that there in the bottom here, we have a 200, which means we have a successful response. And if I click the body of the response, we're going to actually see-- this is the information we are getting back.

00:05:25
Do you see this? We have this all as structured data. Scroll on down. We have our data here. In fact, let me just pull this page up a little bit so we can see a bit better. So we can see some users here. We have Lily Williams with Lily Williams's email.

00:05:38
Her gender is female. Her status is active, and we have more users down here. So you see that? We're able to get the information of particular users we want based on the endpoint we specified our headers to get this information in JSON format. Again, let's go back and try one more.

00:05:56
So it says here that some of the resources we have are things like posts and comments. Let's maybe change the request to get the posts instead of the users. So we'll copy this, and let's change the request. So as opposed to users, we're going to get posts.

00:06:11
Let's try sending this off. We have a 200. OK, as we can see here. Let's scroll on down. In fact, let's just pull this page up a little bit. We can see the type of data we have. We have a post, just checking the title, and the body is just check. Commenting, we have a title, which has got all of this-- looks like Latin here.

00:06:28
And if we scroll on down, that continues on. So like I said, I don't want to dive into the deep details of all the things you can do in Postman. There is so much you can do with this. It would really take hours and hours and hours to go through it all.

00:06:39
But to get a rough idea of how it works, then I would certainly would explore it and lab this out. And then like I said, you can use some of these online servers, these mock servers, which will serve you up mock data. So in this example here, we saw a GET request, but as you know, we can send a POST request to create a new user.

00:06:56
We could have a PUT request to update a user, or let's just say maybe a DELETE request to delete a particular user or a particular post. These are all options available to us. And like I said, if I wanted to save this particular request, I could just save it, and save it to a collection.

00:07:11
You could add a description and just say, this pulls comments and posts on the server. And then what you would do is create a collection. So I could just maybe call this gorest, because that's the server we're using. And create this. And now save this.

00:07:24
So if I happened to go to my collection to the left here, we have this request here, which means if I close this down and just click this, it would all be saved for us. The headers are saved, the request is saved, and if we had authentication that would also be saved.

00:07:39
We just hit Send, and we would get that request back once more. So Postman is a really nice tool to be able to neatly keep together all of these different types of requests that you have, which is really quite useful when testing your REST APIs. But for me, the real fun is using pure Python to interact with these REST APIs.

00:07:57
The library I want to show you is HTTPX, and it's super cool. And that is what we're going to be checking out next. So I hope this has been informative for you, and I'd like to thank you for viewing.

***Quiz:***

**Postman allows users to store HTTP requests in the form of "collections".**  True or false?  **TRUE**

---

## Sending Requests with ```HTTPX```

00:00:00
[MUSIC PLAYING] Hey, guys, and welcome back. So let's now check out HTTPX. This as a super cool Python library that's going to allow us to send our HTTP request to our servers. So first thing's first. We have to install HTTPX. So let's do that first.

00:00:27
So go into a directory-- or the actual directory would be helpful. There we go. I think [INAUDIBLE] has an environment. And we'll just activate it. And let's install HTTPX. I think I've actually already installed this. So if I just say pip install HTTPX, it might say I've installed it, which I think I have.

00:00:45
Yep, as you can see, I've already installed it. But if you haven't installed it, then just run through the installation. Then it's going to go through. That is all you need to type to get HTTPX working. OK, so let's check out how we can go about using this.

00:00:57
Let me make a directory. I'll just call this one restapi-stuff. So I'll CD into this. OK, so let me create a file. And I'll just call this get_example.py. OK, so let me show you how we can craft this script then. So let's open our file. Go into restapi-stuff.

00:01:15
And then get example. OK, so the very first thing which I want to do is to import HTTPX. Just hit import HTTPX. Cool. Now remember, we're going to have to specify the type of headers we want as well as the path we want to send a request to, to get a particular resource.

00:01:34
Now we are going to use the exact same test API that we did with Postman that was using GO REST. So what I'm first going to do here is to craft my headers. So I'll just create a dictionary called headers. So obviously, dictionary is going to be curly brace.

00:01:48
We now know this. And the key for that is going to be an accept key, just like we did with Postman. And the value corresponding to that key is going to be application/json. So that's just going to be our first key-value pair. Let's do a comma. And we'll create a new one, one for content type.

00:02:07
And we'll do a colon. And we'll put in a value corresponding to this key again. It's going to be application/json. And for our GET request, that is all we need and the terms of headers. So now we need to specify the endpoint, which I want to use or want to target, should I say.

00:02:24
So I'll just create a variable. And let's just call it-- maybe say my_url. And the URL is going to be, if I just go back to that website, so I'll just grab this URL able to get the users this time through Python. So I'll just copy this. And the URL is going to be this here.

00:02:39
So I'll put this in quotation marks. So it's going to be a string value. And then what I'll do is I will create a little function here. I will just call this one pull_info. You can call it anything you want. And this is going to take an argument. The argument I'm going to pass then is going to be the URL.

00:02:54
So what I'm going to do here is use HTTPX. But you remember from previous skills, we know that we can use this thing called a context manager. That's is going to allow us to gracefully close the connection automatically when we're done with it. So what we're going to do here is to use a with statement.

00:03:12
So I'll see with. And I'll use HTTPX. Now what I'm going to do here is use the client class. And I'm going to make that as client for a context manager. And what I'm going to do here is create a variable just called response to hold a response. And I'm going to create that client object we've just created.

00:03:31
And now I'm going to specify the HTTP method. So remember we have a GET request, a POST request, so on and so forth. We want to get information from our server. So we are going to use a GET request. And we can see this has been auto completed here by VS Code.

00:03:47
Now we need to pass in two types of information here. We need to pass then the resource we want to get, which is going to be the URL. So we will specify the URL. Now the URL is going to correspond to whatever URL we pass in to this function. So we'll just say URL here, which is whatever we pass in.

00:04:04
And we want to correlate the headers arguments to the actual headers we have defined up here. So we'll see headers is equal to headers. Now what I'm going to do, as to return a response-- this means that we can assign this to a variable. Redirect that output effectively.

00:04:22
So what we'll do here is, if I go down, I'll see a result is equal to my pull_info function. And I'm going to have to pass in a URL. So remember it's expecting this argument. The URL I want to pass in is my URL. And remember because we are returning the response, that means that is going to be redirected and saved into this results variable here.

00:04:42
So all I'll do right now here is just print out results. Let's try saving this right now. And what we'll do here is if I do clear and I say python3 get_example, notice that I'm getting a response of a 200 OK. This means that we have a successful response.

00:04:59
But whereas all the details, whereas all the data we want-- well, actually, within the HTTPX library, we can get that information by taking the .text attribute of a response. So a response returns the actual code. If we actually want the output, we're going to have to use the text attribute.

00:05:18
So we will return the text attribute from a response. So if we save this, that means that the text attribute of the response will be saved to this results variable. So when we print it out, we're actually printing out the text and not just the status code.

00:05:32
So let's add them up and try this again. And bam, look at this. We have all of this data right here. Now here is the thing. This data we can't work with right now as structured data. Let me show you why. If I print the type of results we have here, save here.

00:05:46
And let's add them up. This is actually a string blob, even though it looks very much like structured data. Now what we can do here is use the built-in JSON module to take this data, even though as a string. And that's going to be able to translate all of these curly braces and square brackets into Python dictionaries and lists.

00:06:06
So what I'm going to do here is actually translate this. So I'll import the JSON module. As opposed to returning response.text, what I want to do is to take that text here. So I can actually access it by just saying .text right here. This will gave us the exact same effect as what we saw before.

00:06:23
It gives us the string data of a response. And what I want to do here is to use the JSON module to convert that string data into dictionaries. So I'll say json.loads. And what I want to do is pass in all of this stuff right here, all this text data. Put this all in parentheses right here.

00:06:41
And this means that the response is going to be taking your text attribute of the request and putting that through the JSON module's load function. This means that the response is actually going to be in structured data. So if I save this now and I try this again, this time, we're no longer working with a string.

00:06:58
We actually have a dictionary, which means we can work with it programmatically. So let's go and try this. And in fact, what I'll do here is, to make this look a little bit prettier, I'll see from rich import print as rprint. And I will rprint my results.

00:07:12
I'm not going to print the type. I'm actually going to print the results now that it's been converted into a dictionary. So let's try this again. And look at this. We have all of this structured data here. You see that? And notice that we have these outer keys.

00:07:24
We've got this outer keys in meta, which gives us some type of metadata. And we have this data key, which houses all of the data. So if we just want to get the data and ignore the meta, what we could do here is actually grab that dictionary key. Let's just grab the data key.

00:07:41
So let's save here. Let's add them up. Try again. And now this time, we've stripped away that data key. And all we're left with is the actual data. And you'll notice that we have this list object. See that, the square brackets? And we could just work with this programmatically as we ordinarily would.

00:07:56
We could use for loops to parse that particular data and specify different keys to pull out particular values because we have access to this nice structured data. So this is how we can craft a GET request. Let's see how we can maybe craft a POST request and create a resource.

00:08:12
So what I'll do here is I will create a file called post_example.py. And the difference here is that a POST request actually does require some authentication. So what I'm going to do here is go to my browser again. Now what I'm going to have to do here is to get my own authentication token.

00:08:29
So what I'm going to say here is I'm going to collect to get my access token. And it's going to tell me I'm going to have to log in via Google, Facebook, or GitHub. I'll use my GitHub. OK, so I've log then with GitHub. Here is my personal access token.

00:08:42
It says, don't share it with anyone. Don't publish this on any websites, even though I am. But what I'm going to do is after I'm done with it, I will regenerate a completely new one. So this will not actually be valid by the time you actually see this video.

00:08:54
So don't try to copy it, OK? So let's go for this one now. And I'll just paste this in here, just for safekeeping, for the moment. And obviously, your access token will be different from the one you're seeing here. OK, so let's go and create this POST request, then.

00:09:07
So I'll open this up. And what I'll say here is import. And I'll just do JSON again. And we'll import HTTPX. And like before, we'll just say from rich import print as our rprint. OK, so let's create some headers again. This time, in order to craft my POST request, I'm going to have to create an authorization header.

00:09:26
And the value is going to be the word "bearer." And then I need to paste in whatever my token is. So I'll just paste this in here. Now this is getting a little bit unruly. Let me make this over multiple lanes right here. OK, so that's a little bit neater.

00:09:39
And again, what I'll say is my_url is going to be-- am I going to create a user or a copy the same URL here, in fact? Now I'm also going to have to supply additional data. So what I'll do is I'll create a dictionary called payload. And I'll just grab that as a template right now.

00:09:54
So I'll just copy here. Paste this in. And I'll grab the dictionary right here. Copy this. There we go. And I'll paste us in right here. And what I'll do is I'll change some of the names. So I'll say Trevor Sullivan. And I'll make the address Trevor Sullivan, some random numbers in.

00:10:10
OK, and I'll make this look a little bit easier to read. So I'll just put some spacing in here. And just like before, what we'll do is we'll create a function. We'll just call this maybe post_stuff. And again, we want to pass in a URL. We'll use our context manager.

00:10:22
We'll say with httpx.client as. And we'll just use the word "client" just like we did before. OK, a response variable. And it will take our client object. This time, we'll use the POST method. We want to create a new user. So we're going to pass in the URL, which we're going to target.

00:10:38
This is going to be the resources. I.e., we want to create a user. So we're targeting the users. The headers is going to be equal to, again, the headers up here, this dictionary. And we also have this additional argument called data. This is the argument we're going to specify for the type of data we want to send.

00:10:56
So that's going to be defined by this payload dictionary. So we'll see if data is equal to payloads. And what I'll do here is I will return the response, which will give me the response codes. And in fact, I also want to be able to see what the output is.

00:11:09
So I'll also create a variable for the structured response. So I'll just say structured response and make that equal to json.loads. And we'll take a response object with the text attributes. And we'll also return that as well, then. So just as we saw before, I'll just say results is equal to-- and we'll call a function, which is going to be post_stuff.

00:11:28
And the URL is going to be equal to my_url. And if we just rprint results, we should get a tuple back because we are returning two different objects. What I'll do is I'll actually remove the accept header and just go with the authorization. Arrow up, hit Enter.

00:11:43
And there we go. We get our 201, which is a created response. This means this is a new object that has been created. And the information is right here. Here is the data. We have an ID. We have the name, Trevor. And we have Trevor's email. Trevor is male.

00:11:59
And his status is active. Now if I happen to try to resend that same request, watch what happens. Unprocessable entity-- we've got a client error. That is because the email field has already been taken. The server is not allowing us to recreate another user, effectively, with the same details.

00:12:17
So like I say, very, very explicit. So there we have it. That is how we can use the HTTPX library in order to be able to craft GET requests, POST requests, as well as PUT requests, and DELETE requests. Let's take the same principles that we've just learned and see how we can apply it to a REST conf server.

00:12:35
This is going to allow us to see the applicability of this type of behavior and in networking context. That is what we're going to be doing in the very next Nugget. So I hope this has been informative for you. And I'd like to thank you for viewing.

***Quiz:***

**Which of the following will allow a user to access the string text properties of a request's response body?**

+ **```response.text```**
+ ```response.result```
+ ```response.json```
+ ```response.string```

---

## The ```RESTCONF``` Protocol

##### 00:00:00
Hey guys, and welcome back. Let's now take what we've learned about the ```HTTPX``` library, and let's pull some networking information from a real networking device. What we're going to be using is the Always-On Cisco DevNet Sandbox. This device is a modern device, and it's actually been configured for the ```RESTCONF``` protocol.

##### 00:00:31
So if we do send that request, it should return the data back to us in nice JSON format. So let's check this out then. So what I'll do here is I will copy my get example and I'll just call this getdevnet.py. And what I'm going to have to do is to get the log in credentials for this device.

##### 00:00:49
So let's go to that device then. So if we just search for devnet sandbox, click this, I will just log in with my GitHub, and I'll say get started with Sandbox. So what I'm going to do is search for XE for the Cisco XE device. And we have this always-on device.

##### 00:01:05
Let's click on this one here. So let's scroll on down and get the credentials. So this is the URL we're going to target. Let's copy this, and we're going to get DevNet. So we'll change the URL to this URL here, and what I'll do here is I'll just get rid of this stuff.

##### 00:01:20
And I'm also going to add, then, this auth augments. And that's going to be in the form of a tuple, so I'll use my parentheses. And the username is developer and the password as C1sco12345, with a one for I here. So I'll say developer and C-1-S-C-O 12345.

##### 00:01:38
Now because this is just a lab environment, I don't want to do any type of SSL verification. So I'm just going to say verify as equal false. And what I'll do here is just delete this part. So we're pretty much ready to go. The difference here though, is that what I'm going to have to do is I'll say https.

##### 00:01:56
Now, the URL here isn't going to make much sense. That is because the RESTCONF protocol uses something called YANG data modeling, and this is how you can actually find out what the URL is. It's based on what a particular YANG model is. But we're not going to be looking at this right now.

##### 00:02:11
YANG is pretty complex. If you want to learn more about it, and if you happen to check out my advanced network automation course right here on CBT Nuggets, then all of this will be explained in great detail. But right now all we're trying to do is to get a sense of this type of applicability in the real world.

##### 00:02:28
So let's not worry about the details right now. What I'm going to do is just tell you a working URL. And if you want to craft your own URLs, and understand YANG, then be sure to check out my other course. So I'll just say 443/restconf/data/native. That's just going to be my full URL.

##### 00:02:48
So if I just save this right now, and just before I do anything, I actually I just remembered, with HTTPX, we're going to actually have to pass in the verify argument at the client level right in here instead. My mistake. So I'll make the equal to false here.

##### 00:03:02
So that should be a bit better. Now just before we try that script, we're going to have to make a slight amendment. Now because we're not issuing an irregular REST API, we're using the RESTCONF protocol. And like I said, the RESTCONF protocol is deeply intertwined with YANG data.

##### 00:03:16
But I'm actually going to have to specify this here in our header. So what we're going to say is yang-data+json. Again, we'll do +json. If we save this, and try running the script, then. And we're getting a 200 response. Great, but where is the actual data?

##### 00:03:33
Well, just like before, let's return the text. Save here, try again. And look at all this. We have all of our data here, all our configuration in the form of this nice structured data, and it's saying over HTTPS. See that? We have our BGP data. Here are some OSPF data.

##### 00:03:51
And just like before, if you want to get out particular information, we could translate this into structured data, and work with it programmatically. And in fact, what we could actually do is become even more specific using the URL. And again, this is based on YANG.

##### 00:04:05
So don't worry about how I configure this out. I say router, BGP, I save this, clear the screen, try again. We're now just getting back BGP information. You see that? And again, this is very much based on the REST architecture. By getting more specific information from the URL, we're actually pulling back more specific information from the server.

##### 00:04:24
And these principles of REST APIs are really very much the modern way of automation. This is why we're wanting to learn about different methods or get requests or post requests, understanding what our headers are, understanding our status codes, so that we know when we get a correct response versus a particular failure.

##### 00:04:43
So that really is a lot in this skill, and the truth is we can only scratch the surface of a subject like REST APIs in such a small space of time. But as always, learn about what you've seen here. Try it out, learn those methods, learn those status codes, and begin experimenting with Postman and HTTPX.

##### 00:05:01
I hope this has been informative for you, and I'd like to thank you for viewing.

***Quiz:***

**Which is the name of the data modeling language used by the ```RESTCONF``` protocol?**

+ JSON
+ XML
+ YAML
+ **YANG**
