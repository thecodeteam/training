#System Design for Project Vasco da Gama

##Data Collection:
```sequence
Twitter->Twitter Watcher: Here is a Tweet for You
Twitter Watcher->Redis RQ: Here's an image URL to queue
Redis RQ->Redis DB: Here's a job to store.
Redis DB-->Redis RQ: Got it, thanks
Redis RQ-->Twitter Watcher: I got it, thanks
Twitter Worker->Redis RQ: Do you have any work for me?
Redis RQ-->Twitter Worker: I sure do, here's a URL
Twitter Worker->Twitter Image Server: Gimme that Image!
Twitter Image Server-->Twitter Worker: Fine! So needy!
Note over Twitter Worker: Performs image manipulation
Twitter Worker->ViPR Object: Please store this image, and delete it in 1 day
ViPR Object-->Twitter Worker: Done
Twitter Worker->ViPR Object: Please give me a public URL for this image
ViPR Object-->Twitter Worker: <URL>
Twitter Worker->Redis DB: Please store a record of this image and its URL and size. Delete the record in 1 day
Redis DB-> Twitter Worker: Done
Twitter Worker-->Redis RQ: My Job is Complete, Here's the Result
Redis RQ-->Redis DB: Store this Job Result, and Mark it Complete
Redis DB-->Redis RQ: Done!
```

##Dashboard Generation
```sequence
Dashboard App->Redis RQ: Give me some stats
Redis RQ-> Dashboard App: Here's some
Dashboard App->Redis DB: Give me some stats
Redis DB-> Dashboard App: Here's some
note over Dashboard App: Some internal cleanup of the data
Dashboard App->Redis RQ: Here's some data to post to Freeboard.io
Redis RQ-->Dashboard App: Understood and stored.
Dashboard Worker->Redis RQ: Do I have any work to post?
Redis RQ-> Dashboard Worker: Sure, here you go.
Dashboard Worker->Freeboard: Here's some metrics, buddy
Dashboard Worker->Redis RQ: I'm done
Note over Dashboard App: Sleep 10 seconds and repeat
```

##Scaling Controller
```sequence
participant iPhone App
Scaling App->CloudController: Login
CloudController-->Scaling App: Done, here's a token. Don't lose it.
Scaling App->CloudController: What apps do I have access to?
CloudController-->Scaling App: These ones: [a,b,c]
iPhone App->Scaling App: Hey, here's my login, what apps are there?
Scaling App->iPhone App: Here's a list: [a,b,c]
note over iPhone App: User selects app, and scale target
iPhone App->Scaling App: Scale app named "a" to "n"
Scaling App->iPhone App: Understood
Scaling App->CloudController: scale app A to 'N'
```

