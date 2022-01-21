# Version Control

## Introduction

00:00:00
Hey, guys. And welcome back to another skill and Python for Network Engineers. Now this skill could honestly almost be the very first skill within the courses. It's that important. But I made the decision to focus on the fundamentals of Python first before we deal with this exact topic.

00:00:28
So what am I talking about? Well, we're talking about version control. More specifically, we're talking about using Gits to manage your records. Now, if you've been around the kind of the dev world, you probably will have heard of something called GitHub.

00:00:43
Now GitHub is in fact, different from Git itself. They're not the same thing. But throughout this skill right here, you're going to see that there actually is some quite tight integration between both of these. But before we get to GitHub, let's first talk about Git.

00:00:58
What on earth is that? So let's discuss it then. So Git falls under the rubric of something called a Distributed Version Control System. So as you've seen throughout this course, we've made many modifications to many of our configuration files or code that we've written.

00:01:15
And this is a very common practice. When working with automation, you're going to be making changes to host variable files, maybe updating an access control list and your YAML file. But here's the thing, we don't just want to just change that, and then forever forget about what the configuration used to be.

00:01:32
That is not really ideal. Because what if the situation and the network changes, and we want to be able to roll back to a previous configuration? Well having pretty much every version of that file recorded and stored is going to be very useful for implementing that type of rollback functionality.

00:01:49
And this is what we're talking about when we're dealing with version control. Imagine being able to take a snapshot of all the changes that you have made to a particular file, be it a YAML file or some Python codes. Imagine being able to undo any mistakes or any changes at the drop of a hat-- just easily revert back to a prior version.

00:02:09
Well that's just what Git is going to do for us. So here's the thing, Git this going to effectively track our file. So let's say we've got a little file here and a little file here-- not exactly the best graphics, but we'll go with it. So here's the cool thing about Git.

00:02:23
When we actually use Git to track these files, Git is not going to happen to track, say for example, a particular change within that file-- like if you happen to change this line and this line. It well track that, but that is not what is only being track.

00:02:37
In fact, Git is going to store, not just the changes, it's also going to store all of the metadata associated with that file. And this is really, really powerful. And the way Git does this, is that it in essence, takes what can be described as a full snapshot when we are committing our changes and committing our changes to tracked files.

00:03:00
Now this is some type of Git terminology which I'm using right now. This might not make sense quite just yet, but the idea of tracking a file and committing a file, this is going to become very, very familiar to you as you walk through this skill. But suffice to say, if we have file one here and file two here and file three here-- and again, we have good graphics-- this is denoted some type of code in here.

00:03:23
And if we happen to tell Git get to monitor and effect track these three files-- let's say for example, the first line. And the first file happens to be changed, but nothing happens to these files here. When we happen to take that snapshot of these files, we're not just going to have a snapshot of this file and its changes, but also going to have a snapshot of the files that even weren't changed.

00:03:48
And this is partly what makes Git such a robust and reliable solution. Now you might be thinking well, John, does Git just track absolutely everything? Is there any way that we can exempt ourselves from maybe missing some files that we don't want to track?

00:04:02
Well, absolutely that's just true. And we're going to explore how we can do this within this skill. We're going to learn about how to Gitignore files. These are effectively files we don't want to commit to Git. We don't want them tracked by our version control system.

00:04:16
So this might be things like, I don't know maybe, files which have sensitive information, like say passwords. These types of files are a classic example of something that you would want Git to ignore. Because quite frankly, you're going to learn that during your workflow when we have something committed to Git, we want to be able to store it remotely somewhere in the cloud.

00:04:36
And that is where GitHub comes in. This is where we can really collaborate with all of our files when we're making changes and working on codes. And then when we push all of our files that are stored within our local Git over to the remote GitHub repository, we really don't want to be sharing files which have, like I say, passwords and sensitive information.

00:04:57
So we're certainly going to learn about how we can deal with that in this skill. And what we're also going to learn is that working collaboratively with Git is a huge, huge thing. This really is a big advantage of working with something like Git, being able to collaborate with your teammates, work on changes, track who's done what, so on and so forth.

00:05:16
Now in order to be able to work collaboratively and efficiently, we're going to learn that Git is going to give us the ability to build branches. And we'll learn what branches are in a little bit more detail very, very soon. But suffice to say, this is another key concept that we are going to be talking about in this skill right here.

00:05:33
Now what happens at a high level overview when we create a branch within Git, we effectively create our own little timeline for a particular file. This is a good way so we can make changes and work on new features without having to disturb the stable code base.

00:05:48
But ultimately, if the changes we happen to be experimenting with are good and we want to bring them back in to the main branch that we're working on, we want to learn how we can reintroduce that split back in. And In order to do so, we'll be looking at how we can merge our files, as well as how we can also rebase them, which is really quite similar, but that adds a little bit of a detail here.

00:06:12
In particular situations you're going to want to rebase, and in all those situations you are definitely going to want to merge instead. And we'll get to talk about what to use when. And quite honestly, we do have a little bit more in store. For example, sometimes we're going to realize that we're going to run into things like conflicts, whereas maybe say we've happened to make a change on a particular file and a teammate has also made a change on the same file at the same entry point.

00:06:38
And now Git doesn't know which file to resolve or which change to implement. Again, this is a common problem when we're working collaboratively. And we have to understand how we can resolve this with minimal friction. And again, this is something that we are definitely going to be looking at within this skill.

00:06:54
So suffice to say, Git is a huge topic. We can't cover it all. But we certainly will get to the very main point that we need as network engineers to be able to work collaboratively and efficiently with our team when automating your network. So I really am excited about this skill.

00:07:08
It's going to be so, so useful for you when managing your network. Being able to effectively time travel when managing your files is such a cool feature and really, really useful. So how about a shout out? Let's get to it. Let's begin by finding out how we can set up Git.

00:07:23
And that is what we're going to be doing in the very next Nugget. So I hope it's been informative for you, and I'd like to thank you for viewing.

---

## Setting Up Git

00:00:00
Hey, guys, and welcome back. So let's talk about how we can get Git set up within our environment. So what I'm going to do here is log in to my virtual machine here, which I've just created. I'll type password and perfect. So what I'm going to do here is simply walk through the installation of Git on this new virtual machine, just so that you can see it from scratch.

00:00:32
So what I'm going to do here is open up my browser. And all I'm going to search for is install Git for Ubuntu. This is the virtual machine I'm using. And if I just click on this top link here, so what I'm going to do here is zoom in, and we can see here is that it says that if you're on a Debian-based distribution, such as Ubuntu, try using apt.

00:00:51
So we're going to use sudo apt install git-all. So let's grab this here, copy here, and let's go to our terminal here. And let me just full screen this a little bit, here we go. So I will just paste this in here. I'm going to type in my sudo password, and hit Enter.

00:01:05
So I'll just say, yes, and that's just going to run to the installation of all the things that we need. So let's give it a little bit of time. So that took a few minutes, but now we have everything installed. So what I want to do here is to create a username and a user email.

00:01:19
This is going to uniquely identify the user to the Git system. Now we do have the option of creating a username and an email address globally, which is going to apply across all folders, or we can just work within a particular folder and have a different user in multiple areas.

00:01:35
What we are just going to do for simplicity is to configure a global username. There will be one user on that system. So let's go through that installation, or rather, configuration, should I say. So all I'm going to say here is git config, and then dash dash, and we want a global configuration, and we'll say user.name.

00:01:53
Now, I've got this little throwaway account which I use for many demonstrations. I just call it johnredtest. So this is going to be the username I'm going to use here. So let's hit Enter. Perfect. So let us now configure the email. So I'll say, git config, --global and type.

00:02:09
That would be great. We'll say user.email, and the email is going to be johnredtest@outlook.com. Again, this is the email associated with this throwaway account, which I've actually created an account with on GitHub, and we'll see that about later on.

00:02:25
So for you at home, type in the email address you want to use in this Git system, as well as the username. So what I'm going to do now is create a directory. So I'll just say mkdir, and let's just call this, maybe say, git-folder. So if we go Enter git-folder, there's nothing in here right now.

00:02:42
But what I want to do here is to initialize an empty Git repository. Now, the way I can do this is just simply say, git init, from within that folder. If I hit Enter, it's initialized an empty Git repository in this part right here. Now we're going to see some commands as we work through this skill.

00:02:59
One of them is a very common one we're going to use, is one called git status. This is going to allow us to see the status of all the files that we are tracking, and the commits that we've actually done. So if I say Enter, you're going to see that we're on a branch called master.

00:03:14
Like I said, we're going to have to work with multiple branches, as we found out in the introduction. And it does tell us that no commits have been made yet. Now again, we haven't really discussed what a commit actually is, and that's another thing we'll get to very, very shortly.

00:03:28
But ultimately, what this is telling us right now is that we've got this empty Git repository, and nothing has really happened just yet. We've got no files here. We've done nothing with those non-existent files, obviously. So how about I actually create a little file then.

00:03:42
So what I'll say here is touch, and we'll just say, example1.txt. So let's actually open this up. We'll just say nano example1. And let me just type some configuration in here. Let me just say, router ospf 1, router-id, all the ones. We'll say, network 192.168.31.0.

00:04:03
And we'll do a wildcard of 0.0.0.255, and put this into area 0. And we'll also add in another network of maybe, 10.0.0.0 and same wildcard mask, and we'll put this in to maybe, say, area 10. Whatever. So let's save this. Again, if I say git status, it's going to say that we have one file within this folder.

00:04:24
But this is an untracked file. We're not actually tracking this. Git is not caring about it right now. However, if we want Git to be able to track this, so that if we make changes Git is going to be able to detect those changes, well, it does make sense to add them.

00:04:37
So the way we can add them into our Git, so that Git is going to start tracking them, is we can just say, git add, and then specify the name of the file, which is example1.txt. So if we hit Enter, and then I'll say, git status, it tells me changes to be committed.

00:04:55
So ultimately, in short, a commit, you can kind of think about it as a hard save, for saving the file, making those changes, have an official record, so to speak. So let's commit this one here. So I'll say, git commit. And what I need to do here is to give a particular message.

00:05:10
So what I'm going to say here is, -m and then inverted commas. I'm going to specify my first message, we want this to be something pretty descriptive. And I'll just say, just committing my first file for testing, and we'll close in inverted commas. And now, we want to specify what file we want to commit.

00:05:28
So we just want to commit example1.txt. Let's hit Enter. And it tells us that we have made a commit. Perfect. So again, if we do a git status, this is a favorite command, we have nothing to commit now because any new changes have already been effectively saved with that commit.

00:05:45
But watch this, what if I happen to make a change to that same file again. So again, to example1, and let's maybe change-- I don't know, let's change area 10 to be-- let's say we made the mistake, that should be area 5, let's save this. So If I happen to cat this file, but if we say git status, it's going to tell us that the changes we've made are not actually staged for the commit.

00:06:09
So we want to effectively stage this file again. This is going to add it, so that we're going to track these changes. So say, git add, and we'll say the name, which is example1. If I know say, git status, once again, it's going to say to me changes to be committed.

00:06:25
So now what I can say here is, git commit and then say, m, for our message, and saying updating some-- or rather, let's say updating the-- I'm typing so bad --ospf area ID. So anyone looking at this file can see, this is the change that has been made.

00:06:41
And now after the message, let's specify the name of the file. Let's hit Enter. And now we have a new change. So this is now also being committed. Again, git status, we see nothing to commit. Now when we happen to make a change to a particular file-- let me just make one more change right here quickly.

00:06:57
Let me just add an, maybe say, another network statement. We'll say, network 172.16.1.0 and, again, same wildcards, and make this area 31. Save here. If I happen to say, git diff and then example, notice that we get this diff that's saying, "hey, by the way, this new change you've made to this file now has this additional change, compared to what was last committed." So if we examine this and say, well, yeah we actually do want to have this change be implemented, let's stage it, we'll say, git add, and we can specify the name of the file, and then git commit, with the message, adding area 31.

00:07:35
And then, again, type the file that's now being committed. If we say, git status, now we have nothing left to commit. And if we check the file, and now this copy of this file has effectively been saved. Now here's a thing, see those multiple changes that I just made here?

00:07:50
They've actually been stored in the git log. access the git log, well, that's what we're talking about in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**The ```--global``` flag is used to make system-wide configurations in Git.**

---

## Git Logs

00:00:00
Hey, guys and welcome back. So in the previous Nugget, we had just installed Git. We had initialized a repository, we created a little file, made some changes, and committed those changes. So what we're going to do in this Nugget right here is to explore the git log command, because what the git log is going to do, it's going to show us a record of all the commits that we have made.

00:00:32
To check this out, first clear the screen. And I say, git log. Look at this. You see that? You see the author who made the change, as well as their contact information. This is because this is what we configured with Git when we did the global config.

00:00:45
We get the time of the change, as well as-- remember that message we wrote? We have all that information. Now crucially, what you're also going to see is that each commit is going to be uniquely identified with this checksum right here. So this is the checksum for this one, here is the checksum for the other one, and here is the checksum for the very first one.

00:01:06
So the one at the top is the most recent one we've done, and the one in the bottom was the first one. Now here's the thing. Because we actually have this checksum, we can reference that checksum to quickly snap back in time and get that version of the file back really, really quickly.

00:01:23
So watch this. If I wanted to go back to the very first version of the file that we committed, what I can do here is copy this checksum of that first commit, and I'm going to use the command git checkout. So if I just paste in that checksum, and I hit Enter, we're going to get this issue called a "detached HEAD" state.

00:01:41
Now this is one of these issues whereby we have a little bit of a conflict. And we'll talk about that a little bit later on. But for now, if we happen to just cat that fail once again now-- cat example one-- we're now back to the very first commit. We don't have area 31 or anything anymore.

00:01:58
Remember that? The last commit, we added area 31. We've now went back in time, and we now have this version of the file. But lo and behold, because we happen to went back in time, we've now thrown out the git timeline. So again, like I say, that says a little bit of a conflict that we're going to have to resolve.

00:02:15
We'll look at that in a little bit more detail a little bit later on. So all I'm going to say here is git checkout, and then say HEAD. And you go to the very front of the timeline once again, where we just were, and then specify the name of the file.

00:02:27
Let's hit Enter. So that should now resolve that problem. If I happen to make another change to this file-- let's go into example one, and let's just add network 99.99.99.99, with all the zeros, and I'll say area 99. And let's save this. So we'll stage this.

00:02:43
We'll add the file, we'll commit it. We'll say "m," and we'll say "adding area 99 stuff." And we'll specify the name of the file, hit Enter, and there we go. We cat the file. We now have this version here. We do git status. We can see that we have a head detached.

00:02:59
Again, that;s because we actually went back in time and messed around with the timing a little bit. If we go to git log, notice the git log is actually changed because when I went back to the head, I've effectively removed those old commits. So we've only got the first commit that we went to, and then we added the second one.

00:03:16
So the git log file is going to give you a lot of detail about all your commits. Just be aware that when you happen to go back in time, you're effectively altering the timeline, and you can run into these type of conflicts. In which case, what I've done here is I have effectively went back in time, removed the commits ahead of that point, and now I'm basically writing a new timeline in essence.

00:03:38
But honestly, that type of workflow, when we are just reverting back to old commits, and then in essence altering the timeline like this, this is not really the ideal way to work with git. So how about we'll look at some more real-world workflows that is using git branches?

00:03:55
And that's what we're going to be doing in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**The 'total number of branches' is NOT shown in the ```git log```.**
---

## Git Branches

00:00:00
Hey, guys. And welcome back. So let's see how we can leverage branches when using Git. And first thing which I'm going to do here-- I'm actually going to switch back to VS Code. This is not necessary. But for now, I just find it a little bit cleaner.

00:00:23
So let me just go back and get this IP address. So here is the IP address here, 192.168.31.146. Let me just use the Remote Explorer to connect in here via VS Code and to the same virtual machine. I'll go to Remote Explorer. We'll go to SSH Targets. And I actually have this here.

00:00:43
I'm going to connect to this in a new window. So I'll fullscreen this. I'll type in the password for this right here. Hit Enter. Cool. So that is me now in this same machine right here. So we still have this git-folder we just created. I just happen to like this view a little bit better.

00:00:57
It's easier for me to draw on. So like I said, so far what we've done is we are basically creating this little timeline. When we make a commit, we have a record of a particular file. And then as you move through, we make another commit. First commit, second commit, maybe see a third commit.

00:01:13
And as we've seen here, we've had a unique checksum which identifies each particular file-- each version of that file. So at the very top of the timeline, that is referred to as the head. And what happened when I went back in time, I use my git log. And I happened to use the checksum of the very first commit.

00:01:31
So what we did here is we went back all the way here. And in effect, this led to a detached head. And like I say, I showed how we can still work using this detached head, but the net effect was our git log basically removed these ones here. And like I say, this is not really the typical workflow you're really going to be using when actually working with Git.

00:01:52
Instead, when we have Git, we're going to have a particular timeline here, as we're seeing here. Now this is going to be referred to as the main branch or maybe the master branch. I think main is the newer Git terminology. Master tends to be the older terminology.

00:02:06
So what's going to happen here is that when we want to make a change, say, for example, this file right here, what we want to do is to break off from the timeline and create our own little timeline so that we're actually not manipulating this branch directly.

00:02:19
We're just splitting off from it. And then we can develop our own timeline. And once we are happy with this timeline, we can effectively blend it back in to the main branch once again. So you can imagine the main branch is almost like the production branch.

00:02:33
It's the actual branch that's going to be used for real and production. And all the experimental features we want to work on, we want to break off from that branch so that we can work on in a clean timeline. So to be able to create a new branch, this is what we're going to talk about in this Nugget right here, how we can create these branches.

00:02:53
So let's check out and see what the effect actually does look like then. So again, from Visual Studio Code, I'm going to go into the folder git-folder. And we still have this example file here. So there it is. So what we're doing right now is we are working on the master branch right now.

00:03:08
So what I'm going to do here right now is create a new branch. OK, so I have this file here, example1. Cool. Now what I'll do here is say git checkout. And I'll say -b for branch. And now I'm going to specify a name for the branch. So let's just have a develop branch.

00:03:23
Let's just say-- cool. And now it says we have switched to a new branch called develop. So If I say git status, we are now on branch develop here. So if I happen to cat this file right here, the file is still the same. But when I go to modify this, it's going to be modified within this particular branch.

00:03:43
So let me modify this right here. And what I'll do here, I'll just delete this last one. So I'll remove this last line. And I'll save this. I'm also here as git add example1. To stage those changes, I'll say git commit. I'm committing this within the develop branch.

00:03:59
So I'll say git commit. And I'll just say, "experimenting with removing some config." Cool. And then I'll specify the name of the file. So we can actually see here when I committed this here. It does say develop branch. You see that right there. So, like I say, I've now made this change.

00:04:15
I've committed it within the develop branch. But notice this, if we happen to switch back to the main branch, we'll go back to our main timeline here. We'll say git checkout. And the name of the original branch was just master. Now we don't have to do a -b, because we're not creating a new branch.

00:04:30
We're just switching. I'll say git checkout master. We've now switched back to the master branch. And that change we just made-- we just committed, that is not going to be in effect in the master branch, because that is a completely separate timeline.

00:04:43
So if I say, cat and I cat this again, notice that in this timeline and effectively the production timeline, nothing has changed here. We have still area one right here. However, if I switch back to the develop branch-- I'll say git checkout develop.

00:04:58
And again, we've already created the branch. So we don't need to do a -b anymore. We're now back on develop. If we happen to cat it, in this timeline, that file has been removed. And if we ray git status-- or rather git log, we can see that change that we committed within the develop branch is actually present within the git log.

00:05:15
See that. "Experimenting with removing some config." So we're getting some really cool functionality here. We're getting a nice clean separation whereby we can just work freely on our own little timeline or develop branch without disturbing anything within the actual master branch.

00:05:32
Now there will come a time when we do actually want to move the changes we made in the develop branch-- the things that we are experimenting with. So let's just say they happen to work out very well and we want to have them be present in the main branch.

00:05:46
We're going to have to be able to blend our changes in one branch back into the main branch. And this is something we're going to be looking at very, very shortly. But just before we do that, what I want to do is to introduce you to something called Z Shell, and more explicitly something called Oh My Zsh, because right now, what we're actually using here is a Bash shell within Linux that is known as the Bourne Again Shell.

00:06:08
But when using Z Shell, and more explicitly, using Oh My Zsh, it's going to make it a little bit easier when working with multiple branches within Git. What am I talking about? Well, let's find out in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

00:06:26

***Note:***
**The command ```git checkout -b develop``` will create a new "develop" branch.**

---

### Zshell

00:00:00
Hey, guys. And welcome back. So like I said, when I'm working with Git-- when we have multiple branches, I really do like to have to work with the Zshell. So let me quickly show you how we can get this set up and running, and then, install Oh My Zsh.

00:00:25
So what I'll do here is I'll go back directly to my virtual machine. So that makes it a little bit easier for you to see what exactly is going on, even though I can do this from VS Code, nevertheless. OK, so I'm on my terminal, once again. What I'm going to do here is to install the Snap package manager.

00:00:41
So I'll say, sudo apt install snapd. And I'll type in my password. And I'll type it in the password correctly this time. OK, great. So what I'm going to do here is say, sudo snap install curl. And as it transpires, curl is already installed within my system.

00:00:55
But if you don't have it, just type in that command. And now, what I'm going to do is install Zshell. So I'll say, sudo apt install zsh. And I'm going to say, yes, and hit Enter. And that's going to run through the installation. This will take a couple of minutes maybe, or not even that.

00:01:09
Good. So let's go to our browser. And what we'll do here is search for oh my zsh. So let's click on this top link right here. And if I click this link here, Install. I'm just zooming a little bit here. Click this link here. There we go. That's going to move us down.

00:01:24
And it's going to give us the installation that we're going to do it using curls. Let me just copy this right here. And let's go back to the terminal. And I'll just paste this in here. If I hit Enter, that should run through the installation for Oh My Zsh.

00:01:38
OK. Now I had previously installed Oh My Zsh. So I was not prompted for any type of default configuration. You might be asked, do you want to make this your default shell? You can choose yes or no. I typically just choose yes. Now what you'll notice here is that my shell is a actually a little bit different.

00:01:54
See the prompt is a little bit strange here? You get this nice little prompt. What I want to do is quickly just show you the different themes that you can have because maybe you don't like the theme that I'm going to use here. So if you happen to search for Oh My Zsh themes, click this link here.

00:02:08
You're going to get the names of all the themes that you can have. So these are the different prompts. This is the default one. It looks a little bit different. We have this one here, af-magic. You see the name of it, all these different prompts here.

00:02:20
Agnoster, this is a very popular one, gives you a terminal looking like this. And the one I'm going to use-- and again, you can scroll through all these different themes and just take the name that you like. The name which I like is going to be af-magic.

00:02:33
The way I could change this here is I go into this file right here. Copy here. So I'll say, nano, and just go into this file. And we just change the theme. So one is currently at Robbie Russell. That is the very first one. That is the default one effectively.

00:02:47
I'm going to change it to af-magic. So if I Control-O to save this and Control-X, note that, if I happen to close this terminal-- so just is close here and I re-open it. So I'll say, terminal. OK, now I've got this new terminal here. You see that? Now the cool thing, when using Oh My Zsh-- if I go back into that Git folder, watch what happens.

00:03:09
See this? Look at this. It tells me I'm on the develop branch. We get this nice clear indication of where we're actually working. So anything I do here in this file-- I noticed in develop. If I happen to git checkout master, prompt is going to tell me straight away that I'm on the master branch.

00:03:24
This is why I recommend using this prompt because it really does make it much, much easier, especially, when you're working with multiple branches. Maybe you have three or four branches for different things. Being able to seamlessly switch out branches and be able to have a clear indication of where you are, this is really, really useful.

00:03:42
And it helps you-- or rather, prevents you from getting all tangled up. So definitely consider using this. And if you want to switch back to bash, you can just say, bash. And you get your bash shell. And if you want to go back into Zsh, you just say, zsh.

00:03:55
And you get this other shell. And like I say, if I happen to go back to my VS Code, I can connect once again. So I'll do Remote Explorer. And I'll connect to host a new window. I'll type in the password. And here's the thing, from here I can actually say, zsh, and still get this shell.

00:04:12
So that's really cool. So I can go out again and to Git folder. And I can see I'm on master, Git checkout, develop. I'm now on develop. And it just makes things way, way easier. So definitely check out Zshell, and in particular, check out Oh My Zsh. From the rest of that skill, this is what we're going to be working with.

00:04:30
However, when we actually make a change to a particular branch and we want to move that change from say, develop into master, how can we do this? Well, that's all going to be finding in the very next Nugget. So I hope this has been informative for you.

00:04:42
And I'd like to thank you for viewing.

***Note:***
**Once zshell is installed, you can switch between bash and zshell.**

---

### Merging

00:00:00
Hey, guys, and welcome back. So in the previous Nugget, we had just learned how we could install Zsh to make our branch selection a little bit easier to follow. Let's now talk about what we want to do when we want to move changes from one branch into another.

00:00:27
Now, like I say, we have two main ways we can do this. We can merge our changes, and we can also rebase our changes. Now both of these do work obviously, but they do implement these changes in different ways. And we do have particular reasons when you want to use merge versus rebase.

00:00:44
So let's check this out. Let's first start with merging our changes. Let's first talk about what is actually happening here within the tree. So let's imagine we have our master branch. So we have a change, a commit here, a commit here, and a commit here.

00:00:58
And at some point in the history, we actually break off and create a develop branch. So then we make a change which is on a separate timeline, and a change, and then another change. Now suppose we want to be able to move our changes from the develop branch.

00:01:14
Because we're now happy with our experimentation, we want it to be in the main branch. How do we move those changes? And, well, by merging them, the effect is going to be-- when we merge it, what we're basically doing is taking all the changes here and moving them into the main branch right here.

00:01:30
So now we're going to have all the develop changes integrated here. And this is what the graph actually looks like. Now, the issue here is that a merge can make the history look a little bit confusing. It can be a little bit harder to follow, when you've pushed your changes to somewhere else, somewhere which is not your local environment, because, like I say, merge is actually going to preserve the history even though it does look a little bit more confusing.

00:01:54
Rebase works a little bit differently. So let's quickly look at merge and see how this works then. So to keep this nice and clean, what I'll do is I'll just create a new folder entirely. So I'll say, gitfolder2. And if we cd Enter this folder-- if I [ folder.

00:02:09
This is not actually a git directory. So let's initialize it. We'll say, git init. So there we go. We're now in the master branch of this. Let's create a new file called configuration.cfg. And this is in the master branch. And let's just edit this. Spell nano correctly, which would be helpful.

00:02:24
So what I'm going to do here is just say, "this is master commit 1." So let's just save this. So I'll say, git add. And like I say, we're not actually tracking this file just yet. You want to add it. Now the way we can add this, as we saw, we can say git add and specify the name of the file.

00:02:40
However, we can just be ambiguous and just add everything which is in our directory, which happens to be just one file. In this case, just by saying git add dot, so that's going to add everything. We'll say git status. This file is now being tracked.

00:02:53
So what I'm going to do here is if I actually make a commit here-- I'll say, git commit. And I'll just say, "commit 1 in master." And I can just say dot to be unambiguous about the file. Cool. So that is now being committed. Now, again, if I happen to make a change to this file, I'll say, nano configuration.

00:03:09
And I'll make this commit number 2. Let's say we've updated this configuration of some kind. If I say, git diff configuration.cfg, there's actually been a change. We can see this. Let's add this change. We'll say git add dot. And then let's just make a new commit.

00:03:22
We'll make this git commit 2. So we've now made new commits here. So if we cat this file, we're on commit number 2. But let's say we wanted to create a new branch. So I'll say git checkout -b develop. So now we have our configuration file. And anything I do to this is going to be in the develop branch.

00:03:41
So if I happen to modify this, I'll say, "this is develop changes," I'll just say 1. So I'll add this. Git add. Stage it. I'll say git commit -m "1st commit in dev." Just say dot. Cool. And I'll just make one more change here. Go back in. And I'll say, "develop changes 2." Save here, git add, Arrow Up.

00:04:02
Do a commit. Say it's "2nd commit in dev." So if we happen cat the file here within the dev, we're on this. If we checkout back to master and we say cat configuration, we're still on the master commit there. So if we do git log, in the master, we are only seeing the master commit.

00:04:22
You see that? However, if we go to git checkout and go to develop-- if I spelled develop, that would be super. Enter the git log here. It's actually a little bit different. We're seeing both the master commits and the dev commits from where we actually split apart.

00:04:36
You see that? So what we're going to do here is we want to move these changes from develop into master. So the way we can do this is by moving to the master branch where we actually want to move the changes. So we will git checkout into master. We'll cat this file.

00:04:51
And we want to merge those changes that we had made in the develop branch because we're happy with them. We can do this by saying git merge and now just specify the branch you want to merge from. So we'll say we want to merge from the develop branch into the master branch.

00:05:05
Hit Enter. We now have a configuration change in the master branch. If we now cat master once again, we now have the developed changes within the master branch. You see that? And now if we say git log, now within the master branch, we can see the commit history from the develop branch has all been moved in.

00:05:24
So that's how we can merge configurations using git. Let's check out rebase next. That's coming up in the very next Nugget. So I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**A merge will preserve git history.**

---

### Rebasing

00:00:00
Hey guys, and welcome back. So in the previous Nugget, we had just checked out how we can use git-merge so that we can move changes from a different branch in our case, a develop branch, back into the main or master branch. Now, I don't want to get into too much in the weeds here because it can be a little bit confusing if this is your first introduction to Git.

00:00:32
But here's the thing. We can actually have many more branches than one branch, OK? So we could have say, we have a master, it is our first commit and then maybe your second commit, and then maybe say we branch off and do feature branch. Now here's the thing, if we're actually working in a very, very large team, it might not just be quite so obvious as that we have one develop branch and a feature branch.

00:00:54
Instead, what may happen is that you may have all these different timelines running together, and what happens here is that when we're constantly breaking off and branching out and making new branches, then it does become a little bit hard to track. Now, here's the thing.

00:01:09
When we are using a merge request, merge request is going to preserve the entire history. So if you have a lot of complex history, well, it can be a little bit hard to follow. Now what I will see is that when we are working with repositories which happened to be public, then we definitely want to be using the merge request even though it's a little bit more confusing to look at.

00:01:30
For posterity, we really want to preserve that history, so use a merge request when you are working with public. However, if we have a repository which has not yet been made public but is working with it locally, we can in effect tidy this up a little bit by using a rebase.

00:01:46
Now, a rebase is going to in effect have the same type of effect that's going to allow us to move changes from say like for example, a develop branch into a main branch, but the rebase kind of rewrites history. What rebase does is-- See these changes here that we've got in the side?

00:02:03
It pretty much moves them and rewrites them onto the master branch, and all these little branches here kind of get forgotten about. So you get that kind of fake history almost, and everything looks much more linear just with many, many more commits, but it looks like it's all on one timeline here.

00:02:19
Because in effect, all of the branches which were spiralling off have been rewritten and dumped back into that timeline. So this can make things much, much easier to look at and to interpret. You get this nice linear look of what has happened. And like you see, this is a good candidate when we're working with a private repository that we have not pushed to say for example, git-hub.

00:02:39
So let's quickly do an example of a rebase. OK, so what I'll do here is I'll create a new directory. I'll just say mkdir, and I'll just say maybe rebase example. OK. So going to here, and I'll initialize my Git repository and I'll create a file called blahblah.txt OK, so let's go in and edit blahblah.

00:02:58
And I'll just save this as master 1. Let's save here. And I'll add this and then just commit it. So I'll say, Git commit-m, and I'll just save first master, and I'll just say dot. OK. So we've now committed that. Let's go in and modify the file then.

00:03:11
So I'll say, nano blahblah. I'm making some type of update. Let's just save this as master 2 maybe, pretend this is some type of code or configuration file. Let's stage this for commits. And again, let's just add that up and I'll just say, second master.

00:03:26
Now I'm not going to create multiple branches to highlight the utility of rebase because it's just going to start getting a little bit confusing and lengthy for your first introduction. So what I'll do here is just create a develop branch, just like you saw with merge.

00:03:38
So I'll say, git checkout, and I'll say B for branch, and we'll create a develop branch. OK. So now that file here has been copied from the master, and we've now created this new develop branch. So let's make these changes on develop. We'll say nano blahblah.

00:03:55
And let's just save this as feature 1. And again let's stage this, git add, and we'll commit it. So get commit-n, and we'll just say, first dev change. And finally, we'll go in one more time and just save this as feature 2. Again, save here, arrow up, add it to stage it, and then we'll change the commits to second dev change 2.

00:04:18
So, like I said, if I happen to cat this file now, within the develop branch we've got all these new features. However, as you can expect, if I check out and go to master, if I cat the file in this branch, we don't have any of the features added just yet, as I switch into my master branch, and I'm just going to-- instead of merging it, I'm going to rebase.

00:04:38
So I'll say git, rebase, develop, if I hit Enter, now as you can see I'm in the master branch, and if I actually cat that file just like with merge, I'm now going to have these new features applied. Do you see that? So basically what we're doing here is we're getting a similar effect.

00:04:54
We are moving changes from one branch into another branch. The difference here is the handling of the timeline and therefore the use cases. Like I say, when we're using a public repository, you want to be merging your changes. When you are using a private repository, then it does make sense to rebase them before you make anything public.

00:05:13
Because like I say, when you have multiple branches spiralling out, the rebase is going to make things a little bit easier when you're examining logs and going through all of your changes. So that'll do for now. On merge and rebase, that's our first introduction to Git.

00:05:25
I don't want to get too deep into the weeds, but next time we'll look at that as git-hub integration, and that's what we're going to be talking about in the very next Nugget, so I hope this has been informative for you. And I would like to thank you for viewing.

00:05:36

***Note:***
**A git rebase should NOT be used exclusively on public branches.**

---

### Integrating Github

00:00:00
Hey, guys, and welcome back. So let's now see how we can integrate GitHub with Git, because what we've been doing here is working on a local computer right now. This is where Git is operating. Now, here's the thing. If we want to be able to share our changes with a wider team, we can put them on this remote website, GitHub, and all those commits we've made, we can send them all to GitHub.

00:00:34
That means if someone else is working on their local computer using Git, they can pull down those changes that we've posted to GitHub, and then they can start working with them in their local Git. And then once they've made their changes, they can post them up into GitHub once again.

00:00:49
And if we so choose, we could pull down their changes, so we can have this type of collaborative workflow. Or even just for ourselves and for just working ourselves, we can make our changes locally on Git and then effectively save them on GitHub. And then if you actually want to pull them down at a later date, then we can just pull those changes back from GitHub onto our local computer.

00:01:11
So let's see how we can set up this relationship right here then. So if you go to the website, GitHub, what I'm going to do is to sign in, because I've already created an account. If you haven't, then you can sign up for GitHub. For now, I'm just going to sign in.

00:01:24
So like I say, I've created this little account called johnredtest. And that's just a little dummy account I use to demonstrate workflows. So let me sign it into this. And what I'll do here is I will create a new repository, so let me click this right here.

00:01:37
So let's just call this git-workflow-example. And we'll give this a description, and we'll just say a simple example to demo the workflow. Now we have the option here to make a public repository or a private repository. A public one, as it says here, anyone on the internet can see this repository.

00:01:54
If you want to limit who can see it, maybe perhaps to just a particular team of people, then you could choose private. But for now, I'm just going to choose public. And what I'll say here is I'm going to add a README, so I'll just add this. And a README is just going to give you some type of description about the project.

00:02:10
So let's create the repository. And now we have a repository. The only thing we have here is a README, which is just a simple copy of what I wrote in the description. And if you want to amend that to add more information, we can just click this link here and just begin editing.

00:02:24
But for now what I'll do here is I'll just add the little file. So I'll say Add File, and I'll create a new file. And I'll just call this ghexample1.txt. And I'll just say it this is some example to work with. Cool. So what I'll do here is I'll just scroll down, and I'll just say commit new file.

00:02:42
So this is now being committed on the remote repository. So if I want to be able to work with this file or anyone who is on my team, what we could do here is to clone this repository. That effectively going to bring a local copy of that repository from the remote source on GitHub down onto a local computer.

00:03:02
So what I can do here is click Codes here, click this link, and then just copy this. And I'll go back to my terminal here, and I'll just make a new one. And I'll just say mkdir SomeNewExample, just sort of get a nice clean folder. So this folder has nothing in it.

00:03:18
What I'm going to say here is git clone. And I'll just paste this in here. And if I hit enter, now I don't actually have to do a get a net within this folder, because when I actually cd Enter-- that's the right three here-- watch what's going to happen with Z shell.

00:03:32
It recognizes as the Git repository. It's being cloned. Therefore we're in the main branch. And if I do an LS, I now have a copy of the readme and a copy of that little script here or that little text file, should I say, so I can cat the README, and I can cat the little text file we created.

00:03:47
So now I've got a local copy of this text file. And I can do all the things which I did before. Like, if I wanted to create feature branches that I just wanted to experiment with and then merge them, I can do my merger. But like I say, what if I wanted to make some changes here and I wanted to put the changes that are on my local repository over to the remote repository where anyone can access my changes?

00:04:10
So let's do an example here. Let's go in. And we'll just say nano ghexample. And I'll just say this is some local change. I have made. Perfect. So if I say Git add ghexample, so I've done LS. If I cat this file, we now how this new change that I've added.

00:04:27
So what we're going to do here is try to commit this, but there's actually going to be a little bit of an issue, which I want to show you. And that's just very, very recent. So I'll say git commit -m, and what I'll say here is committing some local changes.

00:04:40
And I'll just say dot to add any file. Perfect. So now what I want to do is I've committed this locally. So the changes have been stored locally. Git log, we have committing local changes. We want to push this latest commit to the remote repository. So here's what we're going to do here.

00:04:57
I'm going to say get, push, and then -u, and I'm going to say the origin as the main branch. That is the branch I want to target remotely. Now, if I Enter here, it's going to ask me for my username. So my username is johnredtest@outlook.com. And it's saying type in the password.

00:05:16
But watch this, this is actually not going to work. Check this out. And it says here support for password authentication was removed on August 13. We're now in September. Now we're going to have to use a personal access token. So let's see how we can use this personal access token then.

00:05:32
So if we go back to GitHub, so clearly we can see here if I go to GitHub example, nothing has changed yet on the remote repository. Our attempt to push our changes have been blocked. We need to get this authentication token. So if I go up to the top right here to this icon, I can now go down to Settings here.

00:05:47
If I scroll on down down the left hand side, we're going to get the setting called Developer Setting. Let's click this. And now I can choose a personal access token. So as you can see, I've already created one before. I'm going to generate a new token.

00:06:01
And I'll just say example of new token. And I can choose the expiration. I'll just make it seven days. This will expire before the time you actually read this. And I can basically select all the access I want together. I'm just going to give access to everything here.

00:06:16
So I'll just click all of these. That means I can do anything with this access token. Click, click, click, create just access notifications, even delete the repository with this token. And what I'll do here is I'll generate this token right here. What it's going to say here is I'm not going to see this again.

00:06:32
So I need to make a copy of it. So if I just click this here, I've copied it. And I like to just paste this into Notepad here. Now I've got a copy of this. So I'll just save this right here. So here's what's going to happen. If I try this again, and I say get push -u origin main, and then I type and the username johnredtest@outlook.com, and then if I just paste in this token here-- you can't actually see it on the screen, but it's now being pasted.

00:06:56
If I hit Enter, it's now actually authenticated. And that change I've made there should now be on the remote repository. So now if I go here, I'll refresh the page. We can see that it actually says committing some local changes. And if I click on this file, the changes I have made locally are now remotely in GitHub.

00:07:14
So if someone else happened to pull down this file, they would get the local changes I've made. Now here's the thing. If I happen to make another change here and just go into GH example, and we'll just save this as some more changes, and I'll save here, and I'll git add it to stage the changes.

00:07:30
And I'll add up, and I'll just say committing some more local changes, if I try to push this, git push -u origin main, I'm going to have to type in johnredtest. And again, I'm going to have to copy that same authentication token and paste it in again, just so we get access, but that can be a little bit cumbersome.

00:07:48
If you want to be able to save your credentials on your local environment, you can have git cache it. So what we can actually say here is git config, and we can say --global if we want to apply this globally, and we will say credential.helper, and I'll say store.

00:08:04
So this means if I happen to make a new change once again, I'll just say, blah, blah, blah, save here. And I'll just say committing even more local changes. If I say git push -u origin main, again, it's going to ask me for my credentials. But this time after this, it's going to store these credentials.

00:08:21
So if I happen to just see my username, type, and I paste then the authentication token one more time, any other times after this it's going to be stored because this came after we have specified that we want to save annual credentials. So one final time we'll make a change, I'll just say nano, and I'll just save this as the final change, save here.

00:08:42
Let's stage it, and we'll commit. We'll say last change, and we'll do a dot. And we'll say get push -u origin main, and this time we're not going to have to type in any credentials, just hit return. And those credentials have already been saved and it automatically pushes.

00:08:58
And now if we go to GitHub, if I go back here, we're going to see that we actually have all these new changes. And again, if we go to the history right here and click on this, you can actually see all the different commits I've put in here. So this one here, we added blah, blah, blah.

00:09:14
And on the very last one here, we added this is the final change. So this is all being stored remotely for anyone on our team to access it. And then they can begin pulling down these changes and began working with them in their own local environment.

00:09:28
So as you can see here, and Git and GitHub, they are very, very different things. But they do integrate very tightly together. And GitHub really is a vital part of the development workflow. So definitely get used to using it. So that is our first introduction to GitHub.

00:09:42
I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**Since August 2021, Github no longer accepts password authentication when pushing to a remote repository.**

---

### Ignoring Files

00:00:00
Hey, guys, and welcome back. So let's see how we can actually separate files that we want to keep just locally from the ones we want to push remotely to GitHub. We're going to be able to do this by using a gitignore file. So what I'll do is, I'll just create a new file, just maybe, say, touch newfile.txt.

00:00:30
And let's just nano this. And I'll just say this is some new file I want to push remotely. So let's save here. And I'll create another one. I'll say touch newfile2.txt. And I'll go into this one-- oh, and I'll need to say newfile2. And I'll just say, this is yet another file I want to share.

00:00:48
OK, so let's save here. And what I'll do here is I'll create one final file, I'll just call this supersecret.txt. So let's go into here and just say password12345. Let's just say it's holding some type of password then. OK, so we don't want supersecret.txt to be ever be committed to the remote repository because this might be something that we just have sensitive to our machine.

00:01:12
We don't want to share that with the rest of the team. So what I'm going to do here is create a hidden file called gitignore. So if I say touch . for a hidden file, and I'll say gitignore. And I can say nano .gitignore. And within this file, I'm just going to specify the files I don't want to track.

00:01:28
So if I say supersecret.txt and just save this, that's just going to let git know that we don't want to track this file. So what I can go here is say git status. Now git is saying that, look, we've got these untracked files. Do we want to track them, basically?

00:01:41
Notice here though that the supersecret file has not been picked up by git. It's seeing the gitignore file. It's seen the newfiles. And we've got the swap file here. Let's forget about that. It's not an issue. But the supersecret one-- git is not even attempting to track that.

00:01:54
So what I can do here is say git add . to add all the files. And I say git status. We are tracking these files, but notice again, this one here, supersecret.txt, is not being tracked at all. If I happen to try to push all of them, now that they've actually been staged, if I say git commit -m "adding new files" and I just say .

00:02:14
to commit at them all. So now we've committed all these files, let's try and push them. I'll say git push u and origin is going to be the main branch in our GitHub repository. Let's hit Enter. They have all been pushed remotely to GitHub. So let's go and check that out then.

00:02:28
So if I just refresh the page here, we now have all of these new files. So we've got newfile.txt, just this one here. We have newfile2. Notice that we have the gitignore, and it specifies supersecret.txt, but the contents of that file are secure. Nobody knows what's inside that.

00:02:46
That's actually not been pushed. The name of the file is being disclosed but the contents have not. So, like I say, if I go to supersecret.txt, this information here has been kept away from GitHub, the remote repository. So as you can see here, the gitignore file is really, really useful.

00:03:01
There's just certain things we don't want to be committing to GitHub, so definitely get used to using gitignore. It's going to be a big help for your workflow. And I hope this has been informative for you, and I'd like to thank you for viewing.

***Notes:***
**```.gitignore``` is the name of the file used by Git to ignore files.**

---

### Merge Conflicts

00:00:00
Hey, guys, and welcome back. So I want to talk to you about in this Nugget right here is how we can resolve conflicts within Git. If you're working collaboratively, this is something you're definitely going to run into at some point no doubt.

00:00:24
So what I'll do here is I'll just create a new directory afresh once again. And I'll just call this conflict example. So we'll cd into ConflictExample, and we'll initialize this as a Git repository. So, what I'll do here is I will create a file. Let's just call this myfile.txt.

00:00:40
And let's actually just open this in Visual Studio Code. Go into myfile.txt, because we have the line numbers. So all I'll do here is I'll say a bbq chicken, eggs, and donuts. That's a healthy meal. OK. So let's save that right here. So if I cat this file, here we have our barbecue chicken, eggs, and donuts.

00:00:59
So what I'll here is I'll add this, and I'll commit it with a message super healthy meal, which it obviously is not. OK. So what I'm going to do here is pretend that we have two different developers working on this project. So what I'll do here is I'll say git checkout -b, and I'll call this johnbranch.

00:01:15
So we now have a branch for me where I'll be doing my development. Here's the thing. If I go to git checkout and go to master, let's also pretend that we have another developer. And that is going to be Trevor. So I'll say, git checkout -b, and I'll just say trevorbranch.

00:01:29
So now we have Trevor's branch where he will be doing some work and John's branch where I will be doing some work. OK. So let's go back to johnbranch just now. We'll say git checkout. We'll go to johnbranch. So we're now in John's branch. And let's make some changes to this file.

00:01:43
So I'll add on irn bru, which is a very tasty Scottish drink, and I'll also add on a pizza crunch. If you don't know what a pizza crunch is, it's a super unhealthy Scottish meal whereby you deep-fry pizza. So we'll add this on. OK. So those are the things which I am adding right here.

00:01:59
So what I want to do is I'll stage my changes, and I'll commit them with the message "making this even healthier," which is dubious. OK. And what I'll do is I'm actually going to go to Trevor's branch. Let's pretend we're Trevor now. So in Trevor's branch, if we go back here, those changes are not actually present, because Trevor has got a copy from the master branch, and the changes that I've made have not been merged there.

00:02:23
So let's say Trevor makes some better changes. Trevor is the better developer-- he makes more smarter decisions. And Trevor says, let's just add regular pizza and let's add beer. So let's save this. So line 4 and 5, John's made some type of changes, and Trevor's made different changes on the same lines.

00:02:40
So what I'm going to do here is Trevor's going to stage his changes, and he's going to commit them as well, making the meal better. So Trevor is got to commit that too. Now, I happen to like Trevor's changes. I want to merge his features into mine. Watch what's going to happen if I try to merge this when I say git merge and I try to merge in Trevor's branch into my branch.

00:03:01
Look at this, we have a merge failed. Basically, we have a conflict, because me and Trevor have put different things on the same lines within the same file. Git doesn't know how we actually want to resolve this. So in order to do so, we've got to instruct Git what we actually want to do.

00:03:18
So if I go back to this file once again, scroll on down, notice what we have here. We can see my changes here-- irn bru and pizza crunch-- and we can see Trevor's here, and it's been split apart with this little line here. What I'm going to have to do here to implement Trevor's changes is to quite simply resolve that conflict by removing the parts which remain here.

00:03:39
Now, VS Code makes this nice and easy for us. We can say, accept the current change, which is my change. We can accept the incoming change, which is Trevor's change. We can accept both changes, or we can just click compare the changes. So if we click this, we will see the differences of what we're actually trying to apply.

00:03:56
So let's just close this back down here. Now, all these arrows and these equal signs, this is just as split apart the different changes. If you want to manually impose these changes, you can just delete one or the other. Say, for example, if I wanted to keep my change, I could just delete this, delete this, delete this, delete this, and the head, and just leave these two and save, and that would save my changes.

00:04:18
Or we could do the inverse, just leave Trevor's changes, delete all my stuff. But like I said, VS Code makes this nice and easy for us. If I want to accept both changes I can. But instead, I happen to like Trevor's idea better. So if I just accept the incoming change, which is Trevor's branch, and I click this, look at that.

00:04:35
We've now been resolved, and Trevor's new feature, which happens to be better than my suggestion, is now going to be the one that's taken. So if I save this and we're in johnbranch, if I happen to cat my file notice that we actually have Trevor's suggestion of pizza and beer added to the meal.

00:04:51
So be aware when working with multiple branches, trying to merge those branches, very often if you have different changes in the same place, you're going to run into this thing called the merge conflict. And as you saw here, VS Code makes it really, really easy to resolve that by accepting the incoming change, or keeping your change, or blending both changes.

00:05:11
All of these options are available to you. So definitely don't freak out if you happen to get this error message. Okie dokes. I hope this has been informative for you, and I'd like to thank you for viewing.

***Note:***
**A merge conflict will NOT be automatically resolved without user interaction.**